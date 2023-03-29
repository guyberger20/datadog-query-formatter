#!/usr/bin/env python3
import sys
import re
import urllib.parse


def formatMsg(msg):
    msg_arr = msg.split(' ')
    out = ''
    for w in msg_arr:
        escaped = w.translate(str.maketrans({"-":  r"\-",
                                             "]":  r"\]",
                                             "[":  r"\[",
                                             "\\": r"\\",
                                             "/": r"\/",
                                             "^":  r"\^",
                                             "$":  r"\$",
                                             "*":  r"\*",
                                             "(":  r"\(",
                                             ")":  r"\)",
                                             ".":  r"\."}))
        out += escaped + '?'
    return out[:len(out) - 1]


def parseEnv(envId):
    prefix = 'env:'
    if envId in ['prod', 'production']:
        return prefix + 'production-production'
    elif envId[0] == 't' and envId[1:].isnumeric():
        return prefix + 'staging-t' + envId[1:]
    elif envId.isnumeric():
        return prefix + 'staging-t' + envId
    elif envId == 'master':
        return prefix + 'staging-master'
    else:
        return prefix + envId


def generateMsg(msg, env):
    out = '@msg:*'
    out += formatMsg(msg)
    return out + '* ' + env


def printQuery(query):
    query = re.sub(' +', ' ', query)
    encoded_query = urllib.parse.quote(query)
    query_link = 'https://app.datadoghq.com/logs?query=' + \
        encoded_query
    print(query_link, end='')


def main():
    global generators, parser
    env = None
    if len(sys.argv) <= 1:
        print('missing message argument')
        return
    if len(sys.argv) == 2:
        env = parseEnv('prod')
    elif len(sys.argv) == 3:
        env = parseEnv(sys.argv[2])
    else:
        print('too many arguments')

    msg = sys.argv[1]
    query = generateMsg(msg, env)
    printQuery(query)


if __name__ == '__main__':
    main()

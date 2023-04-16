#!/usr/bin/env python3
import sys
import re
import urllib.parse

msgPostfix = '*'


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


def generateMsg(msg, env, printMsgOnly):
    global msgPostfix
    prefix = '*' if printMsgOnly else '@msg:*'
    formattedMsg = formatMsg(msg)
    if env:
        formattedEnv = ' ' + env
    else:
        formattedEnv = ''
    return prefix + formattedMsg + msgPostfix + formattedEnv


def printQuery(query, printMsgOnly):
    query = re.sub(' +', ' ', query)
    if printMsgOnly:
        print(query, end='')
        return
    encoded_query = urllib.parse.quote(query)
    query_link = 'https://app.datadoghq.com/logs?query=' + \
        encoded_query
    print(query_link, end='')


def main():
    global generators, parser
    env = None
    printMsgOnly = False
    if len(sys.argv) <= 1:
        print('missing message argument')
        return
    if len(sys.argv) == 2:
        env = parseEnv('prod')
    elif len(sys.argv) == 3:
        if sys.argv[2] == 'msg-only':
            printMsgOnly = True
        else:
            env = parseEnv(sys.argv[2])
    else:
        print('too many arguments')

    msg = sys.argv[1]
    query = generateMsg(msg, env, printMsgOnly)
    printQuery(query, printMsgOnly)


if __name__ == '__main__':
    main()

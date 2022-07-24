#!/usr/bin/env python3

import re
import argparse

QUERY_TITLE = 'DataDog query:'

parser = argparse.ArgumentParser(description='Process query params')
parser.add_argument('-e', metavar='ENV_ID', type=str, nargs='?',
                    help='environment id')
parser.add_argument('-s', metavar='SERVICE', type=str, nargs='?',
                    help='service')
parser.add_argument('-st', metavar='STATUS', type=str, nargs='?',
                    help='status [emergency, info, warn, err]')
parser.add_argument('-m', metavar='\"MESSAGE\"', type=str, nargs='?',
                    help='substring of the msg parameter to search for')
parser.add_argument('-k', metavar='\"KEY:VAL\"', type=str, nargs='?',
                    help='comma-separated pairs of key and value, example: \"id:1,pid:2\"')

class ParamGenerator(object):
	def __init__(self, name, callback, default_val) -> None:
		self.name = name
		self.generate = callback
		self.default = default_val

def formatMsg(msg):
	msg_arr = msg.split(' ')
	out = ''
	for w in msg_arr:
		escaped = w.translate(str.maketrans({"-":  r"\-",
                                          "]":  r"\]",
                                          "\\": r"\\",
                                          "^":  r"\^",
                                          "$":  r"\$",
                                          "*":  r"\*",
                                          ".":  r"\."}))
		out += escaped + '?'
	return out[:len(out) - 1]

def generateEnv(env):
	prefix = 'env:'
	if env in ['prod', 'production']:
		return prefix + 'production-production'
	elif env[0] == 't' and env[1:].isnumeric():
		return prefix + 'staging-t' + env[1:]
	elif env.isnumeric():
		return prefix + 'staging-t' + env
	elif env == 'master':
		return prefix + 'staging-master'
	else:
		return prefix + env

def generateService(service):
	if len(service <= 1):
		return ''
	return 'service:' + service

def generateStatus(status):
	if len(status) <= 1:
		return ''
	return 'status:' + status[0].upper() + status[1:]

def generateMsg(msg):
	out = '@msg:*'
	out += formatMsg(msg)
	return out + '*'

def generateKeyVal(input):
	out = ''
	pairs = input.split(',')
	for pair in pairs:
		keyval = pair.split(':')
		key, val = keyval[0], keyval[1]
		out += '@' + key + ':' + formatMsg(val) + ' '
	return out

generators = {
	'e': ParamGenerator('env', generateEnv, 'env:production-production'),
	's': ParamGenerator('service', generateService, ''),
	'st': ParamGenerator('status', generateStatus, ''),
	'm': ParamGenerator('msg', generateMsg, ''),
	'k': ParamGenerator('keyval', generateKeyVal, ''),
}

def printQuery(query):
	print('\n' + QUERY_TITLE, end = '\n\n')
	print(re.sub(' +', ' ', query), end='\n\n')

def main():
	global generators, parser
	args = parser.parse_args()
	query = ''
	for arg in vars(args):
		val = getattr(args, arg)
		query += generators[arg].default if val == None else generators[arg].generate(val)
		query += ' '
	printQuery(query)

if __name__ == '__main__':
	main()

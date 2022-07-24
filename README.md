# datadog-query-formatter
A tool that formats parameters to a DataDog log query

## About
This tool generates a query for DataDog with appropriate syntax from command line arguments given as plain text.

Mainly used to handle the annoying regex formats and escape special characters.

## Prerequisites
* Python 3
```sh
brew install python
```

## Getting started
Use `-h` flag to see all the input options:
```sh
Process query params

optional arguments:
  -h, --help      show this help message and exit
  -e [ENV_ID]     environment id
  -s [SERVICE]    service
  -st [STATUS]    status [emergency, info, warn, err]
  -m ["MESSAGE"]  substring of the msg parameter to search for
  -k ["KEY:VAL"]  comma-separated pairs of key and value, example: "id:1,pid:2"
```

## Examples
### Find a log message
input:
```sh
./formatter.py -m "This is a log msg for object id ABC-123-456"
```
output:
```sh
env:production-production @msg:*This?is?a?log?msg?for?object?id?ABC\-123\-456*
```
### Query specific environment
input:
```sh
./formatter.py -e 1234 -k "id:1,publicId:123-456"
```
output:
```sh
env:staging-t1234 @id:1 @publicId:123\-456
```


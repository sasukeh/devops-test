#!/usr/bin/env python
# coding: utf-8
"""
data structure:
<time><log level><http method><uri><reqest time><Access ID>

Used modules
sqlite3
glob
os
csv
gzip

"""

import sqlite3
import glob
import os
import csv
import gzip

keys=(
'time',
'level',
'method',
'uri',
'reqtime',
'accessid'
)

def main():
  dbname = 'quipper.db'
  conn = sqlite3.connect(dbname)
  conn.text_factory = str
  csr = conn.cursor()
  show_table = '''select time,level from logs '''
  result = csr.execute(show_table)
  print(result)

if __name__ == '__main__':
  main()


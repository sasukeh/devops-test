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

def logfile_search():
  logfile_list = []
  os.chdir("./logs")
  for file in glob.glob("*.gz"):
    logfile_list.append(file)
  logfile_list.sort()
  return logfile_list

def is_table(csr, dbname):
  check_table = '''Select name from sqlite_master where type='table' and name=''logs' '''
  res = csr.execute(check_table)
  print(res)
  return True

def main():
  dbname = 'quipper.db'
  conn = sqlite3.connect(dbname)
  conn.text_factory = str
  csr = conn.cursor()
  create_table = '''create table logs (time varchar(64), level varchar(64), method varchar(32), uri varchar(32), reqtime varchar(32), accessid varchar(32))'''
  print(create_table)
  csr.execute(create_table)
  
  logfile_list = logfile_search()

  for filename in logfile_list:
    print(filename)
    with gzip.open(filename, 'rt', newline="") as f:
      reader = csv.reader(f, delimiter="\t")
      for row in reader:
        if len(row)==len(keys):
          d=dict(zip(keys,row))
          csr.execute('insert into logs (time, level, method, uri, reqtime, accessid) values(:time,:level,:method,:uri,:reqtime,:accessid)' , d)
  conn.commit()

if __name__ == '__main__':
  main()


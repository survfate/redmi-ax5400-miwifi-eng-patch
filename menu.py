#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
import subprocess

import xmir_base
import gateway
from gateway import die


gw = gateway.Gateway(detect_device = False, detect_ssh = False)

def get_header(delim, suffix = ''):
  header = delim*58 + '\n'
  header += '\n'
  header += 'redmi-ax5400-miwifi-eng-patch {} \n'.format(suffix)
  header += '\n'
  return header

def menu_show():
  gw.load_config()
  print(get_header('='))
  print(' 1 - Set router IP address (current value: {})'.format(gw.ip_addr))
  print(' 2 - Install English language patch')
  print(' 3 - Uninstall English language patch')
  print(' 0 - Exit')

def menu_process(id):
  if id == 1: 
    ip_addr = input("Enter router IP address: ")
    return [ "gateway.py", ip_addr ]
  if id == 2: return "install_lang.py"
  if id == 3: return [ "install_lang.py", "uninstall" ]
  if id == 0: sys.exit(0)
  return None

def menu_choice():
  menu_show()
  return 'Choice: '

def menu():
  level = 1
  while True:
    print('')
    prompt = menu_choice()
    print('')
    select = input(prompt)
    print('')
    if not select:
      continue
    try:
      id = int(select)
    except Exception:
      id = -1
    if id < 0:
      continue
    cmd = menu_process(id)
    if not cmd:
      continue
    if isinstance(cmd, str):
      result = subprocess.run([sys.executable, cmd])
    else:  
      result = subprocess.run([sys.executable] + cmd)

menu()
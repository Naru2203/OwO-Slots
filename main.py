from colorama import init
init()
import time
import os
from os import system
import random
import re
import atexit
import json
try:
 from discum import *
except:
 import setup
 from discum import *
system('cls')
print("""\
░█████╗░░██╗░░░░░░░██╗░█████╗░  ░██████╗███████╗██╗░░░░░███████╗  ██████╗░░█████╗░████████╗
██╔══██╗░██║░░██╗░░██║██╔══██╗  ██╔════╝██╔════╝██║░░░░░██╔════╝  ██╔══██╗██╔══██╗╚══██╔══╝
██║░░██║░╚██╗████╗██╔╝██║░░██║  ╚█████╗░█████╗░░██║░░░░░█████╗░░  ██████╦╝██║░░██║░░░██║░░░
██║░░██║░░████╔═████║░██║░░██║  ░╚═══██╗██╔══╝░░██║░░░░░██╔══╝░░  ██╔══██╗██║░░██║░░░██║░░░
╚█████╔╝░░╚██╔╝░╚██╔╝░╚█████╔╝  ██████╔╝███████╗███████╗██║░░░░░  ██████╦╝╚█████╔╝░░░██║░░░
░╚════╝░░░░╚═╝░░░╚═╝░░░╚════╝░  ╚═════╝░╚══════╝╚══════╝╚═╝░░░░░  ╚═════╝░░╚════╝░░░░╚═╝░░░
**Version: Slots **""")
time.sleep(0.5)
class client:
  stopped = False
  totalcmd = 0
  totalwon = 0
  class color:
    purple = '\033[95m'
    blue = '\033[94m'
    cyan = '\033[96m'
    green = '\033[92m'
    yellow = '\033[93m'
    red = '\033[91m'
    reset = '\033[0m'
    bold = '\033[1m'
    underline = '\033[4m'
  with open('settings.json', "r") as file:
        data = json.load(file)
        token = data["token"]
        channel = data["channel"]
        bet = int(data["bet"])
        rate = int(data["rate"])
  current_bet = bet
  if data["token"] and data["channel"] == 'nothing':
   print(f"{color.red} !!! [ERROR] !!! {color.reset} Please Enter Information To Continue")
   time.sleep(1)
   from newdata import menu
   menu()
  print('=========================')
  print('|                       |')
  print(f'| [1] {color.purple}Load data         {color.reset}|')
  print(f'| [2] {color.purple}Create new data   {color.reset}|')
  print(f'| [3] {color.purple}Credit            {color.reset}|')
  print('=========================')
  time.sleep(1)
choice = input('Enter your choice: ')
if choice == "1":
      pass
elif choice == "2":
      from newdata import menu
      menu()
elif choice == "3":
      print(f'{client.color.okcyan} =========Credit=========={client.color.reset}')
      print(f'{client.color.purple} [Developer] {client.color.reset} ahihiyou20')
      print(f'{client.color.purple} [Developer] {client.color.reset} Naru2203')
      time.sleep(10)
      exit()
else:
     print(f'{client.color.red} !! [ERROR] !! {client.color.reset} Wrong input!')
     time.sleep(2)
     exit()
def at():
  return f'\033[0;43m{time.strftime("%d %b %Y %H:%M:%S", time.localtime())}\033[0;21m'
bot = discum.Client(token=client.token, log=False)
@bot.gateway.command

def on_ready(resp):
    if resp.event.ready_supplemental:
        user = bot.gateway.session.user
        print("Logged in as {}#{}".format(user['username'], user['discriminator']))

@bot.gateway.command
def issuechecker(resp):
 if resp.event.message:
   m = resp.parsed.auto()
   if m['channel_id'] == client.channel:
    if m['author']['id'] == '408785106942164992' or m['author']['username'] == 'OwO' or m['author']['discriminator'] == '8456' or m['author']['public_flags'] == '65536':
     if 'captcha' in m['content']:
      print(f'{at()}{client.color.yellow} !! [CAPTCHA] !! {client.color.reset} CAPTCHA   ACTION REQUİRED')
      bot.gateway.close()
     if '(2/5)' in m['content']:
      print(f'{at()}{client.color.yellow} !! [CAPTCHA] !! {client.color.reset} CAPTCHA   ACTION REQUİRED (2/5)')
      bot.gateway.close()
     if '(3/5)' in m['content']:
      print(f'{at()}{client.color.yellow} !! [CAPTCHA] !! {client.color.reset} CAPTCHA   ACTION REQUİRED (3/5)')
      bot.gateway.close()
     if '(4/5)' in m['content']:
      print(f'{at()}{client.color.yellow} !! [CAPTCHA] !! {client.color.reset} CAPTCHA   ACTION REQUİRED (4/5)')
      bot.gateway.close()
     if '(5/5)' in m['content']:
      print(f'{at()}{client.color.yellow} !! [CAPTCHA] !! {client.color.reset} CAPTCHA   ACTION REQUİRED (5/5)')
      bot.gateway.close()
     if 'banned' in m['content']:
      print(f'{at()}{client.color.red} !!! [BANNED] !!! {client.color.reset} your account have been banned from owo bot please open a issue on the Support Discord server')
      bot.gateway.close()
     if 'complete your captcha to verify that you are human!' in m['content']:
      print(f'{at()}{client.color.yellow} !! [CAPTCHA] !! {client.color.reset} CAPTCHA   ACTION REQUİRED')
      bot.gateway.close()
     if 'you currently have' in m['content']:
      issuechecker.cash = re.findall('[0-9]+', m['content'])
      print("{}You currently have: {} Cowoncy! {}".format(client.color.cyan,','.join(issuechecker.cash[1::]),client.color.reset))
      client.totalwon = int(''.join(issuechecker.cash[1::]))
      

def cash():
    bot.sendMessage(str(client.channel), "owo cash ")
    client.stopped = True
        
@bot.gateway.command
def check(resp):
  if resp.event.message_updated:
   m = resp.parsed.auto()
   if m['channel_id'] == client.channel:
    if m['author']['id'] == '408785106942164992' or m['author']['username'] == 'OwO' or m['author']['discriminator'] == '8456' or m['author']['public_flags'] == '65536':
      if ' and won <:cowoncy:416043450337853441> 'in m['content']and '**`___SLOTS___  `**\n<:eggplant:417475705719226369> <:eggplant:417475705719226369> <:eggplant:417475705719226369>' not in m['content']and '**`___SLOTS___  `**\n<:cowoncy:417475705912426496> <:cowoncy:417475705912426496> <:cowoncy:417475705912426496>'not in m['content']and '**`___SLOTS___  `**\n<:cherry:417475705178161162> <:cherry:417475705178161162> <:cherry:417475705178161162>'not in m['content']and '**`___SLOTS___  `**\n<:o:417475705899843604 > <:w_:417475705920684053> <:o_:417475705899843604>'not in m['content']:
       client.totalwon += client.current_bet
       print("{}[INFO] Won: {} Cowoncy {}/{} Current: {:,} Cowoncy {}".format(client.color.green,client.current_bet,client.color.reset,client.color.cyan,client.totalwon,client.color.reset))
       client.current_bet = client.bet
      if ' and won nothing... :c' in m['content']:
       client.totalwon -= client.current_bet
       print("{}[INFO] Lost: {} Cowoncy {}/{} Current: {:,} Cowoncy {}".format(client.color.red,client.current_bet,client.color.reset,client.color.cyan,client.totalwon,client.color.reset))
       client.current_bet *= client.rate
      if'**`___SLOTS___  `**\n<:eggplant:417475705719226369> <:eggplant:417475705719226369> <:eggplant:417475705719226369>' in m['content']:
              print("{}[INFO] Draw: {} Cowoncy {}/{} Current: {:,} Cowoncy {}".format(client.color.green,client.current_bet,client.color.reset,client.color.cyan,client.totalwon,client.color.reset))
      if'**`___SLOTS___  `**\n<:cherry:417475705178161162> <:cherry:417475705178161162> <:cherry:417475705178161162>' in m['content']:
              client.totalwon += client.current_bet * 2
              print("{}[INFO] Won x 3: {} Cowoncy {}/{} Current: {:,} Cowoncy {}".format(client.color.green,client.current_bet * 3,client.color.reset,client.color.cyan,client.totalwon,client.color.reset))
              client.current_bet = client.bet
      if'**`___SLOTS___  `**\n<:cowoncy:417475705912426496> <:cowoncy:417475705912426496> <:cowoncy:417475705912426496>' in m['content']:
              client.totalwon += client.current_bet * 3
              print("{}[INFO] Won x 4: {} Cowoncy {}/{} Current: {:,} Cowoncy {}".format(client.color.green,client.current_bet * 4,client.color.reset,client.color.cyan,client.totalwon,client.color.reset))
              client.current_bet = client.bet
      if'**`___SLOTS___  `**\n<:o:417475705899843604 > <:w_:417475705920684053> <:o_:417475705899843604>' in m['content']:
              client.totalwon += client.current_bet * 9
              print("{}[INFO] Won x 10: {} Cowoncy {}/{} Current: {:,} Cowoncy {}".format(client.color.green,client.current_bet * 10,client.color.reset,client.color.cyan,client.totalwon,client.color.reset))
              client.current_bet = client.bet
def s():
 
  bot.sendMessage(str(client.channel), "owo s {}  ".format(client.current_bet))
  print("{} {} [SENT] owo s {}  {}".format(at(),client.color.yellow,client.current_bet,client.color.reset))
  time.sleep(15)
  if client.current_bet  > 300000:
    client.current_bet = client.bet
    
@bot.gateway.command
def loopie(resp):
 if resp.event.ready:
  x=True
  main=time.time()
  while x:
      if client.stopped == False:
          cash()
      time.sleep(1)
      s()
       
bot.gateway.run(auto_reconnect=True)


#!/usr/bin/env python

# camel.py - a camel roulette game for chedder

import random

deaths = ("gets a generous portion of spit in their face.", "'s face is covered by camel phlegm.")

slapreply = ("A single tear runs down the camels face", "The camel looks at you knowingly", "The camel bares it's teeth")

thingstohold = ("spork", "cork", "york", "bjork", "fork")

def setup(self):
  self.camel={}
  self.camel['run']=False

def stroke(phenny, input):
  gun = phenny.camel['gun']
  pos = random.randint(0,len(gun)-1)
  gun = gun[pos:]+gun[:pos]
  phenny.camel['gun']=gun

def rrcamel(phenny, input):
  if phenny.camel['run']:
    return "You already have camel!"  
  bullets = 1
  chambers = 6
  try:
    params = input.split(" ")
    bullets = int(params[1])
    chambers = int(params[2])
  except:
    pass
  chambers = max(2,min(chambers,100))
  bullets = max(1,min(bullets,100))
  if bullets > chambers:
    bullets = chambers
  gun = [False]*chambers
  for bullet in range(0,bullets):
    gun[bullet]=True
  phenny.camel['gun']=gun
  stroke(phenny, input)
  phenny.camel['run']=True
  strbul = str(bullets) + ((bullets == 1) and " bullet" or " bullets")
  strcha = str(chambers) + ((chambers == 1) and " chamber" or " chambers")
  phenny.say("I sell you very nice camel. Please, slap or stroke him, very nice.")
rrcamel.commands=["camel"]
rrcamel.thread=False

def rrstroke(phenny, input):
  if phenny.camel['run']:
    stroke(phenny, input)
    phenny.say("The camel purrs.")
rrstroke.commands=["stroke"]
rrstroke.thread=False

def rrfeed(phenny, input):
  if phenny.camel['run']:
    stroke(phenny, input)
    phenny.say("The camel noms your delicious foods.")
rrfeed.commands=["feed"]
rrfeed.thread=False


def rrhold(phenny, input):
  if phenny.camel['run']:
    phenny.say("**The camel holds up a "+random.choice(thingstohold)+"**")
rrhold.commands=["hold"]
rrhold.thread=False

def rrslap(phenny, input):
  if phenny.camel['run']:
    gun = phenny.camel['gun']
    next = gun[0]
    if next:
      phenny.say("*SPIT* "+input.nick+" "+random.choice(deaths))
      phenny.camel['run']=False
    else:
      phenny.say(random.choice(slapreply))
      gun = gun[1:]+gun[:1]
      phenny.camel['gun']=gun
  else:
    phenny.say("Why are you slapping the air?")
    phenny.say("You have no camel you silly scallywag!")
rrslap.commands=["slap"]
rrslap.thread=False

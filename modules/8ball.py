#!/usr/bin/env python
"""
8ball.py - 8ball script
About: http://inamidst.com/phenny

.8ball -> returns the number of questions it received.
.8ball <question>? -> 8ball magic!
"""

import random
import re

#countFile = '/home/vaicine/phenny/8ballcount'
responses = [
  'Yes.',
  'No.',
  'Possibly.',
  'Absolutely!',
  'Absolutely not!',
  'Perhaps.',
  'Please try again.',
  'You can count on it.',
  'Don\'t count on it.',
  'Sure.',
  'Nope.',
  'Maybe.',
  'It depends on the weather.',
  'The outlook is good.',
  'The outlook is not so good.',
  'Always.',
  'Never.',
  'Of course.',
  'Of course not.',
  'Hell yes!',
  'Hell no!'
]

def eightball(phenny, input):
  request = input.group(2)

  # .8ball
  if request == None:
    # count = getCount(countFile)
    phenny.reply('Ask me a question!')

  # User gave an argument to .8ball
  else:
    # .8ball <question>?
    result = re.search(r".*\?$", request)
    if result != None:
      # updateCount(countFile)
      phenny.reply(random.choice(responses))
    # User didn't ask a proper question.
    else:
      phenny.reply('.8ball [<yes/no question>?]')
eightball.commands = ['8ball']

#def getCount(file=countFile):
#  f = open(file, 'r')
#  c = f.read()
#  f.close()
#  return c.strip()
  
#def updateCount(file=countFile):
  # Cast into int to increment, then recast to str to write.
#   count = int(getCount(file)) + 1
  
  
#  f = open(file, 'w')
#  f.write(str(count))
#  f.close()

if __name__ == '__main__':
  print __doc__.strip()

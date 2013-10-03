Chedder
=======

### The infamous #photoshop @ irc.quakenet.org IRC bot. ###

![Cheese](http://github.com/vaicine/chedder/raw/master/cheese.jpg)

**Chedder** bot is a fork of [Phenny](https://github.com/sbp/phenny) by the wonderful [sbp](https://github.com/sbp) ❤

### List of commands: ###

* .8ball <yes/no question> - Chedder will speak to the gods and find the answer to your question
* .bitly <url> - Generate bitly URL for a given <url>
* .c <query> - Query Google calculator
* .camel - Starts camel trading game
  * .feed - Feed your camel (Might make the camel less likely to spit on you)
  * .hold - Ask your camel to hold something
  * .slap - Slap your camel (warning, camel might spit on you)
  * .stroke - Stroke your camel (Might make the camel less likely to spit on you)

* .commands - Lists phennys basic commands
* .doc - Shows a command's documentation, and possibly an example
* .help - Tells you what for and links you to the github page with all the commands

* .ety - Look up the etymology of a word
* .g - Search on Google
* .gc - Get the number of results on Google

* .in - Set a reminder
* .load - Starts russian roulette game
  * .spin - Spin the barrel and offset the bullet
  * .pull/rr/suicide/die - Pull the trigger
* .morning - Say good morning to Chedder!
* .o answers {question} - Get yahoo answers goodness
* .o lastfm {nick} - Returns lastfm info for a user
* .o ud {term} - Returns urban dictionary definition of a given term
* .seen <nick> - Reports when <nick> was last seen
* .t - Return the current time
* .title - Get the title of a link
* .u - Search for a unicode character
* .w - Get a definition of a word
* .wa - Query Wolfram Alpha
* .wiki - Search for something on Wikipedia

* <greeting> chedder - Say <greeting> to chedder and get a reply
* chedder: tell <nick> <message> - When the <nick> speaks on the channel, chedder will tell the user <message>
* chedder: "<message>"? - Translate a phrase

### To run your own "Bot à la fromage" ###

1. ```$ git clone git://github.com/vaicine/chedder.git ~/fridge/chedder```
2. Run ./phenny - this creates a default config file
3. Edit ~/.phenny/default.py
4. Run ./phenny - this now runs phenny with your settings

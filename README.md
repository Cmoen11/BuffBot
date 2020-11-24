<!-- [![Coverage Status](https://coveralls.io/repos/github/Cmoen11/BuffBot/badge.svg?branch=master)](https://coveralls.io/github/Cmoen11/BuffBot?branch=master) -->
[![GitHub version](https://badge.fury.io/gh/cmoen11%2Fbuffbot.svg)](https://badge.fury.io/gh/cmoen11%2Fbuffbot)
[![Build Status](https://travis-ci.org/Cmoen11/BuffBot.svg?branch=master)](https://travis-ci.org/Cmoen11/BuffBot)
[![](https://img.shields.io/github/issues-closed-raw/badges/shields.svg)]()
[![NetflixOSS Lifecycle](https://img.shields.io/osslifecycle/Netflix/osstracker.svg)]()
[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=102)](https://github.com/Cmoen11/BuffBot/)
[![Open Source Love](https://badges.frapsoft.com/os/gpl/gpl.svg?v=102)](https://github.com/Cmoen11/BuffBot/blob/master/LICENSE)


# BuffBot 🐍🤖
Discord is a great communication software itself, however, it does not provide some much wanted features. Some Discord servers may have several hundred members, if all of these users were to join the same voice channel, there would likely be several conversations taking place at the same time. On the other hand, some voice channels may have as little as one, two or three participants, opening the possibility for awkward silent moments.
 
Would it not be great if users could share their music with their fellow gamers, especially during awkward silent moments? Would it not be great if players were automatically sorted into voice channels allocated the game they are playing, instead of everyone manually creating and changing voice channels? 
 
BuffBot is the solution to these lacking features. BuffBot provides features like streaming music into voice channels, queuing songs to a playlist, administrate users into voice channels based on what they do, a global server economy, interacting with the bot through mini games that can earn you an advantage in the global server economy.
!💪 <br>

<img src="https://i.gyazo.com/a11b08dbc9b4cc8ee13b6a8dc1adba58.png"/>

We have many great features we would like to implement to the bot in the future, such as an [online management tool UI](https://github.com/Cmoen11/BuffBot/issues/56).   
We'd love your help, whether you've got a bug or a feature you'd like fixed, or if you'd like to contribute through developing the BuffBot yourself. <br>
<b>However</b>, please read and respect the [Contribution](#contribution) first.
## Table of contents 📍

* [Quick start](#quick-start-)
* [Commands](#commands)
* [Documentation](#documentation-)
* [Folder structure](#folder-structure)
* [Contribution](#contribution)
* [Licence](#licence-)
* [Credits](#credits-for-open-repositories)


## Quick start 💡
- You need to have ffmpeg installed on your machine.. [Tutorial for FFmpeg(Windows)](http://www.hongkiat.com/blog/ffmpeg-guide/). <br> And for ubuntu and mac users.. [Tutorial for ubuntu FFmpeg ](https://medium.com/portfolio-of-bilash/install-ffmpeg-on-ubuntu-mac-os-98588f3251d7)
- [You also need python 3.x.](https://www.python.org/downloads/)
- Open terminal.. you have some pip install(s) to do!

For windows/ubuntu people<br>
`pip install libffi-dev`<br>
`pip install discord.py[voice]`<br>
`pip install youtube-dl`<br>
`pip install simpleeval`<br>
<br>

For mac people!<br>
`pip install discord.py[voice]`<br>
`pip install youtube-dl`<br>
`pip install simpleeval`<br>
`brew install ffmpeg`<br>
`brew install opus`<br>
`brew install libffi`<br>
`brew install libsodium`<br>
`And then open up python3.6 package and run Install Certificates.command`<br>

Finally download the latest files from the project and open your terminal and write python main.py

- Now add your bot token in the file located `botconfig/__init__.py`

### Docker install
If you're not going to develop any new feature to BuffBot and just want to enjoy the features of BuffBot. Please download the zip from the newest release(or whatever version you prefer). Then build your project, edit `BuffBot/botconfig/__init__.py` and add your Bot token.
Then run `docker build -t buffbot_docker .` from your command prompt.  

## Commands 
Head over to the [documentation for commands](https://github.com/Cmoen11/BuffBot/wiki/Commands) to see an extensive list of available commands.


## Documentation 📝 
https://github.com/Cmoen11/BuffBot/wiki 

## Folder structure 
The folder structure is based on having all of the command modules in the root directory, while assisting modules
and files are separated in different directories, such as db and unittest. <br> 
<img src ="http://i.imgur.com/5shUrVr.png"/>

## Contribution 
Would you also like to contribute to BuffBot? Please follow our guidelines for reporting bugs and wanted features, in addition to
how you can contribute through pull requests.
These guidelines helps you communicate to us in an efficient way, that hopefully will improve the project.
<br> <a href="http://discordpy.readthedocs.io/en/latest/api.html#user"> If you're hooked and will dive into Buffbot with us, you find alot of documentation on the API we're using</a>

<h2>Bugs and feature requests</h2>
If you've got a bug or feature request, please respect these restrictions:
* Keep the discussion on topic.
* Please do not open issues if there are segment(s) of code you do not understand that you would like explained to you. <br> 
This is <b>not</b> the purpose of these requests. 


### Bug reports ❌
Definition of a bug: A bug is an error, failure or fault in the program caused by the sourcecode in this repository, resulting the program to produce an incorrect or unexcepted result, or to behave in unintended ways.
<br> We rely on good bug reports, so in advance, thank you for your contribution!
* Search through the [issue tracker](https://github.com/Cmoen11/BuffBot/issues) for the bug or feature you wish to submit. Duplication of requests like these takes time from developers, we'd rather spend on developing the bot.
* Pull the latest 'master' or 'development branch to check if the bug is fixed.
* Isolate the problem. One issue equals one bug.
* Please use the following format:
<br>
<b> Long story short </b>
<br>
<i> ... </i>
<br>
<b> Expected behaviour </b>
<br>
<i> ... </i>
<br>
<b> Actual Behaviour </b>
<br>
<i> ... </i>
<br>
<b> Steps to reproduce </b>
<br>
<i> ... </i>
<br>
<b> Your environment </b>
<br>
<i> OS, Ptyhon version and more if necessarily </i>

### Feature requests 💡
We're open for new features, but keep in mind the scope and relevance of the BuffBot. E.g. We will not implement changes in Discord's UI beyond what's already in the Discord API, as it neither is relevant nor in the scope of this project.
<br>Details<br> is heavily encouraged when opening a feature request, they make it much easier for the developers to understand the scope of the request.


### Pull requests 📥
If the issue you would like to implement does not exist, you must follow the model below. If the issue on the other does
exist, you can ignore the first process in the model.
<img src ="http://i.imgur.com/qTpg9Hf.png"/>
<ul>
<li> Create feature branch</li>
<li> Documentent all code </li>
<li> Follow standards and conventions </li>
<li> All code, except command functions that does not have a return value, must have unittests. These must be implemented in the unitTests folder. </li>
<li> All modules must declare the if__name__ == "__main__":. Sharing is caring!  </li>
<li> Before creating a pull request, pull the latest master</li>
</ul>
<b>Requirements for creating a pull request:</b> <br>
<ul>
<li> Describe the feature(s) you've included in the pull request as detailed as possible. </li>
<li> Tag the related issue(s). </li>
<li> Request <b>two</b> known contributors for their reviews. </li>
<li> Respond to reviewers. </li>
<li> Did your pull request get approved? Awesome, now please document the feature in our wiki</li>
</ul>
<br>


## Licence 📋
[GPL3.0](https://github.com/Cmoen11/BuffBot/blob/master/LICENSE)


## Credits for open repositories 
https://github.com/Rapptz/discord.py

Structure of Github project, considering issues, pull requests and general documentations: https://github.com/twbs/bootstrap

# BuffBot

BuffBot is an open source bot for Discord written in Python 3.6. We'd love your help, wheter you've got a bug or a feature you'd  like fixed, or if you'd like to contribute through developing the BuffBot yourself. <b>However</b>, please read and respect the [Contribution](#contribution) first.

## Table of contents

* [Quick start](#quick-start)
* [Commands](#commands)
* [Documentation](#documentation)
* [Features](#features)
* [Bugs and feature requests](#bugs-and-feature-requests)
* [Contribution](#contribution)
* [Licence](#licence)
* [Credits](#Credits-for-open-repositiories)

<br>

## Quick start
### Getting started, everything you need.
- You need to have ffmpeg installed on your machine.. [Tutorial for FFmpeg(Windows)](http://www.hongkiat.com/blog/ffmpeg-guide/). <br> And for ubuntu and mac users.. [Tutorial for mac and ubuntu for FFmpeg ](https://medium.com/portfolio-of-bilash/install-ffmpeg-on-ubuntu-mac-os-98588f3251d7)
- [You also need python 3.x.](https://www.python.org/downloads/)
- Open terminal.. you have some pip install(s) to do!
- pip install libffi-dev
- pip install discord.py[voice]
- pip install youtube-dl
- pip install dataset
- pip install simpleeval
<br>
Finally download the latest files from the project and open your terminal and write python main.py

- Now add your bot token in the file located `botconfig/__init__.py`



<br><br>
## Commands
Head over to the [documentation for commands](https://github.com/Cmoen11/BuffBot/wiki/Commands) to see an extensive list of available commands.



## Documentation
https://github.com/Cmoen11/BuffBot/wiki 



## Features 
stuff will be added


## Contribution
Would you also like to contribute to BuffBot? Please follow our guidelines for reporting bugs and wanted features, in addition to
how you can contribute through pull requests.
These guidelines helps you communicate to us in an efficient way, that hopefully will improve the project.
<br>
## Bugs and feature requests
If you've got a bug or feature request, please respect these restrictions:
* Keep the discussion on topic.
* Do not open issues if there are segment(s) of code you do not understand. This is <br> not </br> the purpose of these requests.
More restrictions will be added as the project lifetime expands.


### Bug reports
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
<b> Your enviroment </b>
<br>
<i> OS, ptyhon version and more if neccesarily </i>

### Feature requests
We're open for new features, but keep in mind the scope and relevance of the BuffBot. E.g. We will not implement changes in Discord's UI beyond what's already in the Discord API, as it neither is relevant nor in the scope of this project.
<br>Details<br> is heavily encouraged when opening a feature request, they make it much easier for the developers to understand the scope of the request.

<br>
### Pull requests 
* All code should be documentented
* New features should be explained in detail in the wiki-page
* All code, except command functions that does not have a return value, must have unittests. These must be implemented in the unitTests folder. 
* All modules must declare the if__name__ == "__main__":. Sharing is caring!  


## Licence
[GPL3.0](https://github.com/Cmoen11/BuffBot/blob/master/LICENSE)


## Credits for open repositiories 
https://github.com/Rapptz/discord.py

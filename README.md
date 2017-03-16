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
* [Credits](#credits)


<br>

## Quick start
apt install python3 python3-pip libffi-dev ffmpeg
pip3 install discord.py[voice] youtube-dl dataset simpleeval

1. You'll need atleast to have Python 3.x installed
2. You'll also need to install the Discord API wrapper. Do this by run the following command.
python3 -m pip install -U https://github.com/Rapptz/discord.py/archive/master.zip#egg=discord.py[voice]
3. Download the zipped project
4. Rename the folder named `botconfig_example` to `botconfig`
5. Open `botconfig/__init__.py` and insert your bot's token into the `token` variable, this you'll get from [Discord development page](https://discordapp.com/developers/applications/me/). You'll need to create a new application and add a bot to recive your bot token.
7. Save the file and open your terminal
8. navigate to your bot-files and write `python3 main.py`

<br><br>
## Commands
Command | What it does | Who can do it?
--- | --- | ---
`!help` | Gives a list of all of the commands | Everyone
`!math <math question>` | Can do nearly everything you want in math | Everyone
`!summon` | Bot will join your channel if you're in a voice channel | Restricted
`!leaveChannel` | Bot will leave your channel | Restricted
`!patrol` | Bot will set people in jail if they do not currently play a game | Restricted
`!play <music link> ` | Bot will join your channel and start playing fine tunes. It require a link to the music source. | Restricted
`!stop` | Bot will stop playing music. | Restricted
`!setvolume <a number between 0 - 100>`| Bot will change the volume to the given prosent | Restricted
`!smug`| Bot will reply with a smug image | Everyone
`!smugadd <a http link to image that are to be added>` | needs link to a image, and will add it to the smug list | Restricted

Usergroups | # |
--- | ---
Everyone | Everyone in the channel, default usergroup
Restricted | Restricted accsess. default the owner of the bot


<br>
<h2> Documentation</h2>
Grundig forklaring av installasjon og bruk.


<br>
<h2> Features </h2>
stuff will be added

<br>
<h2> Contribution</h2>
Would you also like to contribute to BuffBot? Please follow our guidelines for reporting bugs and wanted features, in addition to
how you can contribute through pull requests.
These guidelines helps you communicate to us in an efficient way, that hopefully will improve the project.
<br>
<h2> Bugs and feature requests</h2>
If you've got a bug or feature request, please respect these restrictions:
* Keep the discussion on topic.
* Do not open issues if there are segment(s) of code you do not understand. This is <br> not </br> the purpose of these requests.
More restrictions will be added as the project lifetime expands.
<br>

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

<h2> Feature requests </h2>
We're open for new features, but keep in mind the scope and relevance of the BuffBot. E.g. We will not implement changes in Discord's UI beyond what's already in the Discord API, as it neither is relevant nor in the scope of this project.
<br>Details<br> is heavily encouraged when opening a feature request, they make it much easier for the developers to understand the scope of the request.

<br>
<h2> Pull requests </h2>
* All code should be documentented
* New features should be explained in detail in the wiki-page
<br>

Her må det legges til hvordan folk kan gjennomføre pullrequests. Skal de forke? osv. @Moen


<br>
<h2>Licence </h2>
[GPL3.0](https://github.com/Cmoen11/BuffBot/blob/master/LICENSE)

<br>

<h2> Credits for open repositiories </h2>
- https://github.com/Rapptz/discord.py

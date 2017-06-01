# Uses predefined setup from:
# https://github.com/docker-library/python/blob/cd1f11aa745a05ddf6329678d5b12a097084681b/3.6/Dockerfile
# This Dockerfile assumues you have copied the buffbot repo onto your server, and run this command from
# the root of the directory.

# From latest official, stable build
FROM python:3.6.1
MAINTAINER martiv15@uia.no

# Creates root directory of image
RUN mkdir -p /discord_bot

# Copies source into the image
COPY . /discord_bot

# Sets the root for upcoming commands // where the main.py is located
WORKDIR /discord_bot/BuffBot

# Fetches dependencies
#RUN pip install libffi-dev
RUN pip install discord.py[voice]
RUN pip install youtube-dl
RUN pip install simpleeval

# Builds the binary on docker build
RUN python main.py


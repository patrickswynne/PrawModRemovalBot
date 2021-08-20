# -*- coding: utf-8 -*-
"""
Created on Wed Apr 21 16:21:08 2021
This program will write out {n} post submissions from a target subreddit
lines will identify posts that have been removed by the mods
the idea here is to get an idea about what mods are removing, we'll start with that

in order to run this you will need a txt config file
[praw-config]
client_id = <client_id>
client_secret = <client_secret>
password = <password>
username = <username>
@author: Patrick Wynne
"""

from pprint import pprint

import nltk
import praw
from praw.models import MoreComments
import configparser

def get_config_dict():
    config = configparser.RawConfigParser()   
    config.readfp(open(r'config.txt'))
    details_dict = dict(config.items('praw-config'))
    if not hasattr(get_config_dict, 'config_dict'):
        get_config_dict.config_dict = dict(config.items('praw-config'))
    return get_config_dict.config_dict

config_details = get_config_dict()

def login():
    reddit = praw.Reddit(
        client_id= config_details['client_id'],
        client_secret= config_details['client_secret'],
        password= config_details['password'],
        user_agent= "PyEng Bot",
        username= config_details['username'],
    )
    print("logged in")
    return reddit

def getOccurrencePosts(occurences):
    with open('readme.txt', 'w') as f:
        f.write('')
    
    for submission in reddit.subreddit("nonewnormal").new(limit=occurences):
        with open('readme.txt', 'a') as f:
            f.writelines('\n' + str(0) + " " +  submission.id + " " 
                    + str(submission.created) + " " 
                    + str(submission.title) + " " 
                    + str(submission.permalink)
                    )

reddit = login()
getOccurrencePosts(3)
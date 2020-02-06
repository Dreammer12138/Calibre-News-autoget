#!/usr/bin/python3 
# Name: 		Calibre News Get
# Author:		Dreammer12138
# Github:		https://github.com/dreammer12138
# Description:	read an write config file
# -*- coding: utf-8 -*-

import json
import configset

def readconfig(path) :
	config_file = open(path, encoding = "utf-8")
	config = json.loads(config_file.read())
	config_file.close()
	return config

def writeconfig(path, config) :
	config_file = open(path, encoding = "utf-8", mode = "w")
	json.dump(config, config_file)
	config_file.close()

def add_recipe(path, config_path, recipe, url) :
	file = open(path, encoding = "utf-8", mode = "w+")
	file.writelines("#!/usr/bin/python3" + "\n")
	file.writelines("# -*- coding: utf-8 -*-" + "\n")
	file.writelines("from __future__ import unicode_literals, division, absolute_import, print_function" + "\n")
	file.writelines("from calibre.web.feeds.news import BasicNewsRecipe" + "\n")
	file.writelines("class AdvancedUserRecipe1580964349(BasicNewsRecipe):" + "\n")
	file.writelines("\t" + "title = '{}'".format(recipe) + "\n")
	file.writelines("\t" + "oldest_article = 7" + "\n")
	file.writelines("\t" + "max_articles_per_feed = 100" + "\n")
	file.writelines("\t" + "auto_cleanup   = True" + "\n")
	file.writelines("\t" + "feeds = [" + "\n")

	file.writelines("\t\t" + "('{}', '{}')".format(recipe, url) + "\n")

	file.writelines("\t" + "]")

	file.close()


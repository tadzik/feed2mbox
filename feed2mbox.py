#!/usr/bin/python
# -*- coding: utf-8 -*-
import feedparser
from time import mktime,strftime,localtime
from os import getenv

def getstamp(x):
    return int(mktime(x.updated_parsed))

# loading feeds data
def loaddata():
	h = {} # new empty hash (or how pythoners say, 'dictionary')
	f = open(getenv("HOME")+"/.config/feed2mbox", "r")
	for line in f:
		t = line.partition(' ')
		if(t[2] != ''):
			h[t[0]] = int(t[2])
	f.close()
	return h

# saving data back to file
def writedata(hash):
	f = open(getenv("HOME")+"/.config/feed2mbox", "w")
	for key in hash:
		f.write(key+" "+str(hash[key])+"\n")
	f.close()

#
# main
#
data = loaddata()
for key in data: # iterating through feed list
	feed = feedparser.parse(key)
	oldest = 0;
	for entry in feed.entries:
		if(getstamp(entry) > oldest):
			oldest = getstamp(entry)
		if(getstamp(entry) > data[key]):
			# printing in mbox format (kinda)
			print "From feed2mbox "+strftime("%a %b %d %H:%M:%S %Y",
			                                 localtime())
			print "From: "+feed.feed.title.encode('utf-8')
			print "Date: "+entry.updated
			print "Subject: "+entry.title.encode('utf-8')
			if hasattr(entry, 'summary'):
				print entry.summary.encode('utf-8')
			print "\nLink: "+entry.link+"\n"
	# updating timestamp
	data[key] = oldest
writedata(data)

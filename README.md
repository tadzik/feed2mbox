Description
===========

This little script fetches your favourite rss/atom feeds and delivers to some local mbox. The feed urls are stored in $HOME/.config/feed2mbox in the following format:

http://some.feed.url/ <timestamp>

So if you want to add a new feed, just add a line to a file like this:

http://feeds.feedburner.com/github 0

And feed2mbox will update the timestamp itself. Maybe some 'add' option will appear in the future.

Usage
=====

feed2mbox.py >> Mail/rss

(or wherever your mailbox is).

Notes
=====

Please note that I'm not a python programmer at all, I'm writing this in python only because there's no good Perl module for feeds, and the existing scripts sucked so hard I couldn't stand even looking at them, not to mention using.

Every constructive criticism will be happily welcome.

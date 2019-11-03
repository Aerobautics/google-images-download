#!/usr/bin/env python3
# Written by Stewart Nash (Aerobautics) November 2019
"""Provides a session for GID.
"""
import sys
import os
import errno
import time
sys.path.insert(1, '../')
from google_images_download import google_images_download

#https://tkdocs.com/index.html

# GID stands for 'Google Image Downloader'

class GidSession:
	'This class encapsulates all of the information for a GID session. It is used by the GUI interface.'
	currentIndex = 0

	def __init__(self):
		self.gidPictures = []
		self.keyword = ""
		self.sessionIndex = 0
		self.thumbnail_only = False

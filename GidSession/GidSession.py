#!/usr/bin/env python3
# Written by Stewart Nash (Aerobautics) November 2019
"""Provides a session for GID.
"""
import sys
import os
import errno
import time
import uuid
sys.path.insert(1, '../')
from google_images_download import google_images_download

#https://google-images-download.readthedocs.io/en/latest/index.html

# GID stands for 'Google Image Downloader'

class GidSession:
	'This class encapsulates all of the information for a GID session. It is used by the GUI interface.'
	searchIndex = 0

	def __init__(self):
		self.searches = [] #GidSearch() xN

	def search(self, input_settings = GidSettings()):
		self.searches.append(GidSearch(input_settings))
		


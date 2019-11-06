#!/usr/bin/env python3
# Written by Stewart Nash (Aerobautics) November 2019
"""Encapsulates a search for GID.
"""
import sys
import os
import errno
import time
sys.path.insert(1, '../')
from google_images_download import google_images_download

#https://google-images-download.readthedocs.io/en/latest/index.html

# GID stands for 'Google Image Downloader'

class GidSearch:
	'This class contains information for a search performed in a GID session. It is used by the GID session and the GUI interface.'
	currentIndex = 0

	def __init__(self, input_settings = GidSettings()):
		#self.gidResults = [] #GidResult() xN
		self.results = None #GidResult() xN
		self.identity = None #uuid.uuid()
		#self.uniqueIdentifier = self.identity
		self.currentPictureIndex = 0
		self.settings = input_settings #GidSettings()


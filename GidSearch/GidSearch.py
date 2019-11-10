#!/usr/bin/env python3
# Written by Stewart Nash (Aerobautics) November 2019
"""Encapsulates a search for GID.
"""
import sys
import os
import errno
import time
import uuid
sys.path.insert(1, '../')
from google_images_download import google_images_download
from GidResult import GidResult
from GidSettings import GidSettings

#https://google-images-download.readthedocs.io/en/latest/index.html

# GID stands for 'Google Image Downloader'

class GidSearch:
	'This class contains information for a search performed in a GID session. It is used by the GID session and the GUI interface.'
	currentIndex = 0

	def __init__(self, input_settings = GidSettings.GidSettings()):
		#if input_settings is None:
		#	input_settings = GidSettings.GidSettings()
		#self.gidResults = [] #GidResult() xN
		self.results = None #GidResult() xN
		#self.identity = None #uuid.uuid()
		self.identity = str(uuid.uuid4())
		#self.uniqueIdentifier = self.identity
		self.currentPictureIndex = 0
		self.settings = input_settings #GidSettings()

	def addResult(self, input_result):
		if self.results is None:
			self.results = [input_result, ]
		else:
			self.results.append(input_result)

	def addItems(self, inputItems):
		for item in inputItems:
			if self.results is None:
				self.results = [GidResults(item), ]
			else:
				self.results.append(GidResults(item))


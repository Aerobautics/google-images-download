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
		self.sessionIndex = 0

		# Input parameters for 'google_images_download'
		# Can extract these to another search class
		self.config_file = None
		self.keywords = None
		self.keywords_from_file = None
		self.prefix_keywords = None
		self.suffix_keywords = None
		self.limit = None
		self.related_images = None
		self.format = None
		self.color = None
		self.color_type = None
		self.usage_rights = None
		self.size = None
		self.exact_size = None
		self.aspect_ration = None
		self.type = None
		self.time = None
		self.time_range = None
		self.delay = None
		self.url = None
		self.single_image = None
		self.output_directory = None
		self.image_directory = None
		self.no_directory = None
		self.proxy = None
		self.similar_images = None
		self.specific_site = None
		self.print_urls = None
		self.print_size = None
		self.print_paths = None
		self.metadata = None
		self.extract_metadata = None
		self.socket_timeout = None
		self.thumbnail = None
		self.thumbnail_only = None
		self.language = None
		self.prefix = None
		self.chromedriver = None
		self.safe_search = None
		self.no_numbering = None
		self.offset = None
		self.save_source = None
		self.no_download = None
		self.silent_mode = None
		self.ignore_urls = None
		self.help = None


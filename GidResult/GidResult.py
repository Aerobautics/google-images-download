#!/usr/bin/env python3
# Written by Stewart Nash (Aerobautics) November 2019
"""Provides a a result class for results in a search.
This was formerly a GidPicture class, but that was deemed too granular.
"""
from tkinter import *
import PIL
from PIL import ImageTk
from PIL import Image
from xml.dom.minidom import parse
import sys
import os
import errno
import time
import xml.dom.minidom
import tkinter.messagebox
sys.path.insert(1, '../')
from google_images_download import google_images_download

# GID stands for 'Google Image Downloader'

class GidResult:
	'This class encapsulates all of the information owned by an individual search result.'
	def __init__(self):
		self.picture = [] #GidPicture()
		self.thumbnail = [] #GidPicture()

		self.image_filename = []

		self.image_format = []
		self.image_height = []
		self.image_width = []
		self.image_link = []
		self.image_description = []
		self.image_host = []
		self.image_source = []
		self.image_thumbnail_url = []

#!/usr/bin/env python3
# Written by Stewart Nash (Aerobautics) November 2019
"""This file contains the GID Picture class. This class
holds all information related to an individual image.
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

class GidPicture:
	'This class encapsulates all of the information owned by an individual image.'
	def __init__(self):
		self.thumbnail = False
		self.location = None
		self.provenance = None
		self.provenance_size = None
		self.provenance_type = None
		self.alternate = None
		self.note = None

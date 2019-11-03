#!/usr/bin/env python3
# Written by Stewart Nash (Aerobautics) November 2019
"""Provides a picture class for pictures in session.
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
	'This class encapsulates all of the information owned by an individual downloaded image.'
	def __init__(self):
		self.imageNumber = 0
		self.fileName = ""
		self.fileOrigin = ""
		self.fileThumbnail = ""

#!/usr/bin/env python3
# Written by Stewart Nash (Aerobautics) November 2019
"""Provides string processing for GID.
"""
from tkinter import *
import sys
import os
import errno
import time
sys.path.insert(1, '../')
from google_images_download import google_images_download

# GID stands for 'Google Image Downloader'

class GidString:
	'This class processes strings.'
	def __init__(self):
		self.isSpaceRemoved = True	


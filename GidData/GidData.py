#!/usr/bin/env python3
# Written by Stewart Nash (Aerobautics) November 2019
"""XML data processing for GID.
"""
from tkinter import *
from xml.dom.minidom import parse
import sys
import os
import errno
import xml.dom.minidom
sys.path.insert(1, '../')
from google_images_download import google_images_download

# GID stands for 'Google Image Downloader'

class GidData:
	'This class contains the XML parsing functions.'
	def __init__(self):
		self.gidSession = []
		self.sessionList = []
		self._currentSession = []
		self.sessionFile = []

	def get_currentSession(self):
		return self.currentSession

	def set_currentSession(self, value):
		self._currentSession = value

	def createXmlString(self, input_items, input_directory):
		xmlString = '<?xml version="1.0" encoding="UTF-8"?>\n'		
		xmlString = xmlString + '<session>\n'
		xmlString = xmlString + '\t<search>\n'
		xmlString = xmlString + '\t\t<setting>\n'
		xmlString = xmlString + '\t\t\t<keyword>' + self._currentSession.keywords
		xmlString = xmlString + '</keyword>\n'
		xmlString = xmlString + '\t\t</setting>\n'
		for item in input_items:
			xmlString = xmlString + '\t\t<result>'
			xmlString = xmlString + '\t\t\t<picture thumbnail="true">\n'
			xmlString = xmlString + '\t\t\t\t<location>'
			xmlString = xmlString + os.path.join(input_directory, item['image_filename']).replace('&', '&amp;')
			xmlString = xmlString + '</location>\n'
			xmlString = xmlString + '\t\t\t\t<provenance>'
			xmlString = xmlString + item['image_link'].replace('&', '&amp;')
			xmlString = xmlString + '</provenance>\n'			
			xmlString = xmlString + '\t\t\t</picture>\n'
			xmlString = xmlString + '\t\t</result>\n'
		xmlString = xmlString + '\t</search>\n'
		xmlString = xmlString + '</session>\n'
		return xmlString

	def readSession(self):
		# Open XML document using the minidom parser
		filenames = []
		session_location = os.path.join(os.path.realpath('.'), 'temp')
		session_location = os.path.join(session_location, 'session.gid')
		session_location = os.path.abspath(session_location)
		#print("[GidData.readSession()] session_location = {}".format(session_location))
		if os.path.exists(session_location):
			DOMTree = xml.dom.minidom.parse(session_location)
			collection = DOMTree.documentElement
			pictures = collection.getElementsByTagName("picture")
			for picture in pictures:
				filename = picture.getElementsByTagName("location")[0]
				filenames.append(filename.childNodes[0].data) 
				#print("readXmlString {}".format(filenames))
		else:
			print("../temp/session.gid does not exist.")
		return filenames

	def storeSearch(self, output_items, thumbnail_folder_path):
		session_location = os.path.join(os.path.realpath('.'), 'temp')
		session_location = os.path.join(session_location, 'session.gid')
		session_location = os.path.abspath(session_location)
		#print("[GidData.storeSearch()] session_location = {}".format(session_location))
		self.sessionFile = open(session_location, "w")
		xmlString = self.createXmlString(output_items, thumbnail_folder_path)
		self.sessionFile.write(xmlString)
		self.sessionFile.close()


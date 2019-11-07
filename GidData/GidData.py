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
		self._currentSession = None
		self.searchList = []
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

	def populateSearch(self, search):
		setting = GidSettings()
		temporary = search.getElementsByTagName("config_file")
		if temporary:
			setting.config_file = temporary.childNodes[0].data
			print(setting.config_file)
		temporary = search.getElementsByTagName("keywords")
		if temporary:
			setting.keywords = temporary.childNodes[0].data
			print(setting.keywords)
		temporary = search.getElementsByTagName("keywords_from_file")
		if temporary:
			setting.keywords_from_file = temporary.childNodes[0].data
			print(setting.keywords_from_file)		
		temporary = search.getElementsByTagName("prefix_keywords")
		if temporary:
			setting.prefix_keywords = temporary.childNodes[0].data
			print(setting.prefix_keywords)
		temporary = search.getElementsByTagName("suffix_keywords")
		if temporary:
			setting.suffix_keywords = temporary.childNodes[0].data
			print(setting.suffix_keywords)
		temporary = search.getElementsByTagName("limit")
		if temporary:
			setting.limit = temporary.childNodes[0].data
			print(setting.limit)
		temporary = search.getElementsByTagName("related_images")
		if temporary:
			setting.related_images = temporary.childNodes[0].data
			print(setting.related_images)
		temporary = search.getElementsByTagName("format")
		if temporary:
			setting.format = temporary.childNodes[0].data
			print(setting.format)
		temporary = search.getElementsByTagName("color")
		if temporary:
			setting.color = temporary.childNodes[0].data
			print(setting.color)
		temporary = search.getElementsByTagName("color_type")
		if temporary:
			setting.color_type = temporary.childNodes[0].data
			print(setting.color_type)
		temporary = search.getElementsByTagName("usage_rights")
		if temporary:
			setting.usage_rights = temporary.childNodes[0].data
			print(setting.usage_rights)
		temporary = search.getElementsByTagName("size")
		if temporary:
			setting.size = temporary.childNodes[0].data
			print(setting.size)		
		temporary = search.getElementsByTagName("exact_size")
		if temporary:
			setting.exact_size = temporary.childNodes[0].data
			print(setting.exact_size)
		temporary = search.getElementsByTagName("aspect_ratio")
		if temporary:
			setting.aspect_ratio = temporary.childNodes[0].data
			print(setting.aspect_ratio)
		temporary = search.getElementsByTagName("type")
		if temporary:
			setting.type = temporary.childNodes[0].data
			print(setting.type)
		temporary = search.getElementsByTagName("time")
		if temporary:
			setting.time = temporary.childNodes[0].data
			print(setting.time)
		temporary = search.getElementsByTagName("delay")
		if temporary:
			setting.delay = temporary.childNodes[0].data
			print(setting.delay)
		temporary = search.getElementsByTagName("url")
		if temporary:
			setting.url = temporary.childNodes[0].data
			print(setting.url)
		temporary = search.getElementsByTagName("single_image")
		if temporary:
			setting.single_image = temporary.childNodes[0].data
			print(setting.single_image)
		temporary = search.getElementsByTagName("output_directory")
		if temporary:
			setting.output_directory = temporary.childNodes[0].data
			print(setting.output_directory)
		temporary = search.getElementsByTagName("image_directory")
		if temporary:
			setting.image_directory = temporary.childNodes[0].data
			print(setting.image_directory)		
		temporary = search.getElementsByTagName("no_directory")
		if temporary:
			setting.no_directory = temporary.childNodes[0].data
			print(setting.no_directory)
		temporary = search.getElementsByTagName("proxy")
		if temporary:
			setting.proxy = temporary.childNodes[0].data
			print(setting.proxy)
		temporary = search.getElementsByTagName("similar_images")
		if temporary:
			setting.similar_images = temporary.childNodes[0].data
			print(setting.similar_images)
		temporary = search.getElementsByTagName("specific_site")
		if temporary:
			setting.specific_site = temporary.childNodes[0].data
			print(setting.specific_site)
		temporary = search.getElementsByTagName("print_urls")
		if temporary:
			setting.print_urls = temporary.childNodes[0].data
			print(setting.print_urls)
		temporary = search.getElementsByTagName("print_size")
		if temporary:
			setting.print_size = temporary.childNodes[0].data
			print(setting.print_size)
		temporary = search.getElementsByTagName("print_paths")
		if temporary:
			setting.print_paths = temporary.childNodes[0].data
			print(setting.print_paths)
		temporary = search.getElementsByTagName("metadata")
		if temporary:
			setting.metadata = temporary.childNodes[0].data
			print(setting.metadata)
		temporary = search.getElementsByTagName("extract_metadata")
		if temporary:
			setting.extract_metadata = temporary.childNodes[0].data
			print(setting.extract_metadata)
		temporary = search.getElementsByTagName("socket_timeout")
		if temporary:
			setting.socket_timeout = temporary.childNodes[0].data
			print(setting.socket_timeout)
		temporary = search.getElementsByTagName("thumbnail")
		if temporary:
			setting.thumbnail = temporary.childNodes[0].data
			print(setting.thumbnail)
		temporary = search.getElementsByTagName("thumbnail_only")
		if temporary:
			setting.thumbnail_only = temporary.childNodes[0].data
			print(setting.thumbnail_only)
		temporary = search.getElementsByTagName("language")
		if temporary:
			setting.language = temporary.childNodes[0].data
			print(setting.language)
		temporary = search.getElementsByTagName("prefix")
		if temporary:
			setting.prefix = temporary.childNodes[0].data
			print(setting.prefix)
		temporary = search.getElementsByTagName("chromedriver")
		if temporary:
			setting.chromedriver = temporary.childNodes[0].data
			print(setting.chromedriver)
		temporary = search.getElementsByTagName("safe_search")
		if temporary:
			setting.safe_search = temporary.childNodes[0].data
			print(setting.safe_search)
		temporary = search.getElementsByTagName("no_numbering")
		if temporary:
			setting.no_numbering = temporary.childNodes[0].data
			print(setting.no_numbering)
		temporary = search.getElementsByTagName("offset")
		if temporary:
			setting.offset = temporary.childNodes[0].data
			print(setting.offset)
		temporary = search.getElementsByTagName("save_source")
		if temporary:
			setting.save_source = temporary.childNodes[0].data
			print(setting.save_source)
		temporary = search.getElementsByTagName("no_download")
		if temporary:
			setting.no_download = temporary.childNodes[0].data
			print(setting.no_download)
		temporary = search.getElementsByTagName("silent_mode")
		if temporary:
			setting.silent_mode = temporary.childNodes[0].data
			print(setting.silent_mode)
		temporary = search.getElementsByTagName("ignore_urls")
		if temporary:
			setting.ignore_urls = temporary.childNodes[0].data
			print(setting.ignore_urls)
		temporary = search.getElementsByTagName("help")
		if temporary:
			setting.help = temporary.childNodes[0].data
			print(setting.help)
		output = GidSearch(setting)
		if search.hasAttribute("identity"):
			output.identity = search.getAttribute("identity")
		return output

	def readSession(self):
		# Open XML document using the minidom parser
		filenames = []
		session_location = os.path.join(os.path.realpath('.'), 'temp')
		session_location = os.path.join(session_location, 'session.gid')
		session_location = os.path.abspath(session_location)
		#print("[GidData.readSession()] session_location = {}".format(session_location))
		if os.path.exists(session_location):
			DOMTree = xml.dom.minidom.parse(session_location)
			self._currentSession = DOMTree
			collection = DOMTree.documentElement
			pictures = collection.getElementsByTagName("picture")
			for picture in pictures:
				filename = picture.getElementsByTagName("location")[0]
				filenames.append(filename.childNodes[0].data)
				#print("readXmlString {}".format(filenames))
		else:
			print("../temp/session.gid does not exist.")
		return DOMTree

	def readSearchList(self):
		if self._currentSession is not None:
			DOMTree = self._currentSession
			collection = DOMTree.documentElement
			searches = collection.getElementsByTagName("search")
			for search in searches:
				self.searchList.append(self.populateSearch(search))
		#return self.searchList
			
		

	def storeSearch(self, output_items, thumbnail_folder_path):
		session_location = os.path.join(os.path.realpath('.'), 'temp')
		session_location = os.path.join(session_location, 'session.gid')
		session_location = os.path.abspath(session_location)
		#print("[GidData.storeSearch()] session_location = {}".format(session_location))
		self.sessionFile = open(session_location, "w")
		xmlString = self.createXmlString(output_items, thumbnail_folder_path)
		self.sessionFile.write(xmlString)
		self.sessionFile.close()


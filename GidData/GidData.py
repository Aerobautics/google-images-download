#!/usr/bin/env python3
# Written by Stewart Nash (Aerobautics) November 2019
"""XML data processing for GID.
"""
from tkinter import *
from xml.dom.minidom import parse
from xml.dom.minidom import getDOMImplementation
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
		self.currentSearch = []
		self.searchList = []
		self.sessionFile = []

	def get_currentSession(self):
		return self.currentSession

	def set_currentSession(self, value):
		self._currentSession = value

	def createXmlString(self, input_items, input_directory):
		xmlString = '<?xml version="1.0" encoding="UTF-8"?>\n'		
		xmlString = xmlString + '<session>\n'
		xmlString = xmlString + '\t<search identity=\"'
		xmlString = xmlString + self.currentSearch.identity + '\">\n'
		xmlString = xmlString + '\t\t<setting>\n'
		xmlString = xmlString + '\t\t\t<keyword>' + self.currentSearch.settings.keywords
		xmlString = xmlString + '</keyword>\n'
		xmlString = xmlString + '\t\t</setting>\n'
		for item in input_items:
			xmlString = xmlString + '\t\t<result>\n'
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
			
		
	# Remove output_items and thumbnail_folder_path parameters
	#def storeSearch(self, search, output_items, thumbnail_folder_path):
	#	self.currentSearch = search
	#	session_location = os.path.join(os.path.realpath('.'), 'temp')
	#	session_location = os.path.join(session_location, 'session.gid')
	#	session_location = os.path.abspath(session_location)
	#	#print("[GidData.storeSearch()] session_location = {}".format(session_location))
	#	self.sessionFile = open(session_location, "w")
	#	xmlString = self.createXmlString(output_items, thumbnail_folder_path)
	#	self.sessionFile.write(xmlString)
	#	self.sessionFile.close()

	def storeSearch(self, inputSearch, searchLocation):
		implementation = getDOMImplementation()
		document = implementation.createDocument(None, "gid", None)
		DOMTree = document
		temporary_child = self.translateSearch(inputSearch)
		DOMTree.documentElement.appendChild(temporary_child)
		self.writeSearch(DOMTree, searchLocation)

	def storeSession(self, inputSession):
		implementation = getDOMImplementation()
		document = implementation.createDocument(None, "gid", None)
		DOMTree = document
		temporary_child = self.translateSession(inputSession)
		DOMTree.documentElement.appendChild(temporary_child)
		self.writeSession(DOMTree)

	def translatePicture(self, inputPicture):
		implementation = getDOMImplementation()
		document = implementation.createDocument(None, "gid", None)
		DOMTree = document
		temporary_child = DOMTree.createElement('picture')
		if inputPicture.thumbnail:
			temporary_child.setAttribute('thumbnail', 'true')
		else:
			temporary_child.setAttribute('thumbnail', 'false')
		sub_child = DOMTree.createElement('location')
		if inputPicture.location is not None:
			text_node = DOMTree.createTextNode(inputPicture.location)
			sub_child.appendChild(text_node)
		temporary_child.appendChild(sub_child)
		sub_child = DOMTree.createElement('provenance')
		if inputPicture.provenance is not None:
			text_node = DOMTree.createTextNode(inputPicture.provenance)
			sub_child.appendChild(text_node)
		temporary_child.appendChild(sub_child)
		if inputPicture.note:
			sub_child = DOMTree.createElement('note')
			text_node = DOMTree.createTextNode(inputPicture.note)
			sub_child.appendChild(text_node)
			temporary_child.appendChild(sub_child)
		if inputPicture.alternate:
			sub_child = DOMTree.createElement('alternate')
			text_node = DOMTree.createTextNode(inputPicture.alternate)
			sub_child.appendChild(text_node)
			temporary_child.appendChild(sub_child)
		if inputPicture.provenance_size:
			sub_child = DOMTree.createElement('provenance_size')
			text_node = DOMTree.createTextNode(inputPicture.provenance_size)
			sub_child.appendChild(text_node)
			temporary_child.appendChild(sub_child)
		if inputPicture.provenance_type:
			sub_child = DOMTree.createElement('provenance_type')
			text_node = DOMTree.createTextNode(inputPicture.provenance_type)
			sub_child.appendChild(text_node)
			temporary_child.appendChild(sub_child)
		return temporary_child

	def translateResult(self, inputResult):
		implementation = getDOMImplementation()
		document = implementation.createDocument(None, "gid", None)
		DOMTree = document
		temporary_child = DOMTree.createElement('result')
		if inputResult.image_filename is not None:
			sub_child = DOMTree.createElement('image_filename')
			text_node = DOMTree.createTextNode(inputResult.image_filename)
			sub_child.appendChild(text_node)
			temporary_child.appendChild(sub_child)
		if inputResult.image_format is not None:
			sub_child = DOMTree.createElement('image_format')
			text_node = DOMTree.createTextNode(inputResult.image_format)
			sub_child.appendChild(text_node)
			temporary_child.appendChild(sub_child)		
		if inputResult.image_height is not None:
			sub_child = DOMTree.createElement('image_height')
			text_node = DOMTree.createTextNode(str(inputResult.image_height))
			sub_child.appendChild(text_node)
			temporary_child.appendChild(sub_child)
		if inputResult.image_width is not None:
			sub_child = DOMTree.createElement('image_width')
			text_node = DOMTree.createTextNode(str(inputResult.image_width))
			sub_child.appendChild(text_node)
			temporary_child.appendChild(sub_child)
		if inputResult.image_link is not None:
			sub_child = DOMTree.createElement('image_link')
			text_node = DOMTree.createTextNode(inputResult.image_link)
			sub_child.appendChild(text_node)
			temporary_child.appendChild(sub_child)
		if inputResult.image_description is not None:
			sub_child = DOMTree.createElement('image_description')
			text_node = DOMTree.createTextNode(inputResult.image_description)
			sub_child.appendChild(text_node)
			temporary_child.appendChild(sub_child)
		if inputResult.image_host is not None:
			sub_child = DOMTree.createElement('image_host')
			text_node = DOMTree.createTextNode(inputResult.image_host)
			sub_child.appendChild(text_node)
			temporary_child.appendChild(sub_child)
		if inputResult.image_source is not None:
			sub_child = DOMTree.createElement('image_source')
			text_node = DOMTree.createTextNode(inputResult.image_source)
			sub_child.appendChild(text_node)
			temporary_child.appendChild(sub_child)
		if inputResult.image_thumbnail_url is not None:
			sub_child = DOMTree.createElement('image_thumbnail_url')
			text_node = DOMTree.createTextNode(inputResult.image_thumbnail_url)
			sub_child.appendChild(text_node)
			temporary_child.appendChild(sub_child)
		if inputResult.thumbnail is not None:
			sub_child = self.translatePicture(inputResult.thumbnail)
			temporary_child.appendChild(sub_child)
		if inputResult.picture is not None:
			sub_child = self.translatePicture(inputResult.picture)
			temporary_child.appendChild(sub_child)
		return temporary_child

	def translateSearch(self, inputSearch):
		implementation = getDOMImplementation()
		document = implementation.createDocument(None, "gid", None)
		DOMTree = document
		temporary_child = DOMTree.createElement('search')
		temporary_child.setAttribute("identity", inputSearch.identity)
		sub_child = self.translateSetting(inputSearch.settings)
		temporary_child.appendChild(sub_child)
		for result in inputSearch.results:
			sub_child = self.translateResult(result)
			temporary_child.appendChild(sub_child)
		return temporary_child

	def translateSession(self, inputSession):
		implementation = getDOMImplementation()
		document = implementation.createDocument(None, "gid", None)
		DOMTree = document
		temporary_child = DOMTree.createElement('session')
		for search in inputSession.searches:
			sub_child = self.translateSearch(search)
			temporary_child.appendChild(sub_child)
		return temporary_child		

	def translateSetting(self, inputSetting):
		implementation = getDOMImplementation()
		document = implementation.createDocument(None, "gid", None)
		DOMTree = document
		temporary_child = DOMTree.createElement('result')
		if inputSetting.config_file is not None:
			sub_child = DOMTree.createElement('config_file')
			text_node = DOMTree.createTextNode(inputSetting.config_file)
			sub_child.appendChild(text_node)
			temporary_child.appendChild(sub_child)
		if inputSetting.keywords is not None:
			sub_child = DOMTree.createElement('keywords')
			text_node = DOMTree.createTextNode(inputSetting.keywords)
			sub_child.appendChild(text_node)
			temporary_child.appendChild(sub_child)			
		if inputSetting.keywords_from_file is not None:
			sub_child = DOMTree.createElement('keywords_from_file')
			text_node = DOMTree.createTextNode(inputSetting.keywords_from_file)
			sub_child.appendChild(text_node)
			temporary_child.appendChild(sub_child)
		if inputSetting.prefix_keywords is not None:
			sub_child = DOMTree.createElement('prefix_keywords')
			text_node = DOMTree.createTextNode(inputSetting.prefix_keywords)
			sub_child.appendChild(text_node)
			temporary_child.appendChild(sub_child)
		if inputSetting.suffix_keywords is not None:
			sub_child = DOMTree.createElement('suffix_keywords')
			text_node = DOMTree.createTextNode(inputSetting.suffix_keywords)
			sub_child.appendChild(text_node)
			temporary_child.appendChild(sub_child)
		if inputSetting.limit is not None:
			sub_child = DOMTree.createElement('limit')
			text_node = DOMTree.createTextNode(str(inputSetting.limit))
			sub_child.appendChild(text_node)
			temporary_child.appendChild(sub_child)
		if inputSetting.related_images is not None:
			sub_child = DOMTree.createElement('related_images')
			text_node = DOMTree.createTextNode(inputSetting.related_images)
			sub_child.appendChild(text_node)
			temporary_child.appendChild(sub_child)
		if inputSetting.format is not None:
			sub_child = DOMTree.createElement('format')
			text_node = DOMTree.createTextNode(inputSetting.format)
			sub_child.appendChild(text_node)
			temporary_child.appendChild(sub_child)
		if inputSetting.color is not None:
			sub_child = DOMTree.createElement('color')
			text_node = DOMTree.createTextNode(inputSetting.color)
			sub_child.appendChild(text_node)
			temporary_child.appendChild(sub_child)
		return temporary_child
					

	def writeSearch(self, DOMTree, searchLocation):
		output_file = open(searchLocation, "w")
		DOMTree.writexml(output_file, indent = "\t", addindent = "\t", newline = '\n')

	def writeSession(self, DOMTree):
		session_location = os.path.join(os.path.realpath('.'), 'temp')
		session_location = os.path.join(session_location, 'session.gid')
		session_location = os.path.abspath(session_location)
		output_file = open(session_location, "w")
		DOMTree.writexml(output_file, indent = "\t", addindent = "\t", newl = '\n')
		


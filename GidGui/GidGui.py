#!/usr/bin/env python3
# Written by Stewart Nash (Aerobautics) November 2019
"""GUI for the customized google_images_download.
"""
from tkinter import *
import PIL
from PIL import ImageTk
from PIL import Image
import sys
import os
import errno
import time
import tkinter.messagebox
sys.path.insert(1, '../')
from google_images_download import google_images_download
from GidData import GidData
from GidResult import GidResult
from GidSearch import GidSearch
from GidSession import GidSession
from GidSettings import GidSettings

#https://tkdocs.com/index.html
#http://effbot.org/tkinterbook/

# GID stands for 'Google Image Downloader'

class GidGui:
	'This class contains the main GUI window used by the application.'

	def __init__(self):
		self.rows = 3
		self.columns = 3
		self.pages = 100
		self.current_page = 0
		self.sessionIndex = 0

		self.currentSettings = []

		self.gidSession = []
		self.sessionList = []

		self.keyword_entry = None
		self.limit_entry = None

		self.mainForm = None
		self.listFrame = None
		self.mainFrame = None
		self.previewFrame = None
		self.sessionListbox = None
		self.searchListbox = None

		self.isListShown = False
		self.isPreviewShown = False
		self.isInitialized = False

		self.preview_height = 300
		self.preview_width = 300

		self.currentSession = []
		self.currentSearch = []

		self.gidData = GidData.GidData()
		self.currentSession = GidSession.GidSession()
		self.currentSearch = GidSearch.GidSearch()
		self.currentSearch.settings.keywords = "polar bear"
		self.currentSearch.settings.thumbnail = True
		self.currentSearch.settings.limit = 10
		#self.gidData.set_currentSession(self.currentSession)

	def initialize(self):
		if not self.isInitialized:
			self.loadSession()
			self.isInitialized = True

	def defaultFunction(self, event):
		print("Google Images Download")

	def getKeyword(self):
		return self.keyword_entry.get()

	def getLimit(self):
		limit = self.limit_entry.get()
		if limit is not None:
			limit = int(limit)
		return limit

	def loadSession(self):
		self.currentSession = self.gidData.readSession()

	def nextPage(self, event):
		print("Go to next page")

	def previousPage(self, event):
		print("Go to previous page")

	def populateCurrentSearch(self, keyword = None, limit = None, thumbnail = None):
		if keyword is not None:
			self.currentSearch.settings.keywords = keyword
		if thumbnail is not None:
			self.currentSearch.settings.thumbnail_only = thumbnail
		if limit is not None:
			self.currentSearch.settings.limit = limit

	def populateCurrentSession(self, inputSearches):
		for search in inputSearches:
			self.currentSession.addSearch(search)

	def populateSearchList(self):
		self.searchListbox.delete(0, END)
		for result in self.currentSession.searches[self.sessionIndex].results:
			self.searchListbox.insert(END, result.image_filename)			

	def populateSessionList(self):
		self.sessionListbox.delete(0, END)
		for search in self.currentSession.searches:
			self.sessionListbox.insert(END, search.settings.keywords)

	def preview(self, event):
		self.showPreview()
		start_time = time.time()
		if self.getKeyword() == "":
			return False
		if self.getLimit is not None:
			self.populateCurrentSearch(keyword = self.getKeyword(), limit = self.getLimit(), thumbnail = True)
		else:
			self.populateCurrentSearch(keyword = self.getKeyword(), limit = 8, thumbnail = True)
		arguments = {
			"keywords": self.currentSearch.settings.keywords,
			"limit": self.currentSearch.settings.limit,
			"print_urls": True,
			"thumbnail_only": self.currentSearch.settings.thumbnail_only
		}
		try:
			temp = arguments['output_folder']
		except KeyError:
			pass
		else:
			assert False, "This test checks download to default location yet an output folder was provided"
		output_folder_path = os.path.join(os.path.realpath('.'), 'downloads', '{}'.format(arguments['keywords'].replace(' ', '_')))
		thumbnail_folder_path = os.path.join(os.path.realpath('.'), 'downloads', '{}-thumbnail'.format(arguments['keywords'].replace(' ', '_')))
		if os.path.exists(output_folder_path):
			start_amount_of_files_in_output_folder = len([name for name in os.listdir(output_folder_path) if os.path.isfile(os.path.join(output_folder_path, name)) and os.path.getctime(os.path.join(output_folder_path, name)) < start_time])
		else:
			start_amount_of_files_in_output_folder = 0
		response = google_images_download.googleimagesdownload()
		outputPaths, outputErrors, outputItems = response.download(arguments)
		#print("outputPaths: {}".format(outputPaths))
		print("outputErrors: {}".format(outputErrors))
		#print("outputItems: {}".format(outputItems))
		files_modified_after_test_started = [name for name in os.listdir(output_folder_path) if os.path.isfile(os.path.join(output_folder_path, name)) and os.path.getmtime(os.path.join(output_folder_path, name)) > start_time]
		end_amount_of_files_in_output_folder = len(files_modified_after_test_started)
		#print(f"Files downloaded by test {__name__}:")
		print("Files downloaded by test {}:".format(__name__))
		for file in files_modified_after_test_started:
			print(os.path.join(output_folder_path, file))
		# assert end_amount_of_files_in_output_folder - start_amount_of_files_in_output_folder == arguments['limit']
		if not self.currentSearch.settings.thumbnail_only:
			assert end_amount_of_files_in_output_folder == arguments['limit']		
		print("Cleaning up all files downloaded by test {}...".format(__name__))
		for file in files_modified_after_test_started:
			if self.removeFile(os.path.join(output_folder_path, file)):
				print("Deleted {}".format(os.path.join(output_folder_path, file)))
			else:
				print("Failed to delete {}".format(os.path.join(output_folder_path, file)))
		filePaths = outputPaths[self.currentSearch.settings.keywords]
		thumbnail_files = []
		for item in outputItems:
			self.currentSearch.addResult(GidResult.GidResult(item))
			current_file = os.path.join(thumbnail_folder_path, item['image_filename'])
			thumbnail_files.append(current_file)
		imagePhotos = []
		imageLabels = []
		gridCount = 0
		for thumbnailFile in thumbnail_files:
			loadImage = Image.open(thumbnailFile)
			renderImage = ImageTk.PhotoImage(loadImage)
			imageLabels.append(Label(self.previewFrame,
				image = renderImage,
				relief = RIDGE,
				height = self.preview_height,
				width = self.preview_width))
			imageLabels[gridCount].image = renderImage
			if gridCount < (self.rows * self.columns):
				imageLabels[gridCount].grid(row = gridCount // self.columns, column = gridCount % self.columns, padx = 5, pady = 5)
			gridCount = gridCount + 1
		#self.gidData.storeSearch(self.currentSearch, outputItems, thumbnail_folder_path)
		self.currentSession.addSearch(self.currentSearch)
		self.gidData.storeSession(self.currentSession)
		#return thumbnail_files						
		return True

	def removeFile(self, file):
		try:
			os.remove(file)
		except OSError as e:
			if e.errno != errno.ENOENT:
				raise e
			return False
		return True

	def showList(self):
		if not self.isListShown:
			self.isListhShown = True
			self.isPreviewShown = False
			self.previewFrame.pack_forget()
			self.listFrame.pack(fill = X)

	def showPreview(self):
		if not self.isPreviewShown:
			self.isPreviewShown = True
			self.isListShown = False
			self.listFrame.pack_forget()
			self.previewFrame.pack(fill = X)

	def display(self):
		self.initialize()

		root = Tk()
		root.title("Google Images Download")
		root.geometry("1080x720")

		# Create menu
		main_menu = Menu(root)
		root.config(menu = main_menu)
		file_menu = Menu(main_menu)
		main_menu.add_cascade(label = "File", menu = file_menu)
		file_menu.add_command(label = "Open", command = self.gidData.readSession)
		file_menu.add_separator()
		file_menu.add_command(label = "Exit", command = root.destroy)
		search_menu = Menu(main_menu)
		main_menu.add_cascade(label = "Search", menu = search_menu)
		search_menu.add_command(label = "Preview", command = self.preview)
		search_menu.add_command(label = "Start", command = self.defaultFunction)
		search_menu.add_command(label = "Stop", command = self.defaultFunction)
		# Top frame
		top_frame = Frame(root)
		top_frame.pack(side = TOP, fill = BOTH, anchor = N)
		# Bottom frame
		# Status frame
		status_frame = Frame(root)
		status_frame.pack(side = BOTTOM, fill = X, anchor = SW)
		# Control frame
		control_frame = Frame(top_frame)
		control_frame.pack(side = LEFT, fill = Y, anchor = N)
		# Main frame
		main_frame = Frame(top_frame)
		main_frame.pack(side = LEFT, anchor = N)
		# Accessory frame
		accessory_frame = Frame(main_frame)
		accessory_frame.pack(side = TOP, fill = X, anchor = N)
		# Display frame
		display_frame = Frame(main_frame)
		display_frame.pack(side = TOP, anchor = N)
		# List frame
		list_frame = Frame(display_frame)
		list_frame.pack(side = LEFT, fill = Y)
		# Preview frame
		preview_frame = Frame(display_frame)
		preview_frame.pack(side = LEFT)
		# Status bar
		status_bar = Label(status_frame, text = "Ready", bd = 1, relief = SUNKEN, anchor = W)
		status_bar.pack(fill = X, expand = True)
		# Search area
		keyword_label = Label(accessory_frame, text = "Keyword: ")
		keyword_entry = Entry(accessory_frame)
		limit_label = Label(accessory_frame, text = "Limit: ")
		limit_entry = Entry(accessory_frame, justify = RIGHT)
		limit_entry.insert(0, "5")
		session_listbox = Listbox(list_frame)
		search_listbox = Listbox(list_frame)
		session_listbox.config(height = 35, width = 25)
		search_listbox.config(height = 35, width = 45)
		session_listbox.pack(side = LEFT, fill = Y)
		search_listbox.pack(side = LEFT, fill = Y)
		preview_button = Button(control_frame, text = "Preview", command = self.preview)
		start_button = Button(control_frame, text = "Start", command = self.defaultFunction)
		cancel_button = Button(control_frame, text = "Cancel", command = self.defaultFunction)
		previous_button = Button(control_frame, text = "Previous", command = self.previousPage)
		next_button = Button(control_frame, text = "Next", command = self.nextPage)
		picture_button = Button(control_frame, text = "Picture", command = self.defaultFunction)
		thumbnail_button = Button(control_frame, text = "Thumbnail", command = self.defaultFunction)
		combo_button = Button(control_frame, text = "Combo", command = self.defaultFunction)
		keyword_label.pack(side = LEFT)
		keyword_entry.pack(side = LEFT)
		limit_label.pack(side = LEFT)
		limit_entry.pack(side = LEFT)
		preview_button.pack(anchor = NW, fill = X)
		start_button.pack(anchor = NW, fill = X)
		cancel_button.pack(anchor = NW, fill = X)
		previous_button.pack(anchor = NW, fill = X)
		next_button.pack(anchor = NW, fill = X)

		self.sessionListbox = session_listbox
		self.searchListbox = search_listbox
		self.keyword_entry = keyword_entry
		self.limit_entry = limit_entry

		self.mainForm = root

		self.listFrame = list_frame
		self.mainFrame = main_frame
		self.previewFrame = preview_frame

		self.populateSessionList()
		self.populateSearchList()
		self.isListShown = True

		root.mainloop()

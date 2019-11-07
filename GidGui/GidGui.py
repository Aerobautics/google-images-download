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

		self.currentSettings = []

		self.gidSession = []
		self.keyword_entry = []
		self.limit_entry = []
		self.sessionList = []
		self.main_form = []
		self.main_frame = []
		self.preview_frame = []

		self.currentSession = []
		self.currentSearch = []

		self.gidData = GidData.GidData()
		self.currentSession = GidSession.GidSession()
		self.currentSearch = GidSearch.GidSearch()
		self.currentSearch.settings.keywords = "polar bear"
		self.currentSearch.settings.thumbnail = True
		self.currentSearch.settings.limit = 10
		#self.gidData.set_currentSession(self.currentSession)

	#def initialization(self):


	def getKeyword(self):
		return self.keyword_entry.get()

	def defaultFunction(self):
		print("Google Images Download")

	def nextPage(self):
		print("Go to next page")

	def previousPage(self):
		print("Go to previous page")

	def populateCurrentSearch(self, keyword = None, limit = None, thumbnail = None):
		if keyword is not None:
			self.currentSearch.settings.keywords = keyword
		if thumbnail is not None:
			self.currentSearch.settings.thumbnail_only = thumbnail
		if limit is not None:
			self.currentSearch.settings.limit = limit

	def previewDownload(self):
		start_time = time.time()
		if self.getKeyword() == "":
			return False
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
		print("outputPaths: {}".format(outputPaths))
		print("outputErrors: {}".format(outputErrors))
		print("outputItems: {}".format(outputItems))
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
			current_file = os.path.join(thumbnail_folder_path, item['image_filename'])
			thumbnail_files.append(current_file)
		imagePhotos = []
		imageLabels = []
		gridCount = 0
		for thumbnailFile in thumbnail_files:
			loadImage = Image.open(thumbnailFile)
			renderImage = ImageTk.PhotoImage(loadImage)
			imageLabels.append(Label(self.preview_frame, image = renderImage))
			imageLabels[gridCount].image = renderImage
			if gridCount < (self.rows * self.columns):
				imageLabels[gridCount].grid(row = gridCount // self.columns, column = gridCount % self.columns, padx = 5, pady = 5)
			gridCount = gridCount + 1
		self.gidData.storeSearch(outputItems, thumbnail_folder_path)
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

	def display(self):
		root = Tk()
		root.title("Google Images Download")
		root.geometry("720x480")

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
		search_menu.add_command(label = "Preview", command = self.previewDownload)
		search_menu.add_command(label = "Start", command = self.defaultFunction)
		search_menu.add_command(label = "Stop", command = self.defaultFunction)
		# Main frame
		main_frame = Frame(root)
		main_frame.pack_propagate(False)
		main_frame.pack(fill = BOTH, expand = True)
		# Preview frame
		preview_frame = Frame(root)
		preview_frame.pack(fill = BOTH, expand = True)
		# Status bar
		status_bar = Label(root, text = "Ready", bd = 1, relief = SUNKEN, anchor = W)
		status_bar.pack(side = BOTTOM, fill = X)
		# Search area
		keyword_label = Label(main_frame, text = "Keyword: ")
		keyword_entry = Entry(main_frame)
		limit_label = Label(main_frame, text = "Limit: ")
		limit_entry = Entry(main_frame, justify = RIGHT)
		limit_entry.insert(0, "5")
		preview_button = Button(main_frame, text = "Preview", command = self.previewDownload)
		start_button = Button(main_frame, text = "Start", command = self.defaultFunction)
		cancel_button = Button(main_frame, text = "Cancel", command = self.defaultFunction)
		previous_button = Button(main_frame, text = "Previous", command = self.previousPage)
		next_button = Button(main_frame, text = "Next", command = self.nextPage)

		keyword_label.grid(row = 0, sticky = E)
		keyword_entry.grid(row = 0, column = 1, columnspan = 2)
		preview_button.grid(row = 1, column = 0)
		start_button.grid(row = 1, column = 1)
		cancel_button.grid(row = 1, column = 2)
		limit_label.grid(row = 0, column = 3)
		limit_entry.grid(row = 0, column = 4)
		previous_button.grid(row = 2, column = 0)
		next_button.grid(row = 2, column = 1)

		self.keyword_entry = keyword_entry
		self.limit_entry = limit_entry
		self.main_form = root
		self.main_frame = main_frame
		self.preview_frame = preview_frame

		root.mainloop()

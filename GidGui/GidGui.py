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
from GidSession import GidSession

#https://tkdocs.com/index.html

# GID stands for 'Google Image Downloader'

class GidGui:
	'This class contains the main GUI window used by the application.'
	def __init__(self):
		self.gidSession = []
		self.sessionList = []
		self.main_form = []
		self.main_frame = []
		self.currentSession = GidSession.GidSession()
		self.currentSession.keyword = "polar bear"
		self.currentSession.thumbnail_only = True
		self.gidData = GidData.GidData()
		self.gidData.set_currentSession(self.currentSession)

	def defaultFunction(self):
		print("Google Images Download")

	def previewDownload(self):
		start_time = time.time()
		arguments = {
			"keywords": self.currentSession.keyword,
			"limit": 5,
			"print_urls": True,
			"thumbnail_only": True
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
		if not self.currentSession.thumbnail_only:
			assert end_amount_of_files_in_output_folder == arguments['limit']		
		print("Cleaning up all files downloaded by test {}...".format(__name__))
		for file in files_modified_after_test_started:
			if self.removeFile(os.path.join(output_folder_path, file)):
				print("Deleted {}".format(os.path.join(output_folder_path, file)))
			else:
				print("Failed to delete {}".format(os.path.join(output_folder_path, file)))
		filePaths = outputPaths[self.currentSession.keyword]
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
			imageLabels.append(Label(self.main_frame, image = renderImage))
			imageLabels[gridCount].image = renderImage
			if gridCount < 4:
				imageLabels[gridCount].grid(row = 2, column = gridCount)
			gridCount = gridCount + 1
		self.gidData.storeSearch(outputItems, thumbnail_folder_path)						
		return thumbnail_files

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
		# Status bar
		status_bar = Label(root, text = "Ready", bd = 1, relief = SUNKEN, anchor = W)
		status_bar.pack(side = BOTTOM, fill = X)
		# Search area
		keyword_label = Label(main_frame, text = "Keyword: ")
		keyword_entry = Entry(main_frame)
		preview_button = Button(main_frame, text = "Preview", command = self.previewDownload)
		start_button = Button(main_frame, text = "Start", command = self.defaultFunction)
		cancel_button = Button(main_frame, text = "Cancel", command = self.defaultFunction)
		keyword_label.grid(row = 0, sticky = E)
		keyword_entry.grid(row = 0, column = 1, columnspan = 2)
		preview_button.grid(row = 1, column = 0)
		start_button.grid(row = 1, column = 1)
		cancel_button.grid(row = 1, column = 2)		

		self.main_form = root
		self.main_frame = main_frame

		root.mainloop()

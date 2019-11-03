#!/usr/bin/env python3
from google_images_download import google_images_download
from GidData import GidData
from GidGui import GidGui
from GidPicture import GidPicture
from GidSession import GidSession
from GidString import GidString

def main():
	#test_download_images_to_default_location()
	gidGui = GidGui.GidGui()
	gidGui.display()
	
if __name__ == "__main__":
	main()

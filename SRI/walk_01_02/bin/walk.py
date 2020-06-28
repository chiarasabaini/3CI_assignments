""" WALK
"""
import sys
import os
from datetime import datetime

__author__ = "Castellani Davide & Sabaini Chiara 3CI"
__version__ = "01.01 2020-03-24"

class walk:
	def __init__(self, directory):
		file = open("..\\log\\log.log", "a")
		walk.log(file, "Start time: " + str(datetime.now()))
		walk.log(file, f"Printing on screen the given directory name: {directory}")
		print(directory)
		for directories, subdirectories, files in os.walk(directory):
			walk.log(file, f"Analizing directory {directories}")
			walk.print_and_log(file, f"Actual directory: {directories}")
			walk.print_and_log(file, f"Present subdirectories: {subdirectories}")
			py_files = [file for file in files if file.endswith(".py")]
			walk.print_and_log(file, f"Present python files are: {py_files}")
		walk.log(file, "Done")
		walk.log(file, "End time: " + str(datetime.now()))
		walk.log(file, "")
		file.close()

	def log(file, item):
		"""Writes a line in the log.log file
		"""
		file.write(item)
		file.write("\n")

	def print_and_log(file, item):
		"""Writes on the screen and in the log file
		"""
		print(item)
		walk.log(file, item)

if __name__ == "__main__":
	try:
		walk(sys.argv[1].replace(f'{"//"}', "\\"))
	except:
		default_directory = "..\\"
		walk(default_directory)
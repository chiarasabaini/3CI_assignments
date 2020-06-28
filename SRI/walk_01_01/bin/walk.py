""" OSWALK
"""
import os
from datetime import datetime

__author__ = "Castellani Davide & Sabaini Chiara 3CI"
__version__ = "01.01 2020-03-24"

class oswalk:
	def __init__(self):
		file = open("..\\log\\log.log", "a")
		oswalk.log(file, "Start time: " + str(datetime.now()))
		for directories, subdirectories, files in os.walk(os.getcwd()):
			oswalk.log(file, f"Analizing directory {directories}")
			print(f"Actual directory: {directories}")
			print(f"Present subdirectories: {subdirectories}")
			py_files = [file for file in files if file.endswith(".py")]
			print(f"My files are: {py_files}")
			print()
		oswalk.log(file, "Done")
		oswalk.log(file, "End time: " + str(datetime.now()))
		oswalk.log(file, "")
		file.close()

	def log(file, item):
		"""Writes a line in the log.log file
		"""
		file.write(item)
		file.write("\n")

if __name__ == "__main__":
	oswalk()

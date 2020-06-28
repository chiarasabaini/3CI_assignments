""" Writes a list of the VM names
"""
from datetime import datetime
import os

__author__ = "contacts@castellanidavide.it", "chiara@sabaini.com"
__version__ = "02.02 2020-03-20"

class vbox:
	def __init__(self):
		""" Opens the log's file, writes date, time and the executed instructions
		"""
		file = open("..\\log\\py_log.log", "a")
		vbox.log(file, str(datetime.now()))
		vbox.log(file, "Try to do the instruction")
		vbox.do_and_write("..\\virtualboxm\\vboxmanage.exe list vms", "..\\doc\\vmsfromp.csv")
		vbox.log(file, "Done")
		vbox.log(file, "End at: " + str(datetime.now()))
		vbox.log(file, "")
		file.close()

	def do_and_write(do, save):
		""" Does my istruction
		"""
		os.system(str(do + " > " + save))

	def log(file, item):
		""" Does a log line
		"""
		file.write(item)
		file.write("\n")

if __name__ == "__main__":
	vbox()

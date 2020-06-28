# Imports
import os
from datetime import *

__author__ = "davidecastellani@castellanidavide.it", "chiara@sabaini.com"
__version__ = "01.01 2020-13-00"

class create_structure_01_01():
	def __init__ (self):
		asks = ["Inserisci il nome (es. Davide): ",					#0
				"Inserisci il cognome (es. Castellani): ",			#1
				"Inserisci nome progetto (es. cc): ",				#2
				"Inserisci versione progetto (es 01): ",			#3
				"Inserisci build progetto (es 01): ",				#4
				"Inserisci estensione file principale (es. py): "]	#5
		results = []
		for current_ask in asks:
			results.append(input(current_ask))
		
		main_folder_name = create_structure.create_folder_structure(results)
		print("Folders builted")

		create_structure.create_source(main_folder_name, results)
		print("Sourgent file builded")

		create_structure.create_README(main_folder_name, results)
		print("README.md builded")


	def create_folder_structure(results):
		#Create main folder
		main_folder_name = "./" + results[1].lower() + "_" + results[0].lower() + "_" + results[2] + "_" + results[3] + "_" + results[4]
		create_structure.create_folder(main_folder_name)

		#Create bin folder
		bin_folder_name = main_folder_name + "/bin"
		create_structure.create_folder(bin_folder_name)

		#Create doc folder
		doc_folder_name = main_folder_name + "/doc"
		create_structure.create_folder(doc_folder_name)

		return main_folder_name

	def create_folder(directory):
		try:
			if not os.path.exists(directory):
				os.makedirs(directory)
		except OSError:
			print ('Error: Creating directory. ' +  directory)

	def create_sourgent(main_folder_name, results):
		file_name_and_path = main_folder_name + "/bin/" + results[2] + "." + results[5]
		text = "# " + results[2] + "\n" + "# Created by " + results[1] + " " + results[0]

		f = open(file_name_and_path, "w+")
		f.write(text)
		f.close()

	def create_README(main_folder_name, results):
		time = datetime.now()
		file_name_and_path = main_folder_name + "/doc/README.md"
		initial = "# " + results[2] + "\n" + "---" + "\n"
		changelog = "## Changelog \n- [" + results[3] + "." + results[4] + "_" + str(time.year) + "-" + str(time.month) + "-" + str(time.day) + "](#" + results[3] + results[4] + "_" + str(time.year) + "-" + str(time.month) + "-" + str(time.day) + ")" + "\n"
		version = "\n" + "---" + "\n### " + results[3] + "." + results[4] + "_" + str(time.year) + "-" + str(time.month) + "-" + str(time.day) + "\n" + " - #### Added" + "\n" + "	 - " + "\n" + " - #### Modificed" + "\n" +"	 - " + "\n"
		some_spaces = "\n" + "\n" + "\n"
		finish = "---" + "\n" + "By " + results[0] + results[1] + "\n" + "---" + "\n" + "If you have any problem please contact me:" + "\n" + "- davidecastellani@castellanidavide.it" + "\n"
		text = initial + changelog + version + some_spaces + finish
		f = open(file_name_and_path, "w+")
		f.write(text)
		f.close()

if __name__ == "__main__":
	try:
		create_structure_01_01()
	except:
		print("There is an error, try again.")

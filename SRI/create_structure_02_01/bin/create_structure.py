"""This is the magic "robottino" by Castellani Davide & Sabaini Chiara
"""
# Imports
import os
from datetime import *

__author__ = "davidecastellani@castellanidavide.it", "chiara@sabaini.com"
__version__ = "02.01 2020-03-24"

class create_structure:
	def __init__ (self):
		"""Main function
		"""
		questions = [	"Inserisci nome progetto (es. create_structur): ",	#0
						"Inserisci estensione file principale (es. py): "]	#1
		results = []
		for current_quest in questions:
			results.append(input(current_quest))
		
		main_folder_name = create_structure_02_01.create_folder_structure(results)
		print(f"Folders built in {main_folder_name}")

		create_structure_02_01.create_source(main_folder_name, results)
		print(f"Source file built")

		create_structure_02_01.create_README(main_folder_name, results)
		print(f"README.md built")

		create_structure_02_01.create_log(main_folder_name)
		print(f"trace.log built")


	def create_folder_structure(results):
		"""Creates del directories structure
		"""
		# Create main folder
		main_folder_name = "./" + results[0].lower() + "_01_01"
		create_structure_02_01.create_folder(main_folder_name)

		# Create bin folder
		bin_folder_name = main_folder_name + "/bin"
		create_structure_02_01.create_folder(bin_folder_name)

		# Create doc folder
		doc_folder_name = main_folder_name + "/doc"
		create_structure_02_01.create_folder(doc_folder_name)

		# Create log folder
		doc_folder_name = main_folder_name + "/log"
		create_structure_02_01.create_folder(doc_folder_name)

		return main_folder_name

	def create_folder(directory):
		"""Creates a folder
		"""
		try:
			if not os.path.exists(directory):
				os.makedirs(directory)
		except OSError:
			print ('Error: Creating directory. ' +  directory)

	def create_source(main_folder_name, results):
		"""Writes the standards line of code based on the extension
		"""
		time = datetime.now()
		file_name_and_path = f"{main_folder_name}/bin/{results[0]}.{results[1]}"
		if(results[1] == "py"):
			text = f'"""{results[0]}\n"""\n\n__author__ = "davidecastellani@castellanidavide.it", "chiara@sabaini.com"\n__version__ = "02.01 2020-03-24"\n\n'	# first part
			text += f'class {results[0]}:\n\tdef __init__ (self):\n\nif __name__ == "__main__":\n\t{results[0]}()'
		elif(results[1] == "js"):
			text = f'/**\n * @file {results[0]}.{results[1]}\n *\n * @version 01.01 {str(time.year)}{str(time.month)}{str(time.day)}\n *\n * @brief desc\n *\n * @ingroup {results[0]}\n * (Note: this needs exactly one @defgroup somewhere)\n *\n * @author Castellani Davide & Sabaini Chiara\n *\n *Contact: davidecastellani@castellanidavide.it, chiara@sabaini.com\n *\n */'
		elif(results[1] == "c"):
			init = f'/**\n * @file {results[0]}.{results[1]}\n *\n * @version 01.01 {str(time.year)}{str(time.month)}{str(time.day)}\n *\n * @brief desc\n *\n * @ingroup {results[0]}\n * (Note: this needs exactly one @defgroup somewhere)\n *\n * @author Castellani Davide & Sabaini Chiara\n *\n *Contact: davidecastellani@castellanidavide.it, chiara@sabaini.com\n *\n */'
			text = init + ""
		elif(results[1] == "cpp"):
			init = f'/**\n * @file {results[0]}.{results[1]}\n *\n * @version 01.01 {str(time.year)}{str(time.month)}{str(time.day)}\n *\n * @brief desc\n *\n * @ingroup {results[0]}\n * (Note: this needs exactly one @defgroup somewhere)\n *\n * @author Castellani Davide & Sabaini Chiara\n *\n *Contact: davidecastellani@castellanidavide.it, chiara@sabaini.com\n *\n */'
			text = init + f'\n\n#include <bits/stdc++.h>\n\nusing namespace std;\n\nint main() {"{"}\n    return 0;\n{"}"}'
		elif(results[1] == "cs"):
			init = f'/**\n * @file {results[0]}.{results[1]}\n *\n * @version 01.01 {str(time.year)}{str(time.month)}{str(time.day)}\n *\n * @brief desc\n *\n * @ingroup {results[0]}\n * (Note: this needs exactly one @defgroup somewhere)\n *\n * @author Castellani Davide & Sabaini Chiara\n *\n *Contact: davidecastellani@castellanidavide.it, chiara@sabaini.com\n *\n */'
		elif(results[1] == "html"):
			text = f'<!DOCTYPE html>\n<!--\n@author: Castellani Davide & Sabaini Chiara 3CI a.s. 2019/2020\n@version: 01.01 {str(time.year)}-{str(time.month)}-{str(time.day)}\n-->\n<html>\n\n<head>\n\n\t<title>{results[0]}</title>\n\n\t<meta charset="utf-8">\n\n\t<meta name="viewport" content="width=device-width, initial-scale=1">\n\n\t<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css">\n\n\t<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>\n\n\t	<script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.16.0/umd/popper.min.js"></script>\n\n\t<script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.4.1/js/bootstrap.min.js"></script>\n\n\t<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>\n\n</head>\n\n\n\n<body>\n\n\t<div class="container">\n\n\t</div>\n\n</body>\n\n</html>'
		elif(results[1] == "bat"):
			text = f"@ECHO OFF\nCLS\n\nREM\n{results[0]}\nREM Made by Castellani Davide & Sabaini Chiara 3CI a.s. 2019/2020\n"
		elif(results[1] == "ino"):
			text =f"// Author: Castellani Davide & Sabaini Chiara\n// Version: 01.01  {str(time.year)}-{str(time.month)}-{str(time.day)}\nvoid setup(){'{'}\n  Serial.begin(9600);\n{'}'}\nvoid loop(){'{'}\n\n{'}'}"
		else:
			text = f"# {results[0]}"

		f = open(file_name_and_path, "w+")
		f.write(text)
		f.close()

	def create_README(main_folder_name, results):
		"""Creates the README.md
		"""
		time = datetime.now()
		file_name_and_path = main_folder_name + "/doc/README.md"
		init = f"# {results[0]}\n"
		tags = f"\n## Tags\n #tag1, #tag2\n"
		desc = f"\n## Description\n"
		req = f"\n## Required\n - \n"
		dir_structure = f"\n### Directories structure\n - bin\n\t - {results[0]}.{results[1]}\n - doc\n\t - README.md\n - log\n\t - trace.log\n"
		exe_examples = f"\n### Execution examples\n - {results[0]}.{results[1]}\n\t - \n"		
		changelog = f"\n## Changelog\n- [01.01_{str(time.year)}-{str(time.month)}-{str(time.day)}](#01.01_{str(time.year)}-{str(time.month)}-{str(time.day)})\n"
		version = f"\n### 01.01_{str(time.year)}-{str(time.month)}-{str(time.day)}\n - first version\n"
		finish = f"\nMade by Castellani Davide & Sabaini Chiara\nIf you have any problem please contact us:\n- davidecastellani@castellanidavide.it\n- chiara@sabaini.com"
		sep = f"\n---"
		text = init + tags + desc + req + sep + dir_structure + sep + exe_examples + sep + changelog + sep + version + sep + finish
		with open(file_name_and_path, "w+") as f:
			f.write(text)

	def create_log(main_folder_name):
		"""Creates the trace.log
		"""
		file_name_and_path = main_folder_name + "/log/trace.log"
		with open(file_name_and_path, "w+"):
			pass
		

if __name__ == "__main__":
	try:
		create_structure()
	except:
		print("There is an error, try again.")

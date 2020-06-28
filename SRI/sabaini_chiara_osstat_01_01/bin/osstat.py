"""OSSTAT
"""

__author__ = "Sabaini Chiara 3CI"
__version__ = "01.01 2020-05-04"

import os
import stat
import time
from datetime import datetime

def main():
    start_time = time.time()
    log("Start time: " + str(datetime.now()))

    directory_path = os.getcwd()
    walk(directory_path)

    log("Done")
    log("End time: " + str(datetime.now()))
    log("Execution time: " + str(time.time() - start_time) + 's')
    log("")

def walk(directory_path):
    """Browses every subdirectory and every file,
    starting from a given directory."""
    
    log(f"Printing on screen the given directory name: {directory_path}")

    for current_directory, subdirectories, files_in_current_directory in os.walk(directory_path):
        log(f"Analizing directory {current_directory}")
        print(f"Actual directory: {current_directory}")
        print_and_log(f"Present files: {files_in_current_directory}")

        for file in files_in_current_directory:
            print('-'*16)
            osstat(current_directory + '\\' + file)
            print('-'*16)

def osstat(filename): 
    """Shows the properties of a file"""

    stats = os.stat(filename)
    print_and_log(f"Analizing file {filename}")
    print_and_log(f"Properties of {filename}:")
    print_and_log(f"Dimension in byte: {stats[stat.ST_SIZE]} byte")
    print_and_log(f"Last modify: {time.ctime(os.path.getmtime(filename))}")
    print_and_log(f"Last access: {time.ctime(os.path.getatime(filename))}")
    print_and_log(f"Created: {time.ctime(os.path.getctime(filename))}")
    print_and_log(f"Last read access: {os.access(filename, os.R_OK)}")
    print_and_log(f"Last write access: {os.access(filename, os.W_OK)}")
    print_and_log(f"Last execution acces: {os.access(filename, os.X_OK)}")
    
def log(item):
    """Writes in the log file"""
    with open(f'log\\log.log', 'a') as log_file:
        log_file.write(str(item) + '\n')

def print_and_log(item):
    """Writes on the screen and in the log file"""
    print(item)
    log(item)
    
if __name__ == "__main__":
    main()

"""OSSTAT"""

__author__ = "Sabaini Chiara 3CI"
__version__ = "01.03"
__date__ = "2020-05-07"

import os
import stat
import time
from pathlib import Path
from datetime import datetime
from urllib.request import urlopen

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

    properties = [
        str(urlopen(f'https://showcase.linx.twenty57.net:8081/UnixTime/fromunix?timestamp={int(time.time())}').read(), encoding="utf-8"),
        filename,
        stats[stat.ST_SIZE],
        time.ctime(os.path.getmtime(filename)),
        time.ctime(os.path.getatime(filename)),
        time.ctime(os.path.getctime(filename)),
        os.access(filename, os.R_OK),
        os.access(filename, os.W_OK),
        os.access(filename, os.X_OK)
    ]

    print_and_log(f"Analizing file {properties[1]}")
    print_and_log(f"Properties of {properties[1]}:")
    print_and_log(f"Dimension in byte: {properties[2]} byte")
    print_and_log(f"Last modify: {properties[3]}")
    print_and_log(f"Last access: {properties[4]}")
    print_and_log(f"Created: {properties[5]}")
    print_and_log(f"Read permissions: {properties[6]}")
    print_and_log(f"Write permissions: {properties[7]}") 
    print_and_log(f"Execution permissions: {properties[8]}")

    csv(properties)


def csv(row):
    """Writes on a csv file"""
    if not Path('flussi').is_dir():
        Path('flussi').mkdir(exist_ok=True)

    with open('flussi\\osstat.csv', 'a') as csv_file:
        for cell in row:
            csv_file.write(str(cell) + ', ')
        csv_file.write('\n')


def log(item):
    """Writes in the log file"""
    with open('log\\log.log', 'a') as log_file:
        log_file.write(str(item) + '\n')

def print_and_log(item):
    """Writes on the screen and in the log file"""
    print(item)
    log(item)
    
if __name__ == "__main__":
    main()

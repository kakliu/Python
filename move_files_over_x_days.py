# Script Name   : move_files_over_x_days.py
# Author        : Craig Richards
# Created       : 8th December 2011
# Last Modified :
# Version       :1.0
# Modifications :
# Description   : This will move all the files from the src directory that are over 240 days old to the destination directory.

import shutil
import sys
import time
import os
src = 'u:\\test'  # Set the source directory
dst = 'c:\\test'  # Set the destination directory
now = time.time()  # Get the current time
for f in os.listdir(src):  # Loop through all the files in the source directory
    if os.stat(f).st_mtime < now - 240 * 86400:  # Work out how old they are, if they are older than 240 days old
        if os.path.isfile(f):  # Check it's a file
            shutil.move(f, dst)  # Move the files
            

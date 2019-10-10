"""------------------------------------------------------------------------------------------------------
Script Name:      Update workspace ids of elements in xml's
Version:          1.1
Description:      This tool updates workspace ids of elements in xml files of the home folder and its 
                  subdirectories.
Created By:       Kusasalethu Sithole
Date:             2019-09-15
Last Revision:    2019-09-15
------------------------------------------------------------------------------------------------------"""
 
#import modules
import os
from pathlib import Path
import glob

root_directory = "C:/Program Files/GeoServer1_Tomcat/webapps/geoserver/data/workspaces/ramm-live-data"

#update passwords
def update_password():
    new = '<entry key="passwd">crypt1:BnJH7G8QrHczVJLOBGAPGV0ypc3eoQMp</entry>'
    working_directory = root_directory + '/' + dir
    for doc in os.listdir(working_directory):
        if doc[-4:] == ".xml": 
            xml = working_directory + "/" + doc
            xml_reader = open(xml, "rt")
            old = ''
            for line in xml_reader:
                line_noSpaces = line.strip()
                split_line = line_noSpaces.split(':')
                for phrase in split_line:
                    if phrase  == '<entry key="passwd">crypt1':
                        old = line_noSpaces
            xml_reader.close()

            txt = Path(xml).read_text()  # pylint: disable=no-member
            txt = txt.replace(old, new)
            
            if old != '':
                xml_writer = open(xml, "wt")
                xml_writer.write(txt)
                xml_writer.close() 

# loop through folders
for subdir, dirs, files in os.walk(root_directory):
    for dir in dirs:
        update_password()
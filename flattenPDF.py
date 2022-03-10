# -*- coding: utf-8 -*-
"""
Created on Thu Mar 10 11:40:06 2022

@author: AlvaroFloresR
"""

#Import Libraries
import os
from pdf2image import convert_from_path

#Initial Variables
resolution = 100 #dpi, 100 is more than enough and higher values usually run out of memory
sourcePDFName = 'nameofSourceFile.pdf'
outputPDFName = 'nameofOutputFile.pdf'

#Create Output Combined Path
cwd = os.getcwd()
sourcePath = os.path.join(cwd, sourcePDFName)
destinationPath = os.path.join(cwd, outputPDFName)

#Obtain List of Images
#Annotation as hidden, make it false to not hide them
tmpImg = convert_from_path(sourcePath,dpi=resolution,hide_annotations=True,fmt='jpeg')

#Save Images as a PDF
tmpImg[0].save(
    destinationPath, "PDF" ,resolution=resolution, save_all=True, append_images=tmpImg[1:]
)

#To also Save the images independently as .jpeg files change this to true
if(False):
    nameImage = 'imgpy-'
    for i, im in enumerate(tmpImg):
        im.save(os.path.join(cwd,'{}{}.jpg').format(nameImage,i))

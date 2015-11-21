#!/usr/bin/python
#title			:texgenerate.py
#description	:Python script to generate Latex assignment template
#author			:T. Tyler Daugherty
#date			:20151119
#version		:0.1
#usage			:python texgenerate.py
#notes			:
#python_version	:2.7.10
#Copyright 2015 T. Tyler Daugherty. All rights reserved.
#==============================================================================

# Import the modules needed to run the script.
from os.path import exists
from time import strftime
import datetime
import os

now = datetime.datetime.now()

title = raw_input("Project Title: ")
doc_title = raw_input("Document Title: ")
doc_due = raw_input("Due Date: ")
doc_course = raw_input("Course: ")

# Add .py to the end of the script.
title = title + '.tex'

# Convert all letters to lower case.
title = title.lower()

# Remove spaces from the title.
title = title.replace(' ', '_')

# Check to see if the file exists to not overwrite it.
if exists(title):
    print "\nA script with this name already exists."
    exit(1)

#define tex document basic characteristics
name = 'T. Tyler Daugherty'
classes = ['article','proc','minimal','report','book','slides','memoir','letter','beamer']
doc_class = classes[int(raw_input('Choose a Class:\n\narticle (0)\nproc (1)\nminimal (2)\nreport (3)\nbook (4)\nslides (5)\nmemoir (6)\nletter (7)\nbeamer (8)\n'))]
fontsize = raw_input('Font Size (pt): ')

#create tex project architecture
os.system('mkdir tex')
os.chdir('tex/')
os.system('mkdir content')
os.system('mkdir content/images')

# Create a file that can be written to.
fname = open(title, 'w')

# Set the date automatically.
date = strftime("%Y%m%d")
year = str(now.year)

# Write the data to the file.
fname.write('\documentclass[letterpaper,' + fontsize + 'pt,oneside]{'+ doc_class +'}')
fname.write('\n\usepackage{amsthm, array, bm, color, comment, float, gensymb, graphicx, hyperref}')
fname.write('\n\usepackage[version = 4]{mhchem}')
fname.write('\n\usepackage[margin=2cm]{geometry}\n\\restylefloat{table}')
fname.write('\n\usepackage[procnames]{listings}')

#Make \nonstopmode
fname.write('\n\n\\nonstopmode\n')

#Define syntax highlighting for python in Lstlisting Environment
fname.write('\n\n%Define local definitions and commands')
fname.write('\n\definecolor{keywords}{RGB}{255,0,90}\n\definecolor{comments}{RGB}{0,0,113}\n\definecolor{red}{RGB}{160,0,0}\n\definecolor{green}{RGB}{0,150,0}')
fname.write('\n\lstset{language=Python,basicstyle=\ttfamily\small,keywordstyle=\color{keywords},commentstyle=\color{comments},stringstyle=\color{red},showstringspaces=false,identifierstyle=\color{green},procnamekeys={def,class}}')

#Define local commands
fname.write('\n\n%Define Local Commands')
fname.write('\n'+'\\newcommand{\ProjAuthors}{'+name+'}')
fname.write('\n\\newcommand{\ProjTitle}{'+doc_title+'}')
fname.write('\n\\newcommand{\ProjNote}{Complied on {\\today}}')
fname.write('\n\\newcommand{\DueDate}{'+doc_due+'}')
fname.write('\n\\newcommand{\Course}{'+doc_course+'}')
fname.write('\n\\newcommand{\Lagr}{\mathcal{L}}')
fname.write('\n')

#Establish PDF Hyper Environment
fname.write('\n%Establish Hyper Environment for PDF')
fname.write('\n\hypersetup{\npdftitle={\ProjTitle},\npdfauthor={\ProjAuthors},\npdfsubject={},\npdfcreator={pdflatex},\npdfproducer={},\npdfkeywords={},\npdfpagemode={},\nbookmarks=true,\nunicode=true,\nbookmarksopen=true,\npdfstartview=FitH,\npdfpagelayout=OneColumn,\npdfpagemode=UseOutlines,\nhidelinks,\nbreaklinks}')

#Define Title Environment
fname.write('\n\n%Define Title Environment')
fname.write('\n\\title{\ProjTitle \\\\ {\\normalsize Due: \DueDate} \\\\ {\\normalsize \\textsc{\Course}}}')
fname.write('\n\n\\author{T. Tyler \\textsc{Daugherty}}')
fname.write('\n\date{}')

#Space before begining of document
fname.write('\n')
fname.write('\n')

#Begin Document
fname.write('\n\\begin{document}')
fname.write('\n\maketitle')
fname.write('\n\n\n')
fname.write('\n\end{document}')

# Close the file after writing to it.
fname.close()

os.system('atom ' + title)

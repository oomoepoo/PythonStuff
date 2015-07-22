#-*- coding: UTF-8 -*-
# Erstmals in Python3, hooray!
# Aufgabe: Alienierungsdateien einlesen, alinierung darstellen und in html ausgeben
# benötigt lingpy
# Läuft sogar auch auf Windows!
# Fuck Windows, you and your stupid backslash! >\\\<


import os
from lingpy import *

html_string = "<html><header></header><body><ul>"

msa_dir=os.path.normpath("./msatest/")
msa_html=os.path.normpath("./msatest/msa_html")
html_name = os.path.join(msa_html,"allinierungs_navigation.html")
if not (os.path.exists(msa_dir)):
    print ("Couldn't find msa-directory, please put in the same folder you run this script from!")

for root, dirs, files in os.walk(msa_dir):
    for name in files:
        n= os.path.join(root,name)
        msa = MSA(n)
        msa.output('html',filename=os.path.join(msa_html,name[0:len(name)-4])	
        
        html_string.append("<li><a href="+name[0:len(name)-4]+">"+name+"</li>")
html_string.append("</ul></body></html>")

with open(html_name, wb) as f:
	f.write(html_string)

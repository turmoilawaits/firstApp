'''
Created on Sep 16, 2014

@author: anksriv2
'''

import csv 

from xml.dom import minidom

xmldoc = minidom.parse('C:\\Users\\anksriv2\\UcsFaults_ElCapMR1.xml')

prop=xmldoc.getElementsByTagName('fault')
out = ('C:\\Users\\anksriv2\\out.csv')
out_file = open(out, "a")



for propName in prop:
    code = propName.getAttribute('code')
    message = propName.getAttribute('message')
    severity = propName.getAttribute('severity')
    type1 = propName.getAttribute('type')
    cause = propName.getAttribute('cause')
    value = code +',' + severity +','+ type1 + ',' + cause +','+ message + "\n"
    out_file.write(value)


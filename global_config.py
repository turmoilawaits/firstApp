'''
Created on Sep 16, 2014

@author: anksriv2
'''
from xml.dom import minidom

xmldoc = minidom.parse('C:\\Users\\anksriv2\\Desktop\\Learning\\XMLReport\\SET_MO.xml')

prop=xmldoc.getElementsByTagName('faults')

for propName in prop:
    mo=propName.getAttribute('code')
    print mo 
    
    
"""
    if mo == 'ManagedObject':
        for child in propName.childNodes:
            dn=child.getAttribute('dn')
            print dn
"""
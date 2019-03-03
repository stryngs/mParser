import os
import re
import sys
import xml.dom.minidom

class Xml(object):
    """High level class for visualizing and deciphering XML scan results from

        - masscan
        - nmap
        - etc...
    """
    
    def __init__(self, xmlInput):
        xmlOutput = '.'.join(xmlInput.split('.')[:-1]) + '_pretty.xml'
        
        ## Write semi pretty file
        with open('tmp_file', 'w') as oFile:
            with open(xmlInput, 'r') as xmldata:
                oFile.write(xml.dom.minidom.parseString(xmldata.read()).toprettyxml())

        ## Open the file and turn into a list so we can iterate
        with open('tmp_file', 'r') as iFile:
            xList = iFile.read().splitlines()

        ## Rewrite into pretty XML output file
        with open(xmlOutput, 'w') as oFile:
            for x in xList:
                if not re.search('^\s*$', x):
                    oFile.write(x.replace('\t', '    ') + '\n')

        ## Done & cleanup
        print('Created {0}\n'.format(xmlOutput))
        os.remove('tmp_file')

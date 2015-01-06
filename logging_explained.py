'''
Created on Sep 16, 2014

@author: anksriv2
'''

import logging

logger = logging.basicConfig(filename='logfile.log',level=logging.DEBUG)
logger = logging.getLogger('root')
logger.setLevel(logging.DEBUG)




def main():
    try:
        logger.info('got inside try block')
        mathFail=1/0
    except Exception, e:
        logger.critical(str(e))
        
main()       




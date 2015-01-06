'''
Created on Nov 24, 2014

@author: anksriv2
'''

import time



ucsmLogFile = open('C:\\Users\\anksriv2\\Cisco.UCSM.ConfigMgr.Service.log','r')      
#start = datetime.time.minute     
start = time.time()
x = 0
while x<5 :    
    for line in ucsmLogFile:        
        if  "Successfully Deleted UCS Domain" in line:
            print "found the string pattern "
            break
        else:
            
            print "still finding the string pattern "
            x += 1
stop = time.time()         
diff = str(stop - start)
print diff                                                                        
ucsmLogFile.close()





import os

class checkFile():    
    
    def is_non_zero_file(self,fpath):      
        if  os.path.getsize(fpath) > 0 :                        
            return 1
        else:      
            return 0


if __name__ == '__main__':
    fpath = 'C:\\Users\\anksriv2\\out.txt'
    reb = checkFile()
    val = reb.is_non_zero_file(fpath)
    
    if val == 1:
        print "plugin installed"
    else:
        print "plugin unistalled"

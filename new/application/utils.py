####################################################
# Copyright (c) 2017  Inphi Corp.                  #
####################################################
###########################################
#          Inphi Confidential             #
###########################################

import math
import inspect
import sys
from time import sleep

class Chip_Revision:
    def __init__(self, revid=None):
        self.revid = revid

    def is_revid(self, revid):
        return self.revid == revid

    def check_revid(self, revid):
        if self.revid != revid:
            print('WARNING: rev id %s is needed, but currently is %s'%(str(revid),str(self.revid)))

    def get_revid(self):
        return self.revid

    def set_revid(self, revid):
        self.revid = revid


def mywait(time_lapse):
    time_start = time.time()
    time_end = (time_start + time_lapse)
    while time_end > time.time():
        pass

def monitor(funcs, niters=-1, sample_time=1, ret = False):
    i = niters-1
    r = []
    while i>=0 or niters < 0:
        for f in funcs:
            data = f()
            print(data)
            if ret == True:
                r.append(data)
            sleep(sample_time)
        if niters > 0:
            i -= 1
    return r

class BitVector:
    def __init__(self, val=0, signed=False):
        self._val = val
        self.signed = signed
        
    def __setslice__(self,highIndx,lowIndx,newVal):

        if newVal != 0:
            r = False
            try:
                if self.signed and newVal<0:
                    r = math.ceil(math.log(-newVal)/math.log(2)) <= (highIndx-lowIndx+1)
                else:
                    r = math.ceil(math.log(newVal)/math.log(2)) <= (highIndx-lowIndx+1)

            except:
                print('highIndx=%i lowIndx=%i newVal=%i'%(highIndx,lowIndx,newVal))
            assert r,  'highIndx=%i lowIndx=%i newVal=%i'%(highIndx,lowIndx,newVal)
            
        # clear out bit slice
        clean_mask = (2**(highIndx+1)-1)^(2**(lowIndx)-1)
        
        self._val = self._val ^ (self._val & clean_mask)
        # set new value
        self._val = self._val | (newVal<<lowIndx)

    def __getslice__(self,highIndx,lowIndx):
        return (self._val >> lowIndx) & (2L**(highIndx - lowIndx + 1)-1)

    def __setitem__(self,index,val):
        self.__setslice__(index,index,val);

    def __getitem__(self,index):
        return self.__getslice__(index,index)

def read_format_base(fstr):
        import re
        if(re.search('^U(\d+)[.]([-]*\d+)',fstr.upper())):
            m = re.search('^U(\d+)[.]([-]*\d+)',fstr.upper())
            number_format = ['fxp',False,int(m.group(1)),int(m.group(2))]
        elif(re.search('^S(\d+)[.]([-]*\d+)',fstr.upper())):
            m = re.search('^S(\d+)[.]([-]*\d+)',fstr.upper())
            number_format = ['fxp',True,int(m.group(1)),int(m.group(2))]
        elif(re.search('^MS(\d+)',fstr.upper())):
            m = re.search('^MS(\d+)',fstr.upper())
            number_format = ['MS',False,int(m.group(1))]
        elif(re.search('^I(\d+)',fstr.upper())):
            m = re.search('^I(\d+)',fstr.upper())
            number_format = ['I',False,int(m.group(1))]
        else:
            raise ValueError("format: "+fstr+" do not exist!\n"+ \
                "Allowed values are 'UN.F', 'SN.F' , 'MSN' or 'IN' where N is the total number of bits(positive integer) and F is the number of fractional bits (integer) ")
        return number_format
    
    
class Tee:
    def __init__(self, log_file_name = 'stdout.txt' ):
        self.log_file        = None
        self.save_sys_stdout = None
        self.files           = []
        if log_file_name != -1:            
            try:
                self.log_file = open(log_file_name,'a')
                self.start_log(self.log_file)
            except:
                print('Tee error open file: '+str(log_file_name))
    def write(self, obj):
        for f in self.files:
            f.write(obj)
    def start_log(self, log_file):
        # save standard output
        self.save_sys_stdout = sys.stdout
        # redirect output
        self.files.append(sys.stdout)
        self.files.append(log_file)
        sys.stdout = self
    def stop_log(self):
        if self.save_sys_stdout != None:
            sys.stdout = self.save_sys_stdout
        try:
            self.log_file.close()
        except:
            pass

####################################################
# Copyright (c) 2017  Inphi Corp.                  #
####################################################
###########################################
#          Inphi Confidential             #
###########################################

#from application.utils import read_format_base

class fxp():

    flp_value = []
    fxp_value = []
    signed = True
    nb = 0
    nbf = 0

    def __init__(self, _signed_or_fstr=True, _nb=0, _nbf=15):

        if not isinstance(_signed_or_fstr, str):
            if(_nb < 1):
                raise ValueError("Integer width needs to be >= 1!")
            #        if(_nbf < 0):
            #            raise ValueError, "Fractional width needs to be >= 0!"
            self.signed = _signed_or_fstr
            self.nb = _nb 
            self.nbf = _nbf
        else:
            f = read_format_base(_signed_or_fstr)
            if(f[0] == 'fxp'):
                self.signed = f[1]
                self.nb = f[2] 
                self.nbf = f[3]
                self.nbi = _nb - _nbf
            else:
                raise ValueError("format: "+signed_or_fstr+" not allow for fxp data!\n")
        self.nbi = _nb - _nbf


###################################################################### 
# Functions:
#           - set_flp()
#           - set_fxp()
#           - get_flp()
#           - get_fxp()
###################################################################### 

## Set Flp
    def set_flp(self, values_list, saturate = False, rounding = False):
                
        values = []
        self.flp_value = []
        self.fxp_value = []

        if type(values_list) is list:
            values = values_list
        else:
            values.append(values_list)
        
        
        for value in values:
            value = float(value)
            self.format_check(value, saturate)
            
            if rounding:
                tmp = value * 2.0**self.nbf + 0.5
            else:
                tmp = value * 2.0**self.nbf
                
            if not self.signed and saturate and tmp >= 2.0**(self.nb)-1:
                tmp = 2.0**(self.nb)-1            
            elif self.signed and saturate and tmp >= 2.0**(self.nb-1)-1 : 
                tmp = 2.0**(self.nb-1) - 1
            elif self.signed and saturate and tmp < -2.0**(self.nb-1) :
                tmp = -2.0**(self.nb-1)

            self.flp_value.append(float(int(tmp)) / pow(2, self.nbf))

            if(tmp<0):            
                self.fxp_value.append(int(pow(2, self.nb) + tmp))
            else:          
                self.fxp_value.append(int(tmp))


## Set Fxp
    def set_fxp(self, values_list, saturate = False):

        values = []
        self.flp_value = []
        self.fxp_value = []

        if type(values_list) is list:
            values = values_list
        else:
            values.append(values_list)


        for value in values:
            if(type(value) is not int and type(value) is not long): 
                raise ValueError("Value have to be Integer, but it is", type(value))

            self.format_check(value, saturate)

            if saturate and value >= 2.0**self.nb:
                self.fxp_value.append(int(2.0**self.nb - 1))
            else:
                self.fxp_value.append(int(value))

            if (self.signed):
                if saturate and value >= 2.0**self.nb:
                    self.flp_value.append(0)
                else:
                    if(value > pow(2, (self.nb-1))-1):
                        tmp = pow(2, self.nb) - value 
                        self.flp_value.append(-(tmp / (2.0 ** self.nbf)))
                    else:
                        self.flp_value.append(value / (2.0 ** self.nbf))
                    
            else:
                if saturate and value >= 2.0**self.nb:
                    self.flp_value.append((2.0**self.nb - 1) / (2.0**self.nbf))
                else:
                    self.flp_value.append(value / (2.0**self.nbf))

## Get Flp
    def get_flp(self):
        return self.flp_value

## Get Fxp
    def get_fxp(self):
        return self.fxp_value

## Get Format
    def get_format(self):
        if (self.signed):
           return "S%d.%d" % (self.nb, self.nbf)
        else:    
           return "U%d.%d" % (self.nb, self.nbf)

## Format Check
    def format_check(self, value, saturate = False):

        if(type(value) is float):  
            if(value < 0 and self.signed==False):
                raise ValueError("Signal is Unsigned")

            tmp = value * 2.0**self.nbf
          
            if not saturate:
                if(self.signed):
                    if (tmp < 0):
                        if (tmp < -(2.0**(self.nb-1))):
                            raise ValueError("Value exceed bit width")

                    else:
                        if (int(tmp) >  2.0**(self.nb-1) - 1):
                            raise ValueError("Value exceed bit width")

                else:
                    if (tmp >  2.0**self.nb - 1):
                        raise ValueError("Value exceed bit width")

        else:
            if(value < 0):
                raise ValueError("Signal have to be Unsigned")

            if not saturate:
                if(value >  2.0**self.nb - 1):
                    raise ValueError("Signal exceed bit width")

            


###################################################################### 
# Test
###################################################################### 
#a = fxp(True, 8, 7, True)
#a.set_flp(1)
#a.set_fxp(255)
#print a.get_flp()
#print a.get_fxp()
#a.set_flp([0.4, 0.3])
#a.set_fxp([4, 5])
#print a.get_flp()
#print a.get_fxp()
# a = fxp(True, 4, 2)

# a.set_flp(0.9, True, True)
# print a.get_fxp()

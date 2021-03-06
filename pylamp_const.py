#!/usr/bin/python3

DEBUG = 3


DIM = 2         # 2 or 3, currently only 2 implemented 


IZ  = 0         # indices for different axes, this should probably
                # be compatible with python array indexing (rows, cols, etc),
                # i.e. zxy
IX  = 1
IY  = 2


IP  = DIM       # order number of the pressure (continuity) equation in stokes,
                # in 2D it's 3rd, in 3D 4th, etc.


# Physical constants
G = [9.81, 0]             # grav. accel., length == DIM 
SECINYR = 60*60*24*365.25
SECINKYR = SECINYR * 1e3
SECINMYR = SECINYR * 1e6
GASR = 8.31446 # (J / molK)


# Tracer constants
NFTRAC = 13     # number of tracer functions
TR_RHO = 0      # indices for tracer functions: density
TR_ETA = 1      # viscosity
TR_MRK = 2      # passive markers
TR_TMP = 3      # temperature
TR_HCD = 4      # heat conductivity
TR_HCP = 5      # heat capacity
TR_RH0 = 6      # inherent density
TR_ALP = 7      # coefficient of thermal expansion
TR_MAT = 8      # material numbering
TR_ACE = 9      # activation energy
TR_ET0 = 10     # inherent viscosity
TR_IHT = 11     # internal heating, W/m3
TR__ID = 12     # special one, unique ID, if <0, outside domain


# Numerical constants
EPS = 2**(-10)

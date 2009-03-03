# mapping with the available HLT tables supported by cmsDriver.py
hltTable = dict()

# HLT trigger table for the 2009 STARTUP 8E29 menu
hltTable['8E29'] = ( 
    'HLTrigger/Configuration/HLT_8E29_cff', 
)

# HLT trigger table for the 2009 STARTUP 1E31 menu
hltTable['1E31'] = ( 
    'HLTrigger/Configuration/HLT_1E31_cff', 
)

hltTable['default'] = hltTable['8E29']

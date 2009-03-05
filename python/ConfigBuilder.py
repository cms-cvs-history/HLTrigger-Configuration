# mapping with the available HLT tables supported by cmsDriver.py
__triggerTable = {

    # HLT trigger table for the 2009 STARTUP 8E29 menu
    '8E29': ( 
        'HLTrigger/Configuration/HLT_8E29_cff', 
    ),

    # HLT trigger table for the 2009 STARTUP 1E31 menu
    '1E31': ( 
        'HLTrigger/Configuration/HLT_1E31_cff', 
    )
}


def getConfigsForScenario(trigger = None):
    """
    Retrieves the list of files needed to run a given trigger menu.
    If no trigger or an invalid trigger is given, use the default one. 
    """
    # default trigger, used if none is 
    default = '8E29'

    if not trigger or trigger not in __triggerTable:
        trigger = default

    return __triggerTable[trigger]

#!/bin/tcsh

# usage: ./getEventContent.sh

setenv HLTtable /dev/CMSSW_3_0_0/pre3/HLT

cmsenv

rehash

 edmConfigFromDB --configName $HLTtable --nopaths --noes --nopsets --noservices --cff --blocks hltDefaultOutput::outputCommands >& HLTDefaultOutput_cff.py
 /bin/mv -f HLTDefaultOutput_cff.py ../python

 edmConfigFromDB --configName $HLTtable --nopaths --noes --nopsets --noservices --cff --blocks hltDefaultOutputWithFEDs::outputCommands >& HLTDefaultOutputWithFEDs_cff.py
 /bin/mv -f HLTDefaultOutputWithFEDs_cff.py ../python

 edmConfigFromDB --configName $HLTtable --nopaths --noes --nopsets --noservices --cff --blocks hltDebugOutput::outputCommands >& HLTDebugOutput_cff.py
 /bin/mv -f HLTDebugOutput_cff.py ../python

 edmConfigFromDB --configName $HLTtable --nopaths --noes --nopsets --noservices --cff --blocks hltDebugWithAlCaOutput::outputCommands >& HLTDebugWithAlCaOutput_cff.py
 /bin/mv -f HLTDebugWithAlCaOutput_cff.py ../python

unsetenv HLTtable

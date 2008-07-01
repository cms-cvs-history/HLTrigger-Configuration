#!/bin/tcsh

cmsenv

rehash

setenv HLTtable /dev/CMSSW_2_1_0_pre6/HLT/V11
setenv HLTid    2E30 

if ($1 == CVS) then

# for things in CMSSW CVS - so needs to be run by hand
# incl. mv, cvs commit & tag

 ./getHLT.py $HLTtable $HLTid GEN-HLT

 edmConfigFromDB --configName $HLTtable --nopaths --noes --nopsets --noservices --cff --blocks hltDefaultOutput::outputCommands --format python >& HLTDefaultOutput_cff.py

 edmConfigFromDB --configName $HLTtable --nopaths --noes --nopsets --noservices --cff --blocks hltDebugOutput::outputCommands --format python >& HLTDebugOutput_cff.py

 edmConfigFromDB --configName $HLTtable --nopaths --noes --nopsets --noservices --cff --blocks hltDebugWithAlCaOutput::outputCommands --format python >& HLTDebugWithAlCaOutput_cff.py

else

# for things NOT in CMSSW CVS:

  ./getHLT.py $HLTtable $HLTid

endif

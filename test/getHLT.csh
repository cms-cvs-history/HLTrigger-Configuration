#!/bin/tcsh

cmsenv

rehash

setenv HLTtable /user/fwyzard/CMSSW_2_2_4_HLT4/8E29/V3
setenv HLTid    8E29

if ($1 == CVS) then

# for things in CMSSW CVS - so needs to be run by hand
# incl. mv, cvs commit & tag

 ./getHLT.py $HLTtable $HLTid GEN-HLT

 edmConfigFromDB --configName $HLTtable --nopaths --noes --nopsets --noservices --cff --blocks hltDefaultOutput::outputCommands --format python >& HLTDefaultOutput_cff.py

 edmConfigFromDB --configName $HLTtable --nopaths --noes --nopsets --noservices --cff --blocks hltDefaultOutputWithFEDs::outputCommands --format python >& HLTDefaultOutputWithFEDs_cff.py

 edmConfigFromDB --configName $HLTtable --nopaths --noes --nopsets --noservices --cff --blocks hltDebugOutput::outputCommands --format python >& HLTDebugOutput_cff.py

 edmConfigFromDB --configName $HLTtable --nopaths --noes --nopsets --noservices --cff --blocks hltDebugWithAlCaOutput::outputCommands --format python >& HLTDebugWithAlCaOutput_cff.py

 ls -lt HLT*_cff.py
 /bin/mv -f HLT*_cff.py ../python

else

# for things NOT in CMSSW CVS:

  ./getHLT.py $HLTtable $HLTid

endif

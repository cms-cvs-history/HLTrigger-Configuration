#!/bin/tcsh

cmsenv
rehash

if ($1 == 1E31) then
  # get thje configuration for 1E31
  setenv HLTtable /dev/CMSSW_2_2_4_HLT4/1E31/V4
  setenv HLTid    1E31
  shift
else if ($1 == 8E29) then
  # get the configuration for 8E29
  setenv HLTtable /dev/CMSSW_2_2_4_HLT4/8E29/V9
  setenv HLTid    8E29
  shift
else
  # get the default configuration (8E29)
  setenv HLTtable /dev/CMSSW_2_2_4_HLT4/8E29/V9
  setenv HLTid    8E29
endif

if ($1 == CVS) then
  # for things in CMSSW CVS - so needs to be run by hand
  # incl. mv, cvs commit & tag
  ./getHLT.py $HLTtable $HLTid GEN-HLT
  edmConfigFromDB --configName $HLTtable --nopaths --noes --nopsets --noservices --cff --blocks hltDefaultOutput::outputCommands         --format python >& HLTDefaultOutput_cff.py
  edmConfigFromDB --configName $HLTtable --nopaths --noes --nopsets --noservices --cff --blocks hltDefaultOutputWithFEDs::outputCommands --format python >& HLTDefaultOutputWithFEDs_cff.py
  edmConfigFromDB --configName $HLTtable --nopaths --noes --nopsets --noservices --cff --blocks hltDebugOutput::outputCommands           --format python >& HLTDebugOutput_cff.py
  edmConfigFromDB --configName $HLTtable --nopaths --noes --nopsets --noservices --cff --blocks hltDebugWithAlCaOutput::outputCommands   --format python >& HLTDebugWithAlCaOutput_cff.py

  ls -lt HLT*_cff.py
  /bin/mv -f HLT*_cff.py ../python
else
  # for things NOT in CMSSW CVS:
  ./getHLT.py $HLTtable $HLTid
endif

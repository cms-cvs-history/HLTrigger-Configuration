#! /bin/bash

cmsenv
hash -r

if [ "$1" == "1E31" ]; then
  # get thje configuration for 1E31
  HLTid="1E31"
  HLTtable="/dev/CMSSW_2_2_4_HLT4/1E31/V9"
  HLTcontent="/dev/CMSSW_2_2_4_HLT4/merged/V4"
  shift
elif [ "$1" == "8E29" ]; then
  # get the configuration for 8E29
  HLTid="8E29"
  HLTtable="/dev/CMSSW_2_2_4_HLT4/8E29/V11"
  HLTcontent="/dev/CMSSW_2_2_4_HLT4/merged/V4"
  shift
else
  # get the default configuration (8E29)
  HLTid="8E29"
  HLTtable="/dev/CMSSW_2_2_4_HLT4/8E29/V11"
  HLTcontent="/dev/CMSSW_2_2_4_HLT4/merged/V4"
fi

if [ "$1" == "CVS" ]; then
  # for things in CMSSW CVS
  ./getHLT.py $HLTtable $HLTid GEN-HLT
  edmConfigFromDB --configName $HLTcontent --nopaths --noes --nopsets --noservices --cff --blocks hltDefaultOutput::outputCommands         --format python > HLTDefaultOutput_cff.py
  edmConfigFromDB --configName $HLTcontent --nopaths --noes --nopsets --noservices --cff --blocks hltDefaultOutputWithFEDs::outputCommands --format python > HLTDefaultOutputWithFEDs_cff.py
  edmConfigFromDB --configName $HLTcontent --nopaths --noes --nopsets --noservices --cff --blocks hltDebugOutput::outputCommands           --format python > HLTDebugOutput_cff.py
  edmConfigFromDB --configName $HLTcontent --nopaths --noes --nopsets --noservices --cff --blocks hltDebugWithAlCaOutput::outputCommands   --format python > HLTDebugWithAlCaOutput_cff.py

  ls -lt HLT*_cff.py
  mv -f HLT*_cff.py ../python
else
  # for things NOT in CMSSW CVS:
  ./getHLT.py $HLTtable $HLTid
fi

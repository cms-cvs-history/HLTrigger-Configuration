#! /bin/bash

HLT='/online/collisions/2011/5e32/v8.0/HLT'
L1T='L1GtTriggerMenu_L1Menu_Collisions2011_v1_mc,frontier://FrontierProd/CMS_COND_31X_L1T'

hltGetConfiguration $HLT --process TEST --l1 $L1T --globaltag L1HLTST311_V0::All --full --offline --mc   --unprescale > offline_mc.py
hltGetConfiguration $HLT --process TEST --l1 $L1T --globaltag GRP311L1HLTV0::All --full --offline --data --unprescale > offline_data.py
hltGetConfiguration $HLT --process TEST --l1 $L1T                                --full --online  --data --unprescale > online_data.py

{
  TABLE=$(echo $HLT | cut -d: -f2)
  DB=$(echo $HLT | cut -d: -f1 -s)
  true ${DB:=hltdev}

  edmConfigFromDB --$DB --configName $TABLE | hltDumpStream 
} > streams.txt

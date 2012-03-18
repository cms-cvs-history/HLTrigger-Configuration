#! /bin/tcsh

cmsenv

rehash

set InputFile = file:/tmp/fwyzard/B814262C-EE97-E011-94FB-003048F118AA.root

hltIntegrationTests /dev/CMSSW_5_2_0/GRun -d hltIntegrationTests -i $InputFile -n 100 -j 4      -x "--l1-emulator" -x "--l1 L1GtTriggerMenu_L1Menu_Collisions2012_v0_mc" -x "--globaltag auto:hltonline"

set InputFile =  file:../RelVal_DigiL1Raw_GRun.root

hltIntegrationTests /dev/CMSSW_5_2_0/GRun -d hltIntegrationTests -i $InputFile -n 100 -j 4 --mc -x "--l1-emulator" -x "--l1 L1GtTriggerMenu_L1Menu_Collisions2012_v0_mc" -x "--globaltag auto:startup"

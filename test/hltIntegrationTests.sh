#! /bin/tcsh

cmsenv

rehash

hltIntegrationTests /dev/CMSSW_4_2_0/GRun -d hltIntegrationTests -i file:/tmp/fwyzard/B814262C-EE97-E011-94FB-003048F118AA.root -n 100 -j 2 -x "--mc --l1 L1GtTriggerMenu_L1Menu_Collisions2011_v4_mc,sqlite_file:/afs/cern.ch/user/g/ghete/public/L1Menu/L1Menu_Collisions2011_v4/sqlFile/L1Menu_Collisions2011_v4_mc.db"

#hltIntegrationTests /dev/CMSSW_4_2_0/GRun -d hltIntegrationTests -i file:../RelVal_DigiL1Raw_GRun.root -n 100 -j 2 -x "--mc --l1 L1GtTriggerMenu_L1Menu_Collisions2011_v4_mc,sqlite_file:/afs/cern.ch/user/g/ghete/public/L1Menu/L1Menu_Collisions2011_v4/sqlFile/L1Menu_Collisions2011_v4_mc.db"

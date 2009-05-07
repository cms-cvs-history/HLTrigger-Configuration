#!/bin/tcsh

cmsenv
rehash

echo "Creating TTbarGenSim"
cmsDriver.py TTbar_Tauola.cfi --step=GEN,SIM --fileout=TTbarGenSim.root --number=100 --mc --no_exec --datatier 'GEN-SIM' --eventcontent=FEVTSIM --python_filename=TTbarGenSim.py

echo
echo "Creating TTbarGenHLT for 2E30"
cmsDriver.py TTbar_Tauola.cfi --step=GEN,SIM,DIGI,L1,DIGI2RAW,HLT --conditions=FrontierConditions_GlobalTag,STARTUP_V9::All                                                --fileout=TTbarGenHLT_2E30.root         --number=100 --mc --no_exec --datatier 'GEN-SIM-DIGI-RAW-HLT' --eventcontent=FEVTDEBUGHLT --customise=HLTrigger/Configuration/customL1THLT_Options.py   --python_filename=TTbarGenHLT_2E30.py

echo
echo "Creating DigiL1Raw for 2E30"
cmsDriver.py RelVal --step=DIGI,L1,DIGI2RAW                       --conditions=FrontierConditions_GlobalTag,STARTUP_V9::All --filein=file:TTbarGenSim.root                 --fileout=RelVal_DigiL1Raw_2E30.root    --number=100 --mc --no_exec --datatier 'GEN-SIM-DIGI-RAW'     --eventcontent=RAW          --customise=HLTrigger/Configuration/customL1T_Options.py      --python_filename=RelVal_DigiL1Raw_2E30.py

echo
echo "Creating DigiL1RawHLT for 2E30"
cmsDriver.py RelVal --step=DIGI,L1,DIGI2RAW,HLT                   --conditions=FrontierConditions_GlobalTag,STARTUP_V9::All --filein=file:TTbarGenSim.root                 --fileout=RelVal_DigiL1RawHLT_2E30.root --number=100 --mc --no_exec --datatier 'GEN-SIM-DIGI-RAW-HLT' --eventcontent=FEVTDEBUGHLT --customise=HLTrigger/Configuration/customL1THLT_Options.py   --python_filename=RelVal_DigiL1RawHLT_2E30.py

echo
echo "Creating HLT for 2E30"
cmsDriver.py RelVal --step=L1,HLT                                 --conditions=FrontierConditions_GlobalTag,STARTUP_V9::All --filein=file:RelVal_DigiL1Raw_2E30.root      --fileout=RelVal_HLT_2E30.root          --number=100 --mc --no_exec --datatier 'RAW-HLT'              --eventcontent=FEVTDEBUGHLT --customise=HLTrigger/Configuration/customHLT_Options.py      --python_filename=RelVal_HLT_2E30.py

echo
echo "Creating HLT2 (re-running HLT) for 2E30"
cmsDriver.py RelVal --step=L1,HLT                                 --conditions=FrontierConditions_GlobalTag,STARTUP_V9::All --filein=file:RelVal_HLT_2E30.root            --fileout=RelVal_HLT2_2E30.root         --number=100 --mc --no_exec --datatier 'RAW-HLT'              --eventcontent=FEVTDEBUGHLT --customise=HLTrigger/Configuration/customHLT2_Options.py     --python_filename=RelVal_HLT2_2E30.py

echo
echo "Creating L1HLT2 (re-running L1 and HLT) for 2E30"
cmsDriver.py RelVal --step=L1,HLT                                 --conditions=FrontierConditions_GlobalTag,STARTUP_V9::All --filein=file:RelVal_DigiL1RawHLT_2E30.root   --fileout=RelVal_L1HLT2_2E30.root       --number=100 --mc --no_exec --datatier 'GEN-SIM-DIGI-RAW-HLT' --eventcontent=FEVTDEBUGHLT --customise=HLTrigger/Configuration/customL1THLT2_Options.py  --python_filename=RelVal_L1HLT2_2E30.py

echo
echo "Creating Reco for 2E30"
cmsDriver.py RelVal --step=RAW2DIGI,RECO                          --conditions=FrontierConditions_GlobalTag,STARTUP_V9::All --filein=file:RelVal_DigiL1Raw_2E30.root      --fileout=RelVal_Reco_2E30.root         --number=100 --mc --no_exec --datatier 'RECO'                 --eventcontent=RECOSIM      --customise=HLTrigger/Configuration/custom_Options.py         --python_filename=RelVal_Reco_2E30.py

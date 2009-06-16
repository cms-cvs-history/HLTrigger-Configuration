#!/bin/tcsh

cmsenv
rehash

echo "Creating TTbarGenSim"
cmsDriver.py TTbar_Tauola.cfi --step=GEN,SIM --fileout=TTbarGenSim.root --number=100 --mc --no_exec --datatier 'GEN-SIM' --eventcontent=FEVTSIM --python_filename=TTbarGenSim.py

foreach lumi ( 8E29 1E31 ) 
  if ( $lumi == 8E29 ) then
    set XL1T = L1:L1Menu_Commissioning2009_v2:Unprescaled
    set XHLT = HLT:$lumi
    set GTAG = STARTUP_V9
  else if ( $lumi == 1E31 ) then
    set XL1T = L1:L1Menu_MC2009_v0:Unprescaled
    set XHLT = HLT:$lumi
    set GTAG = IDEAL_V12
  endif

  echo
  echo "Creating TTbarGenHLT for $lumi"
  cmsDriver.py TTbar_Tauola.cfi --step=GEN,SIM,DIGI,$XL1T,DIGI2RAW,$XHLT  --conditions=FrontierConditions_GlobalTag,${GTAG}::All                                                --fileout=TTbarGenHLT_$lumi.root         --number=100 --mc --no_exec --datatier 'GEN-SIM-DIGI-RAW-HLT' --eventcontent=FEVTDEBUGHLT --customise=HLTrigger/Configuration/customL1THLT_Options.py   --python_filename=TTbarGenHLT_$lumi.py

  echo
  echo "Creating DigiL1Raw for $lumi"
  cmsDriver.py RelVal --step=DIGI,$XL1T,DIGI2RAW                          --conditions=FrontierConditions_GlobalTag,${GTAG}::All --filein=file:TTbarGenSim.root                 --fileout=RelVal_DigiL1Raw_$lumi.root    --number=100 --mc --no_exec --datatier 'GEN-SIM-DIGI-RAW'     --eventcontent=RAW          --customise=HLTrigger/Configuration/customL1T_Options.py      --python_filename=RelVal_DigiL1Raw_$lumi.py

  echo
  echo "Creating DigiL1RawHLT for $lumi"
  cmsDriver.py RelVal --step=DIGI,$XL1T,DIGI2RAW,$XHLT                    --conditions=FrontierConditions_GlobalTag,${GTAG}::All --filein=file:TTbarGenSim.root                 --fileout=RelVal_DigiL1RawHLT_$lumi.root --number=100 --mc --no_exec --datatier 'GEN-SIM-DIGI-RAW-HLT' --eventcontent=FEVTDEBUGHLT --customise=HLTrigger/Configuration/customL1THLT_Options.py   --python_filename=RelVal_DigiL1RawHLT_$lumi.py

  echo
  echo "Creating HLT for $lumi"
  cmsDriver.py RelVal --step=$XL1T,$XHLT                                  --conditions=FrontierConditions_GlobalTag,${GTAG}::All --filein=file:RelVal_DigiL1Raw_$lumi.root      --fileout=RelVal_HLT_$lumi.root          --number=100 --mc --no_exec --datatier 'RAW-HLT'              --eventcontent=FEVTDEBUGHLT --customise=HLTrigger/Configuration/customHLT_Options.py      --python_filename=RelVal_HLT_$lumi.py

  echo
  echo "Creating HLT2 (re-running HLT) for $lumi"
  cmsDriver.py RelVal --step=$XL1T,$XHLT                                  --conditions=FrontierConditions_GlobalTag,${GTAG}::All --filein=file:RelVal_HLT_$lumi.root            --fileout=RelVal_HLT2_$lumi.root         --number=100 --mc --no_exec --datatier 'RAW-HLT'              --eventcontent=FEVTDEBUGHLT --customise=HLTrigger/Configuration/customHLT2_Options.py     --python_filename=RelVal_HLT2_$lumi.py

  echo
  echo "Creating L1HLT2 (re-running L1 and HLT) for $lumi"
  cmsDriver.py RelVal --step=$XL1T,$XHLT                                  --conditions=FrontierConditions_GlobalTag,${GTAG}::All --filein=file:RelVal_DigiL1RawHLT_$lumi.root   --fileout=RelVal_L1HLT2_$lumi.root       --number=100 --mc --no_exec --datatier 'GEN-SIM-DIGI-RAW-HLT' --eventcontent=FEVTDEBUGHLT --customise=HLTrigger/Configuration/customL1THLT2_Options.py  --python_filename=RelVal_L1HLT2_$lumi.py

  echo
  echo "Creating Reco for $lumi"
  cmsDriver.py RelVal --step=RAW2DIGI,RECO                                --conditions=FrontierConditions_GlobalTag,${GTAG}::All --filein=file:RelVal_DigiL1Raw_$lumi.root      --fileout=RelVal_Reco_$lumi.root         --number=100 --mc --no_exec --datatier 'RECO'                 --eventcontent=RECOSIM      --customise=HLTrigger/Configuration/custom_Options.py         --python_filename=RelVal_Reco_$lumi.py

end

#!/bin/tcsh

cmsenv

rehash

foreach lumi ( 8E29 1E31 ) 
  if ( $lumi == 8E29 ) then
    set XL1T = L1:L1Menu_Commissioning2009_v1:Unprescaled
    set XHLT = HLT:$lumi
    set GTAG = STARTUP_31X
  else if ( $lumi == 1E31 ) then
    set XL1T = L1:L1Menu_MC2009_v1:Unprescaled
    set XHLT = HLT:$lumi
    set GTAG = IDEAL_31X
  else
    set XL1T = L1
    set XHLT = HLT
    set GTAG = IDEAL_31X
  endif

  echo " "
  echo "Creating TTbarGenSim $lumi"
cmsDriver.py TTbar_Tauola.cfi --step=GEN,SIM                           --conditions=FrontierConditions_GlobalTag,${GTAG}::All                               --fileout=TTbarGenSim.root               --number=100 --mc --no_exec --datatier 'GEN-SIM'              --eventcontent=FEVTSIM      --customise=HLTrigger/Configuration/custom_Options.py         --python_filename=TTbarGenSim_$lumi.py

  echo " "
  echo "Creating TTbarGenHLT $lumi"
cmsDriver.py TTbar_Tauola.cfi --step=GEN,SIM,DIGI,$XL1T,DIGI2RAW,$XHLT --conditions=FrontierConditions_GlobalTag,${GTAG}::All                               --fileout=TTbarGenHLT_$lumi.root         --number=100 --mc --no_exec --datatier 'GEN-SIM-DIGI-RAW-HLT' --eventcontent=FEVTDEBUGHLT --customise=HLTrigger/Configuration/customL1THLT_Options.py   --python_filename=TTbarGenHLT_$lumi.py

  echo " "
  echo "Creating DigiL1Raw $lumi"
cmsDriver.py RelVal --step=DIGI,$XL1T,DIGI2RAW       --conditions=FrontierConditions_GlobalTag,${GTAG}::All --filein=file:/scratch/cms/TTbarGenSim31X.root  --fileout=RelVal_DigiL1Raw_$lumi.root    --number=100 --mc --no_exec --datatier 'GEN-SIM-DIGI-RAW'     --eventcontent=RAW          --customise=HLTrigger/Configuration/customL1T_Options.py      --python_filename=RelVal_DigiL1Raw_$lumi.py

  echo " "
  echo "Creating DigiL1RawHLT $lumi"
cmsDriver.py RelVal --step=DIGI,$XL1T,DIGI2RAW,$XHLT --conditions=FrontierConditions_GlobalTag,${GTAG}::All --filein=file:/scratch/cms/TTbarGenSim31X.root  --fileout=RelVal_DigiL1RawHLT_$lumi.root --number=100 --mc --no_exec --datatier 'GEN-SIM-DIGI-RAW-HLT' --eventcontent=FEVTDEBUGHLT --customise=HLTrigger/Configuration/customL1THLT_Options.py   --python_filename=RelVal_DigiL1RawHLT_$lumi.py --processName=HLT$lumi

  echo " "
  echo "Creating HLT $lumi"
cmsDriver.py RelVal --step=$XL1T,$XHLT               --conditions=FrontierConditions_GlobalTag,${GTAG}::All --filein=file:RelVal_DigiL1Raw_$lumi.root       --fileout=RelVal_HLT_$lumi.root          --number=100 --mc --no_exec --datatier 'RAW-HLT'              --eventcontent=FEVTDEBUGHLT --customise=HLTrigger/Configuration/customHLT_Options.py      --python_filename=RelVal_HLT_$lumi.py          --processName=HLT$lumi

  echo " "
  echo "Creating HLT2 (re-running HLT) $lumi"
cmsDriver.py RelVal --step=$XL1T,$XHLT               --conditions=FrontierConditions_GlobalTag,${GTAG}::All --filein=file:RelVal_HLT_$lumi.root             --fileout=RelVal_HLT2_$lumi.root         --number=100 --mc --no_exec --datatier 'RAW-HLT'              --eventcontent=FEVTDEBUGHLT --customise=HLTrigger/Configuration/customHLT_Options.py      --python_filename=RelVal_HLT2_$lumi.py         --processName=HLT2$lumi

  echo " "
  echo "Creating L1HLT2 (re-running L1 and HLT - buggy!) $lumi"
cmsDriver.py RelVal --step=$XL1T,$XHLT               --conditions=FrontierConditions_GlobalTag,${GTAG}::All --filein=file:RelVal_DigiL1RawHLT_$lumi.root    --fileout=RelVal_L1HLT2_$lumi.root       --number=100 --mc --no_exec --datatier 'GEN-SIM-DIGI-RAW-HLT' --eventcontent=FEVTDEBUGHLT --customise=HLTrigger/Configuration/customL1THLT2_Options.py  --python_filename=RelVal_L1HLT2_$lumi.py       --processName=HLT2$lumi

  echo " "
  echo "Creating Reco $lumi"
cmsDriver.py RelVal --step=RAW2DIGI,RECO             --conditions=FrontierConditions_GlobalTag,${GTAG}::All --filein=file:RelVal_DigiL1Raw_$lumi.root        --fileout=RelVal_Reco_$lumi.root        --number=100 --mc --no_exec --datatier 'RECO'                 --eventcontent=RECOSIM      --customise=HLTrigger/Configuration/custom_Options.py         --python_filename=RelVal_Reco_$lumi.py

end

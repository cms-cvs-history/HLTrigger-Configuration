#/bin/tcsh


# TTbar GEN-SIM
cmsDriver.py TTbar.cfi --step=GEN,SIM                      --conditions=FrontierConditions_GlobalTag,STARTUP_30X::All --fileout=TTbarGenSim.root --number=100 --mc --no_exec --datatier 'GEN-SIM'              --eventcontent=FEVTSIM      --customise=HLTrigger/Configuration/customHLT_Options.py --python_filename=TTbarGenSim.py

# TTbar GEN-SIM-DIGI-L1-DIGI2RAW-HLT
cmsDriver.py TTbar.cfi --step=GEN,SIM,DIGI,L1,DIGI2RAW,HLT --conditions=FrontierConditions_GlobalTag,STARTUP_30X::All --fileout=TTbarGenHLT.root --number=100 --mc --no_exec --datatier 'GEN-SIM-DIGI-RAW-HLT' --eventcontent=FEVTDEBUGHLT --customise=HLTrigger/Configuration/customHLT_Options.py --python_filename=TTbarGenHLT.py


# DIGI-L1-DIGI2RAW
cmsDriver.py RelVal --step=DIGI,L1,DIGI2RAW     --conditions=FrontierConditions_GlobalTag,STARTUP_30X::All --filein=file:/scratch/cms/TTbarGenSim2110.root --fileout=RelVal_DigiL1Raw.root    --number=100 --mc --no_exec --datatier 'GEN-SIM-DIGI-RAW'     --eventcontent=RAW          --customise=HLTrigger/Configuration/customHLT_Options.py     --python_filename=RelVal_DigiL1Raw.py

# DIGI-L1-DIGI2RAW-HLT
cmsDriver.py RelVal --step=DIGI,L1,DIGI2RAW,HLT --conditions=FrontierConditions_GlobalTag,STARTUP_30X::All --filein=file:/scratch/cms/TTbarGenSim2110.root --fileout=RelVal_DigiL1RawHLT.root --number=100 --mc --no_exec --datatier 'GEN-SIM-DIGI-RAW-HLT' --eventcontent=FEVTDEBUGHLT --customise=HLTrigger/Configuration/customHLT_Options.py     --python_filename=RelVal_DigiL1RawHLT.py

# HLT (from pure raw file)
cmsDriver.py RelVal --step=HLT                  --conditions=FrontierConditions_GlobalTag,STARTUP_30X::All --filein=file:RelVal_DigiL1Raw.root             --fileout=RelVal_HLT.root          --number=100 --mc --no_exec --datatier 'RAW-HLT'              --eventcontent=FEVTDEBUGHLT --customise=HLTrigger/Configuration/customHLT_Options.py     --python_filename=RelVal_HLT.py

# HLT (from file with HLT)
cmsDriver.py RelVal --step=HLT                  --conditions=FrontierConditions_GlobalTag,STARTUP_30X::All --filein=file:RelVal_HLT.root                   --fileout=RelVal_HLT2.root         --number=100 --mc --no_exec --datatier 'RAW-HLT'              --eventcontent=FEVTDEBUGHLT --customise=HLTrigger/Configuration/customHLT_ProcessName.py --python_filename=RelVal_HLT2.py

# L1-HLT (from RelVal step1 - file with L1 and HLT)
cmsDriver.py RelVal --step=L1,HLT               --conditions=FrontierConditions_GlobalTag,STARTUP_30X::All --filein=file:RelVal_DigiL1RawHLT.root          --fileout=RelVal_L1HLT2.root       --number=100 --mc --no_exec --datatier 'GEN-SIM-DIGI-RAW-HLT' --eventcontent=FEVTDEBUGHLT --customise=HLTrigger/Configuration/customHLT_RerunL1HLT.py  --python_filename=RelVal_L1HLT2.py

# RAW2DIGI-RECO
cmsDriver.py RelVal --step=RAW2DIGI,RECO        --conditions=FrontierConditions_GlobalTag,STARTUP_30X::All --filein=file:RelVal_DigiL1Raw.root             --fileout=RelVal_Reco.root         --number=100 --mc --no_exec --datatier 'RECO'                 --eventcontent=RECOSIM      --customise=HLTrigger/Configuration/customHLT_Options.py     --python_filename=RelVal_Reco.py

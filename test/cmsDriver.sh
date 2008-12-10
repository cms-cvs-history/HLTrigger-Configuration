#/bin/tcsh


cmsDriver.py TTbar.cfi --step=GEN,SIM --conditions=FrontierConditions_GlobalTag,STARTUP_30X::All --fileout=TTbarGenSim.root --number=100 --mc --no_exec --datatier 'GEN-SIM' --eventcontent=FEVTSIM --customise=HLTrigger/Configuration/customHLT_Options.py

cmsDriver.py TTbar.cfi --step=GEN,SIM,DIGI,L1,DIGI2RAW,HLT --conditions=FrontierConditions_GlobalTag,STARTUP_30X::All --fileout=TTbarGenSimDigiL1RawHLT.root --number=100 --mc --no_exec --datatier 'GEN-SIM-DIGI-RAW-HLT' --eventcontent=FEVTDEBUGHLT --customise=HLTrigger/Configuration/customHLT_Options.py


cmsDriver.py RelVal --step=DIGI,L1,DIGI2RAW --conditions=FrontierConditions_GlobalTag,STARTUP_30X::All --filein=file:/scratch/cms/TTbarGenSim2110.root --fileout=TTbarRaw.root --number=100 --mc --no_exec --datatier 'RAW' --eventcontent=RAW --customise=HLTrigger/Configuration/customHLT_Options.py

cmsDriver.py RelValFromRaw --step=HLT --conditions=FrontierConditions_GlobalTag,STARTUP_30X::All --filein=file:TTbarRaw.root --fileout=TTbarHLT.root --number=100 --mc --no_exec --datatier 'RAW-HLT' --eventcontent=FEVTDEBUGHLT --customise=HLTrigger/Configuration/customHLT_Options.py

cmsDriver.py RelValFromHLT --step=HLT --conditions=FrontierConditions_GlobalTag,STARTUP_30X::All --filein=file:TTbarRaw.root --fileout=TTbarHLT2.root --number=100 --mc --no_exec --datatier 'RAW-HLT' --eventcontent=FEVTDEBUGHLT --customise=HLTrigger/Configuration/customHLT_ProcessName.py

cmsDriver.py RelVal --step=RAW2DIGI,RECO --conditions=FrontierConditions_GlobalTag,STARTUP_30X::All --filein=file:TTbarRaw.root --fileout=TTbarReco.root --number=100 --mc --no_exec --datatier 'RECO' --eventcontent=RECOSIM --customise=HLTrigger/Configuration/customHLT_Options.py

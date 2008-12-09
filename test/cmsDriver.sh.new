#/bin/tcsh

cmsDriver.py TTbar --step=DIGI,L1,DIGI2RAW --conditions=FrontierConditions_GlobalTag,STARTUP_30X::All --filein=/scratch/cms/TTbarGenSim2110.root --fileout=TTbarRaw.root --number=100 --mc --no_exec --datatier 'RAW' --eventcontent=RAW --python_filename=TTbar_DigiL1Raw_cfg.py

cmsDriver.py TTbar --step=HLT --conditions=FrontierConditions_GlobalTag,STARTUP_30X::All --filein=TTbarRaw.root --fileout=TTbarHLT.root --number=100 --mc --no_exec --datatier 'RAW-HLT' --eventcontent=FEVTDEBUGHLT --python_filename=TTbar_HLT_cfg.py

cmsDriver.py TTbar --step=RAW2DIGI,RECO --conditions=FrontierConditions_GlobalTag,STARTUP_30X::All --filein=TTbarRaw.root --fileout=TTbarReco.root --number=100 --mc --no_exec --datatier 'RECO' --eventcontent=RECOSIM --python_filename=TTbar_Reco_cfg.py

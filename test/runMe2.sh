#!/bin/tcsh

eval `scramv1 runtime -csh`
rehash

cmsRun RelVal_DigiL1Raw.py    >& RelVal_DigiL1raw.log
cmsRun RelVal_DigiL1RawHLT.py >& RelVal_DigiL1rawHLT.log
cmsRun RelVal_HLT.py          >& RelVal_HLT.log
cmsRun RelVal_HLT2.py         >& RelVal_HLT2.log
cmsRun RelVal_L1HLT2.py       >& RelVal_L1HLT2.log
cmsRun RelVal_Reco.py         >& RelVal Reco.log


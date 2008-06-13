#!/bin/tcsh

eval `scramv1 runtime -csh`
rehash

echo " "
echo " Production chain (three jobs: digi+L1emu+digi2raw, HLT, reco):"

echo " "
echo "/bin/rm OnLine_HLTFromRaw_2E30.cfg OnLine_HLTFromRaw_2E30_cfg.py"
      /bin/rm OnLine_HLTFromRaw_2E30.cfg OnLine_HLTFromRaw_2E30_cfg.py
echo "./getHLT.csh"
      ./getHLT.csh 

echo " "
echo "/bin/rm RelVal_Digi_Raw.root RelVal_Pure_Raw.root RelVal_Digi_Digi2Raw.log"
      /bin/rm RelVal_Digi_Raw.root RelVal_Pure_Raw.root RelVal_Digi_Digi2Raw.log
echo "./testcfg RelVal_Digi_Digi2Raw.cfg   >& RelVal_Digi_Digi2Raw.log"
      ./testcfg RelVal_Digi_Digi2Raw.cfg   >& RelVal_Digi_Digi2Raw.log
#echo "cmsRun --strict RelVal_Digi_Digi2Raw.cfg   >& RelVal_Digi_Digi2Raw.log"
#      cmsRun --strict RelVal_Digi_Digi2Raw.cfg   >& RelVal_Digi_Digi2Raw.log

echo " "
echo "/bin/rm HLTFromPureRaw.root             RelVal_HLTFromRaw_2E30.log"
      /bin/rm HLTFromPureRaw.root             RelVal_HLTFromRaw_2E30.log
echo "./testcfg RelVal_HLTFromRaw_2E30.cfg >& RelVal_HLTFromRaw_2E30.log"
      ./testcfg RelVal_HLTFromRaw_2E30.cfg >& RelVal_HLTFromRaw_2E30.log
#echo "cmsRun --strict RelVal_HLTFromRaw_2E30.cfg >& RelVal_HLTFromRaw_2E30.log"
#      cmsRun --strict RelVal_HLTFromRaw_2E30.cfg >& RelVal_HLTFromRaw_2E30.log

echo " "
echo "/bin/rm HLTDe*.root                     OnLine_HLTFromRaw_2E30.log"
      /bin/rm HLTDe*.root                     OnLine_HLTFromRaw_2E30.log
echo "cmsRun OnLine_HLTFromRaw_2E30_cfg.py >& OnLine_HLTFromRaw_2E30.log"
      cmsRun OnLine_HLTFromRaw_2E30_cfg.py >& OnLine_HLTFromRaw_2E30.log
#echo "./testcfg OnLine_HLTFromRaw_2E30.cfg >& OnLine_HLTFromRaw_2E30.log"
#      ./testcfg OnLine_HLTFromRaw_2E30.cfg >& OnLine_HLTFromRaw_2E30.log
#echo "cmsRun --strict OnLine_HLTFromRaw_2E30.cfg >& OnLine_HLTFromRaw_2E30.log"
#      cmsRun --strict OnLine_HLTFromRaw_2E30.cfg >& OnLine_HLTFromRaw_2E30.log

echo " "
echo "/bin/rm RelVal_Reco.root                RelVal_Reco.log"
      /bin/rm RelVal_Reco.root                RelVal_Reco.log
echo "./testcfg RelVal_Reco.cfg            >& RelVal_Reco.log"
      ./testcfg RelVal_Reco.cfg            >& RelVal_Reco.log
#echo "cmsRun --strict RelVal_Reco.cfg            >& RelVal_Reco.log"
#      cmsRun --strict RelVal_Reco.cfg            >& RelVal_Reco.log


echo " "
echo "Finished!"

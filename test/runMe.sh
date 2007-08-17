#!/bin/tcsh

eval `scramv1 runtime -csh`
rehash

echo " "
echo " Quick tests (three jobs: digi2raw, raw2digi, HLT from raw):"

echo " "
echo "/bin/rm myDigiToRaw.root                ConvertDigiToRaw.log"
      /bin/rm myDigiToRaw.root                ConvertDigiToRaw.log
echo "cmsRun --strict ConvertDigiToRaw.cfg >& ConvertDigiToRaw.log"
      cmsRun --strict ConvertDigiToRaw.cfg >& ConvertDigiToRaw.log

echo " "
echo "/bin/rm myRawToDigi.root                ConvertRawToDigi.log"
      /bin/rm myRawToDigi.root                ConvertRawToDigi.log
echo "cmsRun --strict ConvertRawToDigi.cfg >& ConvertRawToDigi.log"
      cmsRun --strict ConvertRawToDigi.cfg >& ConvertRawToDigi.log

echo " "
echo "/bin/rm HLTPoolOutput.root              HLTtable.log"
      /bin/rm HLTPoolOutput.root              HLTtable.log
echo "cmsRun --strict HLTtable.cfg         >& HLTtable.log"
      cmsRun --strict HLTtable.cfg         >& HLTtable.log


echo " "
echo " Production chain (three jobs: digi+digi2raw, HLT, reco):"

echo " "
echo "/bin/rm myDigiToRaw.root                RelVal_Digi_Digi2Raw.log"
      /bin/rm myDigiToRaw.root                RelVal_Digi_Digi2Raw.log
echo "./testcfg RelVal_Digi_Digi2Raw.cfg   >& RelVal_Digi_Digi2Raw.log"
      ./testcfg RelVal_Digi_Digi2Raw.cfg   >& RelVal_Digi_Digi2Raw.log

echo " "
echo "/bin/rm HLTPoolOutput.root              RelVal_HLTFromRaw.log"
      /bin/rm HLTPoolOutput.root              RelVal_HLTFromRaw.log
echo "./testcfg RelVal_HLTFromRaw.cfg      >& RelVal_HLTFromRaw.log"
      ./testcfg RelVal_HLTFromRaw.cfg      >& RelVal_HLTFromRaw.log

echo " "
echo "/bin/rm PD*.root                        RelVal_PrimaryDatasets.log"
      /bin/rm PD*.root                        RelVal_PrimaryDatasets.log
echo "./testcfg RelVal_PrimaryDatasets.cfg >& RelVal_PrimaryDatasets.log"
      ./testcfg RelVal_PrimaryDatasets.cfg >& RelVal_PrimaryDatasets.log

echo " "
echo "/bin/rm reco.root                       RelVal_Reco.log"
      /bin/rm reco.root                       RelVal_Reco.log
echo "./testcfg RelVal_Reco.cfg            >& RelVal_Reco.log"
      ./testcfg RelVal_Reco.cfg            >& RelVal_Reco.log


echo " "
echo "Finished!"

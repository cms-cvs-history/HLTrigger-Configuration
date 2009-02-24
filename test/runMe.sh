#!/bin/tcsh

eval `scramv1 runtime -csh`
rehash

echo " "
echo "Creating offline configs with cmsDriver"
echo "./cmsDriver.sh"
      ./cmsDriver.sh

echo " "
echo "Creating  online configs from ConfDB"
      /bin/rm OnLine_HLT_?E??_cfg.py
echo "./getHLT.sh"
      ./getHLT.sh 
/bin/ln -s RelVal_DigiL1Raw.root RelVal_Pure_Raw.root

echo " "
echo "Special drop on input for old gen-sim files:"
/bin/mv -f RelVal_DigiL1Raw.py RelVal_DigiL1RawOrig.py
/bin/cp  ~/RelVal_DigiL1Raw.py .
diff -C0   RelVal_DigiL1RawOrig.py RelVal_DigiL1Raw.py

foreach task ( RelVal_DigiL1Raw RelVal_HLT OnLine_HLT_2E30 OnLine_HLT_8E29 OnLine_HLT_1E31 RelVal_DigiL1RawHLT RelVal_HLT2 RelVal_L1HLT2 RelVal_Reco )
    echo " "
    foreach ext (log root)
	/bin/rm $task.$ext
    end
    echo "cmsRun $task.py >& $task.log"
          cmsRun $task.py >& $task.log
end

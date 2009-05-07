#!/bin/tcsh

cmsenv
rehash

echo
echo "Creating offline configs with cmsDriver"
./cmsDriver.sh

echo
echo "Creating  online configs from ConfDB"
rm -f OnLine_HLT_*.py
./getHLT.sh 

/bin/ln -s RelVal_DigiL1Raw_2E30.root RelVal_Pure_Raw.root
/bin/ln -s /scratch/cms/TTbarGenSim2110.root TTbarGenSim.root

# foreach task ( RelVal_DigiL1Raw RelVal_HLT OnLine_HLT RelVal_DigiL1RawHLT RelVal_HLT2 RelVal_L1HLT2 RelVal_Reco )
foreach task ( RelVal_DigiL1Raw RelVal_HLT OnLine_HLT RelVal_HLT2 )
    echo
    set name = ${task}_2E30
    foreach ext (log root)
	/bin/rm $name.$ext
    end
    echo "cmsRun $name.py >& $name.log"
          cmsRun $name.py >& $name.log
end

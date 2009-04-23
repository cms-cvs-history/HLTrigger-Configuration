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

foreach lumi ( 8E29 1E31 )
# foreach task ( RelVal_DigiL1Raw RelVal_HLT OnLine_HLT RelVal_DigiL1RawHLT RelVal_HLT2 RelVal_L1HLT2 RelVal_Reco )
foreach task ( RelVal_DigiL1Raw RelVal_HLT OnLine_HLT RelVal_HLT2 )
    echo
    set name = ${task}_${lumi}
    foreach ext (log root)
	/bin/rm $name.$ext
    end
    echo "cmsRun $name.py >& $name.log"
          cmsRun $name.py >& $name.log
  end
end

#!/bin/tcsh

eval `scramv1 runtime -csh`
rehash

echo " "
echo "Creating offline configs with cmsDriver"
echo "./cmsDriver.sh"
#     ./cmsDriver.sh

echo " "
echo "Creating  online configs from ConfDB"
      /bin/rm OnLine_HLT_?E??.py
echo "./getHLT.sh"
      ./getHLT.sh 

# foreach lumi ( 2E30 8E29 1E31 )
foreach lumi ( 8E29 1E31 )
# foreach task ( RelVal_DigiL1Raw RelVal_HLT OnLine_HLT RelVal_DigiL1RawHLT RelVal_HLT2 RelVal_L1HLT2 RelVal_Reco )
# foreach task ( RelVal_DigiL1Raw RelVal_HLT OnLine_HLT )
  foreach task ( RelVal_HLT OnLine_HLT RelVal_HLT2 )
    echo " "
    set name = ${task}_${lumi}
    foreach ext (log root)
	/bin/rm $name.$ext
    end
    echo "cmsRun $name.py >& $name.log"
          cmsRun $name.py >& $name.log
  end
end

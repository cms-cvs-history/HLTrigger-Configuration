#!/bin/tcsh

cmsenv

rehash

echo " "
echo "Removing prescales from online configs"
foreach lumi ( 8E29 GRun 1E31 HIon )
    echo "if 'PrescaleService' in process.__dict__:\n    process.PrescaleService.prescaleTable = cms.VPSet( )" >> OnLine_HLT_${lumi}.py
end

echo " "
echo "Creating offline configs with cmsDriver"
echo "./cmsDriver.sh"
      ./cmsDriver.sh

# GRun = 8E29+MWGR
foreach lumi ( 8E29 GRun 1E31 HIon )
# foreach task ( RelVal_DigiL1Raw RelVal_HLT OnLine_HLT RelVal_DigiL1RawHLT RelVal_HLT2 RelVal_L1HLT2 RelVal_Reco )
foreach task ( RelVal_DigiL1Raw RelVal_HLT OnLine_HLT RelVal_HLT2 )
    echo " "
    set name = ${task}_${lumi}
    foreach ext (log root)
	/bin/rm $name.$ext
    end
    echo "cmsRun $name.py >& $name.log"
          cmsRun $name.py >& $name.log
  end
end

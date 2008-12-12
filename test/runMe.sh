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

foreach task ( DigiL1Raw DigiL1RawHLT HLT HLT2 L1HLT2 Reco )
    echo " "
    echo Running task $task
    foreach ext (log root)
	/bin/rm RelVal_$task.$ext
    end
    cmsRun RelVal_$task.py >& RelVal_$task.log
end

foreach task ( 1E30 8E29 1E31 )
    echo " "
    echo Running task $task
    foreach ext (log root)
	/bin/rm OnLine_HLT_$task.$ext
    end
    cmsRun OnLine_HLT_$task.py >& OnLine_HLT_$task.log
end

#!/bin/tcsh

cmsenv
rehash

echo
echo "Existing cfg files:"
ls -l OnData*.py
ls -l OnLine*.py

echo
echo "Creating offline configs with cmsDriver"
echo "./cmsDriver.sh"
time  ./cmsDriver.sh

echo
echo "Running selected configs from:"
pwd

foreach gtag ( STARTUP DATA )
#foreach gtag ( STARTUP MC DATA )

  foreach table ( GRun HIon )

    if ($gtag != DATA) then
    foreach task ( RelVal_DigiL1Raw )

      echo
      set name = ${task}_${table}_${gtag}
      rm -f $name.{log,root}
      echo "cmsRun $name.py >& $name.log"
#     ls -l        $name.py
      time  cmsRun $name.py >& $name.log
      echo "exit status: $?"

    end
    endif

    if ( $gtag == STARTUP ) then

#     link to input file for subsequent OnLine* step
      rm -f RelVal_DigiL1Raw_${table}.root
      ln -s RelVal_DigiL1Raw_${table}_${gtag}.root RelVal_DigiL1Raw_${table}.root
      foreach task ( OnLine_HLT )

        echo
        set name = ${task}_${table}
        rm -f $name.{log,root}
        echo "cmsRun $name.py >& $name.log"
#       ls -l        $name.py
        time  cmsRun $name.py >& $name.log
        echo "exit status: $?"

      end

    else if ($gtag == DATA ) then

      foreach task ( OnData_HLT )

        echo
        set name = ${task}_${table}
        rm -f $name.{log,root}
        echo "cmsRun $name.py >& $name.log"
#       ls -l        $name.py
        time  cmsRun $name.py >& $name.log
        echo "exit status: $?"

      end
  
    endif

    foreach task ( RelVal_HLT RelVal_HLT2 )

      echo
      set name = ${task}_${table}_${gtag}
      rm -f $name.{log,root}
      echo "cmsRun $name.py >& $name.log"
#     ls -l        $name.py
      time  cmsRun $name.py >& $name.log
      echo "exit status: $?"

    end

  end

end

# special fastsim tests

foreach task ( FastSim_GenToHLT_GRun_STARTUP )

  echo
  set name = ${task}
  rm -f $name.{log,root}
  echo "cmsRun $name.py >& $name.log"
# ls -l        $name.py
  time  cmsRun $name.py >& $name.log
  echo "exit status: $?"

end

foreach task ( IntegrationTestWithHLT_cfg )

  echo
  set name = ${task}
  rm -f $name.{log,root}

  if ( -f $CMSSW_BASE/src/FastSimulation/Configuration/test/$name.py ) then  
    echo "cmsRun  CMSSW_BASE/src/FastSimulation/Configuration/test/$name.py >& $name.log"
#   ls -l        $CMSSW_BASE/src/FastSimulation/Configuration/test/$name.py
    time  cmsRun $CMSSW_BASE/src/FastSimulation/Configuration/test/$name.py >& $name.log
    echo "exit status: $?"
  else
    echo "cmsRun  CMSSW_RELEASE_BASE/src/FastSimulation/Configuration/test/$name.py >& $name.log"
#   ls -l        $CMSSW_RELEASE_BASE/src/FastSimulation/Configuration/test/$name.py
    time  cmsRun $CMSSW_RELEASE_BASE/src/FastSimulation/Configuration/test/$name.py >& $name.log
    echo "exit status: $?"
  endif

end

# separate hlt+reco tasks to run last

foreach gtag ( STARTUP DATA )
#foreach gtag ( STARTUP MC DATA )

  foreach table ( GRun HIon )

    foreach task ( RelVal_HLT_RECO )

      echo
      set name = ${task}_${table}_${gtag}
      rm -f $name.{log,root}
      echo "cmsRun $name.py >& $name.log"
#     ls -l        $name.py
      time  cmsRun $name.py >& $name.log
      echo "exit status: $?"

    end

  end

end

echo
echo "Resulting log files:"
ls -lt *.log

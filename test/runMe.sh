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

foreach gtag ( STARTUP MC )

  foreach task ( RelVal_DigiL1Raw )
    echo
    set name = ${task}_${gtag}
    rm -f $name.{log,root}
    echo "cmsRun $name.py >& $name.log"
    time  cmsRun $name.py >& $name.log
    echo "exit status: $?"
#   link to input file for subsequent OnLine* step
    if ( $gtag == STARTUP ) then
      foreach table ( GRun HIon )
        rm -f RelVal_DigiL1Raw_${table}.root
        ln -s RelVal_DigiL1Raw_${gtag}.root RelVal_DigiL1Raw_${table}.root
      end
    endif
  end

  foreach table ( GRun HIon )
    if ( $gtag == STARTUP ) then
      foreach task ( OnData_HLT OnLine_HLT )
        echo
        set name = ${task}_${table}
        rm -f $name.{log,root}
        echo "cmsRun $name.py >& $name.log"
        time  cmsRun $name.py >& $name.log
        echo "exit status: $?"
      end
    endif

    foreach task ( RelVal_HLT RelVal_HLT2 )
      echo
      set name = ${task}_${table}_${gtag}
      rm -f $name.{log,root}
      if ( $table == GRun ) then
      else if ( $table == HIon ) then
      endif
      echo "cmsRun $name.py >& $name.log"
      time  cmsRun $name.py >& $name.log
      echo "exit status: $?"
    end

  end

end

# separate reco task to run last

foreach gtag ( STARTUP MC )
  foreach task ( RelVal_RECO )
    echo
    set name = ${task}_${gtag}
    rm -f $name.{log,root}
    echo "cmsRun $name.py >& $name.log"
    time  cmsRun $name.py >& $name.log
    echo "exit status: $?"
  end
end

echo
echo "Resulting log files:"
ls -lt *.log

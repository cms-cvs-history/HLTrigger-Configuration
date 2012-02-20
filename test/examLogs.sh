#!/bin/tcsh

touch temp1
touch temp2
/bin/rm -rf temp*

foreach gtag ( STARTUP DATA )
#foreach gtag ( STARTUP MC DATA )

  echo
  echo $gtag

  foreach table ( GRun HIon )
    echo
    set name = ${table}_${gtag}
    echo $name

    if ( $gtag == STARTUP ) then
      echo
      echo "diff -C0 RelVal_HLT_${name}.log OnLine_HLT_${table}.log"
#           diff -C0 RelVal_HLT_${name}.log OnLine_HLT_${table}.log | grep L1T
            diff -C0 RelVal_HLT_${name}.log OnLine_HLT_${table}.log | grep "HLT-Report "
#           diff -C0 RelVal_HLT_${name}.log OnLine_HLT_${table}.log | grep "TrigReport "
    else if ( $gtag == DATA ) then
      echo
      echo "diff -C0 RelVal_HLT_${name}.log OnData_HLT_${table}.log"
#           diff -C0 RelVal_HLT_${name}.log OnData_HLT_${table}.log | grep L1T
            diff -C0 RelVal_HLT_${name}.log OnData_HLT_${table}.log | grep "HLT-Report "
#           diff -C0 RelVal_HLT_${name}.log OnData_HLT_${table}.log | grep "TrigReport "
    endif

      echo
      echo "diff -C0 RelVal_HLT_${name}.log RelVal_HLT_RECO_${name}.log"
#           diff -C0 RelVal_HLT_${name}.log RelVal_HLT_RECO_${name}.log | grep L1T
            diff -C0 RelVal_HLT_${name}.log RelVal_HLT_RECO_${name}.log | grep "HLT-Report "
#           diff -C0 RelVal_HLT_${name}.log RelVal_HLT_RECO_${name}.log | grep "TrigReport "

    if ( $name != HIon_MC ) then
      echo
      echo "diff -C0 RelVal_HLT_${name}.log RelVal_HLT2_${name}.log"
#           diff -C0 RelVal_HLT_${name}.log RelVal_HLT2_${name}.log | grep L1T
            diff -C0 RelVal_HLT_${name}.log RelVal_HLT2_${name}.log | grep "HLT-Report "
#           diff -C0 RelVal_HLT_${name}.log RelVal_HLT2_${name}.log | grep "TrigReport "
    else
      echo
      echo "Currently no globaltags for combination $name!"
    endif
  end

end

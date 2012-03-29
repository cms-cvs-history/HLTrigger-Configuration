#!/bin/tcsh

foreach gtag ( STARTUP DATA )

  echo
  echo $gtag

  foreach table ( GRun HIon )

    echo
    set name = ${table}_${gtag}
    echo $name

    echo
    echo "diff -C0 RelVal_HLT_${name}.log ONLINE_HLT_${name}.log"
#         diff -C0 RelVal_HLT_${name}.log ONLINE_HLT_${name}.log | grep L1T
          diff -C0 RelVal_HLT_${name}.log ONLINE_HLT_${name}.log | grep "HLT-Report "
#         diff -C0 RelVal_HLT_${name}.log ONLINE_HLT_${name}.log | grep "TrigReport "

    echo
    echo "diff -C0 RelVal_HLT_${name}.log RelVal_HLT_RECO_${name}.log"
#         diff -C0 RelVal_HLT_${name}.log RelVal_HLT_RECO_${name}.log | grep L1T
          diff -C0 RelVal_HLT_${name}.log RelVal_HLT_RECO_${name}.log | grep "HLT-Report "
#         diff -C0 RelVal_HLT_${name}.log RelVal_HLT_RECO_${name}.log | grep "TrigReport "

    echo
    echo "diff -C0 RelVal_HLT_${name}.log RelVal_HLT2_${name}.log"
#         diff -C0 RelVal_HLT_${name}.log RelVal_HLT2_${name}.log | grep L1T
          diff -C0 RelVal_HLT_${name}.log RelVal_HLT2_${name}.log | grep "HLT-Report "
#         diff -C0 RelVal_HLT_${name}.log RelVal_HLT2_${name}.log | grep "TrigReport "

  end

end

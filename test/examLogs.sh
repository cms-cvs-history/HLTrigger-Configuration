#!/bin/tcsh

foreach lumi ( 8E29 1E31 )
  echo " "
  echo "diff -C0 RelVal_HLT_${lumi}.log OnLine_HLT_${lumi}.log"
        diff -C0 RelVal_HLT_${lumi}.log OnLine_HLT_${lumi}.log | grep L1T
        diff -C0 RelVal_HLT_${lumi}.log OnLine_HLT_${lumi}.log | grep HLT-Report
  echo " "
  echo "diff -C0 RelVal_HLT_${lumi}.log RelVal_HLT2_${lumi}.log"
        diff -C0 RelVal_HLT_${lumi}.log RelVal_HLT2_${lumi}.log | grep L1T
        diff -C0 RelVal_HLT_${lumi}.log RelVal_HLT2_${lumi}.log | grep HLT-Report
end

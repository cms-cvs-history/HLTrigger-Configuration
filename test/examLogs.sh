#!/bin/tcsh

echo
echo "diff -C0 RelVal_HLT_2E30.log OnLine_HLT_2E30.log"
      diff -C0 RelVal_HLT_2E30.log OnLine_HLT_2E30.log | grep L1T
      diff -C0 RelVal_HLT_2E30.log OnLine_HLT_2E30.log | grep HLT-Report
      diff -C0 RelVal_HLT_2E30.log OnLine_HLT_2E30.log | grep TrigReport
echo
echo "diff -C0 RelVal_HLT_2E30.log RelVal_HLT2_2E30.log"
      diff -C0 RelVal_HLT_2E30.log RelVal_HLT2_2E30.log | grep L1T
      diff -C0 RelVal_HLT_2E30.log RelVal_HLT2_2E30.log | grep HLT-Report
      diff -C0 RelVal_HLT_2E30.log RelVal_HLT2_2E30.log | grep TrigReport

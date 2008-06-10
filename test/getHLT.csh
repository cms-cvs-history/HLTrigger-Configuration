#!/bin/tcsh

eval `~/CMS/TDR/tdr runtime -csh`
rehash

  ./getHLT.py /dev/CMSSW_2_1_0_pre5/HLT/V25 2E30
# ./getHLT.py /dev/CMSSW_2_1_0_pre5/HLT/V25 2E30 GEN-HLT

#!/bin/tcsh

eval `~/CMS/TDR/tdr runtime -csh`
rehash

  ./getHLT.py /dev/CMSSW_2_1_0_pre5/HLT/V13 2E30
# ./getHLT.py /dev/CMSSW_2_1_0_pre5/HLT/V13 2E30 GEN-HLT

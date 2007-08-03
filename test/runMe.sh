#!/bin/tcsh

eval `scramv1 runtime -csh`
rehash

echo "rm -i my*To*.root Convert*To*.log HLTtable.log"
      rm -i my*To*.root Convert*To*.log HLTtable.log

echo "cmsRun --strict ConvertDigiToRaw.cfg >& ConvertDigiToRaw.log"
      cmsRun --strict ConvertDigiToRaw.cfg >& ConvertDigiToRaw.log

echo "cmsRun --strict ConvertRawToDigi.cfg >& ConvertRawToDigi.log"
      cmsRun --strict ConvertRawToDigi.cfg >& ConvertRawToDigi.log

echo "cmsRun --strict HLTtable.cfg         >& HLTtable.log"
      cmsRun --strict HLTtable.cfg         >& HLTtable.log

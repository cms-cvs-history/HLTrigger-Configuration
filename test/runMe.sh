#!/bin/tcsh

eval `scramv1 runtime -csh`
rehash

echo "rm -i myDigiToRaw.root ConvertDigiToRaw.log HLTtable.log"
      rm -i myDigiToRaw.root ConvertDigiToRaw.log HLTtable.log

echo "cmsRun ConvertDigiToRaw.cfg >& ConvertDigiToRaw.log"
      cmsRun ConvertDigiToRaw.cfg >& ConvertDigiToRaw.log

echo "cmsRun HLTtable.cfg         >& HLTtable.log"
      cmsRun HLTtable.cfg         >& HLTtable.log

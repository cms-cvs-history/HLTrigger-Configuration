#!/bin/tcsh

eval `scramv1 runtime -csh`
rehash
cmsRun ConvertDigiToRaw.cfg >& ConvertDigiToRaw.log
cmsRun HLTtable.cfg         >& HLTtable.log

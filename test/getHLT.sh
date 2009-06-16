#! /bin/bash

# ConfDB configurations to use
HLTtable8E29="/dev/CMSSW_2_2_13_HLT/8E29/V8/V7"
HLTtable1E31="/dev/CMSSW_2_2_13_HLT/1E31/V8/V5"
HLTtableFULL="/dev/CMSSW_2_2_13_HLT/FULL/V8"

# getHLT.py
PACKAGE="HLTrigger/Configuration"
if [ -f "./getHLT.py" ]; then
  GETHLT="./getHLT.py"
elif [ -f "$CMSSW_BASE/src/$PACKAGE/test/getHLT.py" ]; then
  GETHLT="$CMSSW_BASE/src/$PACKAGE/test/getHLT.py"
elif [ -f "$CMSSW_RELEASE_BASE/src/$PACKAGE/test/getHLT.py" ]; then
  GETHLT="$CMSSW_RELEASE_BASE/src/$PACKAGE/test/getHLT.py"
else
  echo "cannot find getHLT.py, aborting"
  exit 1
fi

function getConfigForCVS() {
  # for things in CMSSW CVS
  local HLTtable="$1"
  local HLTid="$2"
  $GETHLT $HLTtable $HLTid GEN-HLT
}

function getContentForCVS() {
  local HLTcontent="$1"
  local AlCaOutput="hltOutputALCAPHISYM hltOutputALCAPHISYMHCAL hltOutputALCAP0 hltOutputRPCMON"
  local AlCaBlocks=$(for ALCA in $AlCaOutput; do echo -n "$ALCA::outputCommands,"; done | sed -e 's/,$//')
  edmConfigFromDB --configName $HLTcontent --nopaths --noes --nopsets --noservices --cff --blocks hltOutputA::outputCommands    --format python > hltOutputA_cff.py
  edmConfigFromDB --configName $HLTcontent --nopaths --noes --nopsets --noservices --cff --blocks hltOutputDQM::outputCommands  --format python > hltOutputDQM_cff.py
  edmConfigFromDB --configName $HLTcontent --nopaths --noes --nopsets --noservices --cff --blocks $AlCaBlocks                   --format python > hltOutputALCA_cff.py
}

function getConfigForOnline() {
  # for things NOT in CMSSW CVS:
  local HLTtable="$1"
  local HLTid="$2"
  $GETHLT $HLTtable $HLTid
}

# make sure we're using *this* working area
eval `scramv1 runtime -sh`
hash -r

if [ "$1" == "CVS" ]; then
  # for things in CMSSW CVS
  rm -f HLT*_cff.py
  getConfigForCVS "${HLTtable8E29}" "8E29"
  getConfigForCVS "${HLTtable1E31}" "1E31"
  getConfigForCVS "${HLTtableFULL}" "FULL"
  getContentForCVS "${HLTtableFULL}"
  ls -lt HLT*_cff.py hltOutput*_cff.py
  mv -f HLT*_cff.py hltOutput*_cff.py ../python
else
  # for things NOT in CMSSW CVS:
  rm -f OnLine_HLTFromRaw_*_cfg.py
  getConfigForOnline "${HLTtable8E29}" "8E29"
  getConfigForOnline "${HLTtable1E31}" "1E31"
  ls -lt OnLine_HLTFromRaw_*_cfg.py
fi

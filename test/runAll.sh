#!/bin/tcsh

cmsenv
rehash

echo
echo "Existing cfg files:"
ls -l On*.py

echo
echo "Creating ONLINE cfg files adding the HLTAnalyzerEndpath:"

foreach gtag ( Data Line )
  set GTAG = ` echo $gtag | tr "[a-z]" "[A-Z]" `
  if ( $GTAG == LINE ) then
    set GTAG = STARTUP
  endif
  foreach table ( GRun 5E33v4 7E33v2 HIon )
    set oldfile = On${gtag}_HLT_${table}.py
    set newfile = ONLINE_HLT_${table}_${GTAG}.py
    rm -f $newfile
    cp $oldfile $newfile
    cat >> $newfile <<EOF
#
    if not ('HLTAnalyzerEndpath' in process.__dict__) :
        from HLTrigger.Configuration.HLT_FULL_cff import hltL1GtTrigReport,hltTrigReport
        process.hltL1GtTrigReport = hltL1GtTrigReport
        process.hltTrigReport = hltTrigReport
        process.hltTrigReport.HLTriggerResults = cms.InputTag( 'TriggerResults','',process.name_() )
        process.HLTAnalyzerEndpath = cms.EndPath(process.hltL1GtTrigReport + process.hltTrigReport)
#
EOF
  end
end

echo
echo "Created ONLINE cfg files:"
ls -l ON*.py

echo
echo "Creating offline cfg files with cmsDriver"
echo "./cmsDriver.sh"
time  ./cmsDriver.sh

echo
echo "Creating special FastSim IntegrationTestWithHLT:"

foreach task ( IntegrationTestWithHLT_cfg )

  echo
  set name = ${task}
  rm -f $name.py

  if ( -f $CMSSW_BASE/src/FastSimulation/Configuration/test/$name.py ) then
    cp         $CMSSW_BASE/src/FastSimulation/Configuration/test/$name.py $name.py
  else
    cp $CMSSW_RELEASE_BASE/src/FastSimulation/Configuration/test/$name.py $name.py
  endif

  cat >> $name.py <<EOF

process.GlobalTag.toGet.append(
        cms.PSet(
            record  = cms.string( 'JetCorrectionsRecord' ),
            tag     = cms.string( 'JetCorrectorParametersCollection_Jec12_V8_HLT_AK5CaloHLT' ),
            label   = cms.untracked.string( 'AK5CaloHLT' ),
            connect = cms.untracked.string( 'sqlite_file:/afs/fnal.gov/files/home/room2/apana/public/HLT/Jec12_V8_HLT.db' )
        )
)
process.GlobalTag.toGet.append(
        cms.PSet(
            record  = cms.string( 'JetCorrectionsRecord' ),
            tag     = cms.string( 'JetCorrectorParametersCollection_Jec12_V8_HLT_AK5PFHLT' ),
            label   = cms.untracked.string( 'AK5PFHLT' ),
            connect = cms.untracked.string( 'sqlite_file:/afs/fnal.gov/files/home/room2/apana/public/HLT/Jec12_V8_HLT.db' )
        )
)
process.GlobalTag.toGet.append(
        cms.PSet(
            record  = cms.string( 'JetCorrectionsRecord' ),
            tag     = cms.string( 'JetCorrectorParametersCollection_Jec12_V8_HLT_AK5PFchsHLT' ),
            label   = cms.untracked.string( 'AK5PFchsHLT' ),
            connect = cms.untracked.string( 'sqlite_file:/afs/fnal.gov/files/home/room2/apana/public/HLT/Jec12_V8_HLT.db' )
        )
)

EOF

end

echo
echo "Running selected cfg files from:"
pwd

rm -f                           ./runOne.log 
time  ./runOne.sh DATA    $1 >& ./runOne.log &
time  ./runOne.sh STARTUP $1

  set N = 0
  cp -f ./runOne.log ./runOne.tmp  
  grep -q Finished   ./runOne.tmp
  set F = $?

while ( $F )
  awk "{if (NR>$N) {print}}"  ./runOne.tmp
  set N = `cat ./runOne.tmp | wc -l`
  sleep 13
  cp -f ./runOne.log ./runOne.tmp  
  grep -q Finished   ./runOne.tmp
  set F = $?
end

wait

  awk "{if (NR>$N) {print}}"  ./runOne.log
  rm -f ./runOne.{log,tmp}

echo
echo "Resulting log files:"
ls -l *.log

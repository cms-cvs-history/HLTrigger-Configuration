# /dev/CMSSW_2_2_12/HLT/V3 (CMSSW_2_2_X_2009-06-04-0000_HLT1)

import FWCore.ParameterSet.Config as cms


HLTConfigVersion = cms.PSet(
  tableName = cms.string('/dev/CMSSW_2_2_12/HLT/V3')
)

block_hltDefaultOutput = cms.PSet(
outputCommands = cms.untracked.vstring( 'drop *_hlt*_*_*',
  'keep edmTriggerResults_*_*_*',
  'keep triggerTriggerEvent_*_*_*',
  'keep *_hltGctDigis_*_*',
  'keep *_hltGtDigis_*_*',
  'keep *_hltL1extraParticles_*_*',
  'keep *_hltL1GtObjectMap_*_*' )
)

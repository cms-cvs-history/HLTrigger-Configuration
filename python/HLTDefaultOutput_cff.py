# /dev/CMSSW_3_1_0/pre6/HLT/V64 (CMSSW_3_1_X_2009-05-25-1900)

import FWCore.ParameterSet.Config as cms


HLTConfigVersion = cms.PSet(
  tableName = cms.string('/dev/CMSSW_3_1_0/pre6/HLT/V64')
)

block_hltDefaultOutput = cms.PSet(
outputCommands = cms.untracked.vstring( 'drop *_hlt*_*_*',
  'keep edmTriggerResults_*_*_*',
  'keep triggerTriggerEvent_*_*_*',
  'keep *_hltL1GtObjectMap_*_*' )
)

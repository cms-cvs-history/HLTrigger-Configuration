# /dev/CMSSW_2_2_13_HLT/FULL/V10 (CMSSW_2_2_13_HLT)

import FWCore.ParameterSet.Config as cms


HLTConfigVersion = cms.PSet(
  tableName = cms.string('/dev/CMSSW_2_2_13_HLT/FULL/V10')
)

block_hltOutputA = cms.PSet(
outputCommands = cms.untracked.vstring( 'drop *_hlt*_*_*',
  'keep FEDRawDataCollection_source_*_*',
  'keep FEDRawDataCollection_rawDataCollector_*_*',
  'keep edmTriggerResults_*_*_*',
  'keep triggerTriggerEvent_*_*_*',
  'keep *_hltL1GtObjectMap_*_*' )
)

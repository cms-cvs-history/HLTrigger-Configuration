# /dev/CMSSW_2_2_0/pre1/HLT/V5 (CMSSW_2_2_X_2008-11-14-1200_HLT1)

import FWCore.ParameterSet.Config as cms


HLTConfigVersion = cms.PSet(
  tableName = cms.string('/dev/CMSSW_2_2_0/pre1/HLT/V5')
)

block_hltDefaultOutputWithFEDs = cms.PSet(
outputCommands = cms.untracked.vstring( 'drop *_hlt*_*_*',
  'keep FEDRawDataCollection_rawDataCollector_*_*',
  'keep edmTriggerResults_*_*_*',
  'keep triggerTriggerEvent_*_*_*',
  'keep *_hltGctDigis_*_*',
  'keep *_hltGtDigis_*_*',
  'keep *_hltL1extraParticles_*_*',
  'keep *_hltL1GtObjectMap_*_*' )
)

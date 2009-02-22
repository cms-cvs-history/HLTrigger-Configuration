# /user/fwyzard/CMSSW_2_2_4_HLT4/8E29/V3 (CMSSW_2_2_4_HLT4)

import FWCore.ParameterSet.Config as cms


HLTConfigVersion = cms.PSet(
  tableName = cms.string('/user/fwyzard/CMSSW_2_2_4_HLT4/8E29/V3')
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

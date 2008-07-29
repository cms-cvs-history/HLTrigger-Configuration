# /dev/CMSSW_2_1_0_pre10/HLT/V5 (CMSSW_2_1_X_2008-07-29-0800_HLT1)

import FWCore.ParameterSet.Config as cms

block_hltDefaultOutput = cms.PSet(
outputCommands = cms.untracked.vstring( 'drop *_hlt*_*_*', 'keep FEDRawDataCollection_source_*_*', 'keep FEDRawDataCollection_rawDataCollector_*_*', 'keep edmTriggerResults_*_*_*', 'keep triggerTriggerEvent_*_*_*', 'keep *_hltGtDigis_*_*', 'keep *_hltGctDigis_*_*', 'keep *_hltL1GtObjectMap_*_*', 'keep *_hltL1extraParticles_*_*' )
)

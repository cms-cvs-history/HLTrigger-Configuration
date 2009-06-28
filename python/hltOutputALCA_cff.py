# /dev/CMSSW_2_2_13_HLT/FULL/V37 (CMSSW_2_2_13_HLT)

import FWCore.ParameterSet.Config as cms


HLTConfigVersion = cms.PSet(
  tableName = cms.string('/dev/CMSSW_2_2_13_HLT/FULL/V37')
)

block_hltOutputALCAPHISYM = cms.PSet(
outputCommands = cms.untracked.vstring( 'drop *',
  'keep edmTriggerResults_*_*_*',
  'keep triggerTriggerEvent_*_*_*',
  'keep L1GlobalTriggerReadoutRecord_hltGtDigis_*_*',
  'keep *_hltAlCaPhiSymStream_*_*' )
)
block_hltOutputALCAPHISYMHCAL = cms.PSet(
outputCommands = cms.untracked.vstring( 'drop *',
  'keep edmTriggerResults_*_*_*',
  'keep triggerTriggerEvent_*_*_*',
  'keep *_hltAlCaHcalFEDSelector_*_*' )
)
block_hltOutputALCAP0 = cms.PSet(
outputCommands = cms.untracked.vstring( 'drop *',
  'keep edmTriggerResults_*_*_*',
  'keep triggerTriggerEvent_*_*_*',
  'keep *_hltAlCaEtaRegRecHits1E31_*_*',
  'keep *_hltAlCaPi0RegRecHits8E29_*_*',
  'keep *_hltAlCaPi0RegRecHitsCosmics_*_*',
  'keep *_hltAlCaPi0RegRecHits1E31_*_*',
  'keep *_hltAlCaEtaRegRecHitsCosmics_*_*',
  'keep *_hltAlCaEtaRegRecHits8E29_*_*' )
)
block_hltOutputRPCMON = cms.PSet(
outputCommands = cms.untracked.vstring( 'drop *',
  'keep edmTriggerResults_*_*_*',
  'keep *_hltRpcRecHits_*_*',
  'keep *_hltCscSegments_*_*',
  'keep *_hltMuonRPCDigis_*_*',
  'keep *_hltDt4DSegments_*_*',
  'keep L1MuGMTCands_hltGtDigis_*_*',
  'keep L1MuGMTReadoutCollection_hltGtDigis_*_*',
  'keep *_hltMuonDTDigis_*_*' )
)

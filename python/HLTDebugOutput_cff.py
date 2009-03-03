# /dev/CMSSW_2_2_4_HLT4/8E29/V6 (CMSSW_2_2_4_HLT4)

import FWCore.ParameterSet.Config as cms


HLTConfigVersion = cms.PSet(
  tableName = cms.string('/dev/CMSSW_2_2_4_HLT4/8E29/V6')
)

block_hltDebugOutput = cms.PSet(
outputCommands = cms.untracked.vstring( 'drop *_hlt*_*_*',
  'keep edmTriggerResults_*_*_*',
  'keep triggerTriggerEvent_*_*_*',
  'keep triggerTriggerEventWithRefs_*_*_*',
  'keep *_hltL1IsoEgammaRegionalCkfTrackCandidates_*_*',
  'keep *_hltTowerMakerForAll_*_*',
  'keep *_hltBSoftmuonL3TagInfos_*_*',
  'keep *_hltCkfL1IsoStartUpTrackCandidates_*_*',
  'keep *_hltL1IsolatedPhotonEcalIsol_*_*',
  'keep *_hltL2TauRelaxingIsolationSelector_*_*',
  'keep *_hltMet_*_*',
  'keep *_hltL1NonIsoLargeWindowElectronTrackIsol_*_*',
  'keep *_hltL1NonIsoLargeWindowElectronsRegionalCkfTrackCandidates_*_*',
  'keep *_hltCorrectedHybridSuperClustersL1NonIsolated_*_*',
  'keep *_hltCorrectedEndcapSuperClustersWithPreshowerL1Isolated_*_*',
  'keep *_hltBSoftmuonL25BJetTags_*_*',
  'keep *_hltBLifetimeL3BJetTagsRelaxed_*_*',
  'keep *_hltBSoftmuonL25Jets_*_*',
  'keep *_hltL1NonIsoLargeWindowElectronPixelSeeds_*_*',
  'keep recoTracks_hltL1IsoEgammaRegionalCTFFinalFitWithMaterial_*_*',
  'keep *_hltMCJetCorJetIcone5Regional_*_*',
  'keep *_hltBSoftmuonL3BJetTags_*_*',
  'keep *_hltL1GtObjectMap_*_*',
  'keep *_hltL1NonIsolatedPhotonEcalIsol_*_*',
  'keep recoTracks_hltCtfL1NonIsoStartUpWithMaterialTracks_*_*',
  'keep *_hltL1IsoStartUpElectronTrackIsol_*_*',
  'keep *_hltL1HLTDoubleLooseIsoTau15JetsMatch_*_*',
  'keep *_hltL1NonIsoLargeWindowElectronsRegionalPixelSeedGenerator_*_*',
  'keep *_hltL1NonIsoStartupElectronTrackIsol_*_*',
  'keep *_hltBSoftmuonL3BJetTagsByDR_*_*',
  'keep *_hltL1IsoPhotonTrackIsol_*_*',
  'keep *_hltL1HLTSingleLooseIsoTau20JetsMatch_*_*',
  'keep *_hltBLifetimeL25JetsRelaxed_*_*',
  'keep *_hltL2MuonSeeds_*_*',
  'keep *_hltL2Muons_*_*',
  'keep *_hltL1NonIsoEgammaRegionalPixelSeedGenerator_*_*',
  'keep *_hltL1NonIsoPhotonTrackIsol_*_*',
  'keep *_hltHtMet_*_*',
  'keep *_hltMCJetCorJetIcone5_*_*',
  'keep *_hltPixelVertices_*_*',
  'keep *_hltBLifetimeL3AssociatorRelaxed_*_*',
  'keep *_hltIterativeCone5CaloJets_*_*',
  'keep *_hltSiPixelRecHits_*_*',
  'keep *_hltCkfL1NonIsoStartUpTrackCandidates_*_*',
  'keep *_hltL1NonIsoEgammaRegionalCkfTrackCandidates_*_*',
  'keep *_hltPixelMatchStartUpElectronsL1NonIso_*_*',
  'keep recoTracks_hltCtfL1IsoStartUpWithMaterialTracks_*_*',
  'keep *_hltPixelTracks_*_*',
  'keep *_hltBLifetimeL25BJetTagsRelaxed_*_*',
  'keep *_hltL2TauNarrowConeIsolationProducer_*_*',
  'keep *_hltL3MuonIsolations_*_*',
  'keep recoTracks_hltCtfL1IsoLargeWindowWithMaterialTracks_*_*',
  'keep *_hltL2MuonIsolations_*_*',
  'keep *_hltGctDigis_*_*',
  'keep recoTracks_hltL1IsoLargeWindowElectronsRegionalCTFFinalFitWithMaterial_*_*',
  'keep *_hltL1IsolatedElectronHcalIsol_*_*',
  'keep recoTracks_hltL1NonIsoLargeWindowElectronsRegionalCTFFinalFitWithMaterial_*_*',
  'keep *_hltBLifetimeL3JetsRelaxed_*_*',
  'keep *_hltPixelMatchElectronsL1NonIsoLargeWindow_*_*',
  'keep *_hltL3MuonCandidates_*_*',
  'keep *_hltL1NonIsoStartUpElectronsRegionalPixelSeedGenerator_*_*',
  'keep *_hltBLifetimeL25AssociatorRelaxed_*_*',
  'keep *_hltIterativeCone5CaloJetsRegional_*_*',
  'keep *_hltCkfL1IsoLargeWindowTrackCandidates_*_*',
  'keep *_hltCorrectedEndcapSuperClustersWithPreshowerL1NonIsolated_*_*',
  'keep *_hltCorrectedHybridSuperClustersL1Isolated_*_*',
  'keep *_hltBLifetimeL3TagInfosRelaxed_*_*',
  'keep *_hltGtDigis_*_*',
  'keep recoTracks_hltL1NonIsoEgammaRegionalCTFFinalFitWithMaterial_*_*',
  'keep *_hltL1NonIsoStartUpElectronsRegionalCkfTrackCandidates_*_*',
  'keep *_hltL2MuonCandidates_*_*',
  'keep *_hltBSoftmuonL25TagInfos_*_*',
  'keep *_hltL1NonIsolatedElectronHcalIsol_*_*',
  'keep *_hltL1IsolatedPhotonHcalIsol_*_*',
  'keep *_hltL1IsoLargeWindowElectronsRegionalPixelSeedGenerator_*_*',
  'keep *_hltL1IsoLargeWindowElectronTrackIsol_*_*',
  'keep recoTracks_hltL1IsoStartUpElectronsRegionalCTFFinalFitWithMaterial_*_*',
  'keep *_hltOfflineBeamSpot_*_*',
  'keep *_hltL1NonIsoStartUpElectronPixelSeeds_*_*',
  'keep *_hltL1NonIsoRecoEcalCandidate_*_*',
  'keep recoTracks_hltL1NonIsoStartUpElectronsRegionalCTFFinalFitWithMaterial_*_*',
  'keep *_hltCkfL1NonIsoLargeWindowTrackCandidates_*_*',
  'keep *_hltL1IsoStartUpElectronPixelSeeds_*_*',
  'keep *_hltL3Muons_*_*',
  'keep recoTracks_hltCtfL1NonIsoLargeWindowWithMaterialTracks_*_*',
  'keep *_hltL1IsoEgammaRegionalPixelSeedGenerator_*_*',
  'keep *_hltPixelMatchElectronsL1IsoLargeWindow_*_*',
  'keep *_hltL1NonIsolatedPhotonHcalIsol_*_*',
  'keep *_hltL1IsoRecoEcalCandidate_*_*',
  'keep *_hltL1extraParticles_*_*',
  'keep *_hltL1IsoStartUpElectronsRegionalPixelSeedGenerator_*_*',
  'keep *_hltL3TrajectorySeed_*_*',
  'keep *_hltBLifetimeL25TagInfosRelaxed_*_*',
  'keep *_hltL2TauJets_*_*',
  'keep *_hltBLifetimeRegionalCtfWithMaterialTracksRelaxed_*_*',
  'keep *_hltL1IsoLargeWindowElectronPixelSeeds_*_*',
  'keep *_hltPixelMatchStartUpElectronsL1Iso_*_*',
  'keep *_hltL1IsoLargeWindowElectronsRegionalCkfTrackCandidates_*_*',
  'keep *_hltL1IsoStartUpElectronsRegionalCkfTrackCandidates_*_*' )
)

# /dev/CMSSW_2_2_6_HLT/merged/V39 (CMSSW_2_2_6_HLT_HLT3)

import FWCore.ParameterSet.Config as cms


HLTConfigVersion = cms.PSet(
  tableName = cms.string('/dev/CMSSW_2_2_6_HLT/merged/V39')
)

block_hltDebugWithAlCaOutput = cms.PSet(
outputCommands = cms.untracked.vstring( 'drop *_hlt*_*_*',
  'keep edmTriggerResults_*_*_*',
  'keep triggerTriggerEvent_*_*_*',
  'keep triggerTriggerEventWithRefs_*_*_*',
  'keep *_hltL1IsoEgammaRegionalCkfTrackCandidates_*_*',
  'keep *_hltTowerMakerForAll_*_*',
  'keep *_hltBLifetimeL25FilterStartup_*_*',
  'keep *_hltL25TauLeadingTrackPtCutSelector_*_*',
  'keep *_hltAlCaEtaRegRecHits1E31_*_*',
  'keep *_hltBLifetimeL3BJetTagsStartup_*_*',
  'keep *_hltCorrectedIslandBarrelSuperClustersHI_*_*',
  'keep *_hltL1NonIsoLargeWindowElectronPixelSeeds_*_*',
  'keep *_hltHITCtfWithMaterialTracks_*_*',
  'keep *_hltMCJetCorJetIcone5Regional_*_*',
  'keep *_hltPixelMatchLargeWindowElectronsL1NonIso_*_*',
  'keep *_hltL3TauCkfTrackCandidates_*_*',
  'keep *_hltL1NonIsolatedPhotonEcalIsol_*_*',
  'keep *_hltRpcRecHits_*_*',
  'keep *_hltBJet10U_*_*',
  'keep *_hltL1HLTDoubleLooseIsoTau15JetsMatch_*_*',
  'keep *_hltBJet50U_*_*',
  'keep *_hltCorrectedMulti5x5EndcapSuperClustersWithPreshowerL1Isolated_*_*',
  'keep *_hltBJet120_*_*',
  'keep *_hltL1NonIsoEgammaRegionalPixelSeedGenerator_*_*',
  'keep *_hltBSoftMuonL3BJetTagsUByPt_*_*',
  'keep *_hltAlCaPi0RegRecHits8E29_*_*',
  'keep *_hltPixelVertices_*_*',
  'keep *_hltL1HLTDoubleLooseIsoTau15Trk5JetsMatch_*_*',
  'keep *_hltBLifetimeRegionalCtfWithMaterialTracksStartup_*_*',
  'keep *_hltIterativeCone5CaloJets_*_*',
  'keep *_hltSiPixelRecHits_*_*',
  'keep *_hltL1NonIsoEgammaRegionalCkfTrackCandidates_*_*',
  'keep *_hltBJet80_*_*',
  'keep *_hltL1HLTSingleIsoTau20JetsMatch_*_*',
  'keep *_hltBSoftMuonL25BJetTagsUByDR_*_*',
  'keep *_hltIterativeConePu5CaloJets_*_*',
  'keep *_hltBSoftMuonL25TagInfosU_*_*',
  'keep *_hltL3TauConeIsolation_*_*',
  'keep *_hltCorrectedIslandEndcapSuperClustersHI_*_*',
  'keep *_hltL3MuonCandidates_*_*',
  'keep *_hltBSoftMuonL3BJetTagsByDR_*_*',
  'keep *_hltBSoftMuonL25Jets_*_*',
  'keep *_hltIterativeCone5CaloJetsRegional_*_*',
  'keep *_hltCorrectedHybridSuperClustersL1Isolated_*_*',
  'keep *_hltGtDigis_*_*',
  'keep *_hltBSoftMuonL25JetsU_*_*',
  'keep *_hltL1NonIsolatedElectronHcalIsol_*_*',
  'keep *_hltMuonDTDigis_*_*',
  'keep *_hltL1NonIsoHLTClusterShape_*_*',
  'keep *_hltBLifetimeL25JetsStartupU_*_*',
  'keep *_hltBLifetimeRegionalCtfWithMaterialTracksStartupU_*_*',
  'keep *_hltBLifetimeL3TagInfosStartup_*_*',
  'keep *_hltBSoftMuonL25TagInfos_*_*',
  'keep *_hltBLifetimeL3JetsStartupU_*_*',
  'keep *_hltL1IsoEgammaRegionalPixelSeedGenerator_*_*',
  'keep *_hltL1NonIsolatedPhotonHcalIsol_*_*',
  'keep *_hltL1IsoRecoEcalCandidate_*_*',
  'keep *_hltL1extraParticles_*_*',
  'keep *_hltL3TrajectorySeed_*_*',
  'keep *_hltAlCaPhiSymStream_*_*',
  'keep *_hltL1IsoLargeWindowElectronPixelSeeds_*_*',
  'keep *_hltBSoftMuonL25BJetTagsByDR_*_*',
  'keep *_hltL1NonIsoPhotonHollowTrackIsol_*_*',
  'keep *_hltPixelMatchLargeWindowElectronsL1Iso_*_*',
  'keep *_hltCtfL1NonIsoLargeWithMaterialTracks_*_*',
  'keep *_hltL1IsolatedPhotonEcalIsol_*_*',
  'keep *_hltL2TauRelaxingIsolationSelector_*_*',
  'keep *_hltMet_*_*',
  'keep *_hltL25TauCtfWithMaterialTracks_*_*',
  'keep *_hltCscSegments_*_*',
  'keep *_hltAlCaPi0RegRecHits1E31_*_*',
  'keep *_hltBLifetimeL3AssociatorStartupU_*_*',
  'keep *_hltCorrectedHybridSuperClustersL1NonIsolated_*_*',
  'keep *_hltCorrectedMulti5x5EndcapSuperClustersWithPreshowerL1NonIsolated_*_*',
  'keep *_hltL1IsoEgammaRegionalCTFFinalFitWithMaterial_*_*',
  'keep *_hltBLifetimeL25TagInfosStartup_*_*',
  'keep *_hltBLifetimeL25AssociatorStartup_*_*',
  'keep *_hltBLifetimeL25TagInfosStartupU_*_*',
  'keep *_hltL1GtObjectMap_*_*',
  'keep *_hltIsolPixelTrackProd_*_*',
  'keep *_hltBLifetimeL25BJetTagsStartup_*_*',
  'keep *_hltBSoftMuonL3BJetTagsUByDR_*_*',
  'keep *_hltBLifetimeL25FilterStartupU_*_*',
  'keep *_hltL1HLTSingleLooseIsoTau20JetsMatch_*_*',
  'keep *_hltBLifetimeL3JetsStartup_*_*',
  'keep *_hltL2MuonSeeds_*_*',
  'keep *_hltL2Muons_*_*',
  'keep *_hltBLifetimeL3BJetTagsStartupU_*_*',
  'keep *_hltL1IsoHLTClusterShape_*_*',
  'keep *_hltBLifetimeL25JetsStartup_*_*',
  'keep *_hltHtMet_*_*',
  'keep *_hltBLifetimeL3TagInfosStartupU_*_*',
  'keep *_hltMCJetCorJetIcone5_*_*',
  'keep *_hltHITIPTCorrector_*_*',
  'keep *_hltAlCaEtaRegRecHits8E29_*_*',
  'keep *_hltPixelTracks_*_*',
  'keep *_hltL2TauNarrowConeIsolationProducer_*_*',
  'keep *_hltL3MuonIsolations_*_*',
  'keep *_hltL2MuonIsolations_*_*',
  'keep *_hltGctDigis_*_*',
  'keep *_hltL25TauConeIsolation_*_*',
  'keep *_hltL1IsolatedElectronHcalIsol_*_*',
  'keep *_hltBLifetimeL25BJetTagsStartupU_*_*',
  'keep *_hltCkfL1IsoLargeTrackCandidates_*_*',
  'keep *_hltCtfL1IsoLargeWithMaterialTracks_*_*',
  'keep *_hltL1NonIsoEgammaRegionalCTFFinalFitWithMaterial_*_*',
  'keep *_hltL2MuonCandidates_*_*',
  'keep *_hltL1IsoPhotonHollowTrackIsol_*_*',
  'keep *_hltBSoftMuonL3TagInfosU_*_*',
  'keep *_hltBJet20_*_*',
  'keep *_hltAlCaHcalFEDSelector_*_*',
  'keep *_hltL1IsolatedPhotonHcalIsol_*_*',
  'keep *_hltOfflineBeamSpot_*_*',
  'keep *_hltL1NonIsoStartUpElectronPixelSeeds_*_*',
  'keep *_hltBLifetimeL25AssociatorStartupU_*_*',
  'keep *_hltL1NonIsoRecoEcalCandidate_*_*',
  'keep *_hltBLifetimeL3AssociatorStartup_*_*',
  'keep *_hltBSoftMuonL3TagInfos_*_*',
  'keep *_hltBSoftMuonL3BJetTagsByPt_*_*',
  'keep *_hltCkfL1NonIsoLargeTrackCandidates_*_*',
  'keep *_hltL3TauIsolationSelector_*_*',
  'keep *_hltDt4DSegments_*_*' )
)

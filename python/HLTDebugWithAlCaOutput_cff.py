# /dev/CMSSW_2_1_0_pre6/HLT/V30 (CMSSW_2_1_X_2008-07-03-0200_HLT1)

import FWCore.ParameterSet.Config as cms

block_hltDebugWithAlCaOutput = cms.PSet(
outputCommands = ( cms.untracked.vstring( 'drop *_hlt*_*_*', 'keep FEDRawDataCollection_source_*_*', 'keep FEDRawDataCollection_rawDataCollector_*_*', 'keep triggerTriggerEventWithRefs_*_*_*', 'keep edmTriggerResults_*_*_*', 'keep triggerTriggerEvent_*_*_*', 'keep *_hltGtDigis_*_*', 'keep *_hltGctDigis_*_*', 'keep *_hltL1GtObjectMap_*_*', 'keep *_hltL1extraParticles_*_*', 'keep *_hltOfflineBeamSpot_*_*', 'keep *_hltL1IsoRecoEcalCandidate_*_*', 'keep *_hltL1NonIsoRecoEcalCandidate_*_*', 'keep *_hltL1IsolatedElectronHcalIsol_*_*', 'keep *_hltL1NonIsolatedElectronHcalIsol_*_*', 'keep *_hltL1IsoElectronTrackIsol_*_*', 'keep *_hltL1NonIsoElectronTrackIsol_*_*', 'keep *_hltL1IsoLargeWindowElectronTrackIsol_*_*', 'keep *_hltL1NonIsoLargeWindowElectronTrackIsol_*_*', 'keep *_hltL1IsoStartUpElectronTrackIsol_*_*', 'keep *_hltL1NonIsoStartupElectronTrackIsol_*_*', 'keep *_hltL1IsolatedPhotonEcalIsol_*_*', 'keep *_hltL1NonIsolatedPhotonEcalIsol_*_*', 'keep *_hltL1IsolatedPhotonHcalIsol_*_*', 'keep *_hltL1NonIsolatedPhotonHcalIsol_*_*', 'keep *_hltL1IsoPhotonTrackIsol_*_*', 'keep *_hltL1NonIsoPhotonTrackIsol_*_*', 'keep *_hltHcalDoubleCone_*_*', 'keep *_hltL1NonIsoEMHcalDoubleCone_*_*', 'keep *_hltL1IsoElectronPixelSeeds_*_*', 'keep *_hltL1NonIsoElectronPixelSeeds_*_*', 'keep *_hltL1IsoLargeWindowElectronPixelSeeds_*_*', 'keep *_hltL1NonIsoLargeWindowElectronPixelSeeds_*_*', 'keep *_hltL1IsoStartUpElectronPixelSeeds_*_*', 'keep *_hltL1NonIsoStartUpElectronPixelSeeds_*_*', 'keep *_hltPixelMatchElectronsL1Iso_*_*', 'keep *_hltPixelMatchElectronsL1NonIso_*_*', 'keep *_hltPixelMatchElectronsL1IsoLargeWindow_*_*', 'keep *_hltPixelMatchElectronsL1NonIsoLargeWindow_*_*', 'keep *_hltPixelMatchStartUpElectronsL1Iso_*_*', 'keep *_hltPixelMatchStartUpElectronsL1NonIso_*_*', 'keep *_hltCorrectedHybridSuperClustersL1Isolated_*_*', 'keep *_hltCorrectedHybridSuperClustersL1NonIsolated_*_*', 'keep *_hltCorrectedEndcapSuperClustersWithPreshowerL1Isolated_*_*', 'keep *_hltCorrectedEndcapSuperClustersWithPreshowerL1NonIsolated_*_*', 'keep recoTracks_hltCtfL1IsoWithMaterialTracks_*_*', 'keep recoTracks_hltCtfL1NonIsoWithMaterialTracks_*_*', 'keep recoTracks_hltCtfL1IsoLargeWindowWithMaterialTracks_*_*', 'keep recoTracks_hltCtfL1NonIsoLargeWindowWithMaterialTracks_*_*', 'keep recoTracks_hltCtfL1IsoStartUpWithMaterialTracks_*_*', 'keep recoTracks_hltCtfL1NonIsoStartUpWithMaterialTracks_*_*', 'keep recoTracks_hltL1IsoElectronsRegionalCTFFinalFitWithMaterial_*_*', 'keep recoTracks_hltL1NonIsoElectronsRegionalCTFFinalFitWithMaterial_*_*', 'keep recoTracks_hltL1IsoEgammaRegionalCTFFinalFitWithMaterial_*_*', 'keep recoTracks_hltL1NonIsoEgammaRegionalCTFFinalFitWithMaterial_*_*', 'keep recoTracks_hltL1IsoLargeWindowElectronsRegionalCTFFinalFitWithMaterial_*_*', 'keep recoTracks_hltL1NonIsoLargeWindowElectronsRegionalCTFFinalFitWithMaterial_*_*', 'keep recoTracks_hltL1IsoStartUpElectronsRegionalCTFFinalFitWithMaterial_*_*', 'keep recoTracks_hltL1NonIsoStartUpElectronsRegionalCTFFinalFitWithMaterial_*_*', 'keep *_hltCkfL1IsoTrackCandidates_*_*', 'keep *_hltCkfL1NonIsoTrackCandidates_*_*', 'keep *_hltCkfL1IsoLargeWindowTrackCandidates_*_*', 'keep *_hltCkfL1NonIsoLargeWindowTrackCandidates_*_*', 'keep *_hltCkfL1IsoStartUpTrackCandidates_*_*', 'keep *_hltCkfL1NonIsoStartUpTrackCandidates_*_*', 'keep *_hltL1IsoElectronsRegionalPixelSeedGenerator_*_*', 'keep *_hltL1NonIsoElectronsRegionalPixelSeedGenerator_*_*', 'keep *_hltL1IsoEgammaRegionalPixelSeedGenerator_*_*', 'keep *_hltL1NonIsoEgammaRegionalPixelSeedGenerator_*_*', 'keep *_hltL1IsoLargeWindowElectronsRegionalPixelSeedGenerator_*_*', 'keep *_hltL1NonIsoLargeWindowElectronsRegionalPixelSeedGenerator_*_*', 'keep *_hltL1IsoStartUpElectronsRegionalPixelSeedGenerator_*_*', 'keep *_hltL1NonIsoStartUpElectronsRegionalPixelSeedGenerator_*_*', 'keep *_hltL1IsoElectronsRegionalCkfTrackCandidates_*_*', 'keep *_hltL1NonIsoElectronsRegionalCkfTrackCandidates_*_*', 'keep *_hltL1IsoEgammaRegionalCkfTrackCandidates_*_*', 'keep *_hltL1NonIsoEgammaRegionalCkfTrackCandidates_*_*', 'keep *_hltL1IsoLargeWindowElectronsRegionalCkfTrackCandidates_*_*', 'keep *_hltL1NonIsoLargeWindowElectronsRegionalCkfTrackCandidates_*_*', 'keep *_hltL1IsoStartUpElectronsRegionalCkfTrackCandidates_*_*', 'keep *_hltL1NonIsoStartUpElectronsRegionalCkfTrackCandidates_*_*', 'keep *_hltL2MuonSeeds_*_*', 'keep *_hltL2Muons_*_*', 'keep *_hltL3Muons_*_*', 'keep *_hltL2MuonCandidates_*_*', 'keep *_hltL3MuonCandidates_*_*', 'keep *_hltL2MuonIsolations_*_*', 'keep *_hltL3MuonIsolations_*_*', 'keep *_hltMCJetCorJetIcone5*_*_*', 'keep *_hltIterativeCone5CaloJets*_*_*', 'keep *_hltMet_*_*', 'keep *_hltHtMet_*_*', 'keep *_hltHtMetIC5_*_*', 'keep *_hltCaloTowersTau*_*_*', 'keep *_hltTowerMakerForAll_*_*', 'keep *_hltTowerMakerForTaus_*_*', 'keep *_hltSiPixelRecHits_*_*', 'keep *_hltPixelVertices_*_*', 'keep *_hltPixelTracks_*_*', 'keep *_hltSiStripRecHits_*_*', 'keep *_hltSiStripMatchedRecHits_*_*', 'keep *_hltIcone5Tau1*_*_*', 'keep *_hltIcone5Tau2*_*_*', 'keep *_hltIcone5Tau3*_*_*', 'keep *_hltIcone5Tau4*_*_*', 'keep *_hltHtMet_*_*', 'keep *_hltIterativeCone5CaloJets_*_*', 'keep *_hltBLifetimeHighestEtJets_*_*', 'keep *_hltBLifetimeL25Jets_*_*', 'keep *_hltPixelVertices_*_*', 'keep *_hltPixelTracks_*_*', 'keep *_hltBLifetimeL25Jets_*_*', 'keep *_hltBLifetimeL25Associator_*_*', 'keep *_hltBLifetimeL25TagInfos_*_*', 'keep *_hltBLifetimeL25BJetTags_*_*', 'keep *_hltBLifetimeRegionalCtfWithMaterialTracks_*_*', 'keep *_hltBLifetimeL3Jets_*_*', 'keep *_hltBLifetimeL3Associator_*_*', 'keep *_hltBLifetimeL3TagInfos_*_*', 'keep *_hltBLifetimeL3BJetTags_*_*', 'keep *_hltHtMet_*_*', 'keep *_hltIterativeCone5CaloJets_*_*', 'keep *_hltBSoftmuonHighestEtJets_*_*', 'keep *_hltBSoftmuonL25Jets_*_*', 'keep *_hltL2Muons_*_*', 'keep *_hltBSoftmuonL25TagInfos_*_*', 'keep *_hltBSoftmuonL25BJetTags_*_*', 'keep *_hltBSoftmuonL25Jets_*_*', 'keep *_hltL3Muons_*_*', 'keep *_hltBSoftmuonL3TagInfos_*_*', 'keep *_hltBSoftmuonL3BJetTags_*_*', 'keep *_hltBSoftmuonL3BJetTagsByDR_*_*', 'keep *_hltMumuPixelSeedFromL2Candidate_*_*', 'keep *_hltCkfTrackCandidatesMumu_*_*', 'keep *_hltCtfWithMaterialTracksMumu_*_*', 'keep *_hltMuTracks_*_*', 'keep *_hltMumukPixelSeedFromL2Candidate_*_*', 'keep *_hltCkfTrackCandidatesMumuk_*_*', 'keep *_hltCtfWithMaterialTracksMumuk_*_*', 'keep *_hltMuTracks_*_*', 'keep *_hltMumukAllConeTracks_*_*', 'keep *_hltL2SingleTauJets*_*_*', 'keep *_hltL2SingleTauIsolation*_*_*', 'keep *_hltMet*_*_*', 'keep *_hltCtfWithMaterialTracksL25SingleTau_*_*', 'keep *_hltAssociatorL25SingleTau*_*_*', 'keep *_hltConeIsolationL25SingleTau*_*_*', 'keep *_hltIsolatedL25SingleTau*_*_*', 'keep *_hltCtfWithMaterialTracksL3SingleTau*_*_*', 'keep *_hltAssociatorL3SingleTau*_*_*', 'keep *_hltConeIsolationL3SingleTau*_*_*', 'keep *_hltIsolatedL3SingleTau*_*_*', 'keep *_hltL2SingleTauMETJets*_*_*', 'keep *_hltL2SingleTauMETIsolation*_*_*', 'keep *_hltMet*_*_*', 'keep *_hltAssociatorL25SingleTauMET*_*_*', 'keep *_hltConeIsolationL25SingleTauMET*_*_*', 'keep *_hltIsolatedL25SingleTauMET*_*_*', 'keep *_hltCtfWithMaterialTracksL3SingleTauMET*_*_*', 'keep *_hltAssociatorL3SingleTauMET*_*_*', 'keep *_hltConeIsolationL3SingleTauMET*_*_*', 'keep *_hltIsolatedL3SingleTauMET*_*_*', 'keep *_hltL2DoubleTauJets*_*_*', 'keep *_hltL2DoubleTauIsolation*_*_*', 'keep *_hltAssociatorL25PixelTauIsolated*_*_*', 'keep *_hltConeIsolationL25PixelTauIsolated*_*_*', 'keep *_hltIsolatedL25PixelTau*_*_*', 'keep *_hltL2MuonSeeds_*_*', 'keep *_hltL2Muons_*_*', 'keep *_hltL3Muons_*_*', 'keep *_hltL2MuonCandidates_*_*', 'keep *_hltL2MuonIsolations_*_*', 'keep *_hltL3MuonCandidates_*_*', 'keep *_hltL3MuonIsolations_*_*', 'keep *_hltPixelVertices_*_*', 'keep *_hltPixelTracks_*_*', 'keep *_hltIcone5Tau1_*_*', 'keep *_hltIcone5Tau2_*_*', 'keep *_hltIcone5Tau3_*_*', 'keep *_hltIcone5Tau4_*_*', 'keep *_hltL2TauJetsProviderMuonTau_*_*', 'keep *_hltL2MuonTauIsolationSelector_*_*', 'keep *_hltL2MuonTauIsolationSelector_*_*', 'keep *_hltJetsPixelTracksAssociatorMuonTau_*_*', 'keep *_hltPixelTrackConeIsolationMuonTau_*_*', 'keep *_hltPixelTrackIsolatedTauJetsSelectorMuonTau_*_*', 'keep *_hltIsolatedTauJetsSelectorL25MuonTauPtLeadTk_*_*', 'keep *_hltPixelVertices_*_*', 'keep *_hltPixelTracks_*_*', 'keep *_hltIcone5Tau1_*_*', 'keep *_hltIcone5Tau2_*_*', 'keep *_hltIcone5Tau3_*_*', 'keep *_hltIcone5Tau4_*_*', 'keep *_hltL2TauJetsProvider_*_*', 'keep *_hltL2ElectronTauIsolationSelector_*_*', 'keep *_hltL2ElectronTauIsolationProducer_*_*', 'keep *_hltJetTracksAssociatorAtVertexL25ElectronTau_*_*', 'keep *_hltConeIsolationL25ElectronTau_*_*', 'keep *_hltIsolatedTauJetsSelectorL25ElectronTau_*_*', 'keep *_hltIsolatedTauJetsSelectorL25ElectronTauPtLeadTk_*_*', 'keep *_hltL1IsoRecoEcalCandidate_*_*', 'keep *_hltL1NonIsoRecoEcalCandidate_*_*', 'keep *_hltL1IsolatedElectronHcalIsol_*_*', 'keep *_hltL1NonIsolatedElectronHcalIsol_*_*', 'keep *_hltL1IsoElectronTrackIsol_*_*', 'keep *_hltL1NonIsoElectronTrackIsol_*_*', 'keep *_hltL1IsoLargeWindowElectronTrackIsol_*_*', 'keep *_hltL1NonIsoLargeWindowElectronTrackIsol_*_*', 'keep *_hltL1IsoStartUpElectronTrackIsol_*_*', 'keep *_hltL1NonIsoStartupElectronTrackIsol_*_*', 'keep *_hltL1IsolatedPhotonEcalIsol_*_*', 'keep *_hltL1NonIsolatedPhotonEcalIsol_*_*', 'keep *_hltL1IsolatedPhotonHcalIsol_*_*', 'keep *_hltL1NonIsolatedPhotonHcalIsol_*_*', 'keep *_hltL1IsoPhotonTrackIsol_*_*', 'keep *_hltL1NonIsoPhotonTrackIsol_*_*', 'keep *_hltHcalDoubleCone_*_*', 'keep *_hltL1NonIsoEMHcalDoubleCone_*_*', 'keep *_hltL1IsoElectronPixelSeeds_*_*', 'keep *_hltL1NonIsoElectronPixelSeeds_*_*', 'keep *_hltL1IsoLargeWindowElectronPixelSeeds_*_*', 'keep *_hltL1NonIsoLargeWindowElectronPixelSeeds_*_*', 'keep *_hltL1IsoStartUpElectronPixelSeeds_*_*', 'keep *_hltL1NonIsoStartUpElectronPixelSeeds_*_*', 'keep *_hltPixelMatchElectronsL1Iso_*_*', 'keep *_hltPixelMatchElectronsL1NonIso_*_*', 'keep *_hltPixelMatchElectronsL1IsoLargeWindow_*_*', 'keep *_hltPixelMatchElectronsL1NonIsoLargeWindow_*_*', 'keep *_hltPixelMatchStartUpElectronsL1Iso_*_*', 'keep *_hltPixelMatchStartUpElectronsL1NonIso_*_*', 'keep *_hltCorrectedHybridSuperClustersL1Isolated_*_*', 'keep *_hltCorrectedHybridSuperClustersL1NonIsolated_*_*', 'keep *_hltCorrectedEndcapSuperClustersWithPreshowerL1Isolated_*_*', 'keep *_hltCorrectedEndcapSuperClustersWithPreshowerL1NonIsolated_*_*', 'keep recoTracks_hltCtfL1IsoWithMaterialTracks_*_*', 'keep recoTracks_hltCtfL1NonIsoWithMaterialTracks_*_*', 'keep recoTracks_hltCtfL1IsoLargeWindowWithMaterialTracks_*_*', 'keep recoTracks_hltCtfL1NonIsoLargeWindowWithMaterialTracks_*_*', 'keep recoTracks_hltCtfL1IsoStartUpWithMaterialTracks_*_*', 'keep recoTracks_hltCtfL1NonIsoStartUpWithMaterialTracks_*_*', 'keep recoTracks_hltL1IsoElectronsRegionalCTFFinalFitWithMaterial_*_*', 'keep recoTracks_hltL1NonIsoElectronsRegionalCTFFinalFitWithMaterial_*_*', 'keep recoTracks_hltL1IsoEgammaRegionalCTFFinalFitWithMaterial_*_*', 'keep recoTracks_hltL1NonIsoEgammaRegionalCTFFinalFitWithMaterial_*_*', 'keep recoTracks_hltL1IsoLargeWindowElectronsRegionalCTFFinalFitWithMaterial_*_*', 'keep recoTracks_hltL1NonIsoLargeWindowElectronsRegionalCTFFinalFitWithMaterial_*_*', 'keep recoTracks_hltL1IsoStartUpElectronsRegionalCTFFinalFitWithMaterial_*_*', 'keep recoTracks_hltL1NonIsoStartUpElectronsRegionalCTFFinalFitWithMaterial_*_*', 'keep *_hltCkfL1IsoTrackCandidates_*_*', 'keep *_hltCkfL1NonIsoTrackCandidates_*_*', 'keep *_hltCkfL1IsoLargeWindowTrackCandidates_*_*', 'keep *_hltCkfL1NonIsoLargeWindowTrackCandidates_*_*', 'keep *_hltCkfL1IsoStartUpTrackCandidates_*_*', 'keep *_hltCkfL1NonIsoStartUpTrackCandidates_*_*', 'keep *_hltL1IsoElectronsRegionalPixelSeedGenerator_*_*')+cms.untracked.vstring( 'keep *_hltL1NonIsoElectronsRegionalPixelSeedGenerator_*_*', 'keep *_hltL1IsoEgammaRegionalPixelSeedGenerator_*_*', 'keep *_hltL1NonIsoEgammaRegionalPixelSeedGenerator_*_*', 'keep *_hltL1IsoLargeWindowElectronsRegionalPixelSeedGenerator_*_*', 'keep *_hltL1NonIsoLargeWindowElectronsRegionalPixelSeedGenerator_*_*', 'keep *_hltL1IsoStartUpElectronsRegionalPixelSeedGenerator_*_*', 'keep *_hltL1NonIsoStartUpElectronsRegionalPixelSeedGenerator_*_*', 'keep *_hltL1IsoElectronsRegionalCkfTrackCandidates_*_*', 'keep *_hltL1NonIsoElectronsRegionalCkfTrackCandidates_*_*', 'keep *_hltL1IsoEgammaRegionalCkfTrackCandidates_*_*', 'keep *_hltL1NonIsoEgammaRegionalCkfTrackCandidates_*_*', 'keep *_hltL1IsoLargeWindowElectronsRegionalCkfTrackCandidates_*_*', 'keep *_hltL1NonIsoLargeWindowElectronsRegionalCkfTrackCandidates_*_*', 'keep *_hltL1IsoStartUpElectronsRegionalCkfTrackCandidates_*_*', 'keep *_hltL1NonIsoStartUpElectronsRegionalCkfTrackCandidates_*_*', 'keep *_hltHtMet_*_*', 'keep *_hltIterativeCone5CaloJets_*_*', 'keep *_hltBLifetimeHighestEtJets_*_*', 'keep *_hltBLifetimeL25Jets_*_*', 'keep *_hltPixelVertices_*_*', 'keep *_hltPixelTracks_*_*', 'keep *_hltBLifetimeL25Jets_*_*', 'keep *_hltBLifetimeL25Associator_*_*', 'keep *_hltBLifetimeL25TagInfos_*_*', 'keep *_hltBLifetimeL25BJetTags_*_*', 'keep *_hltBLifetimeRegionalCtfWithMaterialTracks_*_*', 'keep *_hltBLifetimeL3Jets_*_*', 'keep *_hltBLifetimeL3Associator_*_*', 'keep *_hltBLifetimeL3TagInfos_*_*', 'keep *_hltBLifetimeL3BJetTags_*_*', 'keep *_hltL2MuonSeeds_*_*', 'keep *_hltL2Muons_*_*', 'keep *_hltL3Muons_*_*', 'keep *_hltL2MuonCandidates_*_*', 'keep *_hltL3MuonCandidates_*_*', 'keep *_hltL2MuonIsolations_*_*', 'keep *_hltL3MuonIsolations_*_*', 'keep *_hltHtMet_*_*', 'keep *_hltIterativeCone5CaloJets_*_*', 'keep *_hltBSoftmuonHighestEtJets_*_*', 'keep *_hltBSoftmuonL25Jets_*_*', 'keep *_hltL2Muons_*_*', 'keep *_hltBSoftmuonL25TagInfos_*_*', 'keep *_hltBSoftmuonL25BJetTags_*_*', 'keep *_hltBSoftmuonL25Jets_*_*', 'keep *_hltL3Muons_*_*', 'keep *_hltBSoftmuonL3TagInfos_*_*', 'keep *_hltBSoftmuonL3BJetTags_*_*', 'keep *_hltBSoftmuonL3BJetTagsByDR_*_*', 'keep *_hltL2MuonSeeds_*_*', 'keep *_hltL2Muons_*_*', 'keep *_hltL3Muons_*_*', 'keep *_hltL2MuonCandidates_*_*', 'keep *_hltL3MuonCandidates_*_*', 'keep *_hltL2MuonIsolations_*_*', 'keep *_hltL3MuonIsolations_*_*', 'keep *_hltHtMet_*_*', 'keep *_hltIterativeCone5CaloJets_*_*', 'keep *_hltBLifetimeHighestEtJets_*_*', 'keep *_hltBLifetimeL25Jets_*_*', 'keep *_hltPixelVertices_*_*', 'keep *_hltPixelTracks_*_*', 'keep *_hltBLifetimeL25Jets_*_*', 'keep *_hltBLifetimeL25Associator_*_*', 'keep *_hltBLifetimeL25TagInfos_*_*', 'keep *_hltBLifetimeL25BJetTags_*_*', 'keep *_hltBLifetimeRegionalCtfWithMaterialTracks_*_*', 'keep *_hltBLifetimeL3Jets_*_*', 'keep *_hltBLifetimeL3Associator_*_*', 'keep *_hltBLifetimeL3TagInfos_*_*', 'keep *_hltBLifetimeL3BJetTags_*_*', 'keep *_hltL1IsoRecoEcalCandidate_*_*', 'keep *_hltL1NonIsoRecoEcalCandidate_*_*', 'keep *_hltL1IsolatedElectronHcalIsol_*_*', 'keep *_hltL1NonIsolatedElectronHcalIsol_*_*', 'keep *_hltL1IsoElectronTrackIsol_*_*', 'keep *_hltL1NonIsoElectronTrackIsol_*_*', 'keep *_hltL1IsoLargeWindowElectronTrackIsol_*_*', 'keep *_hltL1NonIsoLargeWindowElectronTrackIsol_*_*', 'keep *_hltL1IsoStartUpElectronTrackIsol_*_*', 'keep *_hltL1NonIsoStartupElectronTrackIsol_*_*', 'keep *_hltL1IsolatedPhotonEcalIsol_*_*', 'keep *_hltL1NonIsolatedPhotonEcalIsol_*_*', 'keep *_hltL1IsolatedPhotonHcalIsol_*_*', 'keep *_hltL1NonIsolatedPhotonHcalIsol_*_*', 'keep *_hltL1IsoPhotonTrackIsol_*_*', 'keep *_hltL1NonIsoPhotonTrackIsol_*_*', 'keep *_hltHcalDoubleCone_*_*', 'keep *_hltL1NonIsoEMHcalDoubleCone_*_*', 'keep *_hltL1IsoElectronPixelSeeds_*_*', 'keep *_hltL1NonIsoElectronPixelSeeds_*_*', 'keep *_hltL1IsoLargeWindowElectronPixelSeeds_*_*', 'keep *_hltL1NonIsoLargeWindowElectronPixelSeeds_*_*', 'keep *_hltL1IsoStartUpElectronPixelSeeds_*_*', 'keep *_hltL1NonIsoStartUpElectronPixelSeeds_*_*', 'keep *_hltPixelMatchElectronsL1Iso_*_*', 'keep *_hltPixelMatchElectronsL1NonIso_*_*', 'keep *_hltPixelMatchElectronsL1IsoLargeWindow_*_*', 'keep *_hltPixelMatchElectronsL1NonIsoLargeWindow_*_*', 'keep *_hltPixelMatchStartUpElectronsL1Iso_*_*', 'keep *_hltPixelMatchStartUpElectronsL1NonIso_*_*', 'keep *_hltCorrectedHybridSuperClustersL1Isolated_*_*', 'keep *_hltCorrectedHybridSuperClustersL1NonIsolated_*_*', 'keep *_hltCorrectedEndcapSuperClustersWithPreshowerL1Isolated_*_*', 'keep *_hltCorrectedEndcapSuperClustersWithPreshowerL1NonIsolated_*_*', 'keep recoTracks_hltCtfL1IsoWithMaterialTracks_*_*', 'keep recoTracks_hltCtfL1NonIsoWithMaterialTracks_*_*', 'keep recoTracks_hltCtfL1IsoLargeWindowWithMaterialTracks_*_*', 'keep recoTracks_hltCtfL1NonIsoLargeWindowWithMaterialTracks_*_*', 'keep recoTracks_hltCtfL1IsoStartUpWithMaterialTracks_*_*', 'keep recoTracks_hltCtfL1NonIsoStartUpWithMaterialTracks_*_*', 'keep recoTracks_hltL1IsoElectronsRegionalCTFFinalFitWithMaterial_*_*', 'keep recoTracks_hltL1NonIsoElectronsRegionalCTFFinalFitWithMaterial_*_*', 'keep recoTracks_hltL1IsoEgammaRegionalCTFFinalFitWithMaterial_*_*', 'keep recoTracks_hltL1NonIsoEgammaRegionalCTFFinalFitWithMaterial_*_*', 'keep recoTracks_hltL1IsoLargeWindowElectronsRegionalCTFFinalFitWithMaterial_*_*', 'keep recoTracks_hltL1NonIsoLargeWindowElectronsRegionalCTFFinalFitWithMaterial_*_*', 'keep recoTracks_hltL1IsoStartUpElectronsRegionalCTFFinalFitWithMaterial_*_*', 'keep recoTracks_hltL1NonIsoStartUpElectronsRegionalCTFFinalFitWithMaterial_*_*', 'keep *_hltCkfL1IsoTrackCandidates_*_*', 'keep *_hltCkfL1NonIsoTrackCandidates_*_*', 'keep *_hltCkfL1IsoLargeWindowTrackCandidates_*_*', 'keep *_hltCkfL1NonIsoLargeWindowTrackCandidates_*_*', 'keep *_hltCkfL1IsoStartUpTrackCandidates_*_*', 'keep *_hltCkfL1NonIsoStartUpTrackCandidates_*_*', 'keep *_hltL1IsoElectronsRegionalPixelSeedGenerator_*_*', 'keep *_hltL1NonIsoElectronsRegionalPixelSeedGenerator_*_*', 'keep *_hltL1IsoEgammaRegionalPixelSeedGenerator_*_*', 'keep *_hltL1NonIsoEgammaRegionalPixelSeedGenerator_*_*', 'keep *_hltL1IsoLargeWindowElectronsRegionalPixelSeedGenerator_*_*', 'keep *_hltL1NonIsoLargeWindowElectronsRegionalPixelSeedGenerator_*_*', 'keep *_hltL1IsoStartUpElectronsRegionalPixelSeedGenerator_*_*', 'keep *_hltL1NonIsoStartUpElectronsRegionalPixelSeedGenerator_*_*', 'keep *_hltL1IsoElectronsRegionalCkfTrackCandidates_*_*', 'keep *_hltL1NonIsoElectronsRegionalCkfTrackCandidates_*_*', 'keep *_hltL1IsoEgammaRegionalCkfTrackCandidates_*_*', 'keep *_hltL1NonIsoEgammaRegionalCkfTrackCandidates_*_*', 'keep *_hltL1IsoLargeWindowElectronsRegionalCkfTrackCandidates_*_*', 'keep *_hltL1NonIsoLargeWindowElectronsRegionalCkfTrackCandidates_*_*', 'keep *_hltL1IsoStartUpElectronsRegionalCkfTrackCandidates_*_*', 'keep *_hltL1NonIsoStartUpElectronsRegionalCkfTrackCandidates_*_*', 'keep *_hltL1IsoRecoEcalCandidate_*_*', 'keep *_hltL1NonIsoRecoEcalCandidate_*_*', 'keep *_hltL1IsolatedElectronHcalIsol_*_*', 'keep *_hltL1NonIsolatedElectronHcalIsol_*_*', 'keep *_hltL1IsoElectronTrackIsol_*_*', 'keep *_hltL1NonIsoElectronTrackIsol_*_*', 'keep *_hltPixelMatchElectronsL1Iso_*_*', 'keep *_hltPixelMatchElectronsL1NonIso_*_*', 'keep *_hltCorrectedHybridSuperClustersL1Isolated_*_*', 'keep *_hltCorrectedHybridSuperClustersL1NonIsolated_*_*', 'keep *_hltCorrectedEndcapSuperClustersWithPreshowerL1Isolated_*_*', 'keep *_hltCorrectedEndcapSuperClustersWithPreshowerL1NonIsolated_*_*', 'keep recoTracks_hltCtfL1IsoWithMaterialTracksBarrel_*_*', 'keep recoTracks_hltCtfL1NonIsoWithMaterialTracksBarrel_*_*', 'keep recoTracks_hltCtfL1IsoWithMaterialTracksEndcap_*_*', 'keep recoTracks_hltCtfL1NonIsoWithMaterialTracksEndcap_*_*', 'keep recoTracks_hltL1IsoElectronsRegionalCTFFinalFitWithMaterial_*_*', 'keep recoTracks_hltL1NonIsoElectronsRegionalCTFFinalFitWithMaterial_*_*', 'keep recoTracks_hltL1IsoEgammaRegionalCTFFinalFitWithMaterial_*_*', 'keep recoTracks_hltL1NonIsoEgammaRegionalCTFFinalFitWithMaterial_*_*', 'keep *_hltL2MuonSeeds_*_*', 'keep *_hltL2Muons_*_*', 'keep *_hltL3Muons_*_*', 'keep *_hltL2MuonCandidates_*_*', 'keep *_hltL3MuonCandidates_*_*', 'keep *_hltL2MuonIsolations_*_*', 'keep *_hltL3MuonIsolations_*_*', 'keep *_hltL2MuonSeeds_*_*', 'keep *_hltL2Muons_*_*', 'keep *_hltL3Muons_*_*', 'keep *_hltL2MuonCandidates_*_*', 'keep *_hltL3MuonCandidates_*_*', 'keep *_hltL2MuonIsolations_*_*', 'keep *_hltL3MuonIsolations_*_*', 'keep *_hltMCJetCorJetIcone5*_*_*', 'keep *_hltIterativeCone5CaloJets*_*_*', 'keep *_hltSubdetFED_*_*', 'keep *_hltEcalRegFED_*_*', 'keep *_hltSiStripRegFED_*_*', 'keep *_hltPixelTracks_*_*', 'keep *_hltIsolPixelTrackProd_*_*', 'keep *_hltL1sIsoTrack_*_*', 'keep *_hltGtDigis_*_*', 'keep l1extraL1JetParticles_hltL1extraParticles_*_*', 'keep *_hltAlCaPi0RegRecHits_pi0EcalRecHitsEB_*', 'keep *_hltAlCaPhiSymStream_phiSymEcalRecHitsEB_*', 'keep *_hltAlCaPhiSymStream_phiSymEcalRecHitsEE_*', 'keep *_hltL1GtUnpack_*_*', 'keep *_hltGtDigis_*_*', 'keep *_hltAlCaHcalPhiSymStream_phiSymHcalRecHitsHBHE_*', 'keep *_hltAlCaHcalPhiSymStream_phiSymHcalRecHitsHO_*', 'keep *_hltAlCaHcalPhiSymStream_phiSymHcalRecHitsHF_*') )
)

HLTSchedule = cms.Schedule( )

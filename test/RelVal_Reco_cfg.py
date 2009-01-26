import FWCore.ParameterSet.Config as cms

process = cms.Process("RECO")

process.load("Configuration.StandardSequences.Services_cff")
process.load("FWCore.MessageService.MessageLogger_cfi")

process.options = cms.untracked.PSet(
    wantSummary = cms.untracked.bool(True)
)

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(-1)
)

process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring('file:RelVal_Pure_Raw.root')
)

process.load("Configuration.StandardSequences.GeometryPilot2_cff")
process.load("Configuration.StandardSequences.MagneticField_cff")

# Conditions: fake or frontier
# process.load("Configuration.StandardSequences.FakeConditions_cff")
process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")
# https://twiki.cern.ch/twiki/bin/view/CMS/SWGuideFrontierConditions
process.GlobalTag.globaltag = 'STARTUP_V8::All'

process.load("Configuration.StandardSequences.RawToDigi_cff")
process.load("Configuration.StandardSequences.Reconstruction_cff")

process.p1 = cms.Path(process.RawToDigi+process.reconstruction)

process.load("Configuration.EventContent.EventContent_cff")
process.FEVT = cms.OutputModule("PoolOutputModule",
    process.FEVTDEBUGHLTEventContent,
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string('RECO')
    ),
    fileName = cms.untracked.string('RelVal_Reco.root')
)
process.outpath = cms.EndPath(process.FEVT)

import FWCore.ParameterSet.Config as cms

process = cms.Process("HLT")


process.load("FWCore.MessageLogger.MessageLogger_cfi")
process.options = cms.untracked.PSet(
    wantSummary = cms.untracked.bool(True)
)


process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(100)
)

process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring('file:RelVal_Pure_Raw.root')
)

process.load("Configuration.StandardSequences.Geometry_cff")
process.load("Configuration.StandardSequences.MagneticField_cff")

# Conditions: fake or frontier
# process.load("Configuration.StandardSequences.FakeConditions_cff")
process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")
process.GlobalTag.globaltag = 'STARTUP::All'

process.load("Configuration.StandardSequences.L1Emulator_cff")
# Choose a menu/prescale/mask from one of the choices
# in L1TriggerConfig.L1GtConfigProducers.Luminosity
process.load("Configuration.StandardSequences.L1TriggerDefaultMenu_cff")

# run HLT
process.load("SimGeneral.HepPDTESSource.pythiapdt_cfi")
process.load("HLTrigger.Configuration.HLT_2E30_cff")


process.load("Configuration.EventContent.EventContent_cff")
process.hltPoolOutput = cms.OutputModule("PoolOutputModule",
    process.FEVTDEBUGHLTEventContent,
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string('RECO')
    ),
    basketSize = cms.untracked.int32(4096),
    fileName = cms.untracked.string('file:HLTFromPureRaw.root')
)

process.HLTPoolOutput = cms.EndPath(process.hltPoolOutput)

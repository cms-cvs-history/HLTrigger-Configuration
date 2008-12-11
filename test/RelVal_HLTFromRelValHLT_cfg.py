import FWCore.ParameterSet.Config as cms

process = cms.Process("HLT2")


process.load("FWCore.MessageService.MessageLogger_cfi")
process.options = cms.untracked.PSet(
    wantSummary = cms.untracked.bool(True)
)


process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(100)
)

process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring('file:HLTFromPureRaw.root')
)

process.load("Configuration.StandardSequences.GeometryIdeal_cff")
process.load("Configuration.StandardSequences.MagneticField_cff")

# Conditions: fake or frontier
# process.load("Configuration.StandardSequences.FakeConditions_cff")
process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")
# https://twiki.cern.ch/twiki/bin/view/CMS/SWGuideFrontierConditions
process.GlobalTag.globaltag = 'STARTUP_30X::All'

process.load("Configuration.StandardSequences.L1Emulator_cff")
# Choose a menu/prescale/mask from one of the choices
# in L1TriggerConfig.L1GtConfigProducers.Luminosity
process.load("L1TriggerConfig.L1GtConfigProducers.Luminosity.lumi1030.L1Menu_2008MC_2E30_Unprescaled_cff")

# run HLT
process.load("SimGeneral.HepPDTESSource.pythiapdt_cfi")
process.load("HLTrigger.Configuration.HLT_2E30_cff")
process.schedule = process.HLTSchedule

process.hltTrigReport.HLTriggerResults = cms.InputTag( 'TriggerResults','','HLT2' )

process.load("Configuration.EventContent.EventContent_cff")
process.hltPoolOutput = cms.OutputModule("PoolOutputModule",
    process.FEVTDEBUGHLTEventContent,
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string('RECO')
    ),
    basketSize = cms.untracked.int32(4096),
    fileName = cms.untracked.string('file:HLTFromDigiRaw.root')
)
process.HLTOutput = cms.EndPath(process.hltPoolOutput)
process.schedule.append(process.HLTOutput)

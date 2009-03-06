import FWCore.ParameterSet.Config as cms

process = cms.Process('HLT2')

# Message Logger, default settings
process.load('FWCore.MessageService.MessageLogger_cfi')
process.options = cms.untracked.PSet(
    wantSummary = cms.untracked.bool(True)
)

# Read some events from a RelVal
process.source = cms.Source('PoolSource',
    fileNames = cms.untracked.vstring(
        '/store/relval/CMSSW_2_2_4/RelValTTbar/GEN-SIM-DIGI-RAW-HLTDEBUG/STARTUP_V8_v1/0000/069AA022-5BF3-DD11-9A56-001617E30D12.root',
        '/store/relval/CMSSW_2_2_4/RelValTTbar/GEN-SIM-DIGI-RAW-HLTDEBUG/STARTUP_V8_v1/0000/08DA99A6-5AF3-DD11-AAC1-001D09F24493.root',
        '/store/relval/CMSSW_2_2_4/RelValTTbar/GEN-SIM-DIGI-RAW-HLTDEBUG/STARTUP_V8_v1/0000/0A725E15-5BF3-DD11-8B4B-000423D99CEE.root'
    )
)

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(100)
)

# Geometry and Magnetic field
process.load('Configuration.StandardSequences.GeometryPilot2_cff')
process.load('Configuration.StandardSequences.MagneticField_cff')

# Frontier conditions and GlobalTag
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')
process.GlobalTag.globaltag = 'STARTUP_V8::All'

# L1 emulator
# run trigger primitives generation on unpacked digis
process.load('L1Trigger.Configuration.CaloTriggerPrimitives_cff')
process.simEcalTriggerPrimitiveDigis.Label = 'ecalDigis'
process.simHcalTriggerPrimitiveDigis.inputLabel = 'hcalDigis'

# run the emulator with the chosen configuration
process.load('L1Trigger.Configuration.SimL1Emulator_cff')
process.load('L1Trigger.Configuration.L1StartupConfig_cff')
process.load('L1TriggerConfig.L1GtConfigProducers.Luminosity.startup.L1Menu_Commissioning2009_v0_L1T_Scales_20080926_startup_Imp0_Unprescaled_cff')
process.Emulator = cms.Path( process.SimL1Emulator )
process.schedule = cms.Schedule( process.Emulator )

# HLT
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('HLTrigger.Configuration.HLT_8E29_cff')
process.schedule.extend( process.HLTSchedule )

process.hltL1gtTrigReport = cms.EDAnalyzer( 'L1GtTrigReport',
    UseL1GlobalTriggerRecord = cms.bool( False ),
    L1GtRecordInputTag = cms.InputTag( 'hltGtDigis' )
)
process.hltTrigReport = cms.EDAnalyzer( 'HLTrigReport',
    HLTriggerResults = cms.InputTag( 'TriggerResults','','HLT2' )
)
process.HLTAnalyzerEndpath = cms.EndPath( process.hltL1gtTrigReport + process.hltTrigReport )
process.schedule.append(process.HLTAnalyzerEndpath)

process.load('Configuration.EventContent.EventContent_cff')
process.hltPoolOutput = cms.OutputModule('PoolOutputModule',
    process.FEVTDEBUGHLTEventContent,
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string('RECO')
    ),
    basketSize = cms.untracked.int32(4096),
    fileName = cms.untracked.string('file:HLTFromDigiRaw.root')
)
process.HLTOutput = cms.EndPath(process.hltPoolOutput)
process.schedule.append(process.HLTOutput)

# patch the process to use 'sim*Digis' from the L1 emulator instead of 'hlt*Digis' from the RAW data
from L1Trigger.Configuration import patchToRerunL1Emulator
patchToRerunL1Emulator.switchToSimGtDigis( process )

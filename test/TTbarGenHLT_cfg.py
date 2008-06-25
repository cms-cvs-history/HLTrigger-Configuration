import FWCore.ParameterSet.Config as cms

process = cms.Process("HLT")


process.load("Configuration.StandardSequences.Services_cff")
process.load("FWCore.MessageService.MessageLogger_cfi")
process.options = cms.untracked.PSet(
    wantSummary = cms.untracked.bool(True),
    Rethrow = cms.untracked.vstring('Unknown', 
        'ProductNotFound', 
        'DictionaryNotFound', 
        'InsertFailure', 
        'Configuration', 
        'LogicError', 
        'UnimplementedFeature', 
        'InvalidReference', 
        'NullPointerError', 
        'NoProductSpecified', 
        'EventTimeout', 
        'EventCorruption', 
        'ModuleFailure', 
        'ScheduleExecutionFailure', 
        'EventProcessorFailure', 
        'FileInPathError', 
        'FatalRootError', 
        'NotFound')
)


process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(2)
)

process.load("Configuration.Generator.PythiaUESettings_cfi")
process.source = cms.Source("PythiaSource",
    pythiaHepMCVerbosity = cms.untracked.bool(False),
    maxEventsToPrint = cms.untracked.int32(0),
    pythiaPylistVerbosity = cms.untracked.int32(0),
    filterEfficiency = cms.untracked.double(1.0),
    PythiaParameters = cms.PSet(
        process.pythiaUESettingsBlock,
        processParameters = cms.vstring(
            'MSEL      = 0     ! User defined processes', 
            'MSUB(81)  = 1     ! qqbar to QQbar', 
            'MSUB(82)  = 1     ! gg to QQbar', 
            'MSTP(7)   = 6     ! flavour = top', 
            'PMAS(6,1) = 175.  ! top quark mass'),
        # This is a vector of ParameterSet names to be read, in this order
        parameterSets = cms.vstring(
            'pythiaUESettings', 
            'processParameters')
    )
)


process.load("Configuration.StandardSequences.Geometry_cff")
process.load("Configuration.StandardSequences.MagneticField_cff")
process.load("Configuration.StandardSequences.VtxSmearedEarly10TeVCollision_cff")

# Conditions: fake or frontier
# process.load("Configuration.StandardSequences.FakeConditions_cff")
process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")
# https://twiki.cern.ch/twiki/bin/view/CMS/SWGuideFrontierConditions
process.GlobalTag.globaltag = 'STARTUP::All'

process.load("Configuration.StandardSequences.Generator_cff")
process.load("Configuration.StandardSequences.Sim_cff")
process.load("Configuration.StandardSequences.MixingNoPileUp_cff")
process.load("Configuration.StandardSequences.Digi_cff")
process.load("Configuration.StandardSequences.L1Emulator_cff")
process.load("Configuration.StandardSequences.DigiToRaw_cff")
# Choose a menu/prescale/mask from one of the choices
# in L1TriggerConfig.L1GtConfigProducers.Luminosity
process.load("L1TriggerConfig.L1GtConfigProducers.Luminosity.lumi1030.L1Menu2008_2E30_Unprescaled_cff")
import HLTrigger.HLTfilters.hltBool_cfi
process.pBool = HLTrigger.HLTfilters.hltBool_cfi.hltBool.clone()
process.pBool.result = False

process.GenSimDigiL1Raw = cms.Path(process.pgen+process.psim+process.pdigi+process.L1Emulator+process.DigiToRaw+process.pBool)


# run HLT
process.load("HLTrigger.Configuration.HLT_2E30_cff")

process.load("Configuration.EventContent.EventContent_cff")
process.FEVT = cms.OutputModule("PoolOutputModule",
    process.FEVTDEBUGHLTEventContent,
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string('RAW-HLT')
    ),
    basketSize = cms.untracked.int32(4096),
    fileName = cms.untracked.string('TTbarGenHLT.root')
)

process.outpath = cms.EndPath(process.FEVT)

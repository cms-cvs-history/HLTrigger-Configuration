import FWCore.ParameterSet.Config as cms

block_hltDebugOutput = cms.PSet(
    outputCommands = cms.untracked.vstring( 'drop *_hlt*_*_*' )
)

# the DQM stream has the HLT debug output
import HLTrigger.Configuration.hltOutputDQM_cff
block_hltDebugOutput.outputCommands.extend( [ statement for statement in HLTrigger.Configuration.hltOutputDQM_cff.block_hltOutputDQM.outputCommands if statement.find('drop') != 0 ] )

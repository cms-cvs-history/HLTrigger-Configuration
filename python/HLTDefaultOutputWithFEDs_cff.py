import FWCore.ParameterSet.Config as cms

block_hltDefaultOutputWithFEDs = cms.PSet(
    outputCommands = cms.untracked.vstring( 'drop *_hlt*_*_*' )
)

# the A stream has the HLT default output, with FEDs
import HLTrigger.Configuration.hltOutputA_cff
block_hltDefaultOutputWithFEDs.outputCommands.extend( [ statement for statement in HLTrigger.Configuration.hltOutputA_cff.block_hltOutputA.outputCommands if statement.find('drop') != 0 ] )

import FWCore.ParameterSet.Config as cms

block_hltDefaultOutput = cms.PSet(
    outputCommands = cms.untracked.vstring( 'drop *_hlt*_*_*' )
)

# the A stream has the HLT default output, with FEDs - strip out the FEDRawDataCollection keep statements
import HLTrigger.Configuration.hltOutputA_cff
block_hltDefaultOutput.outputCommands.extend( [ statement for statement in HLTrigger.Configuration.hltOutputA_cff.block_hltOutputA.outputCommands if (statement.find('drop') != 0) or (statement.find('keep FEDRawDataCollection') != 0) ] )

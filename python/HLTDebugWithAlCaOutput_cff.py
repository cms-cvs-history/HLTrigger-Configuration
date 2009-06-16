import FWCore.ParameterSet.Config as cms

block_hltDebugWithAlCaOutput = cms.PSet(
    outputCommands = cms.untracked.vstring( 'drop *_hlt*_*_*' )
)

# the DQM stream has the HLT debug output
import HLTrigger.Configuration.hltOutputDQM_cff
block_hltDebugWithAlCaOutput.outputCommands.extend( [ statement for statement in HLTrigger.Configuration.hltOutputDQM_cff.block_hltOutputDQM.outputCommands             if statement.find('drop') != 0 ] )

# the ALCA streams have the AlCa outputs
import HLTrigger.Configuration.hltOutputALCA_cff
block_hltDebugWithAlCaOutput.outputCommands.extend( [ statement for statement in HLTrigger.Configuration.hltOutputALCA_cff.block_hltOutputALCAPHISYM.outputCommands     if statement.find('drop') != 0 ] )
block_hltDebugWithAlCaOutput.outputCommands.extend( [ statement for statement in HLTrigger.Configuration.hltOutputALCA_cff.block_hltOutputALCAPHISYMHCAL.outputCommands if statement.find('drop') != 0 ] )
block_hltDebugWithAlCaOutput.outputCommands.extend( [ statement for statement in HLTrigger.Configuration.hltOutputALCA_cff.block_hltOutputALCAP0.outputCommands         if statement.find('drop') != 0 ] )
block_hltDebugWithAlCaOutput.outputCommands.extend( [ statement for statement in HLTrigger.Configuration.hltOutputALCA_cff.block_hltOutputRPCMON.outputCommands         if statement.find('drop') != 0 ] )

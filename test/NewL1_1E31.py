
process.load('L1TriggerConfig.L1GtConfigProducers.L1GtTriggerMenuConfig_cff')
process.es_prefer_l1GtParameters = cms.ESPrefer('L1GtTriggerMenuXmlProducer','l1GtTriggerMenuXml')
process.load("L1TriggerConfig.L1GtConfigProducers.Luminosity.lumi1031.L1Menu_MC2009_v4_L1T_Scales_20090624_Imp0_Unprescaled_cff")


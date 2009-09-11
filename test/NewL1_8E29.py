
process.load('L1TriggerConfig.L1GtConfigProducers.L1GtTriggerMenuConfig_cff')
process.es_prefer_l1GtParameters = cms.ESPrefer('L1GtTriggerMenuXmlProducer','l1GtTriggerMenuXml')
process.load("L1TriggerConfig.L1GtConfigProducers.Luminosity.startup.L1Menu_Commissioning2009_v5_L1T_Scales_20080926_startup_Imp0_Unprescaled_cff")


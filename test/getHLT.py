#!/usr/bin/env python

import sys
import os
import commands
import getopt
import fileinput

l1Override = {
  '8E29': 'L1TriggerConfig.L1GtConfigProducers.Luminosity.startup.L1Menu_Commissioning2009_v5_L1T_Scales_20080926_startup_Imp0_Unprescaled_cff',
  'GRun': 'L1TriggerConfig.L1GtConfigProducers.Luminosity.startup.L1Menu_Commissioning2009_v5_L1T_Scales_20080926_startup_Imp0_Unprescaled_cff',
  'data': 'L1TriggerConfig.L1GtConfigProducers.Luminosity.startup.L1Menu_Commissioning2009_v5_L1T_Scales_20080926_startup_Imp0_Unprescaled_cff',
  '1E31': 'L1TriggerConfig.L1GtConfigProducers.Luminosity.lumi1031.L1Menu_MC2009_v4_L1T_Scales_20090624_Imp0_Unprescaled_cff',
  'HIon': 'L1TriggerConfig.L1GtConfigProducers.Luminosity.lumi1031.L1Menu_MC2009_v4_L1T_Scales_20090624_Imp0_Unprescaled_cff',
  None:   'L1TriggerConfig.L1GtConfigProducers.Luminosity.lumi1031.L1Menu_MC2009_v4_L1T_Scales_20090624_Imp0_Unprescaled_cff'              # use as default
}

globalTag = {
  '8E29': 'STARTUP3X_V8D::All',
  'GRun': 'STARTUP3X_V8D::All',
  'data': 'GR09_H_V6OFF::All',          # same as 'GR09_H_V6::All' for offline
  '1E31': 'MC_31X_V9::All',
  'HIon': 'MC_31X_V9::All',
  None:   'MC_31X_V9::All'              # use as default
}

def usage():
    print 'Usage:'
    print '  getHLT.py [--process <Name>] [--globaltag <GlobalTag::All>] [--l1override] [--l1 <L1.menu_cff>]'
    print '            [--full|--cff] [--data|--mc] [--online|--offline]'
    print '            [-f|--force]'
    print '            <Version from ConfDB> <ID>'
    print
    print 'Options:'
    print '  --process          Override the process name [default is "HLT" followed by the "ID"'
    print '  --globaltag        Use a specific GlobalTag (the default comes from the ID'
    print '  --l1override       Enable L1 menu override, identified from the ID'
    print '  --l1               Enable L1 menu override, using the given menu_cff (which must be a valid python import argument)'
    print
    print '  --full             Generate a full configuration file, with minimal modifications [this is the default]'
    print '  --cff              Generate a stripped down configuration file fragment, for inclusion by e.g. cmsDriver.py'
    print '  --data             Prepare a menu for running on data (RAW in "source") [this is the default]'
    print '  --mc               Prepare a menu for running on MC (RAW in "rawDataCollector")'
    print '  --online           Take the online compliant connection string and GlobalTag from the menu'
    print '  --offline          Override with the connection string and GlobalTag with te offline values [this is the default]'
    print
    print '  --force            Overwrite the destination file instead of aborting if it already exists'
    print
    print 'Notes:'
    print '     using "--online" and "--mc" together is not supported (there is no online compliant GlobalTag for MC)'
    print '     using "--online/--offline" has no effect if "--cff" is used'


doL1Override    = False
processName     = ''
fileId          = ''
doCff           = False
runOnData       = True
runOnline       = False
menuOutName     = ''
menuL1Override  = ''
menuGlobalTag   = ''
menuConfigDB    = ''
menuConfigName  = ''
doOverwrite     = False

def parse_options(args):
  # global variables
  global doL1Override
  global processName
  global fileId
  global doCff
  global runOnData
  global runOnline
  global menuOutName
  global menuL1Override
  global menuGlobalTag
  global menuConfigDB
  global menuConfigName
  global doOverwrite

  # valid options 
  options = ( 'process=', 'l1override', 'l1=', 'globaltag=', 'data', 'mc', 'force', 'online', 'offline', 'full', 'cff' )
  
  try:
    (opts, args) = getopt.gnu_getopt(args, 'f', options)
  except getopt.error, error:
    print 'Error:', error.msg
    print
    usage()
    sys.exit(1)

  for (opt, value) in opts:
    # set the process name
    if opt == '--process':
      processName = value
    # generate a cff fragment
    elif opt == '--cff':
      doCff = True
    # generate a full configuration file
    elif opt == '--full':
      doCff = False
    # force L1 override
    elif opt == '--l1override':
      doL1Override = True
    # specify L1 menu and force L1 override
    elif opt == '--l1':
      doL1Override = True
      menuL1Override = value
    # specify GlobalTag 
    elif opt == '--globaltag':
      menuGlobalTag = value
    # run on data (RAW in 'source')
    elif opt == '--data':
      runOnData = True
    # run on MC (RAW in 'rawDataCollector')
    elif opt == '--mc':
      runOnData = False
    # run online (keep online compliant GlobalTag from the menu)
    elif opt == '--online':
      runOnline = True
    # run offline(overrithe the GlobalTag from the menu with an offline one)
    elif opt == '--offline':
      runOnline = False
    # overwrite the destination file
    elif opt in ('-f', '--force'):
      doOverwrite = True
    else:
      print 'Invalid option: %s', opt
      usage()
      sys.exit(1)
 
  # look for the required arguments 
  try:
      configName  = args[0]
      fileId      = args[1]
      if not processName:
        processName = 'HLT' + fileId
  except:
      usage()
      sys.exit(1)

  if doCff:
      menuOutName = "HLT_" + fileId + "_cff.py"
  else:
      menuOutName = "OnLine_HLT_" + fileId + ".py"

  # extract the database and configuration name
  if ':' in configName:
    (menuConfigDB, menuConfigName) = configName.split(':')
    if menuConfigDB not in ('hltdev', 'orcoff'):
      print 'Unknown ConfDB database "%s", valid values are "hltdev" (default) and "orcoff")' % menuConfigDB
      sys.exit(1)
  else:
    (menuConfigDB, menuConfigName) = ('hltdev', configName)


# parse command line arguments and options
parse_options(sys.argv[1:])

if os.path.exists(menuOutName) and not doOverwrite:
    print menuOutName, "already exists - abort!"
    sys.exit(1)
else:
    # Initialize everything
    edsources = ""
    essources = "" 
    esmodules = ""
    modules   = ""
    services  = ""
    paths     = ""
    psets     = ""

    if doCff:
        edsources =  " --noedsources"

        essources  = " --essources "
        essources += "-GlobalTag,"
        essources += "-Level1MenuOverride,"
        essources += "-HepPDTESSource,"
        essources += "-XMLIdealGeometryESSource,"
        essources += "-eegeom,"
        essources += "-es_hardcode,"
        essources += "-magfield"

        esmodules  = " --esmodules "
        esmodules += "-AutoMagneticFieldESProducer,"
        esmodules += "-SlaveField0,"
        esmodules += "-SlaveField20,"
        esmodules += "-SlaveField30,"
        esmodules += "-SlaveField35,"
        esmodules += "-SlaveField38,"
        esmodules += "-SlaveField40,"
        esmodules += "-VBF0,"
        esmodules += "-VBF20,"
        esmodules += "-VBF30,"
        esmodules += "-VBF35,"
        esmodules += "-VBF38,"
        esmodules += "-VBF40,"
        esmodules += "-CSCGeometryESModule,"
        esmodules += "-CaloGeometryBuilder,"
        esmodules += "-CaloTowerHardcodeGeometryEP,"
        esmodules += "-DTGeometryESModule,"
        esmodules += "-EcalBarrelGeometryEP,"
        esmodules += "-EcalElectronicsMappingBuilder,"
        esmodules += "-EcalEndcapGeometryEP,"
        esmodules += "-EcalLaserCorrectionService,"    
        esmodules += "-EcalPreshowerGeometryEP,"
        esmodules += "-HcalHardcodeGeometryEP,"
        esmodules += "-HcalTopologyIdealEP,"
        esmodules += "-MuonNumberingInitialization,"
        esmodules += "-RPCGeometryESModule,"
        esmodules += "-SiStripGainESProducer,"
        esmodules += "-SiStripRecHitMatcherESProducer,"
        esmodules += "-SiStripQualityESProducer,"
        esmodules += "-StripCPEfromTrackAngleESProducer,"
        esmodules += "-TrackerDigiGeometryESModule,"
        esmodules += "-TrackerGeometricDetESModule,"
        esmodules += "-VolumeBasedMagneticFieldESProducer,"
        esmodules += "-ParametrizedMagneticFieldProducer,"
        esmodules += "-ZdcHardcodeGeometryEP,"
        esmodules += "-hcal_db_producer,"
        esmodules += "-l1GtTriggerMenuXml,"
        esmodules += "-L1GtTriggerMaskAlgoTrigTrivialProducer,"
        esmodules += "-L1GtTriggerMaskTechTrigTrivialProducer,"
        esmodules += "-sistripconn"

        services   = " --services -PrescaleService,-MessageLogger,-DQM,-DQMStore,-FUShmDQMOutputService,-MicroStateService,-ModuleWebRegistry,-TimeProfilerService"

        paths      = " --paths -HLTOutput,-AlCaOutput,-ESOutput,-MONOutput,-OfflineOutput,-DQMOutput"

        psets      = " --psets -maxEvents,-options"


        myGet = "edmConfigFromDB --cff --" + menuConfigDB + " --configName " + menuConfigName + edsources + essources + esmodules + modules + services + paths + psets + " > " + menuOutName
        os.system(myGet)

        # FIXME - this should be done by edmConfigFromDB - remove the definition of streams and primary datasets from the dump
        os.system("sed -e'/^streams/,/^)/d' -e'/^datasets/,/^)/d' -i " + menuOutName)

        if not runOnData:
          # FIXME - this should be done looking into the python objects, not working on the text representation
          os.system("sed -e 's/cms.InputTag( \"source\" )/cms.InputTag( \"rawDataCollector\" )/' -i " + menuOutName)
          os.system("sed -e 's/cms.string( \"source\" )/cms.string( \"rawDataCollector\" )/' -i " + menuOutName)

          # FIXME - DTUnpackingModule should not have untracked parameters
          os.system("sed -e'/DTUnpackingModule/a\ \ \ \ inputLabel = cms.untracked.InputTag( \"rawDataCollector\" ),' -i " + menuOutName)

        # open the output file for further tuning
        out = open(menuOutName, 'a')

        # if requested, override the L1 menu from the GlobalTag
        if doL1Override:
          out.write("\n")
          try:
            out.write("from %s import *\n" % l1Override[fileId])
          except:
            out.write("from %s import *\n" % l1Override[None])
          out.write("es_prefer_l1GtParameters = cms.ESPrefer('L1GtTriggerMenuXmlProducer','l1GtTriggerMenuXml')\n")

        # close the output file
        out.close()

    else:
        if runOnData:
          edsources =  " --input file:/tmp/InputCollection.root"
        else:
          edsources =  " --input file:RelVal_DigiL1Raw_"+fileId+".root"

        if not runOnData or doL1Override:
          # remove any eventual L1 override from the table
          essources  = " --essources "
          essources += "-Level1MenuOverride,"

          esmodules  = " --esmodules "
          esmodules += "-l1GtTriggerMenuXml,"
          esmodules += "-L1GtTriggerMaskAlgoTrigTrivialProducer,"
          esmodules += "-L1GtTriggerMaskTechTrigTrivialProducer"

        paths      = " --paths -OfflineOutput"

        myGet = "edmConfigFromDB --" + menuConfigDB + " --configName " + menuConfigName + edsources + essources + esmodules + modules + services + paths + psets + " > " + menuOutName
        os.system(myGet)

        # FIXME - this should be done by edmConfigFromDB - remove the definition of streams and primary datasets from the dump
        os.system("sed -e'/^process\.streams/,/^)/d' -e'/^process\.datasets/,/^)/d' -i " + menuOutName)

        if not runOnData:
          # FIXME - this should be done looking into the python objects, not working on the text representation
          os.system("sed -e 's/cms.InputTag( \"source\" )/cms.InputTag( \"rawDataCollector\" )/' -i " + menuOutName)
          os.system("sed -e 's/cms.string( \"source\" )/cms.string( \"rawDataCollector\" )/' -i " + menuOutName)

          # FIXME - DTUnpackingModule should not have untracked parameters
          os.system("sed -e'/DTUnpackingModule/a\ \ \ \ inputLabel = cms.untracked.InputTag( \"rawDataCollector\" ),' -i " + menuOutName)

        # FIXME - find a better way to override the output modules
        os.system("sed -e's/process\.hltOutput\(\w\+\) *= *cms\.OutputModule( *\"ShmStreamConsumer\" *,/process.hltOutput\\1 = cms.OutputModule( \"PoolOutputModule\",\\n    fileName = cms.untracked.string( \"output\\1.root\" ),/'  -i " + menuOutName)

        # open the output file for further tuning
        out = open(menuOutName, 'a')

        # overwrite ProcessName
        out.write("process.setName_('%s')\n" % processName)
        out.write("\n")

        # add global options
        out.write("process.maxEvents = cms.untracked.PSet(\n")
        out.write("    input = cms.untracked.int32( 100 )\n")
        out.write(")\n")
        out.write("process.options = cms.untracked.PSet(\n")
        out.write("    wantSummary = cms.untracked.bool( True )\n")
        out.write(")\n")
        out.write("\n")

        # Overwrite GlobalTag
        if not runOnline:
          if not menuGlobalTag:
            if runOnData:
              menuGlobalTag = globalTag['data']
            elif fileId in globalTag:
              menuGlobalTag = globalTag[fileId]
            else:
              menuGlobalTag = globalTag[None]
          out.write("if 'GlobalTag' in process.__dict__:\n")
          out.write("    process.GlobalTag.globaltag         = '%s'\n" % menuGlobalTag)
          out.write("    process.GlobalTag.connect           = 'frontier://FrontierProd/CMS_COND_31X_GLOBALTAG'\n")
          out.write("\n")
          out.write("if 'Level1MenuOverride' in process.__dict__:\n")
          out.write("    process.Level1MenuOverride.connect  = 'frontier://FrontierProd/CMS_COND_31X_L1T'\n")
          out.write("\n")

        # if requested, override the L1 menu from the GlobalTag
        if doL1Override:
          out.write("process.load('L1TriggerConfig.L1GtConfigProducers.L1GtTriggerMenuConfig_cff')\n")
          out.write("process.es_prefer_l1GtParameters = cms.ESPrefer('L1GtTriggerMenuXmlProducer','l1GtTriggerMenuXml')\n")
          if not menuL1Override:
            if runOnData:
              menuL1Override = l1Override['data']
            elif fileId in l1Override:
              menuL1Override = l1Override[fileId]
            else:
              menuL1Override = l1Override[None]
          out.write("process.load('%s')\n" % menuL1Override)
          out.write("\n")

        # the following is stolen from HLTrigger.Configuration.customL1THLT_Options
        out.write("if 'hltTrigReport' in process.__dict__:\n")
        out.write("    process.hltTrigReport.HLTriggerResults       = cms.InputTag( 'TriggerResults','',process.name_() )\n")
        out.write("\n")
        out.write("if 'hltDQMHLTScalers' in process.__dict__:\n")
        out.write("    process.hltDQMHLTScalers.triggerResults      = cms.InputTag( 'TriggerResults','',process.name_() )\n")
        out.write("\n")
        out.write("if 'hltPreExpressSmart' in process.__dict__:\n")
        out.write("    process.hltPreExpressSmart.TriggerResultsTag = cms.InputTag( 'TriggerResults','',process.name_() )\n")
        out.write("\n")
        out.write("if 'hltPreHLTMONSmart' in process.__dict__:\n")
        out.write("    process.hltPreHLTMONSmart.TriggerResultsTag  = cms.InputTag( 'TriggerResults','',process.name_() )\n")
        out.write("\n")
        out.write("process.options.wantSummary = cms.untracked.bool(True)\n")
        out.write("process.MessageLogger.categories.append('TriggerSummaryProducerAOD')\n")
        out.write("process.MessageLogger.categories.append('L1GtTrigReport')\n")
        out.write("process.MessageLogger.categories.append('HLTrigReport')\n")

        # close the output file
        out.close()


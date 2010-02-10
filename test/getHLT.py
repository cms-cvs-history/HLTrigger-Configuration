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
  '8E29': 'START3X_V21::All',
  'GRun': 'START3X_V21::All',
  'data': 'GR10_H_V2::All',
  '1E31': 'MC_3XY_V21::All',
  'HIon': 'MC_3XY_V21::All',
  None:   'START3X_V21::All',      # use as default
}

def usage():
    print 'Usage:'
    print '  getHLT.py [--process <Name>] [--globaltag <GlobalTag::All>] [--l1 <L1_MENU_vX>]'
    print '            [--full|--cff] [--data|--mc] [--online|--offline]'
    print '            [-f|--force]'
    print '            <Version from ConfDB> <ID>'
    print
    print 'Options:'
    print '  --process          Override the process name [default is "HLT" followed by the "ID"'
    print '  --globaltag        Use a specific GlobalTag (the default comes from the ID)'
    print '  --l1               Enable L1 menu override, using the given payload from the database'
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
  options = ( 'process=', 'l1=', 'globaltag=', 'data', 'mc', 'force', 'online', 'offline', 'full', 'cff' )
  
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
    # specify L1 menu and force L1 override
    elif opt == '--l1':
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
        if runOnData:
          processName = 'HLT' + fileId
        else:
          processName = 'HLT' # fileId
  except:
      usage()
      sys.exit(1)

  if doCff:
    menuOutName = "HLT_" + fileId + "_cff.py"
  else:
    if runOnData:
      menuOutName = "OnData_HLT_" + fileId + ".py"
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

        paths      = " --paths -HLTOutput,-HLTOutputB,-HLTOutputBnotT0,-AlCaOutput,-ESOutput,-MONOutput,-OfflineOutput,-DQMOutput"

        psets      = " --psets -maxEvents,-options"


        myGet = "edmConfigFromDB --cff --" + menuConfigDB + " --configName " + menuConfigName + edsources + essources + esmodules + modules + services + paths + psets + " > " + menuOutName
        os.system(myGet)

        # FIXME - this should be done by edmConfigFromDB - remove the definition of streams and primary datasets from the dump
        # os.system("sed -e'/^streams/,/^)/d' -e'/^datasets/,/^)/d' -i " + menuOutName)

        if not runOnData:
          # FIXME - this should be done looking into the python objects, not working on the text representation
          os.system("sed -e 's/cms.InputTag( \"source\" )/cms.InputTag( \"rawDataCollector\" )/' -i " + menuOutName)
          os.system("sed -e 's/cms.string( \"source\" )/cms.string( \"rawDataCollector\" )/' -i " + menuOutName)

          # FIXME - DTUnpackingModule should not have untracked parameters
          os.system("sed -e'/DTUnpackingModule/a\ \ \ \ inputLabel = cms.untracked.InputTag( \"rawDataCollector\" ),' -i " + menuOutName)

        # open the output file for further tuning
        out = open(menuOutName, 'a')

        # if requested, override the L1 menu from the GlobalTag
        if menuL1Override:
          out.write("""
Level1MenuOverride = cms.ESSource( "PoolDBESSource",
    BlobStreamerName = cms.untracked.string( "TBufferBlobStreamingService" ),
    connect = cms.string( "frontier://(proxyurl=http://localhost:3128)(serverurl=http://localhost:8000/FrontierOnProd)(serverurl=http://localhost:8000/FrontierOnProd)(retrieve-ziplevel=0)(failovertoserver=no)/CMS_COND_31X_L1T" ),
    label = cms.untracked.string( "" ),
    globaltag = cms.string( "" ),
    tag = cms.untracked.string( "" ),
    RefreshEachRun = cms.untracked.bool( True ),
    appendToDataLabel = cms.string( "" ),
    DBParameters = cms.PSet(
      authenticationPath = cms.untracked.string( "." ),
      connectionRetrialPeriod = cms.untracked.int32( 10 ),
      idleConnectionCleanupPeriod = cms.untracked.int32( 10 ),
      messageLevel = cms.untracked.int32( 0 ),
      enablePoolAutomaticCleanUp = cms.untracked.bool( False ),
      enableConnectionSharing = cms.untracked.bool( True ),
      enableReadOnlySessionOnUpdateConnection = cms.untracked.bool( False ),
      connectionTimeOut = cms.untracked.int32( 0 ),
      connectionRetrialTimeOut = cms.untracked.int32( 60 )
    ),
    toGet = cms.VPSet(
      cms.PSet(  record = cms.string( "L1GtTriggerMenuRcd" ),
        tag = cms.string( "%s" )
      )
    ),
    timetype = cms.string( "runnumber" ),
    siteLocalConfig = cms.untracked.bool( False ),
    messagelevel = cms.untracked.uint32( 0 )
)
es_prefer_Level1MenuOverride = cms.ESPrefer( "PoolDBESSource", "Level1MenuOverride" )\n""" % menuL1Override)

        # close the output file
        out.close()

    else:
        if runOnData:
          if runOnline:
            edsources =  " --input file:/tmp/InputCollection.root"
          else:
            edsources =  " --input rfio:/castor/cern.ch/cms/store/data/BeamCommissioning09/ZeroBias/RAW/v1/000/123/734/D28203D4-AFE3-DE11-ADEE-001D09F2527B.root"
        else:
          edsources =  " --input file:RelVal_DigiL1Raw_"+fileId+".root"

        if not runOnData or menuL1Override:
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
        # os.system("sed -e'/^process\.streams/,/^)/d' -e'/^process\.datasets/,/^)/d' -i " + menuOutName)

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

        # override the L1 menu
        if menuL1Override:
          out.write("""process.Level1MenuOverride = cms.ESSource( "PoolDBESSource",
    BlobStreamerName = cms.untracked.string( "TBufferBlobStreamingService" ),
    connect = cms.string( "frontier://(proxyurl=http://localhost:3128)(serverurl=http://localhost:8000/FrontierOnProd)(serverurl=http://localhost:8000/FrontierOnProd)(retrieve-ziplevel=0)(failovertoserver=no)/CMS_COND_31X_L1T" ),
    label = cms.untracked.string( "" ),
    globaltag = cms.string( "" ),
    tag = cms.untracked.string( "" ),
    RefreshEachRun = cms.untracked.bool( True ),
    appendToDataLabel = cms.string( "" ),
    DBParameters = cms.PSet(
      authenticationPath = cms.untracked.string( "." ),
      connectionRetrialPeriod = cms.untracked.int32( 10 ),
      idleConnectionCleanupPeriod = cms.untracked.int32( 10 ),
      messageLevel = cms.untracked.int32( 0 ),
      enablePoolAutomaticCleanUp = cms.untracked.bool( False ),
      enableConnectionSharing = cms.untracked.bool( True ),
      enableReadOnlySessionOnUpdateConnection = cms.untracked.bool( False ),
      connectionTimeOut = cms.untracked.int32( 0 ),
      connectionRetrialTimeOut = cms.untracked.int32( 60 )
    ),
    toGet = cms.VPSet(
      cms.PSet(  record = cms.string( "L1GtTriggerMenuRcd" ),
        tag = cms.string( "%s" )
      )
    ),
    timetype = cms.string( "runnumber" ),
    siteLocalConfig = cms.untracked.bool( False ),
    messagelevel = cms.untracked.uint32( 0 )
)
process.es_prefer_Level1MenuOverride = cms.ESPrefer( "PoolDBESSource", "Level1MenuOverride" )
\n""" % menuL1Override)

        # overwrite GlobalTag
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
          if runOnData:
            out.write("    process.GlobalTag.pfnPrefix         = cms.untracked.string('frontier://FrontierProd/')\n")
          out.write("\n")
          out.write("if 'Level1MenuOverride' in process.__dict__:\n")
          out.write("    process.Level1MenuOverride.connect  = 'frontier://FrontierProd/CMS_COND_31X_L1T'\n")
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
        out.write("if 'hltPreDQMSmart' in process.__dict__:\n")
        out.write("    process.hltPreDQMSmart.TriggerResultsTag     = cms.InputTag( 'TriggerResults','',process.name_() )\n")
        out.write("\n")
        out.write("process.options.wantSummary = cms.untracked.bool(True)\n")
        out.write("process.MessageLogger.categories.append('TriggerSummaryProducerAOD')\n")
        out.write("process.MessageLogger.categories.append('L1GtTrigReport')\n")
        out.write("process.MessageLogger.categories.append('HLTrigReport')\n")

        # close the output file
        out.close()


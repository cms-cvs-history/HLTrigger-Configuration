#!/usr/bin/env python

import sys
import os
import commands
import getopt
import fileinput

globalTag = {
  '8E29': 'STARTUP31X_V6::All',
  'GRun': 'STARTUP31X_V6::All',
  '1E31': 'MC_31X_V7::All',
  'HIon': 'MC_31X_V7::All',
  None:   'MC_31X_V7::All'              # use as default
}

def usage():
    print 'Usage:'
    print '  getHLT.py <Version from ConfDB> <Id in file name> [use case]'
    print
    print 'If use case "GEN-HLT" is specified, generate a stripped file fragment for the GEN-HLT workflow.'
    print 'If use case "ONLINE" is specified, generate a full configuration file with minimal modifications, for validation.'
    print 'If no use case is specified, the default is "ONLINE".'

argc = len(sys.argv)

try:
    configName  = sys.argv[1]
    fileId      = sys.argv[2]
    processName = 'HLT' + fileId
except:
    usage()
    sys.exit(1)

try:
    useCase = sys.argv[3]
except:
    useCase = "ONLINE"

if useCase == "ONLINE":
    outName = "OnLine_HLT_" + fileId + ".py"
else:
    outName = "HLT_" + fileId + "_cff.py"


if os.path.exists(outName):
    print outName, "already exists - abort!"
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

    if useCase == "GEN-HLT":
        edsources =  " --noedsources"

        essources  = " --essources "
        essources += "-SiStripQualityFakeESSource,"
        essources += "-GlobalTag,"
        essources += "-HepPDTESSource,"
        essources += "-XMLIdealGeometryESSource,"
        essources += "-eegeom,"
        essources += "-es_hardcode,"
        essources += "-magfield"

        esmodules  = " --esmodules "
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
        esmodules += "-StripCPEfromTrackAngleESProducer,"
        esmodules += "-TrackerDigiGeometryESModule,"
        esmodules += "-TrackerGeometricDetESModule,"
        esmodules += "-VolumeBasedMagneticFieldESProducer,"    
        esmodules += "-ZdcHardcodeGeometryEP,"
        esmodules += "-hcal_db_producer,"
        esmodules += "-l1GtTriggerMenuXml,"
        esmodules += "-L1GtTriggerMaskAlgoTrigTrivialProducer,"
        esmodules += "-sistripconn"

        services   = " --services -PrescaleService,-MessageLogger,-DQM,-DQMStore,-FUShmDQMOutputService,-MicroStateService,-ModuleWebRegistry,-TimeProfilerService"

        paths      = " --paths -HLTOutput,-AlCaOutput,-ESOutput,-MONOutput,-OfflineOutput"

        psets      = " --psets -maxEvents,-options"


        myGet = "edmConfigFromDB --cff --configName " + configName + edsources + essources + esmodules + modules + services + paths + psets + " > " + outName
        os.system(myGet)

        # FIXME - this should be done by edmConfigFromDB - remove the definition of streams and primary datasets from the dump
        os.system("sed -e'/^streams/,/^)/d' -e'/^datasets/,/^)/d' -i " + outName)

        # FIXME - this should be done looking into the python objects, not working on the text representation
        os.system("sed -e 's/cms.InputTag( \"source\" )/cms.InputTag( \"rawDataCollector\" )/' -i " + outName)
        os.system("sed -e 's/cms.string( \"source\" )/cms.string( \"rawDataCollector\" )/' -i " + outName)

        # FIXME - DTUnpackingModule should not have untracked parameters
        os.system("sed -e'/DTUnpackingModule/a\ \ \ \ inputLabel = cms.untracked.InputTag( \"rawDataCollector\" ),' -i " + outName)

    else:
        edsources =  " --input file:RelVal_DigiL1Raw_"+fileId+".root"

        esmodules  = " --esmodules "
        esmodules += "-l1GtTriggerMenuXml,"
        esmodules += "-L1GtTriggerMaskAlgoTrigTrivialProducer"

        paths      = " --paths -OfflineOutput"

        myGet = "edmConfigFromDB --configName " + configName + edsources + essources + esmodules + modules + services + paths + psets + " > " + outName
        os.system(myGet)

        # FIXME - this should be done by edmConfigFromDB - remove the definition of streams and primary datasets from the dump
        os.system("sed -e'/^process\.streams/,/^)/d' -e'/^process\.datasets/,/^)/d' -i " + outName)

        # FIXME - this should be done looking into the python objects, not working on the text representation
        os.system("sed -e 's/cms.InputTag( \"source\" )/cms.InputTag( \"rawDataCollector\" )/' -i " + outName)
        os.system("sed -e 's/cms.string( \"source\" )/cms.string( \"rawDataCollector\" )/' -i " + outName)

        # FIXME - DTUnpackingModule should not have untracked parameters
        os.system("sed -e'/DTUnpackingModule/a\ \ \ \ inputLabel = cms.untracked.InputTag( \"rawDataCollector\" ),' -i " + outName)

        # FIXME - find a better way to override the output modules
        os.system("sed -e's/process\.hltOutput\(\w\+\) *= *cms\.OutputModule( *\"ShmStreamConsumer\" *,/process.hltOutput\\1 = cms.OutputModule( \"PoolOutputModule\",\\n    fileName = cms.untracked.string( \"output\\1.root\" ),/'  -i " + outName)


#
# Overwrite ProcessName
#
        # open the output file for appending
        out = open(outName, 'a')
        out.write("process.setName_('%s')\n" % processName)
        out.write("process.DQMHLTScalers.triggerResults = cms.InputTag( 'TriggerResults','','%s' )\n" % processName)
        out.write("\n")

#
# Add global options
#
        out.write("process.maxEvents = cms.untracked.PSet(\n")
        out.write("    input = cms.untracked.int32( 100 )\n")
        out.write(")\n")
        out.write("process.options = cms.untracked.PSet(\n")
        out.write("    wantSummary = cms.untracked.bool( True )\n")
        out.write(")\n")
        out.write("\n")

#
# Overwrite GlobalTag
#
        out.write("process.GlobalTag.connect = 'frontier://FrontierProd/CMS_COND_31X_GLOBALTAG'\n")
        try:
          out.write("process.GlobalTag.globaltag = '%s'\n" % globalTag[fileId])
        except:
          out.write("process.GlobalTag.globaltag = '%s'\n" % globalTag[None])
        out.write("\n")

#
# The following is stolen from cmsDriver's ConfigBuilder.py - addCustomise
#
        final_snippet = '\n\n# Automatic addition of the customisation function\n'

        # let python search for that package and do syntax checking at the same time
        packageName = 'HLTrigger/Configuration/customL1THLT_Options'
        package = __import__(packageName)

        # now ask the package for its definition and pick .py instead of .pyc
        customiseFile = open(package.__file__.rstrip("c"), 'r')

        for line in customiseFile:
            if "import FWCore.ParameterSet.Config" in line:
                continue
            final_snippet += line

        # close the customization file
        customiseFile.close()

        final_snippet += '\n\n# End of customisation function definition\n'
        final_snippet += '\nprocess = customise(process)\n'

        out.write(final_snippet)

        out.close()


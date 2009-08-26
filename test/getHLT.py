#!/usr/bin/env python

import sys
import os
import commands
import getopt
import fileinput

def usage():
    print "Usage:"
    print "  ./getHLT.py <Version from ConfDB> <Id in file name> <use case>"
    print "If use case \"GEN-HLT\" is specified, a stripped file is generated"
    print "  for the GEN-HLT workflow."
    print "The default is to extract a file with minimal modifications"
    print "  for validation."

dbName = sys.argv[1]

argc = len(sys.argv)
if argc == 3:
    useCase = "ONLINE"
    outName = "OnLine_HLT_"+sys.argv[2]+".py"
elif argc == 4:
    useCase = sys.argv[3]
    outName = "HLT_"+sys.argv[2]+"_cff.py"
else:
    usage()
    sys.exit(1)

if os.path.exists(outName):
    print outName, "already exists - abort!"
    sys.exit(1)
else:
    # Initialize everything
    essources = "" 
    esmodules = ""
    modules   = ""
    services  = ""
    paths     = ""
    psets     = ""

    if useCase == "GEN-HLT":
        essources = "--essources "
        essources += "-SiStripQualityFakeESSource,"
        essources += "-GlobalTag,"
        essources += "-HepPDTESSource,"
        essources += "-XMLIdealGeometryESSource,"
        essources += "-eegeom,"
        essources += "-es_hardcode,"
        essources += "-magfield"

        esmodules = "--esmodules "
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

        services  += "--services -PrescaleService,-MessageLogger,-DQM,-DQMStore,-FUShmDQMOutputService,-MicroStateService,-ModuleWebRegistry,-TimeProfilerService"

        paths     += "--paths -HLTOutput,-AlCaOutput,-ESOutput,-MONOutput,-OfflineOutput"

        psets     += "--psets -maxEvents,-options"


        myGet = "edmConfigFromDB --cff --configName " + dbName + " " + essources + " " + esmodules + " " + modules + " " + services + " " + paths + " " + psets + " > " + outName
        os.system(myGet)

        # FIXME - this should be done by edmConfigFromDB - remove the definition of streams and primary datasets from the dump
        os.system("sed -e'/^streams/,/^)/d' -e'/^datasets/,/^)/d' -i " + outName)

        # FIXME - this should be done looking into the python objects, not working on the text representation
        os.system("sed -e 's/cms.InputTag( \"source\" )/cms.InputTag( \"rawDataCollector\" )/' -i " + outName)

        # FIXME - DTUnpackingModule should not have untracked parameters
        os.system("sed -e'/DTUnpackingModule/a\ \ \ \ inputLabel = cms.untracked.InputTag( \"rawDataCollector\" ),' -i " + outName)

    else:
        esmodules = "--esmodules "
        esmodules += "-l1GtTriggerMenuXml,"
        esmodules += "-L1GtTriggerMaskAlgoTrigTrivialProducer"

        paths     += "--paths -OfflineOutput"

        myGet = "edmConfigFromDB --input file:RelVal_DigiL1Raw_"+sys.argv[2]+".root" + " --configName " + dbName + " " + essources + " " + esmodules + " " + modules + " " + services + " " + paths + " " + psets + " > " + outName
        os.system(myGet)

        # FIXME - this should be done by edmConfigFromDB - remove the definition of streams and primary datasets from the dump
        os.system("sed -e'/^process\.streams/,/^)/d' -e'/^process\.datasets/,/^)/d' -i " + outName)

        # FIXME - this should be done looking into the python objects, not working on the text representation
        os.system("sed -e 's/cms.InputTag( \"source\" )/cms.InputTag( \"rawDataCollector\" )/' -i " + outName)

        # FIXME - DTUnpackingModule should not have untracked parameters
        os.system("sed -e'/DTUnpackingModule/a\ \ \ \ inputLabel = cms.untracked.InputTag( \"rawDataCollector\" ),' -i " + outName)

        # FIXME - find a better way to override the output modules
        os.system("sed -e's/process\.hltOutput\(\w\+\) *= *cms\.OutputModule( *\"ShmStreamConsumer\" *,/process.hltOutput\\1 = cms.OutputModule( \"PoolOutputModule\",\\n    fileName = cms.untracked.string( \"output\\1.root\" ),/'  -i " + outName)


#
# Overwrite ProcessName
#
        # open the output file for appending
        out = open(outName, 'a')
        out.write("process.setName_('HLT"+sys.argv[2]+"')\n")

#
# Overwrite GlobalTag
#
        if sys.argv[2]=="8E29":
          out.write("process.GlobalTag.globaltag = 'STARTUP31X_V5::All'\n")
        elif sys.argv[2]=="GRun":
          out.write("process.GlobalTag.globaltag = 'STARTUP31X_V5::All'\n")
        elif sys.argv[2]=="1E31":
          out.write("process.GlobalTag.globaltag = 'MC_31X_V5::All'\n")
        elif sys.argv[2]=="HIon":
          out.write("process.GlobalTag.globaltag = 'MC_31X_V5::All'\n")
        else:
          out.write("process.GlobalTag.globaltag = 'MC_31X_V5::All'\n")

#
# The following is stolen from cmsDriver's ConfigBuilder.py - addCustomise
#
        final_snippet = '\n\n# Automatic addition of the customisation function\n'

        # let python search for that package and do syntax checking at the same time
        packageName = 'HLTrigger.Configuration.customL1THLT_Options'
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


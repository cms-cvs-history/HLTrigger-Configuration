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
    sys.exit(1)

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

if os.path.exists(outName):
    print outName, "already exists - abort!"
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
        esmodules += "-sistripconn"

        services  += "--services -MessageLogger,-DQM,-DQMStore,-FUShmDQMOutputService,-MicroStateService,-ModuleWebRegistry,-TimeProfilerService"

        paths     += "--paths -HLTOutput,-AlCaOutput"

        psets     += "--psets -maxEvents,-options"


        myGet = "edmConfigFromDB --cff --configName " + dbName + " " + essources + " " + esmodules + " " + modules + " " + services + " " + paths + " " + psets + " > " + outName
        os.system(myGet)

    else:
    
        myGet = "edmConfigFromDB       --configName " + dbName + " " + essources + " " + esmodules + " " + modules + " " + services + " " + paths + " " + psets + " > " + outName
        os.system(myGet)

#
# Overwrite ProcessName and PoolSource
#
        os.system("cat >> "+outName+" <<EOI\nprocess.setName_('HLT"+sys.argv[2]+"')\nEOI\n")
        os.system("cat >> "+outName+" <<EOI\nprocess.source.fileNames = cms.untracked.vstring('file:RelVal_DigiL1Raw_"+sys.argv[2]+".root')\nEOI\n")

#
# Overwrite GlobalTag
#
        if sys.argv[2]=="8E29":
          os.system("cat >> "+outName+" <<EOI\nprocess.GlobalTag.globaltag = 'STARTUP31X_V5::All'\nEOI\n")
        elif sys.argv[2]=="GRun":
          os.system("cat >> "+outName+" <<EOI\nprocess.GlobalTag.globaltag = 'STARTUP31X_V5::All'\nEOI\n")
        elif sys.argv[2]=="1E31":
          os.system("cat >> "+outName+" <<EOI\nprocess.GlobalTag.globaltag = 'MC_31X_V5::All'\nEOI\n")
        elif sys.argv[2]=="HIon":
          os.system("cat >> "+outName+" <<EOI\nprocess.GlobalTag.globaltag = 'MC_31X_V5::All'\nEOI\n")
        else:
          os.system("cat >> "+outName+" <<EOI\nprocess.GlobalTag.globaltag = 'MC_31X_V5::All'\nEOI\n")

#
# The following is stolen from cmsDriver's ConfigBuilder.py - addCustomise
#

        # let python search for that package and do syntax checking at the same time
        packageName = 'HLTrigger/Configuration/customL1THLT_Options.py'.replace(".py","").replace(".","/")
        package = __import__(packageName)

        # now ask the package for its definition and pick .py instead of .pyc
        customiseFile = package.__file__.rstrip("c")

        final_snippet='\n\n# Automatic addition of the customisation function\n'
        for line in file(customiseFile,'r'):
            if "import FWCore.ParameterSet.Config" in line:
                continue
            final_snippet += line

        final_snippet += '\n\n# End of customisation function definition'
        final_snippet += "\n\nprocess = customise(process)\n"

        os.system("cat >> "+outName+" <<EOI\n"+final_snippet+"EOI\n")
            

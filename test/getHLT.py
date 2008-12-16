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
    essources = "  " 
    esmodules = "  "
    modules   = "  "
    services  = "--services -PrescaleService"
    paths     = "--paths -AlCaOutput"
    psets     = "  "

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

        services  += ",-MessageLogger"

#       paths     += ",-HLTAnalyzerEndpath"

        psets = "--psets "
        psets += "-maxEvents,"
        psets += "-options,"


        myGet = "edmConfigFromDB --cff --configName " + dbName + " " + essources + " " + esmodules + " " + modules + " " + services + " " + paths + " " + psets + " > " + outName
        os.system(myGet)

    else:
    
        myGet = "edmConfigFromDB       --configName " + dbName + " " + essources + " " + esmodules + " " + modules + " " + services + " " + paths + " " + psets + " > " + outName
        os.system(myGet)

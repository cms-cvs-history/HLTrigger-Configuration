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
    outName = "OnLine_HLTFromRaw_"+sys.argv[2]+"_cfg.py"
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
        essources += "-GlobalTag,"
        essources += "-HepPDTESSource,"
        essources += "-L1GtBoardMapsRcdSource,"
        essources += "-L1GtParametersRcdSource,"
        essources += "-L1GtPrescaleFactorsAlgoTrigRcdSource,"
        essources += "-L1GtPrescaleFactorsTechTrigRcdSource,"
        essources += "-L1GtStableParametersRcdSource,"
        essources += "-L1GtTriggerMaskAlgoTrigRcdSource,"
        essources += "-L1GtTriggerMaskTechTrigRcdSource,"
        essources += "-L1GtTriggerMaskVetoAlgoTrigRcdSource,"
        essources += "-L1GtTriggerMaskVetoTechTrigRcdSource,"
        essources += "-L1MuTriggerScalesRcdSource,"
        essources += "-L1MuTriggerPtScaleRcdSource,"
        essources += "-SiStripQualityFakeESSource,"
        essources += "-XMLIdealGeometryESSource,"
        essources += "-eegeom,"
        essources += "-emrcdsrc,"
        essources += "-es_hardcode,"
        essources += "-jetrcdsrc,"
        essources += "-l1CaloGeomRecordSource,"
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
        esmodules += "-L1GctConfigProducers,"
        esmodules += "-L1MuTriggerScales,"
        esmodules += "-L1MuTriggerPtScale,"
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
        esmodules += "-l1CaloGeometry,"
        esmodules += "-l1CaloScales,"
        esmodules += "-l1GtBoardMaps,"
        esmodules += "-l1GtParameters,"
        esmodules += "-l1GtPrescaleFactorsAlgoTrig,"
        esmodules += "-l1GtPrescaleFactorsTechTrig,"
        esmodules += "-l1GtStableParameters,"
        esmodules += "-l1GtTriggerMaskAlgoTrig,"
        esmodules += "-l1GtTriggerMaskTechTrig,"
        esmodules += "-l1GtTriggerMaskVetoAlgoTrig,"
        esmodules += "-l1GtTriggerMaskVetoTechTrig,"
        esmodules += "-l1GtTriggerMenuXml,"
        esmodules += "-sistripconn"

        services  += ",-MessageLogger"

#       paths     += ",-HLTAnalyzerEndpath"

        psets = "--psets "
        psets += "-maxEvents,"
        psets += "-options,"


        myGet = "edmConfigFromDB --cff --format Python --configName " + dbName + " " + essources + " " + esmodules + " " + modules + " " + services + " " + paths + " " + psets + " > " + outName
        os.system(myGet)

    else:
    
        myGet = "edmConfigFromDB       --format Python --configName " + dbName + " " + essources + " " + esmodules + " " + modules + " " + services + " " + paths + " " + psets + " > " + outName
        os.system(myGet)

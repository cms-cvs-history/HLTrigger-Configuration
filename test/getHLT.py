#!/usr/bin/env python

import sys
import os
import commands
import getopt
import fileinput

def usage():
    print "Usage: ./getHLTcff.py <Version from ConfDB> <Id in file name> <use case>"
    print "If use case \"GEN-HLT\" is specified, a stripped file is generated for the GEN-HLT workflow"
    print "The default is to create file from the ConfDB with minimal modifications for validation"
    sys.exit(1)

dbName = sys.argv[1]

argc = len(sys.argv)
if argc == 3:
    useCase = "ONLINE"
    cffName   = "OnLine_HLTFromRaw_"+sys.argv[2]+".cfg"
    cffNamePy = "OnLine_HLTFromRaw_"+sys.argv[2]+"_cfg.py"
elif argc == 4:
    useCase = sys.argv[3]
    cffName   = "HLT_"+sys.argv[2]+".cff"
    cffNamePy = "HLT_"+sys.argv[2]+"_cff.py"
else:
    usage()

if os.path.exists(cffName):
    print cffName, "already exists"
elif os.path.exists(cffNamePy):
    print cffNamePy, "already exists"
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

        psets = "--psets "
        psets += "-maxEvents,"
        psets += "-options,"

        myGetCff = "edmConfigFromDB --cff --configName " + dbName + " " + essources + " " + esmodules + " " + modules + " " + services + " " + paths + " " + psets + " > " + cffName
        os.system(myGetCff)

        myGetCffPy = "edmConfigFromDB --cff --format Python --cff --configName " + dbName + " " + essources + " " + esmodules + " " + modules + " " + services + " " + paths + " " + psets + " > " + cffNamePy
        os.system(myGetCffPy)

    else:
    
        myGetCff = "edmConfigFromDB       --configName " + dbName + " " + essources + " " + esmodules + " " + modules + " " + services + " " + paths + " " + psets + " > " + cffName
        os.system(myGetCff)

        myGetCffPy = "edmConfigFromDB       --format Python --cff --configName " + dbName + " " + essources + " " + esmodules + " " + modules + " " + services + " " + paths + " " + psets + " > " + cffNamePy
        os.system(myGetCffPy)

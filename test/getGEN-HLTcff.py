#!/usr/bin/env python

# Usage: ./getGEN-HLTcff.py <Version from ConfDB> <Name of cff file> <process Name>

import sys
import os
import commands
import getopt

def usage():
    print "Usage: ./getGEN-HLTcff.py <Version from ConfDB> <Name of cff> <optional process name>" 
    sys.exit(1)

argc = len(sys.argv)

if argc == 3:
    dbName = sys.argv[1]
    cffName = sys.argv[2]
    process = "TriggerResults::HLT"
elif argc == 4:
    dbName = sys.argv[1]
    cffName = sys.argv[2]
    process = "TriggerResults::" + sys.argv[3]
else:
    usage()

if os.path.exists(cffName):
    print cffName, "already exists"
else:
    essources = "--essources "
    essources += "BTagRecord,"
    essources += "DummyCorrector," 
    essources += "MCJetCorrectorIcone5," 
    essources += "MCJetCorrectorIcone7," 
    essources += "MCJetCorrectorMcone5," 
    essources += "MCJetCorrectorMcone7," 
    essources += "MCJetCorrectorScone5," 
    essources += "MCJetCorrectorScone7," 
    essources += "MCJetCorrectorktjet4," 
    essources += "MCJetCorrectorktjet6"

    esmodules = "--esmodules "
    esmodules += "-CSCGeometryESModule,"
    esmodules += "-EcalBarrelGeometryEP,"
    esmodules += "-EcalEndcapGeometryEP,"
    esmodules += "-EcalPreshowerGeometryEP,"
    esmodules += "-HcalHardcodeGeometryEP,"
    esmodules += "-ZdcHardcodeGeometryEP,"
    esmodules += "-CaloTowerHardcodeGeometryEP,"
    esmodules += "-CaloGeometryBuilder,"
    esmodules += "-DTGeometryESModule,"
    esmodules += "-RPCGeometryESModule,"
    esmodules += "-EcalElectronicsMappingBuilder,"
    esmodules += "-EcalLaserCorrectionService,"
    esmodules += "-EcalTrigPrimESProducer,"
    esmodules += "-EcalTrigTowerConstituentsMapBuilder,"
    esmodules += "-L1GctConfigProducers,"
    esmodules += "-L1MuGMTScales,"
    esmodules += "-L1MuTriggerScales,"
    esmodules += "-MuonNumberingInitialization,"
    esmodules += "-SiStripGainESProducer,"
    esmodules += "-SiStripRecHitMatcherESProducer,"
    esmodules += "-StripCPEfromTrackAngleESProducer,"
    esmodules += "-TrackerDigiGeometryESModule,"
    esmodules += "-TrackerGeometricDetESModule,"
    esmodules += "-VolumeBasedMagneticFieldESProducer,"
    esmodules += "-hcal_db_producer,"
    esmodules += "-l1CaloGeometry,"
    esmodules += "-l1CaloScales,"
    esmodules += "-l1GtBoardMaps,"
    esmodules += "-l1GtFactors,"
    esmodules += "-l1GtParameters,"
    esmodules += "-l1GtStableParameters,"
    esmodules += "-l1GtTriggerMenuXml,"
    esmodules += "-sistripconn"

    services = "--services "
    services += "-MessageLogger"

    psets = "--psets "
    psets += "-maxEvents,"
    psets += "-configurationMetadata,"
    psets += "-options,"

    myGetCff = "edmConfigFromDB --cff --configName " + dbName + " " + essources + " " + esmodules + " " + services + " " + psets + " > " + cffName
    os.system(myGetCff)

    myReplaceTrigResults = "replace TriggerResults::HLT " + process + " -- " + cffName
    os.system(myReplaceTrigResults)



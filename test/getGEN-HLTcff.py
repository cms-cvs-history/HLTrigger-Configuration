#!/usr/bin/env python

# Usage: ./getGEN-HLTcff.py <Version from ConfDB> <Name of cff file> <process Name>

import sys
import os
import commands
import getopt
import fileinput

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
    essources += "-trackerAlignment,"
    essources += "-muonAlignment,"
    essources += "-siPixelGainCalibration,"
    essources += "-siPixelCabling,"
    essources += "-siPixelLorentzAngle,"
    essources += "-siStripApvGain,"
    essources += "-siStripNoise,"
    essources += "-siStripLorentzAngle,"
    essources += "-siStripFedCabling,"
    essources += "-SiStripPedestalsFakeESSource,"
    essources += "-maps_frontier,"
    essources += "-cscConditions,"
    essources += "-es_pool,"
    essources += "-es_hardcode,"
    essources += "-ecalConditions,"
    essources += "-trackProbabilityFrontierCond,"
    essources += "-BTauMVAJetTagComputerRecord,"
    essources += "-BeamSpotEarlyCollision,"
    essources += "-DTCabling,"
    essources += "-RPCCabling,"
    essources += "-cscPackingCabling,"
    essources += "-cscUnpackingCabling,"
    essources += "-GlobalPosition,"
    essources += "-HepPDTESSource,"
    essources += "-L1GtBoardMapsRcdSource,"
    essources += "-L1GtParametersRcdSource,"
    essources += "-L1GtPrescaleFactorsAlgoTrigRcdSource,"
    essources += "-L1GtPrescaleFactorsRcdSource,"
    essources += "-L1GtPrescaleFactorsTechTrigRcdSource,"
    essources += "-L1GtStableParametersRcdSource,"
    essources += "-L1GtTriggerMaskAlgoTrigRcdSource,"
    essources += "-L1GtTriggerMaskRcdSource,"
    essources += "-L1GtTriggerMaskTechTrigRcdSource,"
    essources += "-L1GtTriggerMaskVetoAlgoTrigRcdSource,"
    essources += "-L1GtTriggerMaskVetoTechTrigRcdSource,"
    essources += "-L1GtTriggerMenuRcdSource,"
    essources += "-L1MuGMTScalesRcdSource,"
    essources += "-L1MuTriggerScalesRcdSource,"
    essources += "-eegeom,"
    essources += "-emrcdsrc,"
    essources += "-jetrcdsrc,"
    essources += "-l1CaloGeomRecordSource,"
    essources += "-l1GctConfigRecords,"
    essources += "-l1GctJcNegParsRecords,"
    essources += "-l1GctJcPosParsRecords,"
    essources += "-l1GctParamsRecords,"
    essources += "-tpparams,"
    essources += "-tpparams2,"
    essources += "-tpparams3,"
    essources += "-tpparams4,"
    essources += "-tpparams5,"
    essources += "-tpparams6,"
    essources += "-tpparams7,"
    essources += "-tpparams8,"
    essources += "-tpparams9,"
    essources += "-tpparams10,"
    essources += "-tpparams11,"
    essources += "-magfield,"
    essources += "-XMLIdealGeometryESSource"

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
    esmodules += "-hcal_db_producer,"
    esmodules += "-l1CaloGeometry,"
    esmodules += "-l1CaloScales,"
    esmodules += "-l1GtBoardMaps,"
    esmodules += "-l1GtFactors,"
    esmodules += "-l1GtParameters,"
    esmodules += "-l1GtStableParameters,"
    esmodules += "-l1GtTriggerMenuXml,"
    esmodules += "-sistripconn,"
    # 200pre6 additions
    esmodules += "-TrackerDigiGeometryESModule,"
    esmodules += "-TrackerGeometricDetESModule,"
    esmodules += "-VolumeBasedMagneticFieldESProducer,"
    esmodules += "-l1GtPrescaleFactorsAlgoTrig,"
    esmodules += "-l1GtPrescaleFactorsTechTrig,"
    esmodules += "-l1GtTriggerMaskAlgoTrig,"
    esmodules += "-l1GtTriggerMaskTechTrig,"
    esmodules += "-l1GtTriggerMaskVetoAlgoTrig,"
    esmodules += "-l1GtTriggerMaskVetoTechTrig,"
    esmodules += "-HcalTopologyIdealEP"
    
    modules = "--modules -hltTriggerSummaryAOD"
    paths   = "--paths -AlCaIsoTrack,-AlCaEcalPi0,-HLT1MuonTrackerNonIso"

    services = "--services "
    services += "-PrescaleService,"
    services += "-MessageLogger"

    psets = "--psets "
    psets += "-maxEvents,"
    psets += "-configurationMetadata,"
    psets += "-options,"

    myGetCff = "edmConfigFromDB --cff --configName " + dbName + " " + essources + " " + esmodules + " " + paths + " " + modules + " " + services + " " + psets + " > " + cffName
    os.system(myGetCff)

    myReplaceTrigResults = "replace TriggerResults::HLT " + process + " -- " + cffName
    os.system(myReplaceTrigResults)

    # Make replace statements at the beginning of the cff
    for line in fileinput.input(cffName,inplace=1):
        if line.find("sequence HLTBeginSequence") >= 0:
            print "// Begin replace statements specific to the HLT"
            print "include \"HLTrigger/Configuration/data/HLTrigger_EventContent.cff\""
            print "module hltTriggerSummaryAOD = TriggerSummaryProducerAOD {"
            print "  string processName = \"@\""
            print "  using TriggerSummaryAOD"
            print "}"
            print "// End replace statements specific to the HLT"  
        print line[:-1]

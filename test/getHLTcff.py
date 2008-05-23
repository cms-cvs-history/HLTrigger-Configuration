#!/usr/bin/env python

# Usage: ./getHLTcff.py <Version from ConfDB> <Name of cff file> <process Name>

import sys
import os
import commands
import getopt
import fileinput

def usage():
    print "Usage: ./getHLTcff.py <Version from ConfDB> <Name of cff> <cff use case>"
    print "If \"GEN-HLT\" is specified for cff use case, a stripped HLT.cff is generated for the GEN-HLT workflow"
    print "The default is to create an HLT.cff from the ConfDB with minimal modifications for validation"
    sys.exit(1)

argc = len(sys.argv)

useCase = "ONLINE"
if argc == 3:
    dbName = sys.argv[1]
    cffName = sys.argv[2]
elif argc == 4:
    dbName = sys.argv[1]
    cffName = sys.argv[2]
    useCase = sys.argv[3]
else:
    usage()

if os.path.exists(cffName):
    print cffName, "already exists"
else:
    # Initialize everything
    essources = "  " 
    esmodules = "  " 

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

    #essources += "-trackerAlignment,"
    #essources += "-muonAlignment,"
    #essources += "-siPixelGainCalibration,"
    #essources += "-siPixelCabling,"
    #essources += "-siPixelLorentzAngle,"
    #essources += "-siStripApvGain,"
    #essources += "-siStripNoise,"
    #essources += "-siStripLorentzAngle,"
    #essources += "-siStripFedCabling,"
    #essources += "-SiStripPedestalsFakeESSource,"
    #essources += "-maps_frontier,"
    #essources += "-cscConditions,"
    #essources += "-es_pool,"
    #essources += "-ecalConditions,"
    #essources += "-trackProbabilityFrontierCond,"
    #essources += "-BTauMVAJetTagComputerRecord,"
    #essources += "-BeamSpotEarlyCollision,"
    #essources += "-DTCabling,"
    #essources += "-RPCCabling,"
    #essources += "-cscPackingCabling,"
    #essources += "-cscUnpackingCabling,"
    #essources += "-GlobalPosition,"


    #essources += "-L1GtPrescaleFactorsRcdSource,"
    #essources += "-L1GtTriggerMaskRcdSource,"
    #essources += "-L1GtTriggerMenuRcdSource,"
    #essources += "-L1MuGMTScalesRcdSource,"
    #essources += "-l1GctConfigRecords,"
    #essources += "-l1GctJcNegParsRecords,"
    #essources += "-l1GctJcPosParsRecords,"
    #essources += "-l1GctParamsRecords,"
    #essources += "-tpparams,"
    #essources += "-tpparams2,"
    #essources += "-tpparams3,"
    #essources += "-tpparams4,"
    #essources += "-tpparams5,"
    #essources += "-tpparams6,"
    #essources += "-tpparams7,"
    #essources += "-tpparams8,"
    #essources += "-tpparams9,"
    #essources += "-tpparams10,"
    #essources += "-tpparams11,"



    #esmodules += "-EcalTrigPrimESProducer,"
    #esmodules += "-EcalTrigTowerConstituentsMapBuilder,"
    #esmodules += "-L1MuGMTScales,"
    #esmodules += "-l1GtFactors,"
    # 200pre6 additions

    modules = "  " # "--modules -hltTriggerSummaryAOD"

    services = "--services "
    services += "-PrescaleService,"
    services += "-MessageLogger"

    psets = "--psets "
    psets += "-maxEvents,"
    psets += "-configurationMetadata,"
    psets += "-options,"

    myGetCff = "edmConfigFromDB --cff --configName " + dbName + " " + essources + " " + esmodules + " " + modules + " " + services + " " + psets + " > " + cffName
    os.system(myGetCff)

    # myReplaceTrigResults = "replace TriggerResults::HLT " + process + " -- " + cffName
    # os.system(myReplaceTrigResults)

    # Make replace statements at the beginning of the cff
    for line in fileinput.input(cffName,inplace=1):
        if line.find("sequence HLTBeginSequence") >= 0:
            print "// Begin replace statements specific to the HLT"
            print "#"
            print "// End replace statements specific to the HLT"  
        print line[:-1]

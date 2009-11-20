#! /bin/bash

./getHLT.py --process TEST --full --offline --mc   /online/beamhalo/week47/HLT TEST
./getHLT.py --process TEST --full --online  --data /online/beamhalo/week47/HLT TEST
./getHLT.py --process TEST --full --offline --data /online/beamhalo/week47/HLT TEST

#! /bin/bash

HLT='orcoff:/cdaq/special/CirculatingBeam09/v3.0/HLT/V1'

rm -f OnLine_HLT_TEST.py

./getHLT.py --process TEST --full --offline --mc   "$HLT" TEST
mv OnLine_HLT_TEST.py offline_mc.py
./getHLT.py --process TEST --full --offline --data "$HLT" TEST
mv OnLine_HLT_TEST.py offline_data.py
./getHLT.py --process TEST --full --online  --data "$HLT" TEST
mv OnLine_HLT_TEST.py online_data.py

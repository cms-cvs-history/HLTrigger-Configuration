#!/bin/tcsh

cmsenv

rehash

echo " "
echo "Existing cfg files:"
ls -l OnData*.py
ls -l OnLine*.py

echo " "
echo "Creating offline configs with cmsDriver"
echo "./cmsDriver.sh"
time  ./cmsDriver.sh

echo " "
echo "Running selected configs"

foreach gtag ( STARTUP MC )

  foreach task ( RelVal_DigiL1Raw )
    echo " "
    set name = ${task}_${gtag}
    foreach ext (log root)
      /bin/rm $name.$ext
    end
cat >> $name.py <<EOF
# override the L1 menu
if 'GlobalTag' in process.__dict__:
    process.GlobalTag.toGet = cms.VPSet( )
    process.GlobalTag.toGet.append(
        cms.PSet(  
            record  = cms.string( "L1GtTriggerMenuRcd" ),
            tag     = cms.string( "L1GtTriggerMenu_L1Menu_Commissioning2010_v4_mc" ),
            connect = cms.untracked.string( "sqlite_file:/afs/cern.ch/user/g/ghete/public/L1Menu/sqlFile/L1Menu_Commissioning2010_v4_mc.db" )
        )
    )
EOF
    echo "cmsRun $name.py >& $name.log"
    time  cmsRun $name.py >& $name.log
#   link to input file for subsequent OnLine* step
    if ( $gtag == STARTUP ) then
      foreach table ( GRun HIon )
        ln -s RelVal_DigiL1Raw_${gtag}.root RelVal_DigiL1Raw_${table}.root
      end
    endif
  end

  foreach table ( GRun HIon )
    if ( $gtag == STARTUP ) then
      foreach task ( OnData_HLT OnLine_HLT )
        echo " "
        set name = ${task}_${table}
        foreach ext (log root)
          /bin/rm $name.$ext
        end
cat >> $name.py <<EOF
# override the L1 menu
if 'GlobalTag' in process.__dict__:
    process.GlobalTag.toGet = cms.VPSet( )
    process.GlobalTag.toGet.append(
        cms.PSet(  
            record  = cms.string( "L1GtTriggerMenuRcd" ),
            tag     = cms.string( "L1GtTriggerMenu_L1Menu_Commissioning2010_v4_mc" ),
            connect = cms.untracked.string( "sqlite_file:/afs/cern.ch/user/g/ghete/public/L1Menu/sqlFile/L1Menu_Commissioning2010_v4_mc.db" )
        )
    )
EOF
        echo "cmsRun $name.py >& $name.log"
        time  cmsRun $name.py >& $name.log
      end
    endif

    foreach task ( RelVal_HLT RelVal_HLT2 )
      echo " "
      set name = ${task}_${table}_${gtag}
      foreach ext (log root)
        /bin/rm $name.$ext
      end
cat >> $name.py <<EOF
# override the L1 menu
if 'GlobalTag' in process.__dict__:
    process.GlobalTag.toGet = cms.VPSet( )
    process.GlobalTag.toGet.append(
        cms.PSet(  
            record  = cms.string( "L1GtTriggerMenuRcd" ),
            tag     = cms.string( "L1GtTriggerMenu_L1Menu_Commissioning2010_v4_mc" ),
            connect = cms.untracked.string( "sqlite_file:/afs/cern.ch/user/g/ghete/public/L1Menu/sqlFile/L1Menu_Commissioning2010_v4_mc.db" )
        )
    )
EOF
      echo "cmsRun $name.py >& $name.log"
      time  cmsRun $name.py >& $name.log
    end

  end

end

foreach gtag ( STARTUP MC )
  foreach task ( RelVal_Reco )
    echo " "
    set name = ${task}_${gtag}
    foreach ext (log root)
      /bin/rm $name.$ext
    end
cat >> $name.py <<EOF
# override the L1 menu
if 'GlobalTag' in process.__dict__:
    process.GlobalTag.toGet = cms.VPSet( )
    process.GlobalTag.toGet.append(
        cms.PSet(  
            record  = cms.string( "L1GtTriggerMenuRcd" ),
            tag     = cms.string( "L1GtTriggerMenu_L1Menu_Commissioning2010_v4_mc" ),
            connect = cms.untracked.string( "sqlite_file:/afs/cern.ch/user/g/ghete/public/L1Menu/sqlFile/L1Menu_Commissioning2010_v4_mc.db" )
        )
    )
EOF
    echo "cmsRun $name.py >& $name.log"
    time  cmsRun $name.py >& $name.log
  end
end

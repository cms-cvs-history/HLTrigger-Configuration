# checkHLTpaths/Makefile
# 
# This makefile checks that each trigger path gives the same results if run stand-alone or in the global trigger table.
# Given a configName, it extracts from ConfDB the global table (Global_Table.py), the list of path, and a configuration 
# for each path (TriggerName.py).
# Then both the trigger table and each paths are run, the corresponding TrigReport is extracted from the log, and compared.
# 
# run "make help" to get synopsis.
#
# Version 1.3.2, 2009.08.18
# Andrea Bocci <andrea.bocci@cern.ch>

.PHONY: all list clean summary help

# configuration goes here
PROCESS := HLT
EVENTS  := 100

HLT_8E29_CONFIG     := /dev/CMSSW_3_2_2/8E29/V1
HLT_8E29_GLOBALTAG  := STARTUP31X_V4::All
HLT_8E29_SOURCE     := file:RelVal_DigiL1Raw_8E29.root

HLT_1E31_CONFIG     := /dev/CMSSW_3_2_2/1E31/V1
HLT_1E31_GLOBALTAG  := MC_31X_V5::All
HLT_1E31_SOURCE     := file:RelVal_DigiL1Raw_1E31.root

# more configuration, useful for debug the Makefile itself
CMSRUN := cmsRun
GETCONFIG := edmConfigFromDB

# check for cmsRun environmnt
ifeq (,$(CMSSW_RELEASE_BASE))
  $(error Please configure the cmsRun environment with the 'cmsenv' command)
endif

# internal stuff
NORMAL:= \033[0m
BOLD  := \033[1m
RED   := \033[31m
GREEN := \033[32m
YELLOW:= \033[33m
BLUE  := \033[34m
COLUMN:= \033[100G

LIST_OF_8E29_PATHS:= $(shell edmConfigFromDB --configName $(HLT_8E29_CONFIG) --nopsets --noedsources --noes --noservices --nooutput --nosequences --nomodules --format python | gawk '/^process\..*(AlCa|HLT)_.* = cms.Path/ { print gensub(/^process\.(.*(AlCa|HLT)_.*) = cms.Path.*/, "\\1", 1) }' | sort)
LIST_OF_8E29_PYS  := $(patsubst %, 8E29_%.py,   $(LIST_OF_8E29_PATHS))
LIST_OF_8E29_LOGS := $(patsubst %, 8E29_%.log,  $(LIST_OF_8E29_PATHS))
LIST_OF_8E29_DIFFS:= $(patsubst %, 8E29_%.diff, $(LIST_OF_8E29_PATHS))

LIST_OF_1E31_PATHS:= $(shell edmConfigFromDB --configName $(HLT_1E31_CONFIG) --nopsets --noedsources --noes --noservices --nooutput --nosequences --nomodules --format python | gawk '/^process\..*(AlCa|HLT)_.* = cms.Path/ { print gensub(/^process\.(.*(AlCa|HLT)_.*) = cms.Path.*/, "\\1", 1) }' | sort)
LIST_OF_1E31_PYS  := $(patsubst %, 1E31_%.py,   $(LIST_OF_1E31_PATHS))
LIST_OF_1E31_LOGS := $(patsubst %, 1E31_%.log,  $(LIST_OF_1E31_PATHS))
LIST_OF_1E31_DIFFS:= $(patsubst %, 1E31_%.diff, $(LIST_OF_1E31_PATHS))

LIST_OF_PATHS:= $(shell echo $(LIST_OF_8E29_PATHS) $(LIST_OF_1E31_PATHS) | xargs -n1 echo | sort -u)
LIST_OF_PYS  := $(LIST_OF_8E29_PYS)   $(LIST_OF_1E31_PYS)
LIST_OF_LOGS := $(LIST_OF_8E29_LOGS)  $(LIST_OF_1E31_LOGS)
LIST_OF_DIFFS:= $(LIST_OF_8E29_DIFFS) $(LIST_OF_1E31_DIFFS)

.PHONY: $(LIST_OF_PATHS)

all:    pys logs diffs summary

pys:    8E29_GlobalTable.py   1E31_GlobalTable.py   $(LIST_OF_PYS)

logs:   8E29_GlobalTable.log  1E31_GlobalTable.log  $(LIST_OF_LOGS)

diffs:  8E29_GlobalTable.diff 1E31_GlobalTable.diff $(LIST_OF_DIFFS)

clean:
	@rm -f .database_* .dataset_* *.py *.pyc *.log *.diff HLT*.root AlCa*.root
  
list: 
	@echo "$(LIST_OF_PATHS)"

summary:
	@echo
	@DIFF=`ls *.diff | sed -e's/\.diff$$//'`; \
	if [ -z "$$DIFF" ]; then \
	  echo "No discrepancies found."; \
	else \
	  echo "Found discrepancies in the trigger paths:" ;\
	  for P in $$DIFF; do echo -e "\t$(RED)$$P$(NORMAL)"; done; \
	  echo; \
	fi
	@DIFF=`ls *.diff | sed -e's/\.diff$$//'`; \
	PARTIAL=$$(gawk 'FNR==1 { NAME=gensub(/(.*)\.log/,"\\1",1,FILENAME); HEADER="TrigReport ---------- Modules in Path: "NAME" ------------"; } $$0 ~ HEADER { while ($$0 !~ /TrigReport.*hltBoolEnd/) getline; if ($$5 == 0) print NAME; nextfile; }' *_*.log); \
        PARTIAL=$$(for P in $$PARTIAL; do echo $$DIFF | grep -q $$P || echo $$P; done); \
	if [ -z "$$PARTIAL" ]; then \
	  echo "All paths where fully excercised."; \
	else \
	  echo "These paths where not fully excercised:"; \
	  for P in $$PARTIAL; do echo -e "\t$(YELLOW)$$P$(NORMAL)"; done; \
	  echo; \
	fi

# these are kinda tricky: we need rules based on the file content, not on its modification date
DB_8E29_NEW:=$(shell echo -e "CONFIG=$(HLT_8E29_CONFIG)\nSOURCE=$(HLT_8E29_SOURCE)\nGLOBALTAG=$(HLT_8E29_GLOBALTAG)" | md5sum | cut -c -32)
DB_8E29_SUM:=$(shell [ -f .database_8E29 ] && cat .database_8E29 | md5sum | cut -c -32)

ifneq ($(DB_8E29_NEW), $(DB_8E29_SUM))
.database_8E29:
	@echo -e "CONFIG=$(HLT_8E29_CONFIG)\nSOURCE=$(HLT_8E29_SOURCE)\nGLOBALTAG=$(HLT_8E29_GLOBALTAG)" > .database_8E29
endif

DB_1E31_NEW:=$(shell echo -e "CONFIG=$(HLT_1E31_CONFIG)\nSOURCE=$(HLT_1E31_SOURCE)\nGLOBALTAG=$(HLT_1E31_GLOBALTAG)" | md5sum | cut -c -32)
DB_1E31_SUM:=$(shell [ -f .database_1E31 ] && cat .database_1E31 | md5sum | cut -c -32)

ifneq ($(DB_1E31_NEW), $(DB_1E31_SUM))
.database_1E31:
	@echo -e "CONFIG=$(HLT_1E31_CONFIG)\nSOURCE=$(HLT_1E31_SOURCE)\nGLOBALTAG=$(HLT_1E31_GLOBALTAG)" > .database_1E31
endif

# end of tricky rules

8E29_GlobalTable.py: .database_8E29
	@echo -e " ConfDB [$(BLUE)$(HLT_8E29_CONFIG)$(NORMAL)] menu $(BOLD)8E29_GlobalTable$(NORMAL)"
	@$(GETCONFIG) --configName $(HLT_8E29_CONFIG) --input $(HLT_8E29_SOURCE) --nooutput --services -PrescaleService --format python | sed -e's/^process = cms.Process(.*)/process = cms.Process( "$(PROCESS)" )/' -e's/^process.maxEvents = cms.untracked.PSet(  input = cms.untracked.int32( $(EVENTS) ) )/process.maxEvents = cms.untracked.PSet(  input = cms.untracked.int32( 100 ) )/' > 8E29_GlobalTable.py
	@echo -e "process.GlobalTag.globaltag = \"$(HLT_8E29_GLOBALTAG)\"" >> 8E29_GlobalTable.py

1E31_GlobalTable.py: .database_1E31
	@echo -e " ConfDB [$(BLUE)$(HLT_1E31_CONFIG)$(NORMAL)] menu $(BOLD)1E31_GlobalTable$(NORMAL)"
	@$(GETCONFIG) --configName $(HLT_1E31_CONFIG) --input $(HLT_1E31_SOURCE) --nooutput --services -PrescaleService --format python | sed -e's/^process = cms.Process(.*)/process = cms.Process( "$(PROCESS)" )/' -e's/^process.maxEvents = cms.untracked.PSet(  input = cms.untracked.int32( $(EVENTS) ) )/process.maxEvents = cms.untracked.PSet(  input = cms.untracked.int32( 100 ) )/' > 1E31_GlobalTable.py
	@echo -e "process.GlobalTag.globaltag = \"$(HLT_1E31_GLOBALTAG)\"" >> 1E31_GlobalTable.py

8E29_GlobalTable.log: 8E29_GlobalTable.py
	@echo -n "running 8E29 Global Table"
	@$(CMSRUN) 8E29_GlobalTable.py >& 8E29_GlobalTable.log
	@echo -e "$(COLUMN)$(GREEN)done$(NORMAL)"

1E31_GlobalTable.log: 1E31_GlobalTable.py
	@echo -n "running 1E31 Global Table"
	@$(CMSRUN) 1E31_GlobalTable.py >& 1E31_GlobalTable.log
	@echo -e "$(COLUMN)$(GREEN)done$(NORMAL)"

$(LIST_OF_8E29_PYS): %.py: .database_8E29
	@echo -e " ConfDB [$(BLUE)$(HLT_8E29_CONFIG)$(NORMAL)] path $(BOLD)$*$(NORMAL)"
	@$(GETCONFIG) --configName $(HLT_8E29_CONFIG) --input $(HLT_8E29_SOURCE) --paths HLTriggerFirstPath,$*,HLTriggerFinalPath --services -PrescaleService --format python | sed -e's/^process = cms.Process(.*)/process = cms.Process( "$(PROCESS)" )/' -e's/^process.maxEvents = cms.untracked.PSet(  input = cms.untracked.int32( $(EVENTS) ) )/process.maxEvents = cms.untracked.PSet(  input = cms.untracked.int32( 100 ) )/' > $@
	@echo -e "process.GlobalTag.globaltag = \"$(HLT_8E29_GLOBALTAG)\"" >> $@

$(LIST_OF_1E31_PYS): %.py: .database_1E31
	@echo -e " ConfDB [$(BLUE)$(HLT_1E31_CONFIG)$(NORMAL)] path $(BOLD)$*$(NORMAL)"
	@$(GETCONFIG) --configName $(HLT_1E31_CONFIG) --input $(HLT_1E31_SOURCE) --paths HLTriggerFirstPath,$*,HLTriggerFinalPath --services -PrescaleService --format python | sed -e's/^process = cms.Process(.*)/process = cms.Process( "$(PROCESS)" )/' -e's/^process.maxEvents = cms.untracked.PSet(  input = cms.untracked.int32( $(EVENTS) ) )/process.maxEvents = cms.untracked.PSet(  input = cms.untracked.int32( 100 ) )/' > $@
	@echo -e "process.GlobalTag.globaltag = \"$(HLT_1E31_GLOBALTAG)\"" >> $@

$(LIST_OF_LOGS): %.log: %.py
	@echo -n "running trigger path $*"
	@$(CMSRUN) $< >& $@
	@if gawk '/TrigReport ---------- Modules in Path: $* ------------/ { while ($$0 !~ /TrigReport.*hltBoolEnd/) getline; if ($$5 == 0) exit 1; else exit 0; }' $*.log; then echo -e "$(COLUMN)$(GREEN)done$(NORMAL)"; else echo -e "$(COLUMN)$(YELLOW)warning$(NORMAL)"; fi

$(LIST_OF_PATHS): %: %.diff

$(LIST_OF_8E29_DIFFS): 8E29_GlobalTable.log

$(LIST_OF_1E31_DIFFS): 1E31_GlobalTable.log

$(LIST_OF_8E29_DIFFS): %.diff: %.log
	@echo -n "checking trigger path $*"
	@cat $*.log               | gawk 'BEGIN { FOUND=0 } /TrigReport ---------- Modules in Path: $* ------------/ { FOUND=1; print; getline; print "TrigReport  Trig    Visited     Passed     Failed      Error Name"; next; } /^$$/ {FOUND=0; next; } // { if (FOUND) printf "TrigReport   %3d %10d %10d %10d %10d %s\n",$$2,$$4,$$5,$$6,$$7,$$8 }' > $*.single
	@cat 8E29_GlobalTable.log | gawk 'BEGIN { FOUND=0 } /TrigReport ---------- Modules in Path: $* ------------/ { FOUND=1; print; getline; print "TrigReport  Trig    Visited     Passed     Failed      Error Name"; next; } /^$$/ {FOUND=0; next; } // { if (FOUND) printf "TrigReport   %3d %10d %10d %10d %10d %s\n",$$2,$$4,$$5,$$6,$$7,$$8 }' > $*.full
	@if diff -w -U 999 $*.full $*.single > $*.diff; then \
            rm -f $*.diff; \
            echo -e "$(COLUMN)$(GREEN)done$(NORMAL)"; \
        else \
            echo -e "$(COLUMN)$(RED)error$(NORMAL)"; \
        fi
	@rm -f $*.single $*.full

$(LIST_OF_1E31_DIFFS): %.diff: %.log
	@echo -n "checking trigger path $*"
	@cat $*.log               | gawk 'BEGIN { FOUND=0 } /TrigReport ---------- Modules in Path: $* ------------/ { FOUND=1; print; getline; print "TrigReport  Trig    Visited     Passed     Failed      Error Name"; next; } /^$$/ {FOUND=0; next; } // { if (FOUND) printf "TrigReport   %3d %10d %10d %10d %10d %s\n",$$2,$$4,$$5,$$6,$$7,$$8 }' > $*.single
	@cat 1E31_GlobalTable.log | gawk 'BEGIN { FOUND=0 } /TrigReport ---------- Modules in Path: $* ------------/ { FOUND=1; print; getline; print "TrigReport  Trig    Visited     Passed     Failed      Error Name"; next; } /^$$/ {FOUND=0; next; } // { if (FOUND) printf "TrigReport   %3d %10d %10d %10d %10d %s\n",$$2,$$4,$$5,$$6,$$7,$$8 }' > $*.full
	@if diff -w -U 999 $*.full $*.single > $*.diff; then \
            rm -f $*.diff; \
            echo -e "$(COLUMN)$(GREEN)done$(NORMAL)"; \
        else \
            echo -e "$(COLUMN)$(RED)error$(NORMAL)"; \
        fi
	@rm -f $*.single $*.full

help:
	@echo 'This makefile checks that each trigger path gives the same results if run stand-alone or in the global trigger table.'
	@echo 'Given a configName, it extracts from ConfDB the global table (*.py_GlobalTable), the list of path, and a configuration'
	@echo 'for each path (TriggerName.py).'
	@echo 'Then both the trigger table and each paths are run, the corresponding TrigReport is extracted from the log, and compared.'
	@echo
	@echo 'After running each path, a warning is issued if a path is not fully excersided, i.e. no events pass all the filters.'
	@echo 'After comparing with the global table, an error is issued if there are discrepenaices in the TrigReport (at any level).'
	@echo
	@echo 'Working files:'
	@echo '  .database_LUMI         running conditions: ConfDB configuration, input dataset, GlobalTag'
	@echo '  LUMI_GlobalTable.py    configuration for the global table'
	@echo '  LUMI_GlobalTable.log   output of cmsRun LUMI_GlobalTable.py'
	@echo '  TriggerName.py         configuration for TriggerName path'
	@echo '  TriggerName.log        output of cmsRun TriggerName.py'
	@echo '  TriggerName.diff       differences between TrigReport for TriggerName between global table run and stand-alone run'
	@echo
	@echo 'Supported targets:'
	@echo '  all                    same as "pys logs diffs summary"'
	@echo '  list                   list all trigger paths'
	@echo '  pys                    extract all (python) configuration files'
	@echo '  logs                   run all configuration files'
	@echo '  diffs                  extract all differences'
	@echo '  summary                analyze all *available* diff and log files to print the list of trigger paths with discrepancies and/or with no accepted events'
	@echo '  help                   print a simple description of this tool'
	@echo
	@echo '  TriggerName            run the full chain for trigger TriggerName: extract TriggerName.py, cmsRun logging to TriggerName.log,'
	@echo '                         if necessary extract and run the global table, and compare the TrigResults.'
	@echo
	@echo 'Version 1.3.2, 2009.08.18'
	@echo 'Andrea Bocci <andrea.bocci@cern.ch>'

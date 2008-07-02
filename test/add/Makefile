# checkHLTpaths/Makefile
# 
# This makefile checks that each trigger path gives the same results if run stand-alone or in the global trigger table.
# Given a configName, it extracts from ConfDB the global table (Global_Table.py), the list of path, and a configuration 
# for each path (TriggerName.py).
# Then both the trigger table and each paths are run, the corresponding TrigReport is extracted from the log, and compared.
# 
# run "make help" to get synopsis.
#
# Version 1.2.0, 1/7/2008
# Andrea Bocci <andrea.bocci@cern.ch>

.PHONY: all list clean summary help

# configuration goes here
PROCESS:= HLT
CONFIG := /dev/CMSSW_2_1_0_pre6/HLT/V12
SOURCE := file:$(CMSSW_BASE)/src/HLTrigger/Configuration/test/RelVal_Pure_Raw.root
# /store/relval/2008/6/4/RelVal-RelValTTbar-1212543891-STARTUP-2nd/0000/185E7133-9C32-DD11-BC8E-001617E30CC8.root
EVENTS := 100

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

LIST_OF_PATHS:= $(shell edmConfigFromDB --configName $(CONFIG) --nopsets --noedsources --noes --noservices --nooutput --nosequences --nomodules --format python | gawk '/^process\..*(AlCa|HLT)_.* = cms.Path/ { print gensub(/^process\.(.*(AlCa|HLT)_.*) = cms.Path.*/, "\\1", 1) }' | sort)
LIST_OF_PYS  := $(patsubst %, %.py, $(LIST_OF_PATHS))
LIST_OF_LOGS := $(patsubst %, %.log, $(LIST_OF_PATHS))
LIST_OF_DIFFS:= $(patsubst %, %.diff, $(LIST_OF_PATHS))

.PHONY: $(LIST_OF_PATHS)

all: pys logs diffs summary

pys: Global_Table.py $(LIST_OF_PYS)

logs: Global_Table.log $(LIST_OF_LOGS)

diffs: Global_Table.log $(LIST_OF_DIFFS)

clean:
	@rm -f .database .dataset *.py *.pyc *.log *.diff *.root
  
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
	@PARTIAL=$$(gawk 'FNR==1 { NAME=gensub(/(.*)\.log/,"\\1",1,FILENAME); HEADER="TrigReport ---------- Modules in Path: "NAME" ------------"; } $$0 ~ HEADER { while ($$0 !~ /TrigReport.*hltBoolEnd/) getline; if ($$5 == 0) print NAME; nextfile; }' *_*.log); \
	if [ -z "$$PARTIAL" ]; then \
	  echo "All paths where fully excercised."; \
	else \
	  echo "These paths where not fully excercised:"; \
	  for P in $$PARTIAL; do echo -e "\t$(YELLOW)$$P$(NORMAL)"; done; \
	  echo; \
	fi

# these are kinda tricky: we need rules based on the file content, not on its modification date
ifneq ($(CONFIG),$(shell [ -f .database ] && cat .database))
.database:
	@echo $(CONFIG) > .database
endif

ifneq ($(SOURCE),$(shell [ -f .dataset ] && cat .dataset))
.dataset:
	@echo $(SOURCE) > .dataset
endif
# end of tricky rules

Global_Table.py: .database .dataset
	@echo -e " ConfDB [$(BLUE)$(CONFIG)$(NORMAL)] ---- $(BOLD)Global_Table$(NORMAL)"
	@$(GETCONFIG) --configName $(CONFIG) --input $(SOURCE) --services -PrescaleService --format python | sed -e's/^process = cms.Process(.*)/process = cms.Process( "$(PROCESS)" )/' -e's/^process.maxEvents = cms.untracked.PSet(  input = cms.untracked.int32( $(EVENTS) ) )/process.maxEvents = cms.untracked.PSet(  input = cms.untracked.int32( 100 ) )/' > Global_Table.py
#	@echo -e "$(COLUMN)$(GREEN)done$(NORMAL)"

Global_Table.log: Global_Table.py
	@echo -n "running Global Table"
	@$(CMSRUN) Global_Table.py >& Global_Table.log
	@echo -e "$(COLUMN)$(GREEN)done$(NORMAL)"

$(LIST_OF_PYS): %.py: .database .dataset
	@echo -e " ConfDB [$(BLUE)$(CONFIG)$(NORMAL)] path $(BOLD)$*$(NORMAL)"
	@$(GETCONFIG) --configName $(CONFIG) --input $(SOURCE) --paths $* --services -PrescaleService --format python | sed -e's/^process = cms.Process(.*)/process = cms.Process( "$(PROCESS)" )/' -e's/^process.maxEvents = cms.untracked.PSet(  input = cms.untracked.int32( $(EVENTS) ) )/process.maxEvents = cms.untracked.PSet(  input = cms.untracked.int32( 100 ) )/' > $@
#	@echo -e "$(COLUMN)$(GREEN)done$(NORMAL)"

$(LIST_OF_LOGS): %.log: %.py
	@echo -n "running trigger path $*"
	@$(CMSRUN) $< >& $@
	@if gawk '/TrigReport ---------- Modules in Path: $* ------------/ { while ($$0 !~ /TrigReport.*hltBoolEnd/) getline; if ($$5 == 0) exit 1; else exit 0; }' $*.log; then echo -e "$(COLUMN)$(GREEN)done$(NORMAL)"; else echo -e "$(COLUMN)$(YELLOW)warning$(NORMAL)"; fi

$(LIST_OF_PATHS): %: %.diff

$(LIST_OF_DIFFS): Global_Table.log

$(LIST_OF_DIFFS): %.diff: %.log
	@echo -n "checking trigger path $*"
	@cat $*.log         | gawk 'BEGIN { FOUND=0 } /TrigReport ---------- Modules in Path: $* ------------/ { FOUND=1; print; getline; print "TrigReport  Trig    Visited     Passed     Failed      Error Name"; next; } /^$$/ {FOUND=0; next; } // { if (FOUND) printf "TrigReport   %3d %10d %10d %10d %10d %s\n",$$2,$$4,$$5,$$6,$$7,$$8 }' > $*.single
	@cat Global_Table.log | gawk 'BEGIN { FOUND=0 } /TrigReport ---------- Modules in Path: $* ------------/ { FOUND=1; print; getline; print "TrigReport  Trig    Visited     Passed     Failed      Error Name"; next; } /^$$/ {FOUND=0; next; } // { if (FOUND) printf "TrigReport   %3d %10d %10d %10d %10d %s\n",$$2,$$4,$$5,$$6,$$7,$$8 }' > $*.full
	@if diff -w -U 999 $*.full $*.single > $*.diff; then \
            rm -f $*.diff; \
            echo -e "$(COLUMN)$(GREEN)done$(NORMAL)"; \
        else \
            echo -e "$(COLUMN)$(RED)error$(NORMAL)"; \
        fi
	@rm -f $*.single $*.full

help:
	@echo 'This makefile checks that each trigger path gives the same results if run stand-alone or in the global trigger table.'
	@echo 'Given a configName, it extracts from ConfDB the global table (Global_Table.py), the list of path, and a configuration'
	@echo 'for each path (TriggerName.py).'
	@echo 'Then both the trigger table and each paths are run, the corresponding TrigReport is extracted from the log, and compared.'
	@echo ''
	@echo 'After running each path, a warning is issued if a path is not fully excersided, i.e. no events pass all the filters.'
	@echo 'After comparing with the global table, an error is issued if there are discrepenaices in the TrigReport (at any level).'
	@echo ''
	@echo 'Working files:'
	@echo '  .database           configuration name, as looked for in ConfDB'
	@echo '  .dataset            dataset filename, used in PoolSource'
	@echo '  Global_Table.py     configuration for the global table'
	@echo '  Global_Table.log    output of cmsRun Global_Table.py'
	@echo '  TriggerName.py      configuration for TriggerName path'
	@echo '  TriggerName.log     output of cmsRun TriggerName.py'
	@echo '  TriggerName.diff    differences between TrigReport for TriggerName between global table run and stand-alone run'
	@echo ''
	@echo 'Supported targets:'
	@echo '  all                 same as "cfgs logs diffs summary"'
	@echo '  list                list all trigger paths'
	@echo '  pys                 extract all (python) configuration files'
	@echo '  logs                run all configuration files'
	@echo '  diffs               extract all differences'
	@echo '  summary             analyze all *available* diff and log files to print the list of trigger paths with discrepancies and/or with no accepted events'
	@echo '  help                print a simple description of this tool'
	@echo ''
	@echo '  TriggerName         run the full chain for trigger TriggerName: extract TriggerName.py, cmsRun logging to TriggerName.log,'
	@echo '                      if necessary extract and run the global table, and compare the TrigResults.'
	@echo ''
	@echo ''
	@echo 'Version 1.2.0, 1/7/2008'
	@echo 'Andrea Bocci <andrea.bocci@cern.ch>'

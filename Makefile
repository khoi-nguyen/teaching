ifeq ($(OS),Windows_NT)
	MARKDOWN := $(shell dir /b /S *.md)
	DEPENDENCIES := Makefile $(shell dir /b pandoc\\*.md)
	ENV :=
	LATEX := lualatex
else
	MARKDOWN := $(shell find * -name '*.md' | grep -v '^\(env\|node\|www\|README\)')
	DEPENDENCIES := Makefile $(shell find pandoc/*)
	ENV := source env/bin/activate;
	LATEX := latexmk -silent -lualatex -f
endif
TARGETS := $(MARKDOWN:.md=.tex) $(MARKDOWN:.md=.pdf)
HANDOUTS := $(MARKDOWN:.md=.handout.tex) $(MARKDOWN:.md=.handout.pdf)
PANDOC := $(ENV) pandoc -s --pdf-engine=lualatex\
	--filter ./pandoc/pythontex.py\
	--filter ./pandoc/environments.py\
	--filter ./pandoc/multicols.py
BEAMER := $(PANDOC) -t beamer --template=./pandoc/beamer.tex

all: $(TARGETS)

deploy: all $(HANDOUTS)
	. env/bin/activate; python ./data.py
	parcel build index.html --out-dir www --public-url ./ --no-cache
	ls -d */ | grep '^[0-9]' | xargs -I {} cp -R {} www
	rsync -avu --delete www/ khoi@nguyen.me.uk:~/www
	rm -fR www/*

clean:
	@echo Removing all temporary files
	@find [0-9]* -type f | grep -v '\(md\)$$' | xargs rm

%.tex: %.md $(DEPENDENCIES)
	@echo Generating $@...
	@$(BEAMER) -s $< -o $@

%.handout.tex: %.md $(DEPENDENCIES)
	@echo Building $@...
	$(BEAMER) -s $< -o $@ -V handout=true

%.pdf: %.tex
	@echo Building $@ with LaTeX...
	@cd $(<D); $(LATEX) $(<F)

env: env/bin/activate

env/bin/activate: requirements.txt
	test -d env || virtualenv env
	. env/bin/activate; pip install -Ur requirements.txt
	touch env/bin/activate

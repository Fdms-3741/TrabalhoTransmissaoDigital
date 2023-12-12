DOC  := main.tex

RERUN := "(undefined references|Rerun to get (cross-references|the bars|point totals) right|Table widths have changed. Rerun LaTeX.|Linenumber reference failed)"
RERUNBIB := "No file.*\.bbl|Citation.*undefined"

PDFLATEX := pdflatex -interaction nonstopmode -halt-on-error -file-line-error

all: doc

doc: $(DOC:.tex=.pdf)

%.pdf: %.tex
	$(PDFLATEX) $<
	@egrep -q $(RERUNBIB) $*.log && biber $* && $(PDFLATEX) $<; true
	@egrep -q $(RERUN) $*.log && $(PDFLATEX) $<; true
	@egrep -q $(RERUN) $*.log && $(PDFLATEX) $<; true

latexmk:
	-latexmk -pvc -pdf $(DOC)

purge:
	-rm -f *.{aux,dvi,log,bbl,blg,brf,fls,toc,thm,out,fdb_latexmk}

clean: purge
	-rm -f $(DOC:.tex=.pdf)

.PHONY: all purge clean

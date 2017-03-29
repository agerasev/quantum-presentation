all: source.pdf

source.pdf: source.tex deutsch.pdf
	pdflatex $<

deutsch.pdf: deutsch.svg
	rsvg-convert -f pdf -o $@ $<
all: source.pdf

source.pdf: source.tex deutsch.pdf shor.pdf
	pdflatex $<

deutsch.pdf: deutsch.svg
	rsvg-convert -f pdf -o $@ $<

shor.pdf: shor.svg
	rsvg-convert -f pdf -o $@ $<
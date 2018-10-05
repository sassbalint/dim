
all: run-see

run-see: run
	vim out

run:
	python ./dim.py > out


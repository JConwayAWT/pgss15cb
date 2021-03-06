#!/usr/bin/env python
"""Main function"""

from Parser import Parser
import sys, argparse, string


def run_stoch_sim(inFileName, outFileName, timeout=-1, loggingfreq=100):
	p = Parser()
	model = p.get_model(open(inFileName, 'r'), open(outFileName,'w+'), timeout, loggingfreq)
	model.iterate()


if __name__ == "__main__":
	parser = argparse.ArgumentParser()

	parser.add_argument("infile", help="The .react file of the simulation that you want to run")
	parser.add_argument("-o","--outfile", help="The .csv file that you want to write the results of", default="")
	parser.add_argument("-t","--timeout", help="Max running time in seconds", type=int, default=-1)
	parser.add_argument("-l","--loggingfreq", help="Logging Frequency (default 100)", type=int, default=100)

	args = parser.parse_args()

	if args.outfile == "":
		outfile = string.replace(args.infile, "react", "csv") if "react" in args.infile else args.infile+".csv"
	else:
		outfile = args.outfile

	run_stoch_sim(args.infile, outfile, args.timeout, args.loggingfreq)
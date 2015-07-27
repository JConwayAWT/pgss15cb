#!/usr/bin/env python
"""Main function"""

from Parser import Parser
import sys, argparse, string
# if len(sys.argv)!=3:
# 	raise ValueError("This program needs 2 arguments: input file (.react) and output file (.csv)")

parser = argparse.ArgumentParser()

parser.add_argument("infile", help="The .react file of the simulation that you want to run")
parser.add_argument("-o","--outfile", help="The .csv file that you want to write the results of", default="")
parser.add_argument("-t","--timeout", help="Max running time in seconds", type=int, default=-1)
parser.add_argument("-l","--loggingfreq", help="Logging Frequency (default 100)", type=int, default=100)


args = parser.parse_args()

if args.outfile == "":
	outfile = string.replace(args.infile, "react", "csv") if "react" in args.infile else args.infile+".csv"
	print outfile
else:
	outfile = args.outfile

p = Parser()
print args.infile, args.outfile
model = p.get_model(open(args.infile, 'r'), open(outfile,'w+'), args.timeout, args.loggingfreq)
model.iterate()

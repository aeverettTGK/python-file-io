#! /usr/bin/env python3

import argparse
import re
import sys

def transform_into_regexpress(input_string):
    re_expression_obj = re.compile(input_string)
    return re_expression_obj


def find_in_file(input_file, output_file, input_string):
    expression = transform_into_regexpress(input_string)
    line_number = 1
    with open(input_file, "r") as infile, open(output_file, "w") as outfile:
        for line in infile:
            line_number += 1
            word_list = re.findall(expression, line)
            for word in word_list:
                outfile.write("{}\t{}".format(line_number, word))

if __name__=="__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input",
            type = str,
            default = "origin.txt",
            help = "Input file")
    parser.add_argument("-o", "--output",
            type = str,
            default = "origin_output.txt",
            help = "Output file")
    parser.add_argument("-r", "--regex",
            type = str,
            default = r'\b\w*\herit\w*\b',
            help = "Regular expression pattern you want to search (Must be formatted as raw string)")
    args = parser.parse_args()
    print(args)
    #find_in_file(args.input, args.output, args.regex)

#! /usr/bin/env python3

import re
import sys

def transform_into_regexpress(input_string):
    expression = r'{}'.format(input_string)
    re_expression_obj = re.compile(expression)
    return re_expression_obj


def find_in_file(input_file, output_file, input_string):
    expression = transform_into_regexpress(input_string)
    line_number = 0
    with open(input_file, "r") as infile, open(output_file, "w") as outfile:
        for line in infile:
            line_number += 1
            word_list = re.findall(expression, line)
            for word in word_list:
                outfile.write("{}\t{}\n".format(line_number, word))

if __name__=="__main__":
    if len(sys.argv) != 4:
        sys.exit(sys.argv[0] + ": Expecting three arguments (input file, output file, pattern string)")
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    expression =sys.argv[3]
    find_in_file(input_file, output_file, expression)

import os
import argparse


desc = """take just the sentence between the parenthesis and split to 
different files."""


def main(args):
    with open(args.filename, "r") as input_file:
        for line in input_file:
            if args.rule and args.rule not in line:
                continue
            sen_name = line.split()[0]
            with open(args.output + "\\" + sen_name, 'w') as output_file:
                new_line = line[line.find("(")+1:line.find(")")]
                output_file.write(new_line)


if __name__ == "__main__":
    argparser = argparse.ArgumentParser(description=desc)
    argparser.add_argument("filename", help="input txt file")
    argparser.add_argument("-o", "--output", default=".", help="output dir")
    argparser.add_argument("-r", "--rule", default=".", help="rule to filter")
    main(argparser.parse_args())


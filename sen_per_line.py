import os
import argparse


desc = """take just the sentence between the parenthesis."""


def main(args):
    with open(args.filename, 'r') as input_file:
        with open(args.output, 'w') as output_file:
            for line in input_file:
                only_sen = line[line.find("(")+1:line.find(")")]
                output_file.write(only_sen + "\n")


if __name__ == "__main__":
    argparser = argparse.ArgumentParser(description=desc)
    argparser.add_argument("filename", help="input txt file")
    argparser.add_argument("-o", "--output", default=".", help="output txt file")
    main(argparser.parse_args())


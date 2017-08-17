#!/usr/bin/python

import sys
import getopt


def main(argv):
    origindir = ''
    clonedir = ''
    try:
        opts, args = getopt.getopt(argv, "ho:c:", ["odir=", "cdir="])
    except getopt.GetoptError:
        print('diff-dir.py -o <origindir> -c <clonedir>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('diff-dir.py -o <origindir> -c <clonedir>')
            sys.exit()
        elif opt in ("-o", "--odir"):
            origindir = arg
        elif opt in ("-c", "--cdir"):
            clonedir = arg
    print('Origin dir is "{}"'.format(origindir))
    print('Clone dir is "{}"'.format(clonedir))

if __name__ == "__main__":
    main(sys.argv[1:])

#!/usr/bin/python

import sys
import getopt
import hashlib
import os

DEBUGGING = False


def run(odir, cdir):
    ohashes = checksums(odir)
    chashes = checksums(cdir)
    result = []
    for f in chashes:
        if (f not in ohashes) or (chashes[f] != ohashes[f]):
            result.append(f)
    for f in sorted(result):
        print(f)


def checksums(targetdir):
    result = {}
    for root, dirs, files in os.walk(targetdir):
        if DEBUGGING:
            print(root, dirs, files)
        for f in files:
            fpath = os.path.join(root, f)
            frelpath = os.path.relpath(fpath, targetdir)
            result[frelpath] = md5(fpath)
    return result


def md5(fname):
    hash_md5 = hashlib.md5()
    with open(fname, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()


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
    if DEBUGGING:
        print('Origin dir is "{}"'.format(origindir))
        print('Clone dir is "{}"'.format(clonedir))
    run(origindir, clonedir)

if __name__ == "__main__":
    main(sys.argv[1:])
# -*- coding: utf-8 -*-
#!/usr/bin/python

import sys
import getopt
import hashlib
import os

DEBUGGING = False
BINARY = ['.ico', '.png', '.gif', '.jpg', '.jpeg', '.pdf', '.docx']


def run(odir, cdir):
    ohashes = checksums(odir)
    chashes = checksums(cdir)
    result = {}
    for f in chashes:
        if f not in ohashes:
            result[f] = '-'
        elif chashes[f] != ohashes[f]:
            result[f] = '*'
    for f in sorted(result):
        opath = os.path.join(odir, f)
        cpath = os.path.join(cdir, f)
        fname, fext = os.path.splitext(opath)
        if os.path.exists(opath) and os.path.exists(cpath) and (fext not in BINARY) and cmpbylines(opath, cpath):
            continue
        print("{} {}".format(result[f], f))


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


def cmpbylines(path1, path2):
    with open(path1, 'r') as file1, open(path2, 'r') as file2:
        line1, line2 = file1.readline(), file2.readline()
        while line1 != '' and line2 != '':
            if line1 != line2:
                return False
            line1, line2 = file1.readline(), file2.readline()
        if (line1 == '' and line2 != '') or (line1 != '' and line2 == ''):
            return False
    return True


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
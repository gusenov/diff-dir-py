# -*- coding: utf-8 -*-
#!/usr/bin/python

import sys
import getopt
import hashlib
import os

DEBUGGING = False
BINARY = ['.ico', '.png', '.gif', '.jpg', '.jpeg', '.pdf', '.docx']


def cmp(odir, cdir, linebyline):
    ohashes = checksums(odir)
    chashes = checksums(cdir)
    result = {}
    for f in chashes:
        if f not in ohashes:
            result[f] = '-'
        elif chashes[f] != ohashes[f]:
            result[f] = '*'
    for f in sorted(result):
        if linebyline:
            opath = os.path.join(odir, f)
            cpath = os.path.join(cdir, f)
            fname, fext = os.path.splitext(opath)
            if os.path.exists(opath) and os.path.exists(cpath) and (fext not in BINARY) and cmpbylines(opath, cpath):
                continue
        yield (f, result[f])


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
        lines1 = file1.read().splitlines()
        lines2 = file2.read().splitlines()
        if len(lines1) != len(lines2):
            return False
        it1 = iter(lines1)
        it2 = iter(lines2)
        while True:
            try:
                line1 = next(it1)
                line2 = next(it2)
                if line1 != line2:
                    return False
            except StopIteration:
                break
    return True


def main(argv):
    origindir = ''
    clonedir = ''
    linebyline = False
    try:
        opts, args = getopt.getopt(argv, "o:c:lh", ["odir=", "cdir=", "line-by-line", "help"])
    except getopt.GetoptError:
        print('diff-dir.py -o <origindir> -c <clonedir> -l')
        sys.exit(2)
    for opt, arg in opts:
        if opt == "-h":
            print('diff-dir.py -o <origindir> -c <clonedir> -l')
            sys.exit()
        elif opt == "--help":
            print('diff-dir.py --odir <origindir> --cdir <clonedir> --line-by-line')
            sys.exit()
        elif opt in ("-l", "--line-by-line"):
            linebyline = True
        elif opt in ("-o", "--odir"):
            origindir = arg
        elif opt in ("-c", "--cdir"):
            clonedir = arg
    if DEBUGGING:
        print('Origin dir is "{}"'.format(origindir))
        print('Clone dir is "{}"'.format(clonedir))
    for path, status in cmp(origindir, clonedir, linebyline):
        print("{} {}".format(status, path))

if __name__ == "__main__":
    main(sys.argv[1:])

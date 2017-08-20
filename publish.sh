#!/bin/bash
set -x # echo on

# Usage:
#  $ ./publish.sh
#  $ ./publish.sh --repo=pypi
#  $ ./publish.sh -r=testpypi

repo="pypi"

for i in "$@"
do
case $i in
    -r=*|--repo=*)
    repo="${i#*=}"
    shift # past argument=value
    ;;
esac
done

read -p "Вы уверены, что хотите провести публикацию в $repo? " -n 1 -r
echo    # (optional) move to a new line
if [[ $REPLY =~ ^[Yy]$ ]]
then
    pip uninstall diff-dir-py

    python setup.py sdist upload -r $repo

    if [ "$repo" == "pypi" ]
    then
        pip install diff-dir-py --user
    elif [ "$repo" == "testpypi" ]
    then
        pip install --extra-index-url https://testpypi.python.org/pypi diff-dir-py --user
    fi

    pip list
    ls ~/.local/lib/python3.5/site-packages/
fi

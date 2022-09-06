#!/usr/env bash
set -e

COMMIT_MSG=${1:-Updated blog}
DUMMY_USER=${DUMMY_USER:-1}
DEBUG=${DEBUG:-0}

echo "making a commit with message=${COMMIT_MSG}";

if [ $DEBUG -eq "1" ];
then
    echo "DEBUGGING";
else
    echo "RUNNING";
    if [ $DUMMY_USER == 1 ];
    then
        echo "DUMMY_USER=$DUMMY_USER, setting new users."
        git config user.name github-actions
        git config user.email github-actions@github.com
    else
        echo "DUMMY_USER=$DUMMY_USER, reusing env user."
    fi
    cp -r ./docs ../
    git fetch origin gh-pages
    git checkout gh-pages
    rsync -a --delete ../docs/ ./docs/
    git add .
    git diff-index --quiet HEAD || git commit -m "${COMMIT_MSG}"
    git push origin HEAD
    git checkout master
fi



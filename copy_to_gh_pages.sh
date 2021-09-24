#!/usr/env bash
set -e

COMMIT_MSG=${1:-Updated blog}
echo "making a commit with message=${COMMIT_MSG}";

if [ $DEBUG -eq "1" ];
then
    echo "DEBUGGING";
else
    echo "RUNNING";
    git config user.name github-actions
    git config user.email github-actions@github.com
    git fetch origin gh-pages
    git checkout gh-pages
    git add .
    git diff-index --quiet HEAD
    git commit -c user.name=github-actions -c user.email=github-actions@github.com -m "${COMMIT_MSG}"
    git push origin HEAD
fi



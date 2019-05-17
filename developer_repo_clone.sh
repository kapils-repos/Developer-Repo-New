#/bin/bash

pwd=$1

repository="https://kapils-repos:$pwd@github.com/kapils-repos/Developer-Repo-New.git"

git clone --depth=50 --branch=master $repository
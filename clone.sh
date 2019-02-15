#/bin/bash

repository="https://kapils-repos:Kgithub2019@github.com/kapils-repos/Config-Repo.git"
localFolder="Config-Repo"

git clone --depth=50 --branch=master $repository Config-Repo
pwd
ls
cd Config-Repo
pwd
ls
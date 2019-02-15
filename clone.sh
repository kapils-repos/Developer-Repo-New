#/bin/bash
repository1="https://kapils-repos:Kgithub2019@github.com/kapils-repos/Developer-Repo-New.git"
repository2="https://kapils-repos:Kgithub2019@github.com/kapils-repos/Config-Repo.git"
localFolder1="/home/travis/build/kapils-repos/Developer-Repo-New"
localFolder2="/home/travis/build/kapils-repos/Config-Repo"

git clone $repository1 $localFolder1
git clone $repository2 $localFolder2
cd $localFolder1
pwd
cd $localFolder2
pwd
ls

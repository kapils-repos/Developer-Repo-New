#/bin/bash
pwd=$1
repository="https://kapils-repos:$pwd@github.com/kapils-repos/Developer-Repo-New.git"
localFolder="/home/travis/build/kapils-repos/Developer-Repo-New/Developer-Repo-New/"
cd $localFolder
ls
git status
git add .
git commit -m "Added new file"
git remote add destination $repository
git pull
git push destination master

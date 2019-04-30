#/bin/bash
repository="https://kapils-repos:Kgithub2019@github.com/kapils-repos/Developer-Repo-New.git"
localFolder="/home/travis/build/kapils-repos/Developer-Repo-New"
cd $localFolder
ls
git status
git add .
git commit -m "Added new file"
git remote add destination $repository
git push destination master
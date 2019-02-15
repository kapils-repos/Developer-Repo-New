#/bin/bash
repository="https://kapils-repos:Kgithub2019@github.com/kapils-repos/Config-Repo.git"
localFolder="/home/travis/build/kapils-repos/Developer-Repo-New/Config-Repo"
cd Config-Repo
ls
git status
git add .
git commit -m "Updated the manifest.properties file"
git remote add destination $repository
git push destination master
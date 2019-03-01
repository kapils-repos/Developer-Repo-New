#/bin/bash
repository="https://kapils-repos:Kgithub2019@github.com/kapils-repos/Developer-Repo-New.git"

#git clone $repository "C:/Git/new-repo"
cd Developer-Repo-New
file=$(git show --name-only)
echo $file
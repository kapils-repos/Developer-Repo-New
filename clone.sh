#/bin/bash
repository1="https://kapils-repos:Kgithub2019@github.com/kapils-repos/Developer-Repo-New.git"
repository2="https://kapils-repos:Kgithub2019@github.com/kapils-repos/Config-Repo.git"
localFolder1="/kapils-repos/Developer-Repo-New"
localFolder2="/kapils-repos/Config-Repo"

git clone --depth=50 --branch=master $repository2 kapils-repos/Config-Repo
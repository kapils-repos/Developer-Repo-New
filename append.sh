#/bin/bash
repository1="https://kapils-repos:Kgithub2019@github.com/kapils-repos/Developer-Repo-New.git"
repository2="https://kapils-repos:Kgithub2019@github.com/kapils-repos/Config-Repo.git"
localFolder1="C:/Git/developer_repo_new"
localFolder2="C:/Git/config-repo"

git clone $repository1 $localFolder1
cd $localFolder1
git clone $repository2 $localFolder2
cd $localFolder2
echo '--------------------------------------------------------------------' > C:/Git/config-repo/manifest.properties
#cat C:/Git/developer_repo_new/manifest.txt >> C:/Git/config-repo/manifest.properties
#cd $localFolder2
#git remote add destination $repository2
#git push destination master
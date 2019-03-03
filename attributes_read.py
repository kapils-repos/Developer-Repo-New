import os
import sys
import subprocess
import datetime

cmd = "git show --name-only --oneline"

output=subprocess.check_output(cmd, shell=True)
val=str(output)
list = val.split('\\n')
print(list)
for x in list:
    if x.find('.md')!=-1:
        file=x

fileLocation="/home/travis/build/kapils-repos/Developer-Repo-New/"+file

mdFile = open(fileLocation, 'r', encoding='utf-8')
mdRead = mdFile.read()
attributes=mdRead.split('---')[1]

os.system("sh clone.sh")
manifestFile = open("/home/travis/build/kapils-repos/Developer-Repo-New/Config-Repo/manifest.properties",'a+')
manifestFile.write("\n---------------------------------------")
manifestFile.write("\n"+attributes)
manifestFile.write("createdDate: \""+datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')+"\"")
manifestFile.write("\nlastUpdatedDate: \""+datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')+"\"")
manifestFile.write("\nstatus: \"Created\"")
manifestFile.write("\nreviewer: \"\"")
manifestFile.close()

os.system("sh merge.sh")
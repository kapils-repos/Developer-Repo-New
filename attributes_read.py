import os
import sys
import subprocess
import datetime

cmd = "git show --name-only --oneline"

output=subprocess.check_output(cmd, shell=True)
val=str(output)
list = val.split('\\n')
print(list)
files=""
for x in list:
    if x.find('.md')!=-1:
        file=x

for i in range(1,len(list)-1):
    files=files+list[i]
    if i<len(list)-2:
        files = files +","

fileLocation="/home/travis/build/kapils-repos/Developer-Repo-New/"+file

print(files)
category=file.split("/")[0]

mdFile = open(fileLocation, 'r', encoding='utf-8')
mdRead = mdFile.read()
attributes=mdRead.split('---')[1]

os.system("sh clone.sh")
manifestFile = open("/home/travis/build/kapils-repos/Developer-Repo-New/Config-Repo/manifest.properties",'a+')
manifestFile.write("\n---------------------------------------")
manifestFile.write("\n"+attributes)
manifestFile.write("originSource: \"Developer-Repo\"")
manifestFile.write("\ndestination: \"\"")
manifestFile.write("\nfileNames: \""+files+"\"")
manifestFile.write("\ncategory: \""+category+"\"")
manifestFile.write("\ncreatedDate: \""+datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')+"\"")
manifestFile.write("\nlastUpdatedDate: \""+datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')+"\"")
manifestFile.write("\nstatus: \"Created\"")
manifestFile.write("\nreviewer: \"\"")
manifestFile.write("\npublic: \"No\"")
manifestFile.close()

os.system("sh merge.sh")
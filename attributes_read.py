import os
import sys
import subprocess
import datetime
import json

def writeToJSONFile(data):
    filePathNameWExt = '/home/travis/build/kapils-repos/Developer-Repo-New/Config-Repo/manifest.json'
    with open(filePathNameWExt, 'w') as fp:
        json.dump(data, fp)

def checkKey(category):
    if '-' in category:
        catSplit=category.split('-')
        key=catSplit[0][0]+catSplit[1][0]
    else:
        key=category[:2]
    return key

def keyGen(key,num):
    newVal=int(num)+1
    newVal=str(newVal)
    zeros=""
    for i in range(0, 4-len(newVal)):
        zeros=zeros+"0"
    artifactKey=key+zeros+newVal
    return artifactKey

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
attributes = mdRead.split('---')[1]
lineVal = attributes.split('\n')
key = checkKey(category)

os.system("sh clone.sh")
manifestRead = open("/home/travis/build/kapils-repos/Developer-Repo-New/Config-Repo/manifest.json", 'r')

data = json.load(manifestRead)
num=""
for i in range(0, len(data['artifacts'])):
    artKey=data['artifacts'][i]['artifactKey']
    if key==artKey[:2]:
        num=artKey[2:6]
    else:
        num='0000'

artifactKey = keyGen(key,num)
attrToManifest={}
attrToManifest["artifactKey"]=artifactKey
attrToManifest[lineVal[1].split(':')[0]]=lineVal[1].split(':')[1].strip().replace("\"", "")
attrToManifest[lineVal[2].split(':')[0]]=lineVal[2].split(':')[1].strip().replace("\"", "")
attrToManifest[lineVal[3].split(':')[0]]=lineVal[3].split(':')[1].strip().replace("\"", "")
attrToManifest[lineVal[4].split(':')[0]]=lineVal[4].split(':')[1].strip().replace("\"", "")
attrToManifest["originSource"]="Developer-Repo"
attrToManifest["destination"]=""
attrToManifest["fileNames"]=files
attrToManifest["category"]=category
attrToManifest["createdDate"]=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
attrToManifest["lastUpdatedDate"]=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
attrToManifest["status"]="Created"
attrToManifest["reviewer"]=""
attrToManifest["public"]="No"
data["artifacts"].append(attrToManifest)

writeToJSONFile(data)

os.system("sh merge.sh")

import os
import sys
import requests
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

def notification(to_mail, subject, message):
    print(to_mail+' '+subject+' '+message)
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        'Authorization': 'Basic a2hhcmluZHJhbkBjc2EudGFsZW5kLmNvbTpLQHRhbGVuZGNsb3VkMjAxOA==',
    }
    data = '{ \n   "executable": "5cb9afe7d29a2243cd930229", \n   "parameters": {\n     "to": "'+to_mail+'",\n     "subject": "'+subject+'",\n     "message": "'+message+'"\n   }\n }'
    response = requests.post('https://api.eu.cloud.talend.com/tmc/v1.2/executions', headers=headers, data=data)
    print('Below is the response code')
    print(response)

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

os.system("sh clone.sh")
manifestRead = open("/home/travis/build/kapils-repos/Developer-Repo-New/Config-Repo/manifest.json", 'r')
data = json.load(manifestRead)

if lineVal[1].split(':')[0] != "id":
    key = checkKey(category)
    num="0000"
    for i in range(0, len(data['artifacts'])):
        artKey=data['artifacts'][i]['artifactKey']
        if key==artKey[:2]:
            num=artKey[2:6]

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
    attrToManifest[lineVal[5].split(':')[0]]=lineVal[5].split(':')[1].strip().replace("\"", "")
    data["artifacts"].append(attrToManifest)

    writeToJSONFile(data)

    os.system("sh developer_repo_clone.sh")
    newFile = open("/home/travis/build/kapils-repos/Developer-Repo-New/Developer-Repo-New/"+category+"/newFile.md","w+")
    newFile.write("---")
    newFile.write("\nid: \""+artifactKey+"\"\n")
    newFile.write(attributes)
    newFile.write("---")
    newFile.write(mdRead.split('---')[2])
    newFile.close()

    os.remove(fileLocation)
    os.rename("/home/travis/build/kapils-repos/Developer-Repo-New/Developer-Repo-New/"+category+"/newFile.md", "/home/travis/build/kapils-repos/Developer-Repo-New/Developer-Repo-New/"+file)

    os.system("sh repo_merge.sh")

    os.system("sh merge.sh")
    to=lineVal[2].split(':')[1].strip().replace("\"", "")+'@talend.com'
    subject='CWR Upload Notification'
    message='Hi, Your artifact titled '+lineVal[1].split(':')[1].strip().replace("\"", "")+' has been uploaded. The artifact ID is #'+artifactKey+' and will be published on approval.'
    notification(to, subject, message)
else:
    l = len(data['artifacts'])
    for i in range(0, l):
        if data['artifacts'][i]['artifactKey']==lineVal[1].split(':')[1].strip().replace("\"", ""):
            print("The id is available "+data['artifacts'][i]['artifactKey'])


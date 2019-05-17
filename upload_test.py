import os
import sys
import requests
import subprocess
import datetime
import json

#Function to write the attributes to the existing JSON file
def writeToJSONFile(data):
    filePathNameWExt = '/home/travis/build/kapils-repos/Developer-Repo-New/Config-Repo/manifest.json'
    with open(filePathNameWExt, 'w') as fp:
        json.dump(data, fp)

#Function to write the attributes to a new JSON file
def writeToNewJSONFile(data):
    filePathNameWExt = '/home/travis/build/kapils-repos/Developer-Repo-New/Config-Repo/manifest_new.json'
    with open(filePathNameWExt, 'w') as fp:
        json.dump(data, fp)

#Function to check the category and generate the key code
def checkKey(category):
    if '-' in category:
        catSplit=category.split('-')
        key=catSplit[0][0]+catSplit[1][0]
    else:
        key=category[:2]
    return key

#Function to generate artifact key comparing the existing keys available
def keyGen(key,num):
    newVal=int(num)+1
    newVal=str(newVal)
    zeros=""
    for i in range(0, 4-len(newVal)):
        zeros=zeros+"0"
    artifactKey=key+zeros+newVal
    return artifactKey

#Function to trigger a mail to the contributor
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


def getUsername(hash_code):
    print("The hashcode is "+hash_code)
    response = requests.get(
        'https://api.github.com/repos/kapils-repos/Developer-Repo-New/commits/'+hash_code,auth=('kapils-repos', 'Kgithub2019'))
    data=response.content
    json_data=json.loads(data)
    return json_data['author']['login'].replace("-talend","")


def main():
    git_password=sys.argv[1]

    #Command to get the latest commit details
    cmd = "git show --name-only --oneline"
    hash_code_cmd = "git rev-parse HEAD"

    hash=subprocess.check_output(hash_code_cmd, shell=True)
    hash_code_str=str(hash)
    hash_code=hash_code_str.split("'")
    userName=getUsername(hash_code[1].rstrip("\\n"))
    print("Username is "+userName)

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
    os.system("sh clone.sh %s" %(git_password))
    manifestRead = open("/home/travis/build/kapils-repos/Developer-Repo-New/Config-Repo/manifest.json", 'r')
    data = json.load(manifestRead)

    #Check if the .md file already has an id generated
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
        attrToManifest["author"]=userName
        attrToManifest["artifactVersion"]="1"
        attrToManifest[lineVal[2].split(':')[0]]=lineVal[2].split(':')[1].strip().replace("\"", "")
        attrToManifest["originSource"]="Developer-Repo"
        attrToManifest["destination"]=""
        attrToManifest["fileNames"]=files
        attrToManifest["category"]=category
        attrToManifest["createdDate"]=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        attrToManifest["lastUpdatedDate"]=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        attrToManifest["status"]="Created"
        attrToManifest["reviewer"]=""
        attrToManifest["reviewerComments"]=""
        attrToManifest["public"]="No"
        attrToManifest[lineVal[3].split(':')[0]]=lineVal[3].split(':')[1].strip().replace("\"", "")
        data["artifacts"].append(attrToManifest)

        writeToJSONFile(data)

        os.system("sh developer_repo_clone.sh %s" %(git_password))
        newFile = open("/home/travis/build/kapils-repos/Developer-Repo-New/Developer-Repo-New/"+category+"/newFile.md","w+")
        newFile.write("---")
        newFile.write("\nid: \""+artifactKey+"\"")
        newFile.write(attributes)
        newFile.write("author: \""+userName+"\"")
        newFile.write("\nartifactVersion: \"1\"")
        newFile.write("\n---")
        newFile.write(mdRead.split('---')[2])
        newFile.close()

        os.remove(fileLocation)
        os.rename("/home/travis/build/kapils-repos/Developer-Repo-New/Developer-Repo-New/"+category+"/newFile.md", "/home/travis/build/kapils-repos/Developer-Repo-New/Developer-Repo-New/"+file)

        os.system("sh repo_merge.sh %s" %(git_password))

        os.system("sh merge.sh %s" %(git_password))
        to=userName+'@talend.com'
        subject='CWR Upload Notification'
        message='Hi, Your artifact titled '+lineVal[1].split(':')[1].strip().replace("\"", "")+' has been uploaded. The artifact ID is #'+artifactKey+' and will be published on approval.'
        notification(to, subject, message)
    else :
        l = len(data['artifacts'])
        flag = "N"
        for i in range(0, l):
            if data['artifacts'][i]['artifactKey']==lineVal[1].split(':')[1].strip().replace("\"", "") and int(data['artifacts'][i]['artifactVersion'])<int(lineVal[6].split(':')[1].strip().replace("\"", "")):
                flag = "Y"
        if flag=="Y":
            for i in range(0, l):
                if data['artifacts'][i]['artifactKey']==lineVal[1].split(':')[1].strip().replace("\"", ""):
                    print("The id is available "+data['artifacts'][i]['artifactKey'])
                    folder = "/home/travis/build/kapils-repos/Developer-Repo-New/"
                    filesFromConfig=data['artifacts'][i]['fileNames']
                    files = files+","+filesFromConfig
                    filesList = files.split(",")
                    newFileList = set(filesList)
                    newFiles=""
                    version = int(data['artifacts'][i]['artifactVersion'])+1
                    for k in newFileList:
                        exists = os.path.isfile(folder+k)
                        if exists:
                            newFiles=newFiles+k+","

                    if newFiles.endswith(','):
                        newFiles=newFiles[:-1]

                    print("New files are "+newFiles)

                    data['artifacts'][i]['artifactTitle'] = lineVal[2].split(':')[1].strip().replace("\"", "")
                    data['artifacts'][i]['artifactVersion'] = str(version)
                    data['artifacts'][i]['talendVersion'] = lineVal[3].split(':')[1].strip().replace("\"", "")
                    data['artifacts'][i]['destination'] = ""
                    data['artifacts'][i]['fileNames'] = newFiles
                    data['artifacts'][i]['lastUpdatedDate'] = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                    data['artifacts'][i]['status'] = "Updated"
                    data['artifacts'][i]['reviewer'] = ""
                    data['artifacts'][i]['public'] = "No"
                    data['artifacts'][i]['artifactTags'] = lineVal[4].split(':')[1].strip().replace("\"", "")

            print(data['artifacts'])

            writeToNewJSONFile(data)
            os.remove('/home/travis/build/kapils-repos/Developer-Repo-New/Config-Repo/manifest.json')
            os.rename('/home/travis/build/kapils-repos/Developer-Repo-New/Config-Repo/manifest_new.json',
                      '/home/travis/build/kapils-repos/Developer-Repo-New/Config-Repo/manifest.json')

            os.system("sh developer_repo_clone.sh %s" %(git_password))
            newFile = open("/home/travis/build/kapils-repos/Developer-Repo-New/Developer-Repo-New/" + category + "/newFile.md", "w+")
            newFile.write("---")
            newFile.write("\nid: \"" + lineVal[1].split(':')[1].strip().replace("\"", "") + "\"")
            newFile.write("\nartifactTitle: \"" + lineVal[2].split(':')[1].strip().replace("\"", "") + "\"")
            newFile.write("\ntalendVersion: \"" + lineVal[3].split(':')[1].strip().replace("\"", "") + "\"")
            newFile.write("\nartifactTags: \"" + lineVal[4].split(':')[1].strip().replace("\"", "") + "\"")
            newFile.write("\nauthor: \"" + lineVal[5].split(':')[1].strip().replace("\"", "") + "\"")
            newFile.write("\nartifactVersion: \"" + str(version) + "\"")
            newFile.write("\n---")
            newFile.write(mdRead.split('---')[2])
            newFile.close()

            os.remove(fileLocation)
            os.rename("/home/travis/build/kapils-repos/Developer-Repo-New/Developer-Repo-New/" + category + "/newFile.md",
                      "/home/travis/build/kapils-repos/Developer-Repo-New/Developer-Repo-New/" + file)

            os.system("sh repo_merge.sh %s" %(git_password))

            os.system("sh merge.sh %s" %(git_password))
            to=lineVal[5].split(':')[1].strip().replace("\"", "")+'@talend.com'
            subject='CWR Upload Notification'
            message='Hi, Your updated artifact, titled '+lineVal[2].split(':')[1].strip().replace("\"", "")+' has been uploaded. The artifact ID is #'+lineVal[1].split(':')[1].strip().replace("\"", "")+' and will be published on approval.'
            notification(to, subject, message)

        else:
            print("Artifact version is the latest")

if __name__ == '__main__':
    main()
import os
import sys
import datetime

os.system("sh clone.sh")

file1 = open("/home/travis/build/kapils-repos/Developer-Repo-New/manifest.txt", 'r', encoding='utf-8')
attributes = file1.read()

print(attributes)

file2 = open("/home/travis/build/kapils-repos/Developer-Repo-New/Config-Repo/manifest.properties",'a+')
file2.write("\n\n---------------------------------------")
file2.write("\n"+attributes)
file2.write("\nCurrentStatus:Uploaded")
file2.write("\nUploaded DateTime:"+datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
file2.close()

file3 = open("/home/travis/build/kapils-repos/Developer-Repo-New/Config-Repo/manifest.properties",'r')
output = file3.read()

print(output)

os.system("sh merge.sh")
import os
import sys

os.system("sh clone.sh")

file = open("/home/travis/build/kapils-repos/Developer-Repo-New/manifest.txt", 'r', encoding='utf-8')
attributes = file.read()

print(attributes)

file2 = open("/home/travis/build/kapils-repos/Developer-Repo-New/Config-Repo/manifest.properties",'a+')
file2.write("\n\n---------------------------------------")
file2.write("\n"+attributes)
file2.close()

os.system("sh merge.sh")
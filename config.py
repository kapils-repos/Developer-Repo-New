import os
import sys

os.system("sh clone.sh")

file = open("C:\\Git\\developer_repo_new\\manifest.txt", 'r', encoding='utf-8')
attributes = file.read()

print(attributes)

file2 = open("C:\\Git\\config-repo\\manifest.properties",'a+')
file2.write("\n\n---------------------------------------")
file2.write("\n"+attributes)
file2.close()

#os.system("sh merge.sh")
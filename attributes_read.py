
#file = open("C:/Users/kharindran/Desktop/sample.md", 'r', encoding='utf-8')

#content = file.read()
#text=content.split("---")

#attributes = text[1].split("\n")

#print(attributes[1])

import os
import sys
import subprocess

cmd = "git show --name-only --oneline"

#output=os.system(cmd)
output=subprocess.check_output(cmd, shell=True)
#print(output)
val=str(output)
list = val.split('\\n')
print(list)
for x in list:
    if x.find('.md')!=-1:
        file=x
print(file)

#file = open("C:/Users/kharindran/Desktop/sample.md", 'r', encoding='utf-8')

#content = file.read()
#text=content.split("---")

#attributes = text[1].split("\n")

#print(attributes[1])

import os
import sys
import subprocess

cmd = "git show --name-only"

output=os.system(cmd)

print(output)
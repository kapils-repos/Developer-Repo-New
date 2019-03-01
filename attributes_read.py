
#file = open("C:/Users/kharindran/Desktop/sample.md", 'r', encoding='utf-8')

#content = file.read()
#text=content.split("---")

#attributes = text[1].split("\n")

#print(attributes[1])

import os
import sys
import subprocess

answer = subprocess.check_output(['./file.sh'])
#os.system("sh file.sh")
print("\n")
print("Value:{}".format(answer))
with open('silly.txt') as f:
    lines = f.read()

Mydict = {"sunk ship":"scuttle'",
          "wooden leg":"peg leg",
          "cannon ready to fire":"fire in the hole",
          "friends and comrades": "hearties"}
# Dealt with uper and lower case and/or punctuation 

for i in Mydict:
    #print(Mydict[i])
    lines = lines.replace(i,Mydict[i])
    lines = lines.replace(i.upper(),Mydict[i])
    lines = lines.replace(i.lower(),Mydict[i])
    lines = lines.replace(i.title(),Mydict[i])
    lines = lines.replace(i.capitalize(),Mydict[i])
    
print(lines)
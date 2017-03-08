import sys

cnt = {"Windows:": 0, "Ubuntu:": 0, "OS X:": 0, "Unknown:": 0}

for line in sys.stdin:
    a = line.split('"')[5]
    if (a.find("Windows", 0, len(a)) > -1):
        cnt["Windows:"] += 1
    elif (a.find("Ubuntu", 0, len(a)) > -1):
        cnt["Ubuntu:"] += 1
    elif (a.find("Macintosh", 0, len(a)) > -1):
        cnt["OS X:"] += 1
    else:
        cnt["Unknown:"] += 1

for k, v in sorted(cnt.items(), key=lambda x: x[1]):
    print(k, v, end='\n')

#!/usr/bin/env python3
from os import walk

rootDir = 'E:\\workspace\\yujahuaGitHub\\GitLab\\fresh-grad-2021-train'

for root, dir, files in walk(rootDir):
    match = root.rsplit("\\",1)[1]
    if(match in ['.git']):
        dir[:] = [] # ignore sub
        continue;

    times = root[len(rootDir)-1:].count('\\')
    print('|\t' * (times-1) + '├── %s' %match)

    if match in ['练习题','示例']:
        dir[:] = [] # ignore sub
        continue;
    for index,fname in enumerate(files):
        str = '|\t' * times
        if fname not in ['.gitkeep']:
            if index + 1 == len(files):
                print(str+'└── %s' %fname)
            else:
                print(str+'├── %s' %fname)

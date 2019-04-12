#2019/04/11
#Yuki Tsushima
#tsushima@bi.c.titech.ac.jp
#For Python 2.7

import sys

def load_ionosphere():
    #file open
    try:
        file = open('./ionosphere.scale')
    except:
        sys.stderr.write('Error in opening file.\n')
        sys.exit()

    lines = file.readlines()
    target = []
    parameters = []
    for line in lines:
        set = line.split()
        #target is 1 or 0
        target.append(int(set.pop(0))+1//2)
        params = {}
        for data in set:
            params[int(data.split(':')[0])] = float(data.split(':')[1])
        parameters.append(params)
    file.close()
    return [target, parameters]

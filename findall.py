#2019/04/08
#Yuki Tsushima
#tsushima@bi.c.titech.ac.jp

def findall(text, query):
    index = []
    data = -1
    while True:
        data = text.find(query, data+1)
        if data == -1:
            break
        index.append(data)
    return index
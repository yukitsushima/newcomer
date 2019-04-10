#2019/04/05
#Yuki Tsushima
#tsushima@bi.c.titech.ac.jp

def combine(file):
    ans = ''
    for line in file:
        ans = ans + line.strip()
    return ans

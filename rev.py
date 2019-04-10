#2019/04/05
#Yuki Tsushima
#tsushima@bi.c.titech.ac.jp

def rev(text):
    ans = ''
    for char in text:
        if char == 'A':
            ans = 'T' + ans
        elif char == 'T':
            ans = 'A' + ans
        elif char == 'G':
            ans = 'C' + ans
        elif char == 'C':
            ans = 'G' + ans
    return ans

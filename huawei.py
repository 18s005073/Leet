d = {}
for i in '0123456789':
    d[i]=i
for i in 'abcdefghijklmno':
    d[i] = str((ord(i)-ord('a'))//3+2)
for i in 'pqrs':
    d[i] = '7'
for i in 'tuv':
    d[i] = '8'
for i in 'wxyz':
    d[i] = '9'
for i in 'ABCDEFGHIJKLMNOPQRSTUVWXY':
    d[i] = chr(ord(i.lower())+1)
for i in 'Z':
    d[i] = 'a'
while True:
    try:
        str1 = input()
        s = ''
        for i in str1:
            if i in d:
                s += d[i]
            else:
                s += i
        print(s)
    except:
        break
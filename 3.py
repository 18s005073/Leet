# 暴力法
# def longestsubstr(string):
#     i = 1
#     s = string[0]
#     while(i<=len(string)-1):
#         s1 = string[i-1]
#         for j in range(i,len(string)):
#             if string[j] not in s1:
#                 s1 += string[j]
#             else:
#                 break
#             if len(s1) > len(s):
#                 s = s1
#         i+=1
#
#     return s

#队列法
def longestsubstr(string):
    #设置两个指针分别指向队列前后
    if len(string)==0 or len(string)==1:
        return len(string)
    last = 0
    right = last+1
    l = right-last
    while right<len(string):
        if string[right] not in string[last:right]:
            right+=1
            l = max(l, right - last)
        else:
            l = max(l,right-last)
            last += string[last:right].find(string[right])+1
            right = last+1
    return l

if __name__ == '__main__':
    string = 'abcabcbb'
    print(longestsubstr(string))
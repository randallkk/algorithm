# 회문 gold 5
# https://www.acmicpc.net/problem/17609

def isPalindrome(s, flag):
    pnt1 = 0; pnt2 = len(s)-1
    f1 = 3; f2 = 3;
    while pnt1 < pnt2:
        if s[pnt1] != s[pnt2]:
            if flag == 1:
                flag = 2
                break
            if s[pnt1] == s[pnt2-1]:
                psuedo = list(s)
                psuedo.pop(pnt2)
                f1 = isPalindrome(psuedo, 1)
            if s[pnt1+1] == s[pnt2]:
                psuedo = list(s)
                psuedo.pop(pnt1)
                f2 = isPalindrome(psuedo, 1)
            if s[pnt1] != s[pnt2-1] and s[pnt1+1] != s[pnt2]:
                flag = 2
                break
            flag = min(f1, f2)
            if f1 < f2:
                flag = f1
                pnt2 -= 1
            elif f1 > f2:
                flag = f2
                pnt1 += 1
        else:
            pnt1 += 1
            pnt2 -= 1
    return flag

t = int(input())
for _ in range(t):
    s = input()
    print(isPalindrome(s, 0))


# t = int(input())
# for _ in range(t):
#     s = input()
#     pnt1 = math.ceil(len(s)/2-1); pnt2 = math.floor(len(s)/2)
#     flag = 0

#     while pnt1 > 0 or pnt2 < len(s)-1:
#         if s[pnt1] != s[pnt2]:
#             if flag == 1:
#                 flag = 2
#                 break
#             if s[pnt1] == s[pnt2+1]:
#                 pnt2 += 1
#             elif s[pnt1-1] == s[pnt2]:
#                 pnt1 -= 1
#             else:
#                 flag = 2
#                 break
#             flag = 1
#         else: 
#             pnt1 -= 1
#             pnt2 += 1
#     # if pnt1 == 0 and pnt2 == len(s)-1:
#     #     if s[pnt1] != s[pnt2]:
#     #         if flag == 0:
#     #             flag = 1
#     #         else:
#     #             flag = 2
#     print(flag)
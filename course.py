#!/usr/bin/python
#count = 0
#def course(str):
#    n = len(str)
#    for i in range(n-1):
#        if str[i] != str[i+1]:
#            count += 1
#            if str[i] == str[i+2]:
#                return course(str[1:])
#            else:
#                return course(str[:1] + str[2:])
#def course(str):
#    count = 0
#    for i in range(len(str)-2):
#            if str[0] != str[1]:
#                count += 1
#                print i
#                if str[i] == str[i+2]:
#                    str = str[1:]
#                else:
#                    str = str[:1] + str[2:]
#            else:
#                break;
#    return count

#def argue(str):
#    index = 0
#    n = len(str)
#    for i in range(n):
#        if str[i] == 'R':
#            while str[i] == 'R':
#                i += 1
#                index += 1
#            if str[i] == 'L':
#                while str[i] == 'L':
#                    i += 1
#                    index += 1
#                break
#     if 

#import re
#s = raw_input()
#p = re.compile(ur"([L, R])(\1+)")
#new_s = p.sub(ur"\1",s)
#
#for i in range(len(new_s)):
#    if new_s[i] ==


#length = argue(str)
#print length
#print len(str) - length + 1     

#while True:
#    n = int(raw_input())
#    teams = []
#    dic = {}
#    for i in range(n):
#        teams.append(raw_input())
#    for i in range(n *(n-1) / 2):
#    	team_fight, score = raw_input().split()
#        team1, team2 = team_fight[0], team_fight[1]
#        score1, score2 = score[0], score[1]
#        dic[team1] = dic[team1] + score1
#        dic[team2] = dic[team2] + score2
#    new_dic= sorted(dic.iteritems(), key=lambda d:d[1], reverse = True)
#    keys = emp.keys()
#    for i in range(n/2):
#        print keys[i] 

n = int(raw_input())
dic = {}
for i in range(n):
    flag = True
    key, value = map(int, raw_input().split())
    if key in dic:
        flag = False
        print key, dic[key], value
    else:
    	dic[key] = value
if flag:
    print "YES"
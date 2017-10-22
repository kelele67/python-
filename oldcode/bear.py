def bear(sugers, dic):
    li = sorted(dic.iteritems(), key = lambda asd:asd[0], reverse = True)
    li = map(list, li)
    sugers = sorted(sugers)
    sugers.reverse()

    for bears in li:
        flag = 0
        for suger in sugers:
            if flag == len(sugers):
                break
            if bears[1] < suger:
                flag += 1
                print flag
            if bears[1] >= suger:
                bears[1] = bears[1] - suger
                # print bears
                sugers.remove(suger)
    return li



dic = {}
n, m = map(int, raw_input().split())
sugers = map(int, raw_input().split())
for i in range(n):
    bear_force, bear_hunger = map(int, raw_input().split())
    dic[int(bear_force)] = int(bear_hunger)

for value in bear(sugers, dic):
    print value[1]

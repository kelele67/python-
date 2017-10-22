import string
str = list(raw_input())
star = list(raw_input())
new_str = []
for s in str:
    if s in string.punctuation:
        new_str.append(0)
    else:
        new_str.append(1)
count = 0
for i in range(0, len(new_str)):
    if new_str[i] == int(star[i]):
        count = count + 1
p = (count /float(len(str))) * 100;
print "%.2f%%" %(p)
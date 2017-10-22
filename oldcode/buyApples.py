def buyApples(n):
    count = n / 8
    rem = n % 8
    if rem % 6 != 0:
        if (rem+8) % 6 != 0:
            return -1
        else:
            count = count - 1 + (rem+8) / 6
    else:
        count = count + rem / 6
    return count

n = int(raw_input())
print buyApples(n)
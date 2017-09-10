def countCity(city_num, step, parent):
    count = 1
    if step < city_num:
        for i in range(step):
            if parent[i] == i:
                count += 1
    else:
        return city_num
    return count
    
city_num, step = map(int, raw_input().split())
parent = map(int, raw_input().split())
print countCity(city_num, step, parent)
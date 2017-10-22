def _merge_tow_sorted_list(l1, l2, tmp):
    if len(l1) == 0 or len(l2) == 0:
        tmp.extend(l1)
        tmp.extend(l2)
        return tmp
    else:
        if l1[0] < l2[0]:
            tmp.append(l1[0])
            del l1[0]
        else:
            tmp.append(l2[0])
            del l2[0]
        return _merge_tow_sorted_list(l1, l2, tmp)

def merge_tow_sorted_list(l1, l2):
    return _merge_tow_sorted_list(l1, l2, [])
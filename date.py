def next_date(m, d, y):
    lastday=31
    if m in [4,6,9,11]:
        lastday = 30
    elif m == 2:
        lastday = 29 if is_leap(y) else 28
    
    if d == lastday:
        if m == 12:
            return (1,1,y+1)
        else:
            return (m+1,1,y)
    else:
        return (m,d+1,y)
def is_leap(y):
    return (y % 4 == 0 and ((not y % 100 == 0) or (y % 400)))
def url_format(m, d, y):
    result = ''
    if m < 10:
        result += '0' + str(m)
    else: 
        result += str(m)
    
    if d < 10:
        result += '-0' + str(d)
    else:
        result += '-' + str(d)

    result += '-' + str(y)

    return result
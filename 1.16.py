def drop(l,k):
    count = 0
    result = []

    for i in l:
        count += 1
        if count % k != 0:
            result.extend(i)

    return result

print drop(['a','b','c','d','e','f','g','h','i','k'],3)
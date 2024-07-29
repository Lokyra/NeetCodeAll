def replaceElements(arr):
    rightMax = -1

    for i in range(len(arr)-1, -1, -1):
        newMax = max(rightMax, arr[i])
        arr[i] = rightMax
        rightMax = newMax

    print(arr)
    return arr

test = [17,18,5,4,6,1]

replaceElements(test)

def plusMinus(arr):
    pos_count=0
    neg_count=0
    zero_count=0
    for i in range(len(arr)):
        if arr[i]>0:
            pos_count+=1
        elif arr[i]<0:
            neg_count+=1
        else:
            zero_count+=1
    print("{:.6f}".format(pos_count/len(arr)))
    print("{:.6f}".format(neg_count/len(arr)))
    print("{:.6f}".format(zero_count/len(arr)))
if __name__ == '__main__':
    n=int(input())
    r_list=[]
    for i in range(n):
        list=input().split()
        query=list[0]
        if(query=="insert"):
            index = int(list[1])
            value = int(list[2])
            r_list.insert(index, value)
        elif(query=="print"):
            print(r_list)
        elif(query=="remove"):
            value = int(list[1])
            r_list.remove(value)
        elif(query == "append"):
            value = int(list[1])
            r_list.append(value)
        elif(query=="sort"):
            r_list.sort()
        elif(query=="pop"):
            r_list.pop()
        elif(query=="reverse"):
            r_list.reverse()
def LinearSearch(lis,value):
    for i in lis:
        if i == value:
            return "Found"

    return "Not found"

if __name__ == "__main__":
    li = [4,6,7,2,1,87]
    print LinearSearch(li,87)
    

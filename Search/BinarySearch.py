def bsearch(lis,start,end,find):
    if start > end:
        print "Not found" # do not return caz recurssion returns None
    mid = (start+end)/2
    
    if lis[mid] == find :
        print "Found at "+str(mid)
    elif find >= lis[mid]:        
        bsearch(lis,mid+1,end,find)
    else:
        bsearch(lis,start,mid-1,find)

def main():
    li = [1,2,3,4,5,6,7,8,9]
    bsearch(li,0,len(li)-1,3)    


if __name__ == "__main__":main()
    
        

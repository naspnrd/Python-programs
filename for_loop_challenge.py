IP =input("enter your ip address ")
count_seg = 0 
len_seg = 0
i = ''
for i in range(0,len(IP)):
    if(IP[i] =='.'):
        print("segment {} contain {} characters".format(count_seg+1,len_seg))
        count_seg += 1
        len_seg = 0
    else:
        len_seg +=1
   
              
if i != "." :
    print("segment {} contain {} characters".format(count_seg+1,len_seg))

    
    
    
        


    

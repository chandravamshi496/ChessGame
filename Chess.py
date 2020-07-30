from os import system
positives=[1,6,5,3,2,4]
negatives=[-1,-6,-5,-3,-2,-4]
(k1a,k1o)=(0,4)
(k2a,k2o)=(7,4)
arr=[[0 for x in range(8)],[0 for x in range(8)],[0 for x in range(8)],[0 for x in range(8)],[0 for x in range(8)],[0 for x in range(8)],[0 for x in range(8)],[0 for x in range(8)]]
arr[0][0]=4
arr[0][1]=2
arr[0][2]=3
arr[0][3]=5
arr[0][4]=6
arr[0][5]=3
arr[0][6]=2
arr[0][7]=4
arr[7][0]=-4
arr[7][1]=-2
arr[7][2]=-3
arr[7][3]=-5
arr[7][4]=-6
arr[7][5]=-3
arr[7][6]=-2
arr[7][7]=-4
board={1:"*",4:"[",2:"%",3:"()",5:"$",6:"#",-1:"p",-4:"R",-2:"H",-3:"B",-5:"Q",-6:"K",0:"."}
def mkMove(sa,so,da,do):
#===============================================================================
#===============================POSITIVES(SYMBOLS)==============================
#===============================================================================
    if(arr[sa][so] in positives):
        if(arr[sa][so]==positives[0]):#making move for PAWN
            if((da-sa)==1 and (do-so)==0 and arr[da][do]==0):
                (arr[sa][so],arr[da][do])=(arr[da][do],arr[sa][so])
            elif(arr[da][do]!=0 and (da-sa)==1 and ((do-so)==1 or -1)):
                arr[da][do]=arr[sa][so]
                arr[sa][so]=0
            else:
                print("INVALID")
#===================================ROOK=======================================
        elif(arr[sa][so]==positives[5]):#making move for ROOK
            if((da-sa)==0 and (do-so)!=0 and arr[da][do]==0):
                if(do<so):#Move left
                    chk=0
                    for i in range(so+1,do,-1):
                        if(arr[sa][i]!=0):
                            chk=chk+1
                    if(chk==0):#checking if there are any pieces between initial and final position
                        (arr[sa][so],arr[da][do])=(arr[da][do],arr[sa][so])
                    else:
                        print("INVALID")
                else:#Move right
                    chk=0
                    for i in range(so+1,do,+1):
                        if(arr[sa][i]!=0):
                            chk=chk+1
                    if(chk==0):#checking if there are any pieces between initial and final position
                        (arr[sa][so],arr[da][do])=(arr[da][do],arr[sa][so])
                    else:
                        print("INVALID")
            elif((da-sa)==0 and (do-so)!=0 and arr[da][do]!=0):
                if(do<so):#Move left
                    chk=0
                    for i in range(so+1,do,-1):
                        if(arr[sa][i]!=0):
                            chk=chk+1
                    if(chk==0):#checking if there are any pieces between initial and final position
                        arr[da][do]=arr[sa][so]
                        arr[sa][so]=0
                    else:
                            print("INVALID")
                else:#Move right
                    chk=0
                    for i in range(so+1,do,+1):
                        if(arr[sa][i]!=0):
                            chk=chk+1
                    if(chk==0):#checking if there are any pieces between initial and final position
                        arr[da][do]=arr[sa][so]
                        arr[sa][so]=0
            elif((da-sa)!=0 and (do-so)==0 and arr[da][do]==0):
                if(da<sa):#Move up
                    chk=0
                    for i in range(sa-1,da,-1):
                        if(arr[i][do]!=0):
                            chk=chk+1
                    if(chk==0):#checking if there are any pieces between initial and final position
                        (arr[sa][so],arr[da][do])=(arr[da][do],arr[sa][so])
                    else:
                        print("INVALID")
                else:#Move down
                    chk=0
                    for i in range(sa+1,da,+1):
                        if(arr[i][do]!=0):
                            chk=chk+1
                    if(chk==0):#checking if there are any pieces between initial and final position
                        (arr[sa][so],arr[da][do])=(arr[da][do],arr[sa][so])
                    else:
                        print("INVALID")
            elif((da-sa)!=0 and (do-so)==0 and arr[da][do]!=0):
                if(da<sa):#Move up
                    chk=0
                    for i in range(sa+1,da,-1):
                        if(arr[i][do]!=0):
                            chk=chk+1
                    if(chk==0):#checking if there are any pieces between initial and final position
                        arr[da][do]=arr[sa][so]
                        arr[sa][so]=0
                    else:
                        print("INVALID")
                else:#Move down
                    chk=0
                    for i in range(sa+1,da,+1):
                        if(arr[i][do]!=0):
                            chk=chk+1
                    if(chk==0):#checking if there are any pieces between initial and final position
                        arr[da][do]=arr[sa][so]
                        arr[sa][so]=0
                    else:
                        print("INVALID")
            else:
                print("INVALID")
#===============================BISHOP========================================
        elif(arr[sa][so]==positives[3]):#making move for BISHOP
            if(abs(da-sa)==abs(do-so)):
                if(da>sa and do>so and arr[da][do]==0):#south-east move
                    chk=0
                    i=1
                    j=1
                    while(i!=da and j!=do):
                        if(arr[sa+i][so+j]!=0):
                            chk=chk+1
                        i=i+1
                        j=j+1
                    if(chk==0):
                        (arr[sa][so],arr[da][do])=(arr[da][do],arr[sa][so])
                    else:
                        print("INVALID")
                elif(da>sa and do>so and arr[da][do]!=0):
                    chk=0
                    i=1
                    j=1
                    while(i!=da and j!=do):
                        if(arr[sa+i][so+j]!=0):
                            chk=chk+1
                        i=i+1
                        j=j+1
                    if(chk!=0):
                        arr[da][do]=arr[sa][so]
                        arr[sa][so]=0
                    else:
                        print("INVALID")
                elif(da>sa and do<so and arr[da][do]==0):#south-west move
                    chk=0
                    i=1
                    j=1
                    while(i!=da and j!=do):
                        if(arr[sa+i][so+j]!=0):
                            chk=chk+1
                        i=i+1
                        j=j-1
                    if(chk==0):
                        (arr[sa][so],arr[da][do])=(arr[da][do],arr[sa][so])
                    else:
                        print("INVALID")
                elif(da>sa and do<so and arr[da][do]!=0):
                    chk=0
                    i=1
                    j=1
                    while(i!=da and j!=do):
                        if(arr[sa+i][so+j]!=0):
                            chk=chk+1
                        i=i+1
                        j=j-1
                    if(chk!=0):
                        arr[da][do]=arr[sa][so]
                        arr[sa][so]=0
                    else:
                        print("INVALID")
                elif(da<sa and do>so and arr[da][do]==0):#north-east move
                    chk=0
                    i=1
                    j=1
                    while(i!=da and j!=do):
                        if(arr[sa+i][so+j]!=0):
                            chk=chk+1
                        i=i-1
                        j=j+1
                    if(chk==0):
                        (arr[sa][so],arr[da][do])=(arr[da][do],arr[sa][so])
                    else:
                        print("INVALID")
                elif(da<sa and do>so and arr[da][do]!=0):
                    chk=0
                    i=1
                    j=1
                    while(i!=da and j!=do):
                        if(arr[sa+i][so+j]!=0):
                            chk=chk+1
                        i=i-1
                        j=j+1
                    if(chk!=0):
                        arr[da][do]=arr[sa][so]
                        arr[sa][so]=0
                    else:
                        print("INVALID")
                elif(da<sa and do<so and arr[da][do]==0):#north-west move
                    chk=0
                    i=1
                    j=1
                    while(i!=da and j!=do):
                        if(arr[sa+i][so+j]!=0):
                            chk=chk+1
                        i=i-1
                        j=j-1
                    if(chk==0):
                        (arr[sa][so],arr[da][do])=(arr[da][do],arr[sa][so])
                    else:
                        print("INVALID")
                elif(da<sa and do<so and arr[da][do]!=0):
                    chk=0
                    i=1
                    j=1
                    while(i!=da and j!=do):
                        if(arr[sa+i][so+j]!=0):
                            chk=chk+1
                        i=i-1
                        j=j-1
                    if(chk!=0):
                        arr[da][do]=arr[sa][so]
                        arr[sa][so]=0
                else:
                    print("INVALID")
#================================KNIGHT=========================================
        elif(arr[sa][so]==positives[4]):#Making move for KNIGHT
            if((da-sa)==-2 and (do-so)==1):#north-east straight L
                arr[da][do]=arr[sa][so]
                arr[sa][so]=0
            elif((da-sa)==-1 and (do-so)==2):#north-east slant L
                arr[da][do]=arr[sa][so]
                arr[sa][so]=0
            elif((da-sa)==1 and (do-so)==2):#south-east slant L
                arr[da][do]=arr[sa][so]
                arr[sa][so]=0
            elif((da-sa)==2 and (do-so)==1):#south-east straight L
                arr[da][do]=arr[sa][so]
                arr[sa][so]=0
            elif((da-sa)==2 and (do-so)==-1):#south-west straight L
                arr[da][do]=arr[sa][so]
                arr[sa][so]=0
            elif((da-sa)==1 and (do-so)==-2):#south-west slant L
                arr[da][do]=arr[sa][so]
                arr[sa][so]=0
            elif((da-sa)==-1 and (do-so)==-2):#north-west slant L
                arr[da][do]=arr[sa][so]
                arr[sa][so]=0
            elif((da-sa)==-2 and(do-so)==-1):#north-west straight L
                arr[da][do]=arr[sa][so]
                arr[sa][so]=0
            else:
                print("INVALID")
#===================================KING========================================
        elif(arr[sa][so]==positives[1]):#Making move for KING
            if((da-sa)==1 and (do-so)==1):#south-east move
                arr[da][do]=arr[sa][so]
                arr[sa][so]=0
                (k1a,k1o)=(da,do)
            elif((da-sa)==1 and (do-so)==0):#south move
                arr[da][do]=arr[sa][so]
                arr[sa][so]=0
                (k1a,k1o)=(da,do)
            elif((da-sa)==1 and (do-so)==-1):#south-west move
                arr[da][do]=arr[sa][so]
                arr[sa][so]=0
                (k1a,k1o)=(da,do)
            elif((da-sa)==0 and (do-so)==-1):#west move
                arr[da][do]=arr[sa][so]
                arr[sa][so]=0
                (k1a,k1o)=(da,do)
            elif((da-sa)==0 and (do-so)==1):#east move
                arr[da][do]=arr[sa][so]
                arr[sa][so]=0
                (k1a,k1o)=(da,do)
            elif((da-sa)==-1 and (do-so)==-1):#north-west move
                arr[da][do]=arr[sa][so]
                arr[sa][so]=0
                (k1a,k1o)=(da,do)
            elif((da-sa)==-1 and(do-so)==0):#north move
                arr[da][do]=arr[sa][so]
                arr[sa][so]=0
                (k1a,k1o)=(da,do)
            elif((da-sa)==-1 and (do-so)==1):#north-east move
                arr[da][do]=arr[sa][so]
                arr[sa][so]=0
                (k1a,k1o)=(da,do)
            else:
                print("INVALID")
#=====================================QUEEN===================================
        elif(arr[sa][so]==positives[2]):#Making move for QUEEN
#============================HORIZONTAL/VERTICAL=================================
            if((da-sa)==0 and (do-so)!=0 and arr[da][do]==0):
                if(do<so):
                    chk=0
                    for i in range(so+1,do,-1):
                        if(arr[sa][i]!=0):
                            chk=chk+1
                    if(chk==0):#checking if there are any pieces between initial and final position
                        (arr[sa][so],arr[da][do])=(arr[da][do],arr[sa][so])
                    else:
                        print("INVALID")
                else:
                    chk=0
                    for i in range(so+1,do,+1):
                        if(arr[sa][i]!=0):
                            chk=chk+1
                    if(chk==0):#checking if there are any pieces between initial and final position
                        (arr[sa][so],arr[da][do])=(arr[da][do],arr[sa][so])
                    else:
                        print("INVALID")
            elif((da-sa)==0 and (do-so)!=0 and arr[da][do]!=0):
                if(do<so):
                    chk=0
                    for i in range(so+1,do,-1):
                        if(arr[sa][i]!=0):
                            chk=chk+1
                    if(chk==0):#checking if there are any pieces between initial and final position
                        arr[da][do]=arr[sa][so]
                        arr[sa][so]=0
                    else:
                            print("INVALID")
                else:
                    chk=0
                    for i in range(so+1,do,+1):
                        if(arr[sa][i]!=0):
                            chk=chk+1
                    if(chk==0):#checking if there are any pieces between initial and final position
                        arr[da][do]=arr[sa][so]
                        arr[sa][so]=0
            elif((da-sa)!=0 and (do-so)==0 and arr[da][do]==0):
                if(da<sa):
                    chk=0
                    for i in range(sa+1,da,-1):
                        if(arr[i][do]!=0):
                            chk=chk+1
                    if(chk==0):#checking if there are any pieces between initial and final position
                        (arr[sa][so],arr[da][do])=(arr[da][do],arr[sa][so])
                    else:
                        print("INVALID")
                else:
                    chk=0
                    for i in range(sa+1,da,+1):
                        if(arr[i][do]!=0):
                            chk=chk+1
                    if(chk==0):#checking if there are any pieces between initial and final position
                        (arr[sa][so],arr[da][do])=(arr[da][do],arr[sa][so])
                    else:
                        print("INVALID")
            elif((da-sa)!=0 and (do-so)==0 and arr[da][do]!=0):
                if(da<sa):
                    chk=0
                    for i in range(sa+1,da,-1):
                        if(arr[i][do]!=0):
                            chk=chk+1
                    if(chk==0):#checking if there are any pieces between initial and final position
                        arr[da][do]=arr[sa][so]
                        arr[sa][so]=0
                    else:
                        print("INVALID")
                else:
                    chk=0
                    for i in range(sa+1,da,+1):
                        if(arr[i][do]!=0):
                            chk=chk+1
                    if(chk==0):#checking if there are any pieces between initial and final position
                        arr[da][do]=arr[sa][so]
                        arr[sa][so]=0
                    else:
                        print("INVALID")
#==================================DIAGONAL=====================================
            elif(abs(da-sa)==abs(do-so)):
                if(da>sa and do>so and arr[da][do]==0):#south-east move
                    chk=0
                    i=1
                    j=1
                    while(i!=da and j!=do):
                        if(arr[sa+i][so+j]!=0):
                            chk=chk+1
                        i=i+1
                        j=j+1
                    if(chk==0):
                        (arr[sa][so],arr[da][do])=(arr[da][do],arr[sa][so])
                    else:
                        print("INVALID")
                elif(da>sa and do>so and arr[da][do]!=0):
                    chk=0
                    i=1
                    j=1
                    while(i!=da and j!=do):
                        if(arr[sa+i][so+j]!=0):
                            chk=chk+1
                        i=i+1
                        j=j+1
                    if(chk!=0):
                        arr[da][do]=arr[sa][so]
                        arr[sa][so]=0
                    else:
                        print("INVALID")
                elif(da>sa and do<so and arr[da][do]==0):#south-west move
                    chk=0
                    i=1
                    j=1
                    while(i!=da and j!=do):
                        if(arr[sa+i][so+j]!=0):
                            chk=chk+1
                        i=i+1
                        j=j-1
                    if(chk==0):
                        (arr[sa][so],arr[da][do])=(arr[da][do],arr[sa][so])
                    else:
                        print("INVALID")
                elif(da>sa and do<so and arr[da][do]!=0):
                    chk=0
                    i=1
                    j=1
                    while(i!=da and j!=do):
                        if(arr[sa+i][so+j]!=0):
                            chk=chk+1
                        i=i+1
                        j=j-1
                    if(chk!=0):
                        arr[da][do]=arr[sa][so]
                        arr[sa][so]=0
                    else:
                        print("INVALID")
                elif(da<sa and do>so and arr[da][do]==0):#north-east move
                    chk=0
                    i=1
                    j=1
                    while(i!=da and j!=do):
                        if(arr[sa+i][so+j]!=0):
                            chk=chk+1
                        i=i-1
                        j=j+1
                    if(chk==0):
                        (arr[sa][so],arr[da][do])=(arr[da][do],arr[sa][so])
                    else:
                        print("INVALID")
                elif(da<sa and do>so and arr[da][do]!=0):
                    chk=0
                    i=1
                    j=1
                    while(i!=da and j!=do):
                        if(arr[sa+i][so+j]!=0):
                            chk=chk+1
                        i=i-1
                        j=j+1
                    if(chk!=0):
                        arr[da][do]=arr[sa][so]
                        arr[sa][so]=0
                    else:
                        print("INVALID")
                elif(da<sa and do<so and arr[da][do]==0):#north-west move
                    chk=0
                    i=1
                    j=1
                    while(i!=da and j!=do):
                        if(arr[sa+i][so+j]!=0):
                            chk=chk+1
                        i=i-1
                        j=j-1
                    if(chk==0):
                        (arr[sa][so],arr[da][do])=(arr[da][do],arr[sa][so])
                    else:
                        print("INVALID")
                elif(da<sa and do<so and arr[da][do]!=0):
                    chk=0
                    i=1
                    j=1
                    while(i!=da and j!=do):
                        if(arr[sa+i][so+j]!=0):
                            chk=chk+1
                        i=i-1
                        j=j-1
                    if(chk!=0):
                        arr[da][do]=arr[sa][so]
                        arr[sa][so]=0
                else:
                    print("INVALID")
    elif(arr[sa][so] in negatives):
#==============================================================================
#========================NEGATIVES(CHARACTERS)=================================
#==============================================================================
        if(arr[sa][so]==negatives[0]):#making move for PAWN
            if((da-sa)==-1 and (do-so)==0 and arr[da][do]==0):
                (arr[sa][so],arr[da][do])=(arr[da][do],arr[sa][so])
            elif(arr[da][do]!=0 and (da-sa)==-1 and ((do-so)==1 or -1)):
                arr[da][do]=arr[sa][so]
                arr[sa][so]=0
            else:
                print("INVALID")
#===================================ROOK=======================================
        elif(arr[sa][so]==negatives[5]):#making move for ROOK
            if((da-sa)==0 and (do-so)!=0 and arr[da][do]==0):
                if(do<so):#Move left
                    chk=0
                    for i in range(so+1,do,-1):
                        if(arr[sa][i]!=0):
                            chk=chk+1
                    if(chk==0):#checking if there are any pieces between initial and final position
                        (arr[sa][so],arr[da][do])=(arr[da][do],arr[sa][so])
                    else:
                        print("INVALID")
                else:#Move right
                    chk=0
                    for i in range(so+1,do,+1):
                        if(arr[sa][i]!=0):
                            chk=chk+1
                    if(chk==0):#checking if there are any pieces between initial and final position
                        (arr[sa][so],arr[da][do])=(arr[da][do],arr[sa][so])
                    else:
                        print("INVALID")
            elif((da-sa)==0 and (do-so)!=0 and arr[da][do]!=0):
                if(do<so):#Move left
                    chk=0
                    for i in range(so+1,do,-1):
                        if(arr[sa][i]!=0):
                            chk=chk+1
                    if(chk==0):#checking if there are any pieces between initial and final position
                        arr[da][do]=arr[sa][so]
                        arr[sa][so]=0
                    else:
                            print("INVALID")
                else:#Move right
                    chk=0
                    for i in range(so+1,do,+1):
                        if(arr[sa][i]!=0):
                            chk=chk+1
                    if(chk==0):#checking if there are any pieces between initial and final position
                        arr[da][do]=arr[sa][so]
                        arr[sa][so]=0
            elif((da-sa)!=0 and (do-so)==0 and arr[da][do]==0):
                if(da<sa):#Move up
                    chk=0
                    for i in range(sa-1,da,-1):
                        if(arr[i][do]!=0):
                            chk=chk+1
                    if(chk==0):#checking if there are any pieces between initial and final position
                        (arr[sa][so],arr[da][do])=(arr[da][do],arr[sa][so])
                    else:
                        print("INVALID")
                else:#Move down
                    chk=0
                    for i in range(sa+1,da,+1):
                        if(arr[i][do]!=0):
                            chk=chk+1
                    if(chk==0):#checking if there are any pieces between initial and final position
                        (arr[sa][so],arr[da][do])=(arr[da][do],arr[sa][so])
                    else:
                        print("INVALID")
            elif((da-sa)!=0 and (do-so)==0 and arr[da][do]!=0):
                if(da<sa):#Move up
                    chk=0
                    for i in range(sa+1,da,-1):
                        if(arr[i][do]!=0):
                            chk=chk+1
                    if(chk==0):#checking if there are any pieces between initial and final position
                        arr[da][do]=arr[sa][so]
                        arr[sa][so]=0
                    else:
                        print("INVALID")
                else:#Move down
                    chk=0
                    for i in range(sa+1,da,+1):
                        if(arr[i][do]!=0):
                            chk=chk+1
                    if(chk==0):#checking if there are any pieces between initial and final position
                        arr[da][do]=arr[sa][so]
                        arr[sa][so]=0
                    else:
                        print("INVALID")
            else:
                print("INVALID")
#===============================BISHOP========================================
        elif(arr[sa][so]==negatives[3]):#making move for BISHOP
            if(abs(da-sa)==abs(do-so)):
                if(da>sa and do>so and arr[da][do]==0):#south-east move
                    chk=0
                    i=1
                    j=1
                    while(i!=da and j!=do):
                        if(arr[sa+i][so+j]!=0):
                            chk=chk+1
                        i=i+1
                        j=j+1
                    if(chk==0):
                        (arr[sa][so],arr[da][do])=(arr[da][do],arr[sa][so])
                    else:
                        print("INVALID")
                elif(da>sa and do>so and arr[da][do]!=0):
                    chk=0
                    i=1
                    j=1
                    while(i!=da and j!=do):
                        if(arr[sa+i][so+j]!=0):
                            chk=chk+1
                        i=i+1
                        j=j+1
                    if(chk!=0):
                        arr[da][do]=arr[sa][so]
                        arr[sa][so]=0
                    else:
                        print("INVALID")
                elif(da>sa and do<so and arr[da][do]==0):#south-west move
                    chk=0
                    i=1
                    j=1
                    while(i!=da and j!=do):
                        if(arr[sa+i][so+j]!=0):
                            chk=chk+1
                        i=i+1
                        j=j-1
                    if(chk==0):
                        (arr[sa][so],arr[da][do])=(arr[da][do],arr[sa][so])
                    else:
                        print("INVALID")
                elif(da>sa and do<so and arr[da][do]!=0):
                    chk=0
                    i=1
                    j=1
                    while(i!=da and j!=do):
                        if(arr[sa+i][so+j]!=0):
                            chk=chk+1
                        i=i+1
                        j=j-1
                    if(chk!=0):
                        arr[da][do]=arr[sa][so]
                        arr[sa][so]=0
                    else:
                        print("INVALID")
                elif(da<sa and do>so and arr[da][do]==0):#north-east move
                    chk=0
                    i=1
                    j=1
                    while(i!=da and j!=do):
                        if(arr[sa+i][so+j]!=0):
                            chk=chk+1
                        i=i-1
                        j=j+1
                    if(chk==0):
                        (arr[sa][so],arr[da][do])=(arr[da][do],arr[sa][so])
                    else:
                        print("INVALID")
                elif(da<sa and do>so and arr[da][do]!=0):
                    chk=0
                    i=1
                    j=1
                    while(i!=da and j!=do):
                        if(arr[sa+i][so+j]!=0):
                            chk=chk+1
                        i=i-1
                        j=j+1
                    if(chk!=0):
                        arr[da][do]=arr[sa][so]
                        arr[sa][so]=0
                    else:
                        print("INVALID")
                elif(da<sa and do<so and arr[da][do]==0):#north-west move
                    chk=0
                    i=1
                    j=1
                    while(i!=da and j!=do):
                        if(arr[sa+i][so+j]!=0):
                            chk=chk+1
                        i=i-1
                        j=j-1
                    if(chk==0):
                        (arr[sa][so],arr[da][do])=(arr[da][do],arr[sa][so])
                    else:
                        print("INVALID")
                elif(da<sa and do<so and arr[da][do]!=0):
                    chk=0
                    i=1
                    j=1
                    while(i!=da and j!=do):
                        if(arr[sa+i][so+j]!=0):
                            chk=chk+1
                        i=i-1
                        j=j-1
                    if(chk!=0):
                        arr[da][do]=arr[sa][so]
                        arr[sa][so]=0
                else:
                    print("INVALID")
#================================KNIGHT=========================================
        elif(arr[sa][so]==negatives[4]):#Making move for KNIGHT
            if((da-sa)==-2 and (do-so)==1):#north-east straight L
                arr[da][do]=arr[sa][so]
                arr[sa][so]=0
            elif((da-sa)==-1 and (do-so)==2):#north-east slant L
                arr[da][do]=arr[sa][so]
                arr[sa][so]=0
            elif((da-sa)==1 and (do-so)==2):#south-east slant L
                arr[da][do]=arr[sa][so]
                arr[sa][so]=0
            elif((da-sa)==2 and (do-so)==1):#south-east straight L
                arr[da][do]=arr[sa][so]
                arr[sa][so]=0
            elif((da-sa)==2 and (do-so)==-1):#south-west straight L
                arr[da][do]=arr[sa][so]
                arr[sa][so]=0
            elif((da-sa)==1 and (do-so)==-2):#south-west slant L
                arr[da][do]=arr[sa][so]
                arr[sa][so]=0
            elif((da-sa)==-1 and (do-so)==-2):#north-west slant L
                arr[da][do]=arr[sa][so]
                arr[sa][so]=0
            elif((da-sa)==-2 and(do-so)==-1):#north-west straight L
                arr[da][do]=arr[sa][so]
                arr[sa][so]=0
            else:
                print("INVALID")
#===================================KING========================================
        elif(arr[sa][so]==negatives[1]):#Making move for KING
            if((da-sa)==1 and (do-so)==1):#south-east move
                arr[da][do]=arr[sa][so]
                arr[sa][so]=0
                (k2a,k2o)=(da,do)
            elif((da-sa)==1 and (do-so)==0):#south move
                arr[da][do]=arr[sa][so]
                arr[sa][so]=0
                (k2a,k2o)=(da,do)
            elif((da-sa)==1 and (do-so)==-1):#south-west move
                arr[da][do]=arr[sa][so]
                arr[sa][so]=0
                (k2a,k2o)=(da,do)
            elif((da-sa)==0 and (do-so)==-1):#west move
                arr[da][do]=arr[sa][so]
                arr[sa][so]=0
                (k2a,k2o)=(da,do)
            elif((da-sa)==0 and (do-so)==1):#east move
                arr[da][do]=arr[sa][so]
                arr[sa][so]=0
                (k2a,k2o)=(da,do)
            elif((da-sa)==-1 and (do-so)==-1):#north-west move
                arr[da][do]=arr[sa][so]
                arr[sa][so]=0
                (k2a,k2o)=(da,do)
            elif((da-sa)==-1 and(do-so)==0):#north move
                arr[da][do]=arr[sa][so]
                arr[sa][so]=0
                (k2a,k2o)=(da,do)
            elif((da-sa)==-1 and (do-so)==1):#north-east move
                arr[da][do]=arr[sa][so]
                arr[sa][so]=0
                (k2a,k2o)=(da,do)
            else:
                print("INVALID")
#=====================================QUEEN===================================
        elif(arr[sa][so]==negatives[2]):#Making move for QUEEN
#============================HORIZONTAL/VERTICAL=================================
            if((da-sa)==0 and (do-so)!=0 and arr[da][do]==0):
                if(do<so):
                    chk=0
                    for i in range(so+1,do,-1):
                        if(arr[sa][i]!=0):
                            chk=chk+1
                    if(chk==0):#checking if there are any pieces between initial and final position
                        (arr[sa][so],arr[da][do])=(arr[da][do],arr[sa][so])
                    else:
                        print("INVALID")
                else:
                    chk=0
                    for i in range(so+1,do,+1):
                        if(arr[sa][i]!=0):
                            chk=chk+1
                    if(chk==0):#checking if there are any pieces between initial and final position
                        (arr[sa][so],arr[da][do])=(arr[da][do],arr[sa][so])
                    else:
                        print("INVALID")
            elif((da-sa)==0 and (do-so)!=0 and arr[da][do]!=0):
                if(do<so):
                    chk=0
                    for i in range(so+1,do,-1):
                        if(arr[sa][i]!=0):
                            chk=chk+1
                    if(chk==0):#checking if there are any pieces between initial and final position
                        arr[da][do]=arr[sa][so]
                        arr[sa][so]=0
                    else:
                            print("INVALID")
                else:
                    chk=0
                    for i in range(so+1,do,+1):
                        if(arr[sa][i]!=0):
                            chk=chk+1
                    if(chk==0):#checking if there are any pieces between initial and final position
                        arr[da][do]=arr[sa][so]
                        arr[sa][so]=0
            elif((da-sa)!=0 and (do-so)==0 and arr[da][do]==0):
                if(da<sa):
                    chk=0
                    for i in range(sa+1,da,-1):
                        if(arr[i][do]!=0):
                            chk=chk+1
                    if(chk==0):#checking if there are any pieces between initial and final position
                        (arr[sa][so],arr[da][do])=(arr[da][do],arr[sa][so])
                    else:
                        print("INVALID")
                else:
                    chk=0
                    for i in range(sa+1,da,+1):
                        if(arr[i][do]!=0):
                            chk=chk+1
                    if(chk==0):#checking if there are any pieces between initial and final position
                        (arr[sa][so],arr[da][do])=(arr[da][do],arr[sa][so])
                    else:
                        print("INVALID")
            elif((da-sa)!=0 and (do-so)==0 and arr[da][do]!=0):
                if(da<sa):
                    chk=0
                    for i in range(sa+1,da,-1):
                        if(arr[i][do]!=0):
                            chk=chk+1
                    if(chk==0):#checking if there are any pieces between initial and final position
                        arr[da][do]=arr[sa][so]
                        arr[sa][so]=0
                    else:
                        print("INVALID")
                else:
                    chk=0
                    for i in range(sa+1,da,+1):
                        if(arr[i][do]!=0):
                            chk=chk+1
                    if(chk==0):#checking if there are any pieces between initial and final position
                        arr[da][do]=arr[sa][so]
                        arr[sa][so]=0
                    else:
                        print("INVALID")
#==================================DIAGONAL=====================================
            elif(abs(da-sa)==abs(do-so)):
                if(da>sa and do>so and arr[da][do]==0):#south-east move
                    chk=0
                    i=1
                    j=1
                    while(i!=da and j!=do):
                        if(arr[sa+i][so+j]!=0):
                            chk=chk+1
                        i=i+1
                        j=j+1
                    if(chk==0):
                        (arr[sa][so],arr[da][do])=(arr[da][do],arr[sa][so])
                    else:
                        print("INVALID")
                elif(da>sa and do>so and arr[da][do]!=0):
                    chk=0
                    i=1
                    j=1
                    while(i!=da and j!=do):
                        if(arr[sa+i][so+j]!=0):
                            chk=chk+1
                        i=i+1
                        j=j+1
                    if(chk!=0):
                        arr[da][do]=arr[sa][so]
                        arr[sa][so]=0
                    else:
                        print("INVALID")
                elif(da>sa and do<so and arr[da][do]==0):#south-west move
                    chk=0
                    i=1
                    j=1
                    while(i!=da and j!=do):
                        if(arr[sa+i][so+j]!=0):
                            chk=chk+1
                        i=i+1
                        j=j-1
                    if(chk==0):
                        (arr[sa][so],arr[da][do])=(arr[da][do],arr[sa][so])
                    else:
                        print("INVALID")
                elif(da>sa and do<so and arr[da][do]!=0):
                    chk=0
                    i=1
                    j=1
                    while(i!=da and j!=do):
                        if(arr[sa+i][so+j]!=0):
                            chk=chk+1
                        i=i+1
                        j=j-1
                    if(chk!=0):
                        arr[da][do]=arr[sa][so]
                        arr[sa][so]=0
                    else:
                        print("INVALID")
                elif(da<sa and do>so and arr[da][do]==0):#north-east move
                    chk=0
                    i=1
                    j=1
                    while(i!=da and j!=do):
                        if(arr[sa+i][so+j]!=0):
                            chk=chk+1
                        i=i-1
                        j=j+1
                    if(chk==0):
                        (arr[sa][so],arr[da][do])=(arr[da][do],arr[sa][so])
                    else:
                        print("INVALID")
                elif(da<sa and do>so and arr[da][do]!=0):
                    chk=0
                    i=1
                    j=1
                    while(i!=da and j!=do):
                        if(arr[sa+i][so+j]!=0):
                            chk=chk+1
                        i=i-1
                        j=j+1
                    if(chk!=0):
                        arr[da][do]=arr[sa][so]
                        arr[sa][so]=0
                    else:
                        print("INVALID")
                elif(da<sa and do<so and arr[da][do]==0):#north-west move
                    chk=0
                    i=1
                    j=1
                    while(i!=da and j!=do):
                        if(arr[sa+i][so+j]!=0):
                            chk=chk+1
                        i=i-1
                        j=j-1
                    if(chk==0):
                        (arr[sa][so],arr[da][do])=(arr[da][do],arr[sa][so])
                    else:
                        print("INVALID")
                elif(da<sa and do<so and arr[da][do]!=0):
                    chk=0
                    i=1
                    j=1
                    while(i!=da and j!=do):
                        if(arr[sa+i][so+j]!=0):
                            chk=chk+1
                        i=i-1
                        j=j-1
                    if(chk!=0):
                        arr[da][do]=arr[sa][so]
                        arr[sa][so]=0
                else:
                    print("INVALID")
def printTable():
    for i in range(8):
        print("\t\t")
        for j in range(8):
            print(board[arr[i][j]], end=" ")
            print("\t", end=" ")
        print("\n", end=" ")
        print()
def mainMenu():
    print("\t\t\t\tC H E S S")
    print("\t\t\t(For genius brains only!)")
    print("\n\t\t\t1.Start Game")
    print("\n\t\t\t2.Instructions")
    ch=int(input())
    return ch
def instructions():
    fh=open("ChessRules.txt","r")
    contents=fh.read()
    print(contents)
    print("Enter 1 to start the game")
    ch=int(input())
    if(ch==1):
        game()
def game():
    system("cls")
    for x in range(8):
        arr[1][x]=1
        arr[6][x]=-1
    printTable()
    while(True):
        print("SYMBOLS:")
        sa=int(input())
        so=int(input())
        da=int(input())
        do=int(input())
        if(arr[sa][so]>0):
            if(arr[da][do]<=0):
                mkMove(sa,so,da,do)
        else:
            print("INVALID")
        system("cls")
        printTable()
        if(arr[k1a][k1o]!=6):
            print("\n\n\t\t\t\tCONGRATULATIONS")
            print("\n\t\tPLAYER '''CHARACTERS''' WON THE GAME")
            break
        elif(arr[k2a][k2o]!=-6):
            print("\n\n\t\t\t\tCONGRATULATIONS")
            print("\n\t\tPLAYER '''SYMBOLS''' WON THE GAME")
            break
        print("CHARACTERS:")
        sa=int(input())
        so=int(input())
        da=int(input())
        do=int(input())
        if(arr[sa][so]<0):
            if(arr[da][do]>=0):
                mkMove(sa,so,da,do)
        else:
            print("INVALID")
        system("cls")
        printTable()
        if(arr[k1a][k1o]!=6):
            print("\n\n\t\t\t\tCONGRATULATIONS")
            print("\n\t\tPLAYER '''CHARACTERS''' WON THE GAME")
            break
        elif(arr[k2a][k2o]!=-6):
            print("\n\n\t\t\t\tCONGRATULATIONS")
            print("\n\t\tPLAYER '''SYMBOLS''' WON THE GAME")
            break
ch=mainMenu()
if(ch==1):
    game()
elif(ch==2):
    instructions()


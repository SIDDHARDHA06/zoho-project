#!/usr/bin/env python
# coding: utf-8

# In[ ]:


LEN = int(input("enter the size of NxN matrix:"))
matrix = []

def fin_show():
    #traversing the ball
    trav = input("Enter the direction in which the ball need to traverse :")
    if(trav=="ST"):
        pass
    elif(trav=="LD"):
        matrix[int(LEN-1)][int((((LEN-1)/2)-1))]=str("o")
        matrix[int(LEN-1)][int((LEN-1)/2)]=str("W")
    elif(trav=="RD"):
        matrix[int(LEN-1)][int((((LEN-1)/2)+1))]=str("o")
        matrix[int(LEN-1)][int((LEN-1)/2)]=str("W")
    
    #to print the final matrix        
    for i in range(LEN):
        for j in range(LEN):
             print(matrix[i][j], end=" ")
        print()
    print("Ball count is ",balls)


def show():
    #to create a matrix containg "W"
    for i in range(LEN):
        empt_mat =[]
        for j in range(LEN):
            k = str("W")
            empt_mat.append(k)
        matrix.append(empt_mat)
    
    #to make the inside matrix empty    
    for i in range(1,LEN-1):
        for j in range(1,LEN-1):
            matrix[int(i)][int(j)]=str(" ")
            
    #to make ground and a ball        
    for i in range(LEN-1,LEN):
        for j in range(1,LEN-1):
            matrix[int(i)][int(j)]=str("G")
    matrix[int(LEN-1)][int((LEN-1)/2)]=str("o")
    
    #to input brick values and number of balls
    ans = "Y"
    while(ans!="N"):
        i,j,new_val = input("Enter the brick's position and the brick type :").split()
        matrix[int(i)][int(j)]=int(new_val)
        ans = input("Do you want to continue(Y or N)?")
    balls = int(input("enter ball count: "))
   
    #to print the final matrix        
    for i in range(LEN):
        for j in range(LEN):
             print(matrix[i][j], end=" ")
        print()
    print("Ball count is ",balls)
    fin_show()
show()




# In[ ]:





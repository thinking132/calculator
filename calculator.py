import math
import time


def int_combination(split_sick):
    n=0
    while True:
        #time.sleep(1)
        if split_sick[n+1] != "null":
            #print(n)
            if (type(split_sick[n]) == int) == True and (type(split_sick[n+1]) == int) == True:
                if split_sick[n] == 0 :
                    split_sick.insert(n,"@~")
                    split_sick.pop(n+1)
                else:
                    split_sick.insert(n,(split_sick[n]*10+split_sick[n+1]))
                    split_sick.pop(n+1)
                    split_sick.pop(n+1)
                #print(split_sick)
                #print("status:",1)
                
            else:
                n+=1
                split_sick.insert(n,(split_sick[n]))
                split_sick.pop(n+1)
                #print(split_sick)
                #print("status:",2)


            
        else:
            return split_sick

def find_point_and_combination(sick):
    max_len=0
    while '.' in sick:
        point_location=sick.index(".")
        if sick[point_location+1] =="@~":
            sick.pop(point_location+1)
            print(sick,sick[point_location-1],sick[point_location+1])
            
            point_len=len(str(sick[point_location+1]))+1
            if point_len > max_len :
                max_len=point_len
            point_front=float(sick[point_location-1])
            point_back=sick[point_location+1]/10**point_len
            print(max_len,point_len)
            print(point_len,point_front,point_back)
            sick.insert(point_location-1,point_front+point_back)

            for i in range(3):
                sick.pop(point_location)
        else:
            print(sick,sick[point_location-1],sick[point_location+1])

            point_len=len(str(sick[point_location+1]))
        if point_len > max_len :
            max_len=point_len
        point_front=float(sick[point_location-1])
        point_back=sick[point_location+1]/10**point_len
        print(max_len,point_len)
        print(point_len,point_front,point_back)
        sick.insert(point_location-1,point_front+point_back)

        for i in range(3):
            sick.pop(point_location)
    if max_len != 0:
        for i in range(len(sick)):
            if isinstance(sick[i],int) == True:
                sick.insert(i,sick[i])
                sick.pop(i+1)
    return sick,max_len


def the_most_high_precedence_operator(sick,max_len):
    i=len(sick)-1
    while i > 0:
        #print("high2",len(sick),i,sick)
        imsi_sick=0
        print(sick)
        if sick[i] == "^":
            if sick[i+1] == "-":
                imsi_sick=1/sick[i-1]**sick[i+2]
                
            else:
                imsi_sick=sick[i-1]**sick[i+1]
            sick.insert(i-1,imsi_sick)
            for j in range(3):
                sick.pop(i)
            i+=1
        i-=1
    return sick


def high_precedence_operator(sick,max_len):
    #print("high")
    i=0
    while i < len(sick):
        #print("high2",len(sick),i,sick)
        imsi_sick=0
        print(sick)
        if sick[i] == "*":
            if sick[i+1] == "-" :
                imsi_sick=sick[i-1]*10**max_len*(-sick[i+2])*10**max_len
                sick.insert(i-1,imsi_sick/10**(max_len*2))
                for j in range(3):
                    sick.pop(i)
            #print("*")
            else:
                imsi_sick=sick[i-1]*10**max_len*sick[i+1]*10**max_len
                sick.insert(i-1,imsi_sick/10**(max_len*2))
                for j in range(3):
                    sick.pop(i)
            i-=1

        elif sick[i] == "/":
            if sick[i+1] == "-" :
                imsi_sick=sick[i-1]*10**max_len/(-sick[i+2])*10**max_len
                sick.insert(i-1,imsi_sick/10**(max_len*2))
                for j in range(3):
                    sick.pop(i)
            else:
                imsi_sick=sick[i-1]*10**max_len/sick[i+1]*10**max_len
                sick.insert(i-1,imsi_sick/10**(max_len*2))
                for j in range(3):
                    sick.pop(i)
            i-=1
        i+=1
    return sick

def low_precedence_operator(sick,max_len):
    #print("low")
    i=0
    while i < len(sick):
        #print(sick[i])
        imsi_sick=0
        if sick[i] == "+":
            imsi_sick=sick[i-1]*10**max_len+sick[i+1]*10**max_len
            sick.insert(i-1,imsi_sick/10**max_len)
            for j in range(3):
                sick.pop(i)
            i-=1
        elif sick[i] == "-":
            imsi_sick=sick[i-1]*10**max_len-sick[i+1]*10**max_len
            sick.insert(i-1,imsi_sick/10**max_len)
            for j in range(3):
                sick.pop(i)
            i-=1
        i+=1
    return sick

def this_is_core_calculator(sick,max_len):
    sick=the_most_high_precedence_operator(sick,max_len)
    print(sick)
    sick=high_precedence_operator(sick,max_len)
    #print(sick)
    sick=low_precedence_operator(sick,max_len)
    print(sick)
    return sick


def end_calculation(sick,divide):
    max_len=divide
    print(sick)
    n=0     
    open_parentheses=0
    im_sick=[]
    while "(" in sick:
        #time.sleep(0.1)
        if sick[n] == "(":
            open_parentheses=n
        elif sick[n] == ")":
            im_sick=sick[open_parentheses+1:n]
            print(this_is_core_calculator(im_sick,max_len))
            claculation=this_is_core_calculator(im_sick,max_len)
            sick.insert(open_parentheses,claculation[0])
            for i in range(n-open_parentheses+1):
                sick.pop(open_parentheses+1)
            if isinstance(sick[open_parentheses-1],(int,float)):
                sick.insert(open_parentheses,"*")
            
            open_parentheses=0
            n=0
        print(sick,im_sick,n,open_parentheses,n-open_parentheses+2)
        n+=1
    dap =this_is_core_calculator(sick,max_len)[0]
    return dap
    
    
    """open_parentheses_location=[]
    close_parentheses_location=[]
    if "(" in  sick:
        for i in range(len(sick)):
            if sick[i] == "(":
                open_parentheses_location.append(i)
            elif sick[i] == ")":
                close_parentheses_location.append(i)
    if len(open_parentheses_location) < 2:
        for i in range(len(open_parentheses_location)-1):
            if open_parentheses_location[i] < close_parentheses_location[i] and open_parentheses_location[i+1] > close_parentheses_location[i]:
                inside_parentheses=[]"""
        


#def change_big_parentheses_to_small_parentheses(sick):                  #괄호 위치 찾고 소괄호로 전부 바꾸고 가장 안쪽 괄호를 찾는거

    
        
while True:
    split_sick=[]

    sick=input("식을 입력하시오")
    #sick="2^3^2"

    sick=sick.replace("]",")")
    sick=sick.replace("[","(")
    sick=sick.replace("}",")")
    sick=sick.replace("{","(")

    for i in range(len(sick)):
        split_sick.append(sick[i])     #진짜 완전히 문자 하나달 리스트 1칸으로 전환
    
    int_split_sick=[]
    for i in range (len(split_sick)):
        if split_sick[i].isdigit() == True:      #각 칸이 전부 문자열이니까 만약 int 였던게 잇으면 그걸 int 로 변환
            int_split_sick.append(int(split_sick[i]))

        else:
            int_split_sick.append(split_sick[i])

    
    #print(int_split_sick)
    int_split_sick.append("null")
    befor_point_final_split_sick=int_combination(int_split_sick)
    befor_point_final_split_sick.pop(len(befor_point_final_split_sick)-1)
    #print(befor_point_final_split_sick)

    I_make_point_sick,max_len=find_point_and_combination(befor_point_final_split_sick)
    #print(find_point_and_combination(befor_point_final_split_sick))
    #print(I_make_point_sick,max_len)
    
    #print(this_is_core_calculator(I_make_point_sick))
    print(end_calculation(I_make_point_sick,max_len))
    
    
    
    
    
    
    
    
    break
    
    
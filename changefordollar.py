# -*- coding: utf-8 -*-
"""
Created on Mon Oct 31 15:14:43 2022

@author: nelso
Title: chnage for $1
Status: on going
"""
counter = 0

# def check(t):
#     if t == true:
#         prin(let)
def counte():
    counter+=1
    return counter
    #finds the total
    

def totalv(letters,coins):
    total =0
    for x in range(0,5):
        total+=coins[x]*letters[x]
        #print(f"{total} = {coins[x]} * {letters[x]}")
    if total == 100:
        print("dollar = ",let)
        #counter()
    return total

    #prints the array
def prin(let):
    print(let)
    
    #resets the rest of the array
def reset(let,start):
    for x in range(start,5):
        let[x]=0
    
p = 0
n = 0 
d = 0
q = 0
h = 0
        # [h, q, d, n, p]
#letters = [h, q, d, n, p]
let = [0,0,0,0,0]

coins = ([50, 25, 10, 5 , 1])
true = 1
boolean = true

total = 0;
for h in range(0,3): #for coins[0] in range(0,3):
    #print("h ",coins[0])
    #total += coins[0]
    #letters[0]+=1
    let[1]=0#letters[1]=0
    let[2] = 0
    let[0]=h
    #prin(let)
    #if totalv(let,coins) == 100: counter+=1
    
    for q in range(0,5):
        #print("q ",let[1])
        #total += coins[1]
        #letters[1] +=1
        let[2]=0
        let[1]=q
        #if totalv(let,coins) == 100: counter+=1
        #prin(let)
        
        for d in range(0,11):
            #print("d ",let[2])#print("d ",coins[2])
            #total += coins[1]
            #letters[1] +=1
            #prin(let)
            let[3]=0
            let[2]=d
            #if totalv(let,coins) == 100: counter+=1
            
            for n in range(0,21):
                #print("d ",let[2])#print("d ",coins[2])
                #total += coins[1]
                #letters[1] +=1
                #prin(let)
                let[4]=0
                let[3]=n
                #if totalv(let,coins) == 100: counter+=1
                
                for p in range(0,101):
                    #print("d ",let[2])#print("d ",coins[2])
                    #total += coins[1]
                    #letters[1] +=1
                    #prin(let)
                    #let[5]=0
                    let[4]=p
                    if totalv(let,coins) == 100: counter+=1
print(counter)
            
     #works       
"""for h in range(0,2): #for coins[0] in range(0,3):
    #print("h ",coins[0])
    #total += coins[0]
    #letters[0]+=1
    let[1]=0#letters[1]=0
    let[2] = 0
    let[0]+=h
    #prin(let)
    
    totalv(let,coins)
    
    for q in range(0,4):
        #print("q ",coins[1])
        #total += coins[1]
        #letters[1] +=1
        let[2]=0
        let[1]+=1
        totalv(let,coins)
        
        for d in range(0,11):
            #print("d ",let[2])#print("d ",coins[2])
            #total += coins[1]
            #letters[1] +=1
           # prin(let)
            let[3]=0
            let[2]+=1
            totalv(let,coins)
           
            if let[2] == 10:
                break"""


"""if totalv(let,coins) == 100:
    print("dollar = ",let)#print("dollar = ",letters)
    counter+=1"""

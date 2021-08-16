# -*- coding: utf-8 -*-
"""
Created on Mon Aug 16 14:30:49 2021

@author: admin
"""
#The person at the (window). height how many times see the ball which is fall down from (height). height.
def jumping_ball(height,bounce,window):
    count = 0
    if height < 0:
        print( " Condition 1 is not fulfilled"  )
    elif (bounce >= 1 or bounce < 0):
        print(" Condition 2 is not fulfilled" )
    elif window >= height:
        print(" Condition 3 is not fulfilled" )
    else:
        while True:
             height = height*bounce
             if height < window:
                break
             count += 1
        print(count*2+1)
    
jumping_ball(5, 2/3, 1.5)
        
    
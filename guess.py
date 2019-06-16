import random
print('hey wanna play a game')
ans=input()
try:
    if ans=='no':
          print('ok bye')
    if ans=='yes':
        print('what z ur name?')
        name=input()
        print('hey '+name+ ', i have chose a no btw 20 to 40 !! you have to guess the no')
        num=random.randint(20,40)
        for i in range(0,5):
            k=input()
            if i<4:
                if int(k)>num:
                    print('your guess is high')
                elif int(k)<num:
                    print('guess too low')
                elif int(k)==num:
                    print('hey ' +name+' ,you guess correct no')
                    break
            else:
                print('no chance left!!! No was '+str(num))
                break
except:
     print('some error baby')
   
                
            
        

    
    

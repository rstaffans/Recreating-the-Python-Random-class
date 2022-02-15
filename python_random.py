#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import time

class MyRandom():
    
    #user can choose if they provide a seed or not
    def __init__(self,**kwargs):
        self.seedlist=[]
        
        if "seed" in kwargs:
            self.myseed=kwargs["seed"]
            self.seedlist.append(self.myseed)
        
        else:
            self.myseed=int(time.time())
            self.seedlist.append(self.myseed)
        
    #produces a random integer whenever it's called
    def _randint(self):
        """Linear congruental generator (mixed congruential generator) using Borland C/C++ for the values
        from https://en.wikipedia.org/wiki/Linear_congruential_generator#Python_code"""
        
        a=22695477
        c=1
        m=2**32
        RandomInt=int((a*self.seedlist[-1]+c)%m)
        self.seedlist.append(RandomInt)
        return RandomInt
   
    #takes two integers as argument and returns a random integer between these two integers.
    def randint(self,bot,top):
        self.bot=bot
        self.top=top
        
        if type(bot)!=int or type(top)!=int:
            print ("Both arguments have to be integers. Try again")
        
        elif top<=bot:
            print ("The second argument needs to be larger than the first argument. Try again")
        
        else:
            RandomNumber=self._randint()%(top-bot+1) #RandomNumber is the number of steps from bot where the number is located
            return bot+RandomNumber
        
    #resets the list of seeds
    def seed(self,value):
        try:
            self.seedlist=[]    
            self.myseed=int(value)
            self.seedlist.append(self.myseed)
            return self.myseed
        
        except ValueError:
            print ("The value needs to be an integer or a float. Try again please!")
        
    #returns a random float between 0 and 1  
    def rand(self):
        RandomInt=self._randint()
        RandomStrLen=len(str(RandomInt))
        return float(RandomInt*(10**-RandomStrLen))
    
    #takes a list as argument and returns a shuffled version of that list  
    def shuffle(self,thelist):
        """Using Durstenfeld's algorithm from https://en.wikipedia.org/wiki/Fisher%E2%80%93Yates_shuffle#Pseudorandom_generators"""
        self.thelist=thelist

        if isinstance(self.thelist,list)==False:
            print ('This method can only take a list as an argument. Please try again.')
        
        else:
            n=len(self.thelist) 
            for i in range(0, n-1):
                j=self.randint(i,n-1)
                self.thelist[i],self.thelist[j]=self.thelist[j],self.thelist[i]

            return self.thelist
    
    #selects a single item at random from a list   
    def choice(self,thelist):
        self.thelist=thelist

        if isinstance(self.thelist,list)==False:
            print ('This method can only take a list as an argument. Please try again.')
        
        else:
            RandomItem=self.thelist[self._randint()%(len(self.thelist))]
            return RandomItem
        


# In[ ]:


#provides dice toss functionality
class MyDie(MyRandom):
    def throw(self):
        self.result=self.randint(1,6)
        return self.result


# In[ ]:


#provides coin toss functionality
class MyCoin(MyRandom):
    def toss(self):
        Sides = ["Heads", "Tails"]
        return self.choice(Sides)


# In[ ]:





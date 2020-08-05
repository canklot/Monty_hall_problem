import random
    
def Game(change):

    doors = {'a':9 , 'b':9 ,'c':9}
    Prizes = [0, 1, 0]
    
    #Place random prize at doors
    for d in doors:
      myrandom = random.randint(0 , len(Prizes)-1)
      doors[d] = Prizes.pop(myrandom)
    
    #player choose a random door 
    player = random.choice(list(doors))
    
    #Reveal a unchoosen empty door 
    while True:
      revealedDoor = random.choice(list(doors))
      if revealedDoor != player and doors[revealedDoor] == 0 :
          doors.pop(revealedDoor)
          break
      
    #player change the door  
    if change:
        for x in range(len(doors)):
            if list(doors)[x] != player:
                player = list(doors)[x]
                break
        
    #Retrun win or loose
    if doors[player] == 1:
        return("win")
        
    elif doors[player] == 0:
        return("loose")
#-----------------------------------------------------

#Store results in a list
results = []
for x in range(1000000):
    results.append(Game(0)) #Game(0) for no door change
                            #Game(1) for change the door adter reveal    
#print(*results)

winCount = results.count("win")
looseCount = results.count("loose")

print("winCount   = " , winCount)
print("looseCount = " ,looseCount)


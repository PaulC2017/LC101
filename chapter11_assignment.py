def sort_contacts(theNames):
    newNames = []
    
    # put the names  into a list
    
    for names in theNames:
        newNames.append(names)
    
    # sort them
   
    newNames = sorted(newNames)
    
   
    # add the other info
   
    newNames2 = ["*"]*(len(newNames))
    
    for i in range(  len(newNames2) ): 
      
        # get all the info for each person and put it in a list so as to combine all info into a single tuple
        
        tempy = list( theNames.get(newNames[i]) )
        
        t = (newNames[i],tempy[0],tempy[1] )
        
        # now put each tuple into the list  
    
        newNames2[i] = t
        
   
    
    return newNames2 
# Testing that the arrays are the same shape for visualization overlap
print("Total size of the array:", CB0.size)  
print("Total size of the array:", NewCB0.size)

#Test that there are values within the array I created in the code above
print(percent_changes[3, 134]) # remember this is python so the indexing is a little bit different. Starts at 0 not 1 so to get the % change of CB3 at data point 133, I would use the previous point
print(percent_changes[3, -1]) # the last value when the system reaches steady state will most likely be the most useful number.
print(percent_changes[1,0]) 

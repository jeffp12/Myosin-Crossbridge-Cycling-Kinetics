import tellurium as te
import numpy as np

# Test that the intial concentration parameters sum to 1. This is critical as they proportions 
# Copy any changed parameters from the code above here
CB0 = 0.478
CB1 = 0.0
CB2 = 0.014
CB3 = 0.143
CB4 = 0.0
CB5 = 0.144
CB6 = 0.221
total = CB0 + CB1 + CB2 + CB3 + CB4 + CB5 + CB6

# Test if the total is approximately 1 (accounting for floating-point precision)
if abs(total - 1) == 0:  
    print("The variables sum to 1. Test passed!")
else:
    print(f"Oh no, test failed! The variables do not sum to 1. Total = {total}")

# Fucntional test to make sure the proportions add up to 1
new_total = new_CB0 + new_CB1 + new_CB2 + new_CB3 + new_CB4 + new_CB5 + new_CB6
# Print out the new values for adjustment to code parameters
new_conditions = {
    "NewCB0": new_CB0,
    "NewCB1": new_CB1,
    "NewCB2": new_CB2,
    "NewCB3": new_CB3,
    "NewCB4": new_CB4,
    "NewCB5": new_CB5,
    "NewCB6": new_CB6,
    "New Total": new_total
}
NewCB = pd.DataFrame(new_conditions.items(), columns=["State", "Value"])
print(NewCB)

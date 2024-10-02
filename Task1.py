# Help! My code is too messy :( Please help me organise it and extract out the duplications.

# Define your reusable functions here: 
def len_and_width():
# get the length and width of the first triangle from the user
    opp = float(input("Enter your first triangle's opposite side length: "))
    adj = float(input("Enter your first triangle's adjacent side length: "))
return(opp, adj)     
  
def hypotenuse(opp, adj):
    hyp = math.sqrt(opp**2 + adj**2)
return(hyp)   

def triangle_3_info(triangle_1_hyp, triangle_2_hyp):
    opp= triangle_1_hyp
    adj= triangle_2_hyp
return(opp, adj)
# Make sure each function only does ONE thing!!!!!!!!!!!



###########################################
triangle_1_info= len_and_width()
triangle_1_hyp= hypotenuse(triangle_1_info)
triangle_2_info= len_and_width()
triangle_2_hyp= hypotenuse(triangle_2_info)
triangle_3_hyp= hypotenuse(triangle_3_info)
print(triangle_3_hyp)


# After you have written the reusable functions, answer the following:
# Questions:
# 1. What are the preconditions for your code not to break? The opposite and adjacent valurs must be floats. 
# 2. Validate the user's input based on your preconditions. Its already validated..?
# 3. Why was it useful to use reusable components in this case? Please mention at least 2 reasons and don't forget to contextualise.
# Reason 1: It means that the program is more reliable since the functions are tested and known to work the way they should to output the third triangle's hypotenuse.
# Reason 2: It means that if changes must be made to the procedures carried out in the functions such as the input being changed to an integer the change would only have to be made once.



#Further Tasks:
# 1. Put your functions in seperate appropriate files and import them in.
# 2. In your new file add functions for SOH CAH TOA. Also for the sine and cosine rule.
# 3. Let the user choose whether they would like to use Pythogras, SOH, CAH, TOA, sine or cosine rule. Then ask for the relavent information and return the result to them.
# 4. Make sure all of your functions (except the main one) only do ONE thing or process.

# Extension:
# After you calculate the the result for the user. Use a library like Turtle to draw an approximation of their triangle for them.
# Hint: import the functions in drawing_functions.py and call them. See what happens. BTW check out the turtle docs for further info on how to use Turtle. 

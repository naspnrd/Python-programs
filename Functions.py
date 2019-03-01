#function in python
#A function is a set of statements that take inputs,
#do some specific computation and produces output.
##The idea is to put some commonly or repeatedly done
##task together and make a function, so that instead of
#writing the same code again and again for different inputs,
#we can call the function.

#even or odd 

##Pass by Reference or pass by value?

##One important thing to note is, in Python every variable name
##is a reference. When we pass a variable to a function, a new
##reference to the object is created. Parameter passing in
##Python is same as reference passing in Java.

# Here x is a new reference to same list list 
##def myFunction(val): 
##  val[0]=20
##  print(val)
##
### Driver Code (Note that lst is modified 
### after function call. 
##list = [100, 120, 130, 150] 
##myFunction(list); 
##print(list)

#output
#[20,120,130,150]
#[20,120,130,150]

##When we pass a reference and change the received reference to
##something else, the connection between passed and received parameter
##is broken.

##def myFunction(val): 
##  val = 20
##  print(val)
##
##list = [100, 120, 130, 150] 
##myFunction(list); 
##print(list)

#output
#20
#[100,120,130,150]

##Keyword arguments:
##    
##The idea is to allow caller to specify argument name with values
##so that caller does not need to remember order of parameters.
# Python program to demonstrate Keyword Arguments 
##def data(firstname, lastname): 
##	print(firstname, lastname) 
##	
##					 
##data(firstname ='neeraj', lastname ='chaudhary')	 
##data(lastname ='chaudhary', firstname ='neeraj') 

##Anonymous functions:
##    
##In Python, anonymous function means that a function is without a name.
##As we already know that def keyword is used to define the normal functions
##and the lambda keyword is used to create anonymous functions.


# using labmda function 
	
square = lambda x: x*x 
print(square(11))

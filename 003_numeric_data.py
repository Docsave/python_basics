#creating two variables
integer_value = 10
float_value = 5.5
#perform arithmetic operation and print the results
#Addition
addition = integer_value + float_value
print(f"Addition: {integer_value} + {float_value}={addition}")
#Subtraction
subtraction = integer_value - float_value
print(f"Subtraction: {integer_value} - {float_value}={subtraction}")
#Multiplication
multiplication = integer_value * float_value
print(f"multiplication: {integer_value} * {float_value}={multiplication}")
#Division
division = integer_value / float_value
print(f"division: {integer_value} / {float_value}={division}")
#Floor division
floor_division = integer_value // float_value
print(f"floor division: {integer_value} // {float_value}={floor_division}")
#Exponential
exponential = integer_value **2
print(f"exponential: {integer_value} **2 = {exponential}")
#Modulus
modulus = integer_value %3
print(f"modulus: {integer_value} %3 = {modulus}")
#calculation of expression
result_expression = (10+3)*2**2/4-1
print(f"result of(10+3)*2**2/4-1 = {result_expression}")
#use abs() function to print the absolute value of -15
absolute_value= abs(-15)
print(f"absolute value of -15 = {absolute_value}")
#use round() to round the float variable
rounded_one_decimal= round(float_value, 1)
rounded_two_decimals = round(float_value, 2)
print(f"rounded(1 decimal place): {rounded_one_decimal}")
print(f"rounded(2 decimal place): {rounded_two_decimals}")
#using two comparison operators to compare two variables
print(f"integer_value == float_value:{integer_value == float_value}")
print(f"integer_value != float_value:{integer_value != float_value}")
print(f"integer_value > float_value:{integer_value > float_value}")
print(f"integer_value < float_value:{integer_value < float_value}")
print(f"integer_value >= float_value:{integer_value >= float_value}")
print(f"integer_value <= float_value:{integer_value <= float_value}")
#perform data type casting
int_converted = int(float_value) #convert float to integer
print(f"float value{float_value} converted to integer:{int_converted}")
float_converted = float(integer_value) #convert integer to float
print(f"integer_value{integer_value} converted to float:{float_converted}")
string_to_int=int("20")#convert string to integer
print(f"string '20' converted to integer:{string_to_int}")



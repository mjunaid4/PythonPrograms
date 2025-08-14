import math
from statistics import mean, harmonic_mean

#function to calculate LCM for multiple numbers
def lcm(number):
    lcm_value = number[0]
    for i in number[1:]:
        lcm_value = (lcm_value * i) // math.gcd(lcm_value, i)   
    return lcm_value

#function to calculate GCD for multiple numbers
def gcd(number):
    gcd_value = number[0]
    for i in number[1:]:
        gcd_value = math.gcd(gcd_value, i)
    return gcd_value

#Taking input from user
numbers = list(map(int, input("Enter numbers separated by space: ").split()))

#Calculating LCM, GCD, Mean, and Harmonic Mean
lcm_value = lcm(numbers)
gcd_value = gcd(numbers)
mean_value = mean(numbers)
harmonic_mean_value = harmonic_mean(numbers)

#Displaying the results
print("Results:")
print(f"LCM: {lcm_value}")
print(f"GCD: {gcd_value}")
print(f"Mean: {mean_value}")
print(f"Harmonic Mean: {harmonic_mean_value}")
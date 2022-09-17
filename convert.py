import pandas as pd

print("Choose a scale for entering your temperature:")
print("1. Celsius")
print("2. Fahrenheit")
print("3. Kelvin")
choice=int(input('ENTER YOUR CHOICE NUMBER: '))

if choice==1:
    cel=float(input("Enter temperature: "))
    data=pd.DataFrame([[cel,(9/5)*cel+32,cel+273.15]],columns=list(["Celsius","Fahrenheit","Kelvin"]))
elif choice==2:
    fahr=float(input("Enter temperature: "))
    data=pd.DataFrame([[(fahr-32)*(5/9),fahr,(fahr-32)*(5/9)+273.15]],columns=list(["Celsius","Fahrenheit","Kelvin"]))
elif choice==3:
    kel=float(input("Enter temperature: "))
    data=pd.DataFrame([[kel-273.15,(kel-273.15)*(9/5)+32,kel]],columns=list(["Celsius","Fahrenheit","Kelvin"]))

print("Converter ended with the following output:")
print(data)
print("Thank You!!!")
input()
def cel_fahr():
    cel=float(input('Enter the temperature in Celsius(°C): '))
    fahr=(9/5)*cel+32
    print(f'The temperature in Fahrenheit is: {fahr}F')

def fahr_cel():
    fahr=float(input('Enter the temperature in Fahrenheit(F): '))
    cel=(fahr-32)*(5/9)
    print(f'The temperature in Celsius is: {cel}°C')

def cel_kel():
    cel=float(input('Enter the temperature in Celsius(°C): '))
    kel=cel+273.15
    print(f'The temperature in Kelvin is: {kel}K')

def kel_cel():
    kel=float(input('Enter the temperature in Kelvin(K): '))
    cel=kel-273.15
    print(f'The temperature in Celsius is: {cel}°C')

def kel_fahr():
    kel=float(input('Enter the temperature in Kelvin(K): '))
    fahr=(kel-273.15)*(9/5)+32
    print(f'The temperature in Kelvin is: {fahr}F')

def fahr_kel():
    fahr=float(input('Enter the temperature in Fahrenheit(F): '))
    kel=(fahr-32)*(5/9)+273.15
    print(f'The temperature in Kelvin is: {kel}K')

print('This is a temperature conversion tool. Choose from the below given options how you might like to convert temperature.')
print('How do you want to convert the temperature?')
print('1. Celsius->Fahrenheit')
print('2. Fahrenheit->Celsius')
print('3. Celsius->Kelvin')
print('4. Kelvin->Celsius')
print('5. Kelvin->Fahrenheit')
print('6. Fahrenheit->Kelvin')
choice=int(input('ENTER YOUR CHOICE NUMBER: '))
if choice==1:
    cel_fahr()
elif choice==2:
    fahr_cel();
elif choice==3:
    cel_kel()
elif choice==4:
    kel_cel()
elif choice==5:
    kel_fahr()
elif choice==6:
    fahr_kel()
print('Thank You!!!')
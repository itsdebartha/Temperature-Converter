# Temperature-Converter

![Python](https://img.shields.io/static/v1?label=Language%20Used&message=Python&color=blue&logo=python&logoColor=white)<br>
A repository for converting temperature entered by a user from a given scale to other units<br>
The underlying theory is the formula for conversion of temperatures from one unit to another. Suppose `cel` is the temperature in Celsius scale and you want to change it into `fahr`(Fahrenheit). Then the conversion is given as:<br>
![](https://latex2png.com/pngs/d6c12fdd6f27ad27810020ac282e3949.png)<br>
Similarly if you `kel` is the temperature in the Kelvin scale, then the conversion from `cel` is given by:<br>
![](https://latex2png.com/pngs/2156a8f977e31fd8ac9db2f364411e27.png)<br><br>
If the temperature is given in `fahr` and you need to change it to `kel` then the program first converts it to `cel` and then proceeds to convert that to `kel`.

### Usage
The program prompts the user to `Choose a scale for entering the temperature`. Upon entering the choice, the program then asks to `Enter temperature` and finally outputs a `pandas.DataFrame` which has:
- `Celsius`:  The temperature in Celsius scale (if value entered in Celsius, then same as input)
- `Fahrenheit`: The temperature in Fahrenheit scale (if value entered in Fahrenheit, then same as input)
- `Kelvin`: The temperature in Kelvin scale (if value entered in Kelvin, then same as input)

If an invalid option is chosen, the program exits with an error message. The program doesn't use any functions for these tasks however, it does the basic operations and returns the output as a `pandas.DataFrame`. Only one dependency is required and that is the `pandas` package. After the successful execution of the program, it prompts the user to hit `Enter` to exit.

### Example runs

```
Choose a scale for entering your temperature:
1. Celsius
2. Fahrenheit
3. Kelvin
ENTER YOUR CHOICE NUMBER: 1
Enter temperature: 37.8
Converter ended with the following output:
   Celsius  Fahrenheit  Kelvin
0     37.8      100.04  310.95
Thank You!!!
Press 'Enter' to exit
```

```
Choose a scale for entering your temperature:
1. Celsius
2. Fahrenheit
3. Kelvin
ENTER YOUR CHOICE NUMBER: 2
Enter temperature: 98.6
Converter ended with the following output:
   Celsius  Fahrenheit  Kelvin
0     37.0        98.6  310.15
Thank You!!!
Press 'Enter' to exit
```

```
Choose a scale for entering your temperature:
1. Celsius
2. Fahrenheit
3. Kelvin
ENTER YOUR CHOICE NUMBER: 3
Enter temperature: 308
Converter ended with the following output:
   Celsius  Fahrenheit  Kelvin
0    34.85       94.73   308.0
Thank You!!!
Press 'Enter' to exit
```

```
Choose a scale for entering your temperature:
1. Celsius
2. Fahrenheit
3. Kelvin
ENTER YOUR CHOICE NUMBER: 4
Wrong output
```

### Future Implementations
Coming soon to this is the ability to input multiple temperatures, ability to support various temperatures in one input and other cool improvements. A detailed documentation will also be provided.

----
The program was implemented in:
```
3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)]
```
----
### This repository contains
- **convert.py**: The main program

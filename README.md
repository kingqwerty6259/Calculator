# Basic Calculator (v1)

## Overview

This Python script is a simple command-line calculator that allows users to perform basic mathematical operations between two numbers. Users can input two numbers and select an operation (addition, subtraction, multiplication, or division). The calculator then displays the result.

## Requirements

- Python 3.x

## How to Use

1. Run the script.
2. Follow the prompts:
   - Enter the first number.
   - Enter the second number.
   - Enter the operation type (`+`, `-`, `*`, or `/`).
3. The script will display the result or an error message if invalid input is detected.
4. To exit the script, use `Ctrl + C`.

## Supported Operations

- `+` : Addition
- `-` : Subtraction
- `*` : Multiplication
- `/` : Division (note: division by zero will return an error message)

## Code Details

1. The `doMath()` function prompts the user for two numbers and an operation.
2. It validates each input to ensure only valid numbers and operations are accepted.
3. If both inputs are numbers, they are parsed as integers or floats as necessary.
4. Based on the operation, the function performs the corresponding calculation and prints the result.
5. The program runs in an infinite loop (`while run:`), allowing repeated calculations until manually stopped.

## Example

```plaintext
Calculator
Enter First Number: 12
Enter Second Number: 4
Enter Operation Type (+,-,*,/): *
12 x 4 = 48

Enter First Number: 9
Enter Second Number: 0
Enter Operation Type (+,-,*,/): /
Division by 0 isn't possible
```

This basic calculator is designed for quick, simple calculations directly from the command line.

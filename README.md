# Matrix-Operation-tool

An interactive Python application that allows users to perform common matrix operations using NumPy, with a colorful and structured interface using Colorama and Tabulate.

Features

Input matrices of any size dynamically.

Perform Matrix Addition, Subtraction, Multiplication.

Compute Transpose of a matrix.

Calculate Determinant for square matrices.

Displays results in structured tables for easy reading.

Color-coded menu and messages for better user experience.

Handles invalid inputs gracefully.

Requirements

Python 3.x

Libraries:

NumPy → pip install numpy

Tabulate → pip install tabulate

Colorama → pip install colorama

Installation

Clone the repository or download the script matrix_tool.py.

Install the required libraries:

pip install numpy tabulate colorama


Run the application:

python matrix_tool.py

Usage

Run the program using Python:

python matrix_tool.py


Choose the operation you want to perform from the menu:

1. Matrix Addition
2. Matrix Subtraction
3. Matrix Multiplication
4. Matrix Transpose
5. Matrix Determinant
6. Exit


Input the matrix dimensions and elements when prompted.

View results in a structured, color-coded table.

Repeat for other operations or choose Exit to quit.

Example
Select an operation:
1. Matrix Addition
2. Matrix Subtraction
3. Matrix Multiplication
4. Matrix Transpose
5. Matrix Determinant
6. Exit

Enter your choice (1-6): 1

Enter the number of rows for Matrix A: 2
Enter the number of columns for Matrix A: 2
Enter the elements row-wise, separated by space:
Row 1: 1 2
Row 2: 3 4

Enter the number of rows for Matrix B: 2
Enter the number of columns for Matrix B: 2
Enter the elements row-wise, separated by space:
Row 1: 5 6
Row 2: 7 8

Result:
╒═════╤═════╕
│ 6.0 │ 8.0 │
├─────┼─────┤
│ 10.0│ 12.0│
╘═════╧═════╛

Notes

Matrix Addition/Subtraction: Requires matrices of the same dimensions.

Matrix Multiplication: Number of columns in the first matrix must equal the number of rows in the second.

Determinant: Only for square matrices.

import numpy as np
from tabulate import tabulate
from colorama import Fore, Style, init

init(autoreset=True)  # Initialize colorama

def input_matrix(name="Matrix"):
    """Function to input a matrix from the user"""
    try:
        rows = int(input(f"{Fore.CYAN}Enter the number of rows for {name}: "))
        cols = int(input(f"{Fore.CYAN}Enter the number of columns for {name}: "))
    except ValueError:
        print(f"{Fore.RED}Please enter valid integers for rows and columns.")
        return None

    print(f"{Fore.YELLOW}Enter the elements row-wise, separated by space:")
    matrix = []
    for i in range(rows):
        while True:
            row = input(f"Row {i + 1}: ").strip().split()
            if len(row) != cols:
                print(f"{Fore.RED}Please enter exactly {cols} values.")
            else:
                try:
                    matrix.append([float(x) for x in row])
                    break
                except ValueError:
                    print(f"{Fore.RED}Please enter numeric values only.")
    return np.array(matrix)

def display_matrix(matrix, name="Result"):
    """Function to display a matrix in a table format"""
    print(f"\n{Fore.GREEN}{name}:")
    print(tabulate(matrix, tablefmt="fancy_grid", floatfmt=".2f"))
    print("-" * 40)

def matrix_operations():
    print(f"{Fore.MAGENTA}Welcome to the Enhanced Matrix Operations Tool!\n")
    
    while True:
        print(f"{Fore.BLUE}Select an operation:")
        print(f"1. Matrix Addition")
        print(f"2. Matrix Subtraction")
        print(f"3. Matrix Multiplication")
        print(f"4. Matrix Transpose")
        print(f"5. Matrix Determinant")
        print(f"6. Exit")
        
        choice = input(f"{Fore.CYAN}Enter your choice (1-6): ").strip()
        
        if choice == "1":
            print(f"\n{Fore.YELLOW}Matrix Addition")
            A = input_matrix("Matrix A")
            B = input_matrix("Matrix B")
            if A is not None and B is not None:
                if A.shape == B.shape:
                    display_matrix(A + B, "A + B")
                else:
                    print(f"{Fore.RED}Error: Matrices must have the same dimensions for addition.")
        
        elif choice == "2":
            print(f"\n{Fore.YELLOW}Matrix Subtraction")
            A = input_matrix("Matrix A")
            B = input_matrix("Matrix B")
            if A is not None and B is not None:
                if A.shape == B.shape:
                    display_matrix(A - B, "A - B")
                else:
                    print(f"{Fore.RED}Error: Matrices must have the same dimensions for subtraction.")
        
        elif choice == "3":
            print(f"\n{Fore.YELLOW}Matrix Multiplication")
            A = input_matrix("Matrix A")
            B = input_matrix("Matrix B")
            if A is not None and B is not None:
                if A.shape[1] == B.shape[0]:
                    display_matrix(np.dot(A, B), "A x B")
                else:
                    print(f"{Fore.RED}Error: Number of columns in A must equal number of rows in B.")
        
        elif choice == "4":
            print(f"\n{Fore.YELLOW}Matrix Transpose")
            A = input_matrix("Matrix")
            if A is not None:
                display_matrix(A.T, "Transpose")
        
        elif choice == "5":
            print(f"\n{Fore.YELLOW}Matrix Determinant")
            A = input_matrix("Matrix")
            if A is not None:
                if A.shape[0] == A.shape[1]:
                    det = np.linalg.det(A)
                    print(f"{Fore.GREEN}\nDeterminant: {det:.2f}")
                    print("-" * 40)
                else:
                    print(f"{Fore.RED}Error: Determinant can only be calculated for square matrices.")
        
        elif choice == "6":
            print(f"{Fore.MAGENTA}Exiting Matrix Operations Tool. Goodbye!")
            break
        
        else:
            print(f"{Fore.RED}Invalid choice. Please select a valid option (1-6).")

if __name__ == "__main__":
    matrix_operations()

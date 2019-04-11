import codes
import os
import time
#Aici ai switch-ul, pentru fiecare obtiune apelez functia, iar la search deschid un alt switch
def switch(lines,matrix,new_lines):
    while True:
        print("Type 'read' to read the matrix.")
        print("Type 'print' to print the matrix.")
        print("Type 'add' to add 2 matrices.")
        print("Type 'acces' to acces an item.")
        print("Type 'search' to open the search menue.")
        print("Type 'multiply' to multiply 2 matrices")
        print("Type 'compare' to lexicographically compare 2 matrices")
        print("Type anything else to exit.")
        action = input(': ')
        if "read" in action:
            codes.read_matrix(lines, matrix)
        elif "print" in action:
            codes.print_matrix(lines, matrix)
        elif "add" in action:
            print("Note, if the matrices are diferent size the program won't return an error, rather it will compute the matrices eitherway")
            time.sleep(3)
            matrix=codes.matrix_addition(lines,matrix,new_lines)
            lines = int(new_lines[0])
        elif "acces" in action:
            codes.access_item(lines,matrix)
        elif "multiply" in action:
            matrix=codes.matrix_multiplication(lines,matrix,new_lines)
            lines = int(new_lines[0])
        elif "search" in action:
            while True:
                print("Type 'first' to search the first aparition of the string.")
                print("Type 'all' to search all the aparitions of the string.")
                print("Type 'last' to search for the last aparition of the string.")
                print("Type anything else to exit.")
                action_2=input(': ')
                if "first" in action_2:
                    codes.search_item_1st(matrix,lines)
                elif "all" in action_2:
                    codes.search_item_all(matrix,lines)
                elif "last" in action_2:
                    codes.search_item_last(matrix,lines)
                else:
                    break
                time.sleep(2)
                os.system('cls')
        elif "compare" in action:
            codes.lex_copare(lines,matrix)
        else:
            break
        input('Press enter to continue...')
        os.system('cls')
def read_matrix(lines,matrix):
    for i in range(lines):
         for j in range(lines):
             matrix[i][j]=input("matrix[" + str(i) + "][" + str(j) + "]= ")#aici citesc matricea

def print_matrix(lines,matrix):
    for i in range(lines):
        print()
        for j in range (lines):
            print(matrix[i][j], end = " ")#Aici o afisez, end=" " face ca printul sa nu mai dea enter si " "
    print()#asta practic e endl

def size_determination(matrix):
    j = 0
    for i in matrix:
        j += 1#in python nu merce cu ++ asa ca +=... a si determin marimea matricii introduse
    return j

def matrix_addition(lines,matrix,new_lines):
    lines_2 = int(input('The length of the 2nd matrix: '))#ok aici citesc alta matrice ca sa o adun
    matrix_to_add = [[0 for i in range(lines_2)] for j in range(lines_2)]#o initializez
    read_matrix(lines_2,matrix_to_add)#o citesc
    if size_determination(matrix) <= size_determination(matrix_to_add):#daca matricea intiala e mai mica decat aia introduse aici
        for i in range(lines):#atunci facem asa
            for j in range(lines):
                matrix_to_add[i][j] = matrix[i][j] + matrix_to_add[i][j]#aici le adun
        matrix = [[0 for i in range(lines_2)] for j in range(lines_2)]#maresc matricea intiala
        new_lines[0]=lines_2#aici maresc si new_linse ca apoi sa schimb permanent lines practic schimb liniile citite
        for i in range(lines_2):
            for j in range(lines_2):
                matrix[i][j] = matrix_to_add[i][j]#aici schimb matricea element cu element
        return matrix#ca in forurile trecute calculeaza in matricea introdusa aici
    else:
        for i in range(lines_2):
            for j in range(lines_2):
                matrix[i][j] += matrix_to_add[i][j]#aici intrii daca matricea initiala e egala sau mai mare cu aia
        return matrix#intodusa aici si practic nu mai am nev sa o maresc


def access_item(lines,matrix):#aici accesezi un singur string din toata matricea
    print(len(matrix),end=" ")#len(matric) e lungimea matricii, aparent o vede ca pe o lista ce are comanda de len
    print("this is the maximum value")
    i=int(input('The number of the line: '))
    j=int(input('The numbe of the column: '))
    if i > lines or j > lines:
        print("Out of range")#in caz ca sunt val prea mari la iteratori, da eroare
        return 0
    print("The string accesed is:",end=" ")
    print(matrix[i][j])
    return matrix[i][j]


def search_item_1st(matrix,lines):#aici faci cautarea unui string(matrix[i][j]), si se opreste la prima aparitie
    sir = input("Enter the string you want to search: ")
    for i in range(lines):
        for j in range(lines):
            if matrix[i][j]==sir:
                print("The string was found at the coornates: " + str(i) + " " + str(j))#afsez doar coordonatele la care a fost
                return 0#gasit sirul
    print("The string couldn't be found")#si aici in caz mu gaseste

def search_item_last(matrix,lines):#aici afisez coord la ultima aparitie la sirul cautat
    sir = input("Enter the string you want to search: ")
    a = int(-1)
    b = int(-1)
    for i in range(lines):
        for j in range(lines):
            if matrix[i][j]==sir:
                a = i
                b = j
    if a == -1 and b == -1:
        print("The string couldn't be found in the matrix")
    else:
        print("The string was found at the coornates: " + str(a) + " " + str(b))

def search_item_all(matrix,lines):#si aici afisez toate aparitiile
    sir = input("Enter the string you want to search: ")
    for i in range(lines):
        for j in range(lines):
            if matrix[i][j]==sir:
                print(str(i) + " " + str(j))
    print("The string couldn't be found!")

def matrix_multiplication(lines,matrix,new_lines):#aici trebuie inmultite matricile
    lines_2 = int(input('The length of the 2nd matrix: '))
    matrix_to_add = [[0 for i in range(lines_2)] for j in range(lines_2)]#citesc alta matrice, cu care inmultesc
    read_matrix(lines_2,matrix_to_add)
    if lines_2 < lines:
        new_lines[0] = str(lines_2)#modific marimea matricii initiale, bine asta cand se termina functia
    alt_line=new_lines[0]#asta il folosesc ca si iterator in unul din foruri
    for i in range(lines):#for(i=0;i<lines;i++)
        for j in range(len(matrix_to_add)):
            for k in range(lines_2):
              h =multiply_items(matrix[i][k],matrix_to_add[k][j])#aici folosesc h ca rezultat la apelul functiei
              if h!=matrix[i][k]:#daca funtia apelata anterior a modificat sirul intram in if
                if k==0:#ptr k=0 nu facem chestia de mai jos ca ar aduna de mai multe ori decat trebuie ex 
                    matrix[i][j]=h#daca avem a si a ar trebuii sa dea a dar daca lasi fara k=0 o sa iti dea aa
                else:
                    matrix[i][j] += h#aici matricea o adun cu h gen adun a cu b si da ab
    for i in range(int(alt_line)):
        print()
        for j in range(int(alt_line)):
            print(matrix[i][j],end=" ")#aici am bagat afisajul matricii dupa inmultire da sunt sigur ca poti folosii si
    return matrix#functia de print de am facut-o mai sus

def multiply_items(x,y):#ei asta e functia pentru inmultire
    z="\n"#tu daca ax si bb pentru inmultire trebuie sa faci ascii(el din bb) - ascii(a)(da doar primul element)
    a="o"#apoi rezultatul in cazul de mai sus va da "11" b=97, a=96 97-96=1, cum sunt 2 el da 11
    b=x#deci va trebuii sa scrii ax de 11 ori
    for i in y:
     if ord(i) < ord(x[0]):#aici fac codul ascii ord e functia ptr transformarea in ascii
         z= ord(x[0])-ord(i)#memorez cat da
     else:
         z = ord(i)-ord(x[0])#asta e cazul in care primul el din primul sir e mai mic decat ala din al 2-lea sir
     a = a + str(z)#aici in sirul a bag z si "o" sa fie o11 ca a il initializez cu "o" ca sa stie ca e string
    i, z= a.split("o")#functia split e ca strtok, si in cazul asta in z o sa ramana tot ce e dupa o iar in i nu baga nimic
    for i in range (0, int(z)):
     if i!=0:
       x += b#aici calculam x de b ori
    return x

def lex_copare(lines,matrix):#comparare lexicografica
    lines_2 = int(input('The length of the 2nd matrix: '))
    matrix_to_add = [[0 for i in range(lines_2)] for j in range(lines_2)]#citesc alta matrice cu care sa compar
    read_matrix(lines_2,matrix_to_add)
    if lines_2 < lines:#intializez length cu cea mai mica marime dintre matrici
        length = lines_2
    else:
        length = lines
    for i in range(int(length)):
        for j in range(int(length)):
            if matrix[i][j] > matrix_to_add[i][j]:#testez sa vad care e mai mare
                print("The string with coornates: " +str(i) +" "+str(j)+" is bigger")#daca matrix[i][j] e mai mare
                print("Thus the matrix you added is smaller than the original matrix")#atunci afisez ca mat initiala e mai mare
                return 0
            elif matrix[i][j] < matrix_to_add[i][j]:
                print("The string with coornates: " +str(i) +" "+str(j)+" is bigger")
                print("Thus the matrix you added is bigger than the original matrix")
                return 0
    if lines_2 < lines:#si aici daca a iesit cu toate itemele egale vad care dintre matrici e mai mare
        print("The original matrix is bigger!")
    elif lines_2 > lines:
        print("The original matrix is smaller!")
    else:
        print("The matrices are equal!")

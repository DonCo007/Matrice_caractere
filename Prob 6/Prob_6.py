import options
matrix = list(),list()
lines= int(input('Input the number of lines and columns from options the matrix: '))#Aici citesc liniile
matrix = [[0 for i in range(lines)] for j in range(lines)]#Aici aloc spatiu matricii si intializez toate val cu 0
new_lines = ["0"]#Asta e un 'vector' defapt o lista cu un element, o folosesc sa schimb nr de linii la matrice in anumite func
new_lines[0] = lines

options.switch(lines,matrix,new_lines)#Apelez switchul

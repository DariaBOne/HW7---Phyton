def print_operation_table(operation, rows, columns):
    for x in range(1, rows+1):
        for y in range(1, columns+1):
            print(f"{operation(x,y):>6}", end = "")
        print()
def multipl(i,j):
    return i*j
print_operation_table(multipl,6,6)
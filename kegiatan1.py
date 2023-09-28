# Fungsi tambah
def add(a, b):
    return a + b

# Fungsi pengurangan
def minus(a, b):
    return a - b

# Fungsi perkalian
def mult(a, b):
    return a * b

# Fungsi pembagian
def div(a, b):
    if b == 0:
        return "Tidak bisa dibagi oleh nol"
    return a / b

# Fungsi pohon ekspresi
def tree(node):
    if type(node) in (int, float):
        return node
    elif type(node) is tuple and len(node) == 3:
        operator, left_operand, right_operand = node
        left_result = tree(left_operand)
        right_result = tree(right_operand)
        
        if left_result is None or right_result is None:
            return None  # Mengembalikan None jika ada operan yang tidak valid
        
        if operator == '+':
            return add(left_result, right_result)
        elif operator == '-':
            return minus(left_result, right_result)
        elif operator == '*':
            return mult(left_result, right_result)
        elif operator == '/':
            return div(left_result, right_result)
    else:
        return None  # Mengembalikan None jika node tidak valid

# Contoh pohon ekspresi: (2 + 3) * (5 - 1)
expression_tree = ('*', ('+', 2, 3), ('-', 5, 1))

# Evaluasi pohon ekspresi dengan fungsi pada paradigma fungsional
result = tree(expression_tree)
if result is not None:
    print("Hasil evaluasi pohon ekspresi:", result)
else:
    print("Pohon ekspresi tidak valid")

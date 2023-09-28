random_list = [105, 3.1, "Hello", 737, "Python", 2.7, "World", 412, 5.5, "AI"]

int_values = {}
float_values = ()
string_values = []

for item in random_list:
    item_type = type(item)

    if item_type is int:
        # Memisahkan angka satuan, puluhan, dan ratusan
        satuan = item % 10
        puluhan = (item // 10) % 10
        ratusan = item // 100

        # Menyimpan dalam dictionary
        int_values[item] = {"ratusan": ratusan, "puluhan": puluhan, "satuan": satuan}
    elif item_type is float:
        # Menyimpan dalam tuple
        float_values += (item,)
    elif item_type is str:
        # Menyimpan dalam list
        string_values.append(item)

print("Data integer dalam bentuk dictionary:")
print(int_values)
print("\nData float dalam bentuk tuple:")
print(float_values)
print("\nData string dalam bentuk list:")
print(string_values)

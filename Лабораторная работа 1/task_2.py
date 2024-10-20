# TODO Найдите количество книг, которое можно разместить на дискете

lists_in_book = 100
string_in_list = 50
simbols_in_string = 25
size_of_simbol = 4
oneKB=1024
totalsiz = (lists_in_book*string_in_list*simbols_in_string*size_of_simbol)/oneKB

available_size=1.44*oneKB

number_of_books = available_size//totalsiz



print("Количество книг, помещающихся на дискету:", int(number_of_books))

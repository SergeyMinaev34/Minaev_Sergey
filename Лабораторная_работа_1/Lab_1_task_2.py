# TODO Найдите количество книг, которое можно разместить на дискете
disk = 1.44
book_pages = 100
book_strings = 50
symbols_in_string = 25
symbol = 4

one_book_size = book_pages * book_strings * symbols_in_string * symbol
disk_size = disk * 1024 * 1024

print("Количество книг, помещающихся на дискету:", int(disk_size // one_book_size))

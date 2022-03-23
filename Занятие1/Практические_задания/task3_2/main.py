BYTES_ONE_CHAR = 1

pages = 100
lines = 50
chars = 25

total_chars = chars * lines * pages
total_bytes = BYTES_ONE_CHAR * total_chars

disk_size = 1.44 * 1024 * 1024

print(disk_size // total_bytes)  # TODO найти количество книг, которое поместится на дискете

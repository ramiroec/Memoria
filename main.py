import psutil

total_ram = psutil.virtual_memory().total / (1024 ** 3)
print(f"La cantidad total de memoria RAM es de {total_ram:.2f} GB")

string = """## UC0{:02d}
![images/seq_diag/uc0{:02d}.png](images/seq_diag/uc0{:02d}.png)\n"""

for i in range(1, 16):
    print(string.format(i, i, i))
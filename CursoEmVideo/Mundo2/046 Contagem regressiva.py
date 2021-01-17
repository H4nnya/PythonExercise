from time import sleep

while True:
    for c in range(10,-1, -1):
        sleep(1.0)
        print(f' {c}')
    input(' 🎉 \033[33mB\033[34mO\033[35m0\033[36mM\033[m 🎉')

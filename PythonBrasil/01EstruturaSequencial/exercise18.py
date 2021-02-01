"""
Faça um programa que peça o tamanho de um arquivo para download (em MB)
e a velocidade de um link de Internet (em Mbps), calcule e informe o tempo
aproximado de download do arquivo usando este link (em minutos).
"""
size = int(input('Digite o tamanho do arquivo(Megabyte): '))
velocity = int(input('Digite a velocidade da internet(Mbps): '))
time = int(size / (velocity / 8))
minute = second = 0
while time > 0:
    if time >= 60:
        time -= 60
        minute += 1
    else:
        second = time
        time = 0
print(f'O tempo estimado é de {minute} Minuto(s) e {second} Segundo(s)')

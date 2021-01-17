from os import system

while 1:
    system('clear')
 
    altura = float(input('Digite sua altura em metros:\033[33m '))
    peso = float(input('\033[m Digite seu peso (kg):\033[33m '))
    imc = peso/(altura**2)
 
    print(' \033[m\n IMC \033[32m{:.2f}\033[m'.format(imc))
 

    if imc < 18.5:
          print(' Você está \033[33mabaixo do peso\033[m.\n Recomendo para a sua saúde que ganhe mais peso.'.format(imc))
 
    elif imc <= 24.99 and imc >= 18.5:
          print(' Seu peso está \033[32mnormal\033[m\n continuei se alimentando bem e fazendo exercícios.'.format(imc))
 
    elif imc >= 25 and imc <= 29.99:
          print(' Você está com \033[32msobrepeso\033[m.\n Recomendo uma alimentação saudável e exercícios.')
 
    elif imc >= 30 and imc <= 34.99:
          print(' Você tem \033[31mObesidade grau 1\033[m.\n Recomendo comidas mais saudáveis e muito execícios físicos.')
 
    elif imc >= 35  and imc <= 39.99:
          print(' Você \033[31mObesidade grau 2\033[m.\n Recomendo comidas mais saudáveis e muito exercícios físicos.')
 
    elif imc > 40:
          print(' Você \033[31mObesidade grau 3\033[m.\n Recomendo comidas mais saudáveis e muito exercícios físicos.')
     
    input('\n Aperte \033[36mEnter\033[m para reiniciar... ')

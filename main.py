altura = float(input('Qual a sua altura em cm: '))
peso = float(input('Qual e o seu peso em kg: '))

IMC = peso / (altura/100)**2

print(IMC)

if IMC < 18.5:
    print(f'Seu IMC é de {IMC}, e é classificado como Magreza')

elif IMC >= 18+5 and IMC < 24.9:
    print (f'Seu IMC é de {IMC}, e é classificado como Normal')

elif IMC >= 25 and IMC < 29.9:
    print (f'Seu IMC é de {IMC}, e é classificado como Sobrepeso')

elif IMC >= 30 and IMC < 39.9:
    print (f'Seu IMC é de {IMC}, e é classificado como Obeso')

else: 
    print ("Pode parar de comer e começar a malhar pois o negócio está feio! Obesidade Grave")
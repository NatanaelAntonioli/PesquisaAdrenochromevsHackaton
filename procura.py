

contador_presente = 0
contador_ausente = 0
AUSENTES = []

with open('Adreno.txt', 'r') as file:
        # reading each line
    for line in file:

            # reading each word
        for word in line.split():

            if word.isalpha():

                if word.replace(",","") in open('hacka.txt').read():
                    contador_presente = contador_presente + 1;
                else:
                    if word in AUSENTES:
                        pass
                    else:
                        AUSENTES.append(word)
                        contador_ausente = contador_ausente + 1;
                        print(word)


print("O total de palavras presentes é: " + str(contador_presente))
print("O total de palavras ausentes é: " + str(contador_ausente) + " e elas estão acima.")
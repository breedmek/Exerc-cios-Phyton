# 2° Desafio

class removerletrasRepetidas:

    def removeLetrasRepetidas(frase):

        caracteresUnicos = []
        for letra in frase:
            if letra not in caracteresUnicos:
                caracteresUnicos.append(letra)
        return ''.join(caracteresUnicos)

    frase = input('Digite uma frase com letras repetidas: ') # Exemplo : "Hello, World!"
    fraseSemRepeticao = removeLetrasRepetidas(frase)
    print(fraseSemRepeticao)
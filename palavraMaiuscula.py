# 4°. Desafio

class palavrasMaiusculas:

    def capitalizar_frases(texto):
        
        texto = texto.split('. ')
        frases = []
        for frase in texto:
            frases.append(frase.capitalize()+'. ')
        return ''.join(frases).replace('..','.')

    frases = input('Digite uma frase: ')
    textoFinal = capitalizar_frases(frases)

    print(textoFinal)


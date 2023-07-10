# 1° Desafio
class fraseInversa:

    def fraseInvertida(frase):

        palavras = frase.split()
        frases = []
        if frases != palavras:
            frases = palavras[-1::-1]
        return " ".join(frases)

    frase = input('Digite uma frase: ') # Exemplo: 'Hello, World! OpenAI is amazing'
    fraseInver = fraseInvertida(frase)
    print(fraseInver)


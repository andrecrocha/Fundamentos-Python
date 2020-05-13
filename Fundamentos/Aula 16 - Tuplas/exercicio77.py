""" Desafio 77. Fazer uma lista com palavras e mostrar suas vogais. """

palavras = ("Abacaxi",
            "TomateE",
            "Alface",
            "Arroz",
            "Quiabo",
            "Vagem")

for itens in palavras:
    print(f"\nA palavra {itens} tem essas vogais = ", end=" ")
    for letra in itens:
        if letra.lower() in "aeiou":
            print(letra.lower(), end=" ")
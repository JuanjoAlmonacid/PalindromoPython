#JUAN ALMONACID
#creamos una funcion llamada reverse
#que se encargara de invertir la palabra ingresada
#recorriendo un for char, de esta manera se itera cada caracter
#y lo reordenada al reves
def reverse(texto):
    texto_al_reves = ""
    for char in texto:
        texto_al_reves = char + texto_al_reves
    return texto_al_reves

#toma una cadena de texto como entrada y devuelve una nueva cadena
#que contiene todos los caracteres de la cadena original, excepto los espacios en blanco
def no_space(texto):
    nuevo_texto = ""
    for char in texto:
        if char != " ":
            nuevo_texto += char
    return nuevo_texto

#en esta funcion tomamos la palabra ingresada, lo dejamos en minuscula
#luego de que se quitaran los espacio y se colocara invertida
#se comparara con la cedena original y si es palindromo sera TRUE y sino FALSE
def es_palindromo(texto):
    texto = no_space(texto)
    texto_al_reves = reverse(texto)
    return texto.lower() == texto_al_reves.lower()

#JUAN ALMONACID

print("Abba", es_palindromo("Abba"))
print("Reconocer", es_palindromo("Reconocer"))
print("Amo la paloma", es_palindromo("Amo la paloma"))
print("Hola mundo", es_palindromo("Hola mundo"))


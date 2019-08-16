#Importar collections para contar y re para buscar palabras.
import collections, re
import matplotlib.pyplot as plt

#Abrir el documento y encontrar las palabras mediante un regex.
words = re.findall(r'\w+', open(str(input('Ingrese el nombre de archivo: '))).read().lower())
#Usar Counter para contar y devolver en una lista las 10 mas usadas.
c = collections.Counter(words).most_common(10)
#Eje y
y = [i[1] for i in c]

#Eje x
x = [i[0] for i in c]
#Creación del gráfico.
plt.bar(x, y,align='center', width=0.4, color='red')
plt.xlabel('Palabras')
plt.ylabel('Cantidad')
plt.title('Palabras más usadas')
plt.show()

grades = [4,5,6,7,8,3,4,5,6,7,2]
# ¿Cómo podríamos filtrar los números pares y los impares?
# Pares
even = []
# Impares
odd = []

# Es par cuando el resto o residuo de dividir al número en 2 es cero
for grade in grades:
  if grade % 2 == 0:
      even.append(grade)
  else:
      odd.append(grade)

print(f"Los pares son {even}")
print(f"Los impares son {odd}")


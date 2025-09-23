""" 1. Variabler & Datatyper """

name = "User1"
age = 102
height = 159.5

print(str(name), int(age), float(height))

print(type(name),"for", name)
print(type(age), "for", age)
print(type(height), "for", height)


# 2 Input & Utskrift
color = input("Vilken är din favoritfärg? ")
tal1 = int(input("Ge mig ett heltal: "))
tal2 = int(input("Ge mig ett till heltal: "))
print(f"Din favoritfärg är {color} och summan av dina heltal blir {tal1 + tal2}")


# 3. Strängformatering

print(str("Mitt namn är ... och jag är ... år"))
upperStr = str(input("Skriv en mening"))
x = upperStr.upper()
print(x)
print(len(x))


# 4. Loopar och villkor
# a)
for z in range(1, 11):
  print(z)

# b)
for y in range (5, 0, -1):
  print(y)
else:
  print("Klar")

# c)
age = int(input("hur gammal är du? "))
if (age >= 18):
  print("Du är mynding")
else:
  print("Du är omynding") 

# 5. Listor

# a)
movies = ["Programmerings Film", "DevOps Film", "IT Film"]
# b)
movies.append("Chas Academy Film")
# c)
for x in movies:
  print(x)
# d)
print("Första filmen: ", movies[0])
print("Sista filmem: ", movies[-1])

# 6. Dictionaries
# a)
obj = {
  'name': "Testar",
  'ålder': 5,
  'stad': "Stockholm"
}
# b)
print(obj)
# c)
obj["favoritfärg"] = "guld"
# d) Loopa igenom dictionary
for key, value in obj.items():
  print(f"{key}: {value}")

# 7. Mini proj - Komplett program
print("\n=== MINI-PROJEKT ===")
# 1. Fråga användaren
namn = input("Vad heter du? ")
alder = int(input("Hur gammal är du? "))
favoritfarg = input("Vad är din favoritfärg? ")

# 2. Spara i dictionary
user_info = {
  'namn': namn,
  'ålder': alder,
  'favoritfärg': favoritfarg
}

# 3. Lägg till favoritfilmer i lista
favoritfilmer = []
print("Ange dina 3 favoritfilmer:")
for i in range(3):
  film = input(f"Film {i+1}: ")
  favoritfilmer.append(film)

# 4. Personlig hälsning och sammanfattning
print(f"\n🎬 Hej {namn}!")
print(f"Du är {alder} år gammal och din favoritfärg är {favoritfarg}.")
print("Dina favoritfilmer är:")
for film in favoritfilmer:
  print(f"- {film}")

# 5. Extra rad för minderåriga
if alder < 18:
  print("Du är minderårig.")
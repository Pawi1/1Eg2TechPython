# Zadanie 1

print("Zadanie 1: Program, który sprawdzi, czy wpisana liczba jest podzialna przez 3")

print("Wpisz liczbe a:")
input_a = int(input())

if input_a%3==0:
 print("Tak")
else:
 print("Nie")

# Zadanie 2

print("Zadanie 2: Program, który sprawdzi, czy wpisana liczba jest trzycyfrowa i podzielna przez 17.")

print("Wpisz liczbe a:")
input_a = int(input())

if 100 <= input_a  >= 999 & input_a%17==0 :
 print("Tak")
else:
 print("Nie")

# Zadanie 3

print("Zadanie 3: Program, który sprawdzi, czy użytkownik jest osobą pełnoletnią")
print("Wpisz wiek:")
input_a = int(input())
if input_a<18:
 print("Jesteś niepełnoletni")
else:
 print("Jesteś pełnoletni")

# Zadanie 4

print("Zadanie 4: Program, który sprawdzi, czy ciężarówka może wjechać bezpiecznie na most. Max obciążenie mostu przyjmij na sztywno na 20 ton. Utwórz stałą o nazwie limit")
print("Wpisz wage:")
input_a = int(input())
if input_a>20:
 print("Nie możesz wjechać na most")
else:
 print("Możesz bezpiecznie wjechać na most")
 
# Zadanie 5 
# Przykłady:
# 3 6 5 – TAK
# 4 8 9 – NIE
# 3 8 3 – NIE
# 6 3 5 – TAK
print("Zadanie 5: Program, który sprawdzi, czy trzecia z podanych liczb mieści się między pierwszą a drugą. Weź pod uwagę, że kolejność wpisywania dwóch pierwszych liczb może nie być zachowana")

print("Wpisz liczbe a:")
input_a = int(input())
print("Wpisz liczbe b:")
input_b = int(input())
print("Wpisz liczbe c:")
input_c = int(input())
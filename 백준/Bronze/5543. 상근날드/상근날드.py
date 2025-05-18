burger_A = int(input())
burger_B = int(input())
burger_C = int(input())
soda_A = int(input())
soda_B = int(input())
set_burger = burger_A
set_soda = soda_A

if burger_B <= set_burger:
    set_burger = burger_B
if burger_C <= set_burger:
    set_burger = burger_C

if soda_B <= set_soda:
    set_soda = soda_B

set_total = set_burger + set_soda - 50
print(set_total)
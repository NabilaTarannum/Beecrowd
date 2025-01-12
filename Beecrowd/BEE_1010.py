# -*- coding: utf-8 -*-

"""
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
"""

code_of_a_product_1, units_of_product_1, price_1 = input().split()
code_of_a_product_2, units_of_product_2, price_2 = input().split()

amount_to_be_paid = int(units_of_product_1) * float(price_1) + int(
    units_of_product_2
) * float(price_2)

print("VALOR A PAGAR: R$ {:.2f}".format(amount_to_be_paid))

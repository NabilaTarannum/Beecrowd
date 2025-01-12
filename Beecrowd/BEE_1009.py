# -*- coding: utf-8 -*-

"""
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
"""

sellers_name = str(input())
fixed_salary = float(input())
sales_total = float(input())

total = (sales_total * 0.15) + fixed_salary

print("TOTAL = R$ {:.2f}".format(total))

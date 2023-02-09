"""
algoritmo que gera cpfs validos
"""
from generator import cpf_generator

cpf = int(input("Quantos cpfs deseja gerar? "))

cpf_generator.cpf_generator(cpf)
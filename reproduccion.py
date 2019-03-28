#!/usr/bin/python
# -*- coding: utf-8 -*-
from random import randint
from poblacion import *

def pmx(ind1, ind2):
	'''
	funcion que genera dos hijos a traves de la cruza de partial mapped pero con un
	ligero cambio para la aceptacion de 2 valores (verdadero y falso).
	ind1= el primer padre
	ind2= el segundo padre
	'''
	fin=randint(0,len(ind1.valoresVerdad))
	ini=randint(0,fin)
	values1=ind1.valoresVerdad.values()
	values2=ind2.valoresVerdad.values()
	#se realiza el intercambio de cadenas
	sub1=values1[:ini:]+values1[fin::]
	sub2=values2[:ini:]+values2[fin::]
	#se comienza a mapear e intercambiar
	for i in range(ini, fin):
		cambio=values1[i]
		if cambio in sub2:
			indice=sub2.index(cambio)
			sub2[indice]=values2[indice]
		cambio=values2[i]
		if cambio in sub1:
			indice=sub1.index(cambio)
			sub1[indice]=values1[indice]
	#se generan a los hijos
	valueshijo1=sub1[:ini]+values2[ini:fin]+sub1[ini:]
	valueshijo2=sub2[:ini]+values1[ini:fin]+sub2[ini:]
	return Individuo(valueshijo1), Individuo(valueshijo2)
	
def ox(ind1, ind2):
	'''
	funcion que genera dos hijos a traves de la cruza de partial mapped pero con un
	ligero cambio para la aceptacion de 2 valores (verdadero y falso)
	ind1= el primer padre
	ind2= el segundo padre
	'''
	fin=randint(0,len(ind1.valoresVerdad))
	ini=randint(0,fin)
	values1=ind1.valoresVerdad.values()
	values2=ind2.valoresVerdad.values()
	#se realiza el intercambio de cadenas
	sub1=values1[fin::]+values1[0:ini:]
	sub2=values2[fin::]+values2[0:ini:]
	valueshijo1=[]
	valueshijo2=[]
	for i in range(0,ini):
		valueshijo1.append(sub2[i])
		valueshijo2.append(sub1[i])
	valueshijo1=valueshijo1+values1[ini:fin]
	valueshijo2=valueshijo2+values2[ini:fin]
	for i in range(ini, len(sub1)):
		valueshijo1.append(sub2[i])
		valueshijo2.append(sub1[i])

	return Individuo(valueshijo1), Individuo(valueshijo2)

def mutationDisp(ind):
	'''
	funcion que genera la mutacion por desplazamiento en un individuo
	'''
	values=ind.valoresVerdad.values()
	posDestino=randint(0,len(values)-1)
	posIni=randint(0,len(values)-1)
	valor=values[randint(0,posIni)]
	values.pop(posIni)
	if posDestino != posIni:
		values.insert(posDestino, valor)
	else:
		values.append(valor)
	return Individuo(values)
	
def mutationEx(ind):
	'''
	funcion que genera la mutacion por intercambio en un individuo
	'''
	values=ind.valoresVerdad.values()
	posDestino=randint(0,len(values)-1)
	posIni=randint(0,len(values)-1)
	valor1=values[randint(0,posIni)]
	valor2=values[randint(0,posDestino)]
	if posDestino != posIni:
		values[posIni]=valor2
		values[posDestino]=valor1

	return Individuo(values)
	

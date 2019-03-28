#!/usr/bin/python
# -*- coding: utf-8 -*-
from random import randint, randrange
from poblacion import *
from reproduccion import *

def generaEjemplar(numClausulas, numVars):
	'''
	funcion que genera un ejemplar inicial para el problema
	numClausulas =  numero de clausulas del ejemplar
	numVars= numero de variables en el ejemplar
	'''
	clausulas=[]
	#generamos las clausulas del ejemplar de forma aleatoria
	for i in range(0,numClausulas+1):
		tam=randint(3,5) #Entre 3 y 5 variables
		clausulas.append(Clausula(numVars))
	#Guardamos el ejemplar en un archivo de texto para que sea legible
	with open('ejemplar.txt', 'w') as archivo:
		archivo.write("-1 = False, 1= True, 0= no esta en la clausula\n\n")
		cont=0
		for c in clausulas:
			archivo.write("\n-----CLAUSULA %d -------\n" %(cont))
			archivo.write(str(c))
			cont+=1
	return clausulas
	

def seleccion(poblacion):
	'''
	funcion que define la forma de seleccion de los individuos para la cruza
	'''
	poblacion=sorted(poblacion,key=lambda Individuo: Individuo.apt)
	mitad=len(poblacion)/2
	#escojo la mitad mas apta
	aptos=poblacion[mitad:]
	#escojo la mitad menos apta
	noAptos=poblacion[:mitad]
	seleccionados=[]
	for i in range(0,mitad):
		#Utilizare 25% probabilidad de que sea no apto
		res= randrange(1,4)
		if res == 1:
			seleccionados.append(noAptos[i])
		else:
			seleccionados.append(aptos[i])
	return seleccionados
	
def reemplazo(generacion,generacionNueva,permite):
	'''
	funcion que selecciona cuales individuos reemplazar por los
	nuevos individuos.
	generacion= generacion anterior
	generacionNueva= nuevos individuos recien generados por reproduccion
	permite= si es True, permitira reemplazar al individuo mas apto
			 si es False, el mas apto de la generacion se queda
	'''
	tamPoblacion=len(generacion)
	tamNueva=len(generacionNueva)
	#Ordenamos la generacion de los que tienen el peor fitness a los que tienen el mejor
	generacion=sorted(generacion,key=lambda Individuo: Individuo.apt)
	ini=tamPoblacion-1
	cont=0
	nueva=[]
	if permite==False: #Si se mantendra el mejor individuo de la generacion anterior
		nueva= generacion[((tamPoblacion)/2)-1:tamPoblacion-1]+generacionNueva
	else:#Si NO se mantendra el mejor individuo de la generacion anterior
		nueva= generacion[(tamPoblacion)/2:]+generacionNueva
	return nueva
	
def creaGeneracion(gen_anterior, clausulas):
	'''
	Funcion que se encarga de crear la siguiente generacion con base a la
	anterior. En esta se lleva a cabo el cruce y la mutacion, asi como la
	seleccion y el reemplazo.
	gen_anterior= generacion de padres
	clausulas= conjunto de clausulas que debe satisfacer
	'''
	gen_nueva=[]
	for individuo in gen_anterior:
		individuo.calcula_aptitud(clausulas)
	#Realizamos la seleccion de los padres
	padres=seleccion(gen_anterior)
	cont=0
	hijos=[]
	#Por cada par de padres, aplicamos la reproduccion
	while cont < len(padres)-1:
		tipoRep=randint(0,1)
		if tipoRep==1:#Se lleva a cabo Partial Mapped Crossover
			hijo1,hijo2=pmx(padres[cont],padres[cont+1])
			tipoMut=randrange(0,8)# para decidir si llevara o no mutacion y cual
			if tipoMut == 1:
				hijo1=mutationDisp(hijo1)
			if tipoMut == 2:
				hijo1=mutationEx(hijo1)
			tipoMut=randrange(0,8)
			if tipoMut == 1:
				hijo2=mutationDisp(hijo2)
			if tipoMut == 2:
				hijo2=mutationEx(hijo2)
			hijos.append(hijo1)
			hijos.append(hijo2)

		else:#si se lleva a cabo Order Crossover
			hijo1,hijo2=ox(padres[cont],padres[cont+1])
			tipoMut=randint(0,8)# para decidir si llevara o no mutacion y cual
			if tipoMut == 1:
				hijo1=mutationDisp(hijo1)
			if tipoMut == 2:
				hijo1=mutationEx(hijo1)
			tipoMut=randrange(0,8)
			if tipoMut == 1:
				hijo2=mutationDisp(hijo2)
			if tipoMut == 2:
				hijo2=mutationEx(hijo2)
			hijos.append(hijo1)
			hijos.append(hijo2)
		cont+=2
	#realizamos el reemplazo de la generacion anterior con los nuevos hijos
	gen_nueva=reemplazo(gen_anterior, hijos,True)
	for ind in gen_nueva:
		ind.calcula_aptitud(clausulas)

	return gen_nueva
	
	
#___________________Primero creamos el ejemplar__________________#
num_variables=randrange(100,150)
num_clausulas=randrange(50,60)
pobInicial=[]
il=1
print "Generamos el ejemplar \n"
EJEMPLAR=generaEjemplar(num_clausulas,num_variables)

#________Creamos la primera generacion (poblacion inicial)________#
while il <=20: #En este caso seran 20 individuos, si se desea cambiar, solo pares
	pobInicial.append(Individuo([randint(0,1) for i in range(0,num_variables)]))
	il+=1
	
#________Comenzamos con las interaciones (reproducciones)________#
nGen=creaGeneracion(pobInicial,EJEMPLAR)
for i in range(0,30):
	pobi=creaGeneracion(nGen,EJEMPLAR)
	nGen=pobi
	nGen=sorted(nGen,key=lambda Individuo: Individuo.apt)
	print " El mejor fitness en la generacion %d : %d"% (i,nGen[-1].apt)
#_________________Obtenemos el mejor resultado____________________#
print "\nEl mejor ejemplar fue: "
mejor=nGen[-1]
for i in mejor.valoresVerdad.keys():
	print "var %d: %d"%(i,mejor.valoresVerdad[i])
print "Satisface %d clausulas" %(mejor.apt)
print "Donde 0 = False y 1 = True"

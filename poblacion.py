#!/usr/bin/python
# -*- coding: utf-8 -*-
from random import randint, randrange, choice
class Clausula:
	
	def __init__(self, numVars):
		'''
		Crearemos un diccionario que contendra la variable y 1 si esta siendo usada o
		0 si no
		'''
		tam=randint(3,5)
		dicValores={}
		cont=0
		for i in range(0,numVars):
			dicValores[i]=0
		while cont < tam:
			pos= randrange(0,numVars-1)
			if dicValores[pos]==0:
				dicValores[pos]=randint(-1,1)
				cont+=1
		self.variables=dicValores
		self.verdadera=False

	def __str__(self):
		'''
		Funcion que genera la representacion en cadena de la clausula
		'''
		cad="["
		for i in self.variables.keys():
			cad+=" var%d=%d "% (i,self.variables[i])
		cad=cad+"]"
		return cad



class Individuo:

	def __init__(self,variables):
		'''
		Crea un individui (solucion) a traves de un conjunto de variables 
		o valores aleatorios '0'(False) o '1'(True) para la solucion
		'''
		dicValores={}
		for i in range(0,len(variables)):
			dicValores[i]=variables[i]
		self.valoresVerdad=dicValores
		self.apt=0
       
	def calcula_aptitud(self,clausulas):
		'''
		Funcion fitness que se calculara de un individuo (solucion) a partir
		de un conjunto de clausulas y evaluara cuantas de estas satisface
		'''
		aptitud=0
		for clausula in clausulas:
			aceptada=0
			for i in clausula.variables.keys():
				if self.valoresVerdad[i]==0 and clausula.variables[i]==-1:
					n=1
				elif  self.valoresVerdad[i]==1 and clausula.variables[i]==1:
					n=1
				else:
					n=0	
				aceptada=aceptada or n
			if aceptada != 0:
				aptitud+=1
		self.apt=aptitud
	



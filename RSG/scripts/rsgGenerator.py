#!/usr/bin/python
# -*- coding: latin-1 -*-
#
# Gerador de RSGs para utilizar na visualização de coordenadas paralelas.
#
# Será utilizado um formato .csv, na seguinte configuração:
#
# curso,rsg de 2008/1, ,rsg de 2008/2, ...,rsg de 2012/2  
#
#
from random import randrange, uniform

sems =  ['2008/1',
	'2008/2',
	'2009/1',
	'2009/2',
	'2010/1',
	'2010/2',
	'2011/1',
	'2011/2',
	'2012/1',
	'2012/2']

# Imprime cabeçalho
cabecalho = 'curso'
for sem in sems:
	cabecalho += ','+sem
print cabecalho

alunos = 200
for i in range(0,alunos):
	cursos = ['si','cc']
	aluno = cursos[randrange(0,2)]
	vida=3 # quantidade de semestres permitdo ficar abaixo de 1
	for sem in sems:
		rsg = float('%.2f' %uniform(0,5))
		if (rsg<1):
			vida-=1
		if (vida>=0):
			aluno += ','+str(rsg)
	print aluno

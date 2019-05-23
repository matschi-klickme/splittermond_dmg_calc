#! /usr/bin/python
# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np
from math import exp, expm1
import math

# krit, multidice, dmgbonus
dice = input("Heyhoo- um welchen Typ Würfel geht es?  W-? ")
ndmgdice = input("Wie viele Schadenswürfel hat die Waffe? Also für x*W"+str(dice)+" ist x=")
dmgbonus = input("Wie hoch ist der Schadensbonus der Waffe? ")
exakt = input("Wie hoch soll der Wert Exakt sein? ")
ndices=exakt+1
scharf = input("Wie hoch soll der Wert von Scharf sein? ")
minwurf= max(scharf,1)
kritisch = input("Wie hoch ist der Wert in Kritisch? ")

WGS = input("Wie hoch ist die WGS ? ")
print
graphics = input("Ergebnis mit Matplotlib graphisch darstellen? \"1\" = grafische Ausgabe ")
print
throws=np.zeros((dice**ndices,ndices))
results=np.zeros(dice**ndices)
for i in range(dice**ndices):
	for column in range(ndices):
		throws[i][column]=(i/( dice**(ndices -column -1 ) ))%dice+1
	# DMG = wurfergebnis+evtl kritisch+dmgbonus
	throwresult=max(max(throws[i][:]),minwurf)
	results[i]=throwresult+int(throwresult/dice)*kritisch+dmgbonus


erwartungswert=(np.sum(results)/(dice**ndices))*ndmgdice
plt.hist(results,bins=np.arange(0.5,dice+kritisch+dmgbonus+1,1),density=True)

if graphics==1:
	plt.hist(results,bins=np.arange(0.5,dice+kritisch+dmgbonus+1,1),density=True)
	plt.title("EW: "+str(erwartungswert)+", EW pro Tick WGS: "+str(erwartungswert/WGS) )
	#plt.suptitle("Schaden f."+str(ndmgdice)+"W"+str(dice)+" +"+str(dmgbonus) + "mit \"Exakt "+str(exakt)+"\" und \"Scharf "+str(scharf)+"\"")
	plt.suptitle("Schaden f. " + str(ndmgdice)+"W"+str(dice)+" + "+str(dmgbonus)+" mit: exakt " + str(exakt) + ", scharf "+ str(scharf) + ", kritisch " + str(kritisch) + " und WGS " + str(WGS) )
	plt.xlabel("Schaden f. Einzelwurf")
	plt.ylabel("Wahrscheinlichkeit")
	plt.show()
else:
	print("Gewählt: "+str(ndmgdice)+"W"+str(dice)+" + "+str(dmgbonus)+" mit: exakt " + str(exakt) + ", scharf "+str(scharf)+", kritisch "+str(kritisch)+" und WGS "+str(WGS) )
	print
	print("Erwartungswert: "+str(erwartungswert)+", EW pro Tick WGS: "+str(erwartungswert/WGS))
	print("Schadenswerte:")
	uniqueresults= np.unique(results)
	print uniqueresults
	uniquebins=np.append([uniqueresults-0.5],[uniqueresults[-1]+0.5])
	histogram,bins=np.histogram(results,bins=uniquebins,density=True)
	print("Schadens-Wahrscheinlichkeiten:")
	print histogram*100
	
print
debug = input("Debugging-Ergebnisse anzeigen? \"1\" zeigt an, ansonsten verborgen ")print
	

if debug == 1:
	print("--> Das bedeutet "+str(dice**ndices)+" Mögliche Wurfergebnisse")
	print("Debug output: Einzelne Würfe und Ergebnis incl exakt, scharf und kritisch")
	print
	for i in range(dice**ndices):
		print throws[i][:]
		print("Ergebnis: "+str(results[i]))


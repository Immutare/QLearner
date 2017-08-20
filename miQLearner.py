# -*- coding: utf-8 -*-
"""
Created on Sat Aug 19 22:30:13 2017

@author: Carlos Eduardo Garcia Garcia
"""
import numpy as np
import random

class MDP:
    """Clase usada para el MDP """
    
    def __init__(self):
        self.estadoPrima=[]
        self.probabilidad=[]
        self.recompensa=[]
    
    def inicializar(self,sPrima,prob,rew):
        self.estadoPrima=sPrima
        self.probabilidad=prob
        self.recompensa=rew
        
    def rand(self):
        return random.random()
    
    def ejecuciondeAccion(self):
        aleatorio = self.rand()
        acum = 0.0
        #ind = 0
        #print("Probabilidad: ", len(self.probabilidad), "\n Recompensa: ", len(self.recompensa))
        if len(self.probabilidad) == 1:
            #print("Solo hay 1! :o")
            return self.estadoPrima[0],self.recompensa[0]
        else:
            for i in range(len(self.probabilidad)):#Para recorrer todo el vector 
                acum = acum + self.probabilidad[i]
                if aleatorio<=acum:
                    #print (i)
                    return self.estadoPrima[i], self.recompensa[i]



#Filas:
    #0 Hippoglucemia
    #1 Glucosa baja
    #2 Glucosa normal
    #3 Glucosa alta
    #4 Hyperglucemia

#Columnas:
    #0 No comer
    #1 Comer sano (Poco)
    #2 Comer sano
    #3 Comer sano (Mucho)
    #4 Comer mal (Poco)
    #5 Comer mal
    #6 Comer mal (Mucho)  

matriz = [[MDP(),MDP(),MDP(),MDP(),MDP(),MDP(),MDP()],
          [MDP(),MDP(),MDP(),MDP(),MDP(),MDP(),MDP()],
          [MDP(),MDP(),MDP(),MDP(),MDP(),MDP(),MDP()],
          [MDP(),MDP(),MDP(),MDP(),MDP(),MDP(),MDP()],
          [MDP(),MDP(),MDP(),MDP(),MDP(),MDP(),MDP()]]

#ASIGNACION DE LOS DATOS

#0 Hippoglucemia    
matriz[0][0].inicializar([0],[1],[-0.04])
matriz[0][1].inicializar([0,1],[0.7,0.3],[-0.04,1])
matriz[0][2].inicializar([0,1],[0.4,0.6],[-0.04,2])
matriz[0][3].inicializar([2],[1],[2])
matriz[0][4].inicializar([0,1,2],[0.1,0.3,0.6],[-0.04,1,2])
matriz[0][5].inicializar([2,3],[0.5,0.5],[0,-5])
matriz[0][6].inicializar([3,4],[0.7,0.3],[-5,-10])

#1 Glucosa baja
matriz[1][0].inicializar([0,1],[0.2,0.8],[-1,-0.04])
matriz[1][1].inicializar([1,2],[0.7,0.3],[-0.04,1])
matriz[1][2].inicializar([1,2],[0.2,0.8],[-0.04,2])
matriz[1][3].inicializar([3],[1],[-1])
matriz[1][4].inicializar([1,2,3],[0.1,0.3,0.6],[-0.04,2,-1])
matriz[1][5].inicializar([3],[1],[-1])
matriz[1][6].inicializar([4],[1],[-10])

#2 Glucosa normal
matriz[2][0].inicializar([1,2],[0.1,0.9],[-1,1])
matriz[2][1].inicializar([2,3],[0.8,0.3],[1,-1])
matriz[2][2].inicializar([2,3],[0.6,0.4],[1.5,-1])
matriz[2][3].inicializar([4],[1],[-10])
matriz[2][4].inicializar([2,3],[0.2,0.8],[1,-1])
matriz[2][5].inicializar([4],[1],[-10])
matriz[2][6].inicializar([4],[1],[-10])

#3 Glucosa alta
matriz[3][0].inicializar([2,3],[0.2,0.8],[10,-1])#cuidado porque es la unica que regresa
matriz[3][1].inicializar([3,4],[0.8,0.3],[-1,-10])
matriz[3][2].inicializar([3,4],[0.6,0.4],[-1,-10])
matriz[3][3].inicializar([4],[1],[-50])
matriz[3][4].inicializar([3,4],[0.2,0.8],[-10,-100])
matriz[3][5].inicializar([4],[1],[-50])
matriz[3][6].inicializar([4],[1],[-100])


#4 Hiperglucemia
matriz[4][0].inicializar([3,4],[0.2,0.8],[10,-1])
matriz[4][1].inicializar([4],[1],[-100])
matriz[4][2].inicializar([4],[1],[-100])
matriz[4][3].inicializar([4],[1],[-100])
matriz[4][4].inicializar([4],[1],[-100])
matriz[4][5].inicializar([4],[1],[-100])
matriz[4][6].inicializar([4],[1],[-100])



#################FUNCIONES#################%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

def actualizarQ(state, next_state, action, alpha, gamma, reward):
    rsa = reward
    qsa = reward
    new_q = qsa + alpha * (rsa + gamma * max(q[next_state, :]) - qsa)
    q[state, action] = new_q
    # renormalize row to be between 0 and 1
    rn = q[state][q[state] > 0] / np.sum(q[state][q[state] > 0])
    q[state][q[state] > 0] = rn
    
def printMatrix(a):
   print("Matriz Q[",("%d" %a.shape[0]),"][",("%d" %a.shape[1]),"]")
   rows = a.shape[0]
   cols = a.shape[1]
   for i in range(0,rows):
      for j in range(0,cols):
         print ("%.8f"%a[i,j], end="\t")
      print (" ")
   print 

def imprimirPolitica(q):
    print("------POLITICA------")
    ban = True
    may = 0
    estados = ["Hippoglucemia", "Glucosa baja", "Glucosa normal","Glucosa alta","Hiperglucemia"]
    acciones = ["No comer","Comer sano (Poco)","Comer sano","Comer sano (Mucho)","Comer mal (Poco)"]
    indMay = 0
    #5 "Comer mal"
    #6 "Comer mal (Mucho)"]
    for i in range(len(q)):
        if ban:
            ban = False
            may=q[i][0]
            indMay=0
        for j in range(len(q[i])):
            if may < q[i][j]:
                may = q[i][j]
                indMay=j
        print("%s \t=>%s" % (estados[i],acciones[indMay]))
            
        
        
    
###########################################%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

q = np.zeros_like(matriz)

# Core algorithm
gamma = 0.8  #Descuento
alpha = 1. #Pasos
n_episodes = 1E3
n_states = 5
n_actions = 7
epsilon = 0.05
random_state = np.random.RandomState(1999)
#

#Numero de iteraciones para Q-Learning
for e in range(int(n_episodes)):
    #Genera la cantidad de posibles estados
    states = list(range(n_states))
    #Se revuelven los estados
    random_state.shuffle(states)
    #Se obtiene el estado actual 
    current_state = states[0]
    #Mientras no se encuentre el objetivo sigue recorriendo la matriz
    goal = False
    while not goal:
        #Se sacan las acciones para la lista
        actions = list(range(n_actions))
        #Se barajean las acciones
        random_state.shuffle(actions)
        #Sacamos la accion
        current_action = actions[0]
        
        #Ejecutamos la accion
        #print("Matriz[",current_state,"][",current_action,"]")
        #print("Matriz[%d][%d]" % (current_state,current_action))
        sPrima, reward = matriz[current_state][current_action].ejecuciondeAccion()
        
        #Se actualiza Q
        actualizarQ(current_state, sPrima, current_action,alpha, gamma, reward)
        
        #Se cambia de estado
        current_state = sPrima
        
    
        
        
        if(reward>=0):
            goal = True


printMatrix(q)
imprimirPolitica(q)

        
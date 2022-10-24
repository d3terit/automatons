import os
from graphviz import *


class Transducto():

    def __init__(self):
        self.states = ['s0', 's1']
        self.alphabetIn = ['a', 'b']
        self.alphabetOut = [1, 2]
        self.initState = "s0"
        self.transitionIn = [
            {'currentState': 's0',
             'transisitions': [
                 {'letter': 'a', 'nexState': 's0'},
                 {'letter': 'b', 'nexState': 's1'}
             ]
            },
            {'currentState': 's1',
             'transisitions': [
                 {'letter': 'a', 'nexState': 's0'},
                 {'letter': 'b', 'nexState': 's1'}
             ]
            }
        ]
        self.transitionOut = [
            {'currentState': 's0',
             'transisitions': [
                 {'letter': 'a', 'nexState': '0'},
                 {'letter': 'b', 'nexState': '0'}
             ]
            },
            {'currentState': 's1',
             'transisitions': [
                 {'letter': 'a', 'nexState': '1'},
                 {'letter': 'b', 'nexState': '1'}
             ]
            }
        ]
        self.string = ""
    
    def clearConsole(self):
        os.system('cls' if os.name in ('nt', 'dos') else 'clear')
    
    def menu(self):
        while True:
            self.clearConsole()
            print("1. Ingresar cadena")
            print("2. Ver tabla de transiciones")
            print("3. Ver diagrama de estados")
            print("0. Salir")
            option = input("Ingrese una opcion: ")
            if option == "1":
                self.clearConsole()
                self.string = input("Ingrese la cadena: ")
                self.processString()
            elif option == "2":
                self.clearConsole()
                self.showData()
            elif option == "3":
                self.clearConsole()
                self.showDiagram()
            elif option == "0":
                break
            else:
                print("Opcion no valida")
                input("Presione enter para continuar")

    def searchLetterOut(self, letter, state):
        for transition in self.transitionOut:
            if transition['currentState'] == state:
                for t in transition['transisitions']:
                    if t['letter'] == letter:
                        return t['nexState']
        return None
    
    def processString(self):
        output = []
        currentState = self.initState
        for letter in self.string:
            if letter in self.alphabetIn:
                for transition in self.transitionIn:
                    if transition['currentState'] == currentState:
                        for t in transition['transisitions']:
                            if t['letter'] == letter:
                                output.append(self.searchLetterOut(letter, currentState))
                                currentState = t['nexState']
                                break
                        break
            else:
                print("La cadena no pertenece al lenguaje")
                input("Presione enter para continuar")
                return
        print("La cadena pertenece al lenguaje")
        print("Salida: ", output)
        input("Presione enter para continuar")
        return
    
    def showData(self):
        print("Tabla de transiciones")
        print("Estado Inicial: ", self.initState)
        print("Estados: ", self.states)
        print("Alfabeto de entrada: ", self.alphabetIn)
        print("Alfabeto de salida: ", self.alphabetOut)
        print("Transiciones de entrada: ")
        for transition in self.transitionIn:
            print("Estado: ", transition['currentState'])
            for t in transition['transisitions']:
                print("Letra: ", t['letter'], " Proximo estado: ", t['nexState'])
        print("Transiciones de salida: ")
        for transition in self.transitionOut:
            print("Estado: ", transition['currentState'])
            for t in transition['transisitions']:
                print("Letra: ", t['letter'], " Proximo estado: ", t['nexState'])
        input("Presione enter para continuar")
    
    def calcTransitions(self):
        transitions = []
        for transition in self.transitionIn:
            for t in transition['transisitions']:
                for transitionOut in self.transitionOut:
                    if transitionOut['currentState'] == transition['currentState']:
                        for tOut in transitionOut['transisitions']:
                            if tOut['letter'] == t['letter']:
                                transitions.append(
                                    {
                                        "current_state": transition['currentState'],
                                        "letter": t['letter'] + "/" + tOut['nexState'],
                                        "next_state": t['nexState']
                                    }
                                )
        return transitions
    
    def showDiagram(self):
        diagram = Digraph(comment="Diagrama de estados")
        diagram.attr(rankdir="LR", size='100,100')
        for i in range(len(self.states)):
            if self.states[i] == self.initState:
                diagram.node(self.states[i], fillcolor="green", style="filled")
            else:
                diagram.node(self.states[i])
        transitions = self.calcTransitions()
        for transition in transitions:
            if type(transition["next_state"]) == list:
                for next_state in transition["next_state"]:
                    diagram.edge(transition["current_state"],
                                     next_state, label=transition["letter"])
            else:
                diagram.edge(transition["current_state"],
                                 transition["next_state"], label=transition["letter"])
        diagram.node("init", shape='point')
        diagram.edge("init", self.initState)
        diagram.render(filename='diagram.gv', directory='diagrams',
                       view=True, cleanup=True)

if "__main__" == __name__:
    transductor = Transducto()
    transductor.menu()
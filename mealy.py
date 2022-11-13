from graphviz import *
import moore
from utils import clearConsole

class Mealy():

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
    
    def menu(self):
        while True:
            clearConsole()
            print("1. Ingresar alfabeto de entrada")
            print("2. Ingresar alfabeto de salida")
            print("3. Ingresar estados")
            print("4. Ingresar estado inicial")
            print("5. Ingresar matriz de transición de entrada")
            print("6. Ingresar matriz de transición de salida")
            print("7. Ver información del transducto")
            print("8. Evaluar cadena")
            print("9. Ver diagrama de estados")
            print("T. Transformar a Moore")
            print("0. Salir")
            option = input("Ingrese una opcion: ")
            clearConsole()
            if option == "1":
                self.setAlphabetIn()
            elif option == "2":
                self.setAlphabetOut()
            elif option == "3":
                self.setStates()
            elif option == "4":
                self.setInitState()
            elif option == "5":
                self.setTransitionIn()
            elif option == "6":
                self.setTransitionOut()
            if option == "7":
                self.showData()
            elif option == "8":
                self.processString()
            elif option == "9":
                self.showDiagram()
            elif option == "T":
                self.transformToMoore()
            elif option == "0":
                break
            else:
                print("Opcion no valida")
                input("Presione enter para continuar")
            
    def setAlphabetIn(self):
        self.alphabetIn = input("Ingrese el alfabeto de entrada: ").split(" ")
        input("Presione enter para continuar")
    
    def setAlphabetOut(self):
        self.alphabetOut = input("Ingrese el alfabeto de salida: ").split(" ")
        input("Presione enter para continuar")
    
    def setStates(self):
        self.states = input("Ingrese los estados: ").split(" ")
        input("Presione enter para continuar")

    def setInitState(self):
        self.initState = input("Ingrese el estado inicial: ")
        input("Presione enter para continuar")

    def setTransitionIn(self):
        self.transitionIn = []
        for state in self.states:
            transitions = []
            for letter in self.alphabetIn:
                transitions.append({'letter': letter, 'nexState': input("Ingrese el proximo estado de " + state + " con la letra " + letter + ": ")})
            self.transitionIn.append({'currentState': state, 'transisitions': transitions})
        input("Presione enter para continuar")
    
    def setTransitionOut(self):
        self.transitionOut = []
        for state in self.states:
            transitions = []
            for letter in self.alphabetIn:
                transitions.append({'letter': letter, 'nexState': input("Ingrese el proximo estado de " + state + " con la letra " + letter + ": ")})
            self.transitionOut.append({'currentState': state, 'transisitions': transitions})
        input("Presione enter para continuar")

    def searchLetterOut(self, letter, state):
        for transition in self.transitionOut:
            if transition['currentState'] == state:
                for t in transition['transisitions']:
                    if t['letter'] == letter:
                        return t['nexState']
        return None
    
    def processString(self):
        string = input("Ingrese la cadena: ")
        output = []
        currentState = self.initState
        for letter in string:
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
    
    def showTransformMenu(self):
        while True:
            clearConsole()
            print("Transducto de Mealy")
            print("1. Ver información del transducto")
            print("2. Procesar cadena")
            print("3. Mostrar diagrama de estados")
            print("0. Regresar")
            option = input("Ingrese una opcion: ")
            clearConsole()
            if option == "1":
                self.showData()
            elif option == "2":
                self.processString()
            elif option == "3":
                self.showDiagram()
            elif option == "0":
                break
            else:
                print("Opcion invalida")
                input("Presione enter para continuar")     

    def transformToMoore(self):
        mooreTransdurcer = moore.Moore()
        mooreTransdurcer.alphabetIn = self.alphabetIn
        mooreTransdurcer.alphabetOut = self.alphabetOut
        mooreTransdurcer.states = self.states
        mooreTransdurcer.initState = self.initState
        mooreTransdurcer.transitionIn = self.transitionIn
        mooreTransdurcer.transitionOut = self.transitionOut
        mooreTransdurcer.showTransformMenu()   

if "__main__" == __name__:
    transductor = Mealy()
    transductor.menu()
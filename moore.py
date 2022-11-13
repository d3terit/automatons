from graphviz import *
import mealy
from utils import clearConsole


class Moore():

    def __init__(self):
        self.states = ['r0', 'r1', 'r2', 'r3']
        self.alphabetIn = ['a', 'b']
        self.alphabetOut = [1, 2]
        self.initState = "r0"
        self.transitionIn = [{
            'currentState':
            'r0',
            'transisitions': [{
                'letter': 'a',
                'nexState': 'r0'
            }, {
                'letter': 'b',
                'nexState': 'r2'
            }]
        }, {
            'currentState':
            'r1',
            'transisitions': [{
                'letter': 'a',
                'nexState': 'r0'
            }, {
                'letter': 'b',
                'nexState': 'r2'
            }]
        }, {
            'currentState':
            'r2',
            'transisitions': [{
                'letter': 'a',
                'nexState': 'r1'
            }, {
                'letter': 'b',
                'nexState': 'r3'
            }]
        }, {
            'currentState':
            'r3',
            'transisitions': [{
                'letter': 'a',
                'nexState': 'r1'
            }, {
                'letter': 'b',
                'nexState': 'r3'
            }]
        }]
        self.transitionOut = [{
            'currentState':
            'r0',
            'transisitions': [{
                'letter': 'a',
                'nexState': '0'
            }, {
                'letter': 'b',
                'nexState': '0'
            }]
        }, {
            'currentState':
            'r1',
            'transisitions': [{
                'letter': 'a',
                'nexState': '0'
            }, {
                'letter': 'b',
                'nexState': '0'
            }]
        }, {
            'currentState':
            'r2',
            'transisitions': [{
                'letter': 'a',
                'nexState': '1'
            }, {
                'letter': 'b',
                'nexState': '1'
            }]
        }, {
            'currentState':
            'r3',
            'transisitions': [{
                'letter': 'a',
                'nexState': '1'
            }, {
                'letter': 'b',
                'nexState': '1'
            }]
        }]
        self.auxNames = {}

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
            print("T. Transformar a Mealy")
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
                self.transform()
            elif option == "0":
                break
            else:
                print("Opcion no valida")
                input("Presione enter para continuar")

    def setAlphabetIn(self):
        self.alphabetIn = input("Ingrese el alfabeto de entrada: ").split()
        input("Presione enter para continuar")

    def setAlphabetOut(self):
        self.alphabetOut = input("Ingrese el alfabeto de salida: ").split()
        input("Presione enter para continuar")

    def setStates(self):
        self.states = input("Ingrese los estados: ").split()
        input("Presione enter para continuar")

    def setInitState(self):
        self.initState = input("Ingrese el estado inicial: ")
        input("Presione enter para continuar")

    def setTransitionIn(self):
        self.transitionIn = []
        for state in self.states:
            transitions = []
            for letter in self.alphabetIn:
                transitions.append({
                    'letter':
                    letter,
                    'nexState':
                    input("Ingrese el estado siguiente de " + state + " con " +
                          letter + ": ")
                })
            self.transitionIn.append({
                'currentState': state,
                'transisitions': transitions
            })
        input("Presione enter para continuar")

    def setTransitionOut(self):
        self.transitionOut = []
        for state in self.states:
            transitions = []
            for letter in self.alphabetIn:
                transitions.append({
                    'letter':
                    letter,
                    'nexState':
                    input("Ingrese el estado siguiente de " + state + " con " +
                          letter + ": ")
                })
            self.transitionOut.append({
                'currentState': state,
                'transisitions': transitions
            })
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
                                output.append(
                                    self.searchLetterOut(letter, currentState))
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
                print("Letra: ", t['letter'], " Proximo estado: ",
                      t['nexState'])
        print("Transiciones de salida: ")
        for transition in self.transitionOut:
            print("Estado: ", transition['currentState'])
            for t in transition['transisitions']:
                print("Letra: ", t['letter'], " Proximo estado: ",
                      t['nexState'])
        input("Presione enter para continuar")

    def getName(self, name):
        resp = name
        if name in self.auxNames:
            for i in self.auxNames[name]:
                resp += '/' + i
        return resp

    def calcOutput(self):
        self.auxNames = {}
        for transition in self.transitionIn:
            self.auxNames[transition['currentState']] = []
        for transition in self.transitionIn:
            for t in transition['transisitions']:
                for transitionOut in self.transitionOut:
                    if transitionOut['currentState'] == transition[
                            'currentState']:
                        for tOut in transitionOut['transisitions']:
                            if tOut['letter'] == t['letter']:
                                if tOut['nexState'] not in self.auxNames[t['nexState']]:
                                    self.auxNames[t['nexState']].append(
                                        tOut['nexState'])

    def showDiagram(self):
        self.calcOutput()
        diagram = Digraph(comment="Diagrama de estados")
        diagram.attr(rankdir="LR", size='100,100')
        for transition in self.transitionIn:
            for t in transition['transisitions']:
                diagram.edge(self.getName(transition['currentState']),
                             self.getName(t['nexState']),
                             label=t['letter'])
        diagram.render(filename='diagram.gv',
                       directory='diagrams',
                       view=True,
                       cleanup=True)
        diagram.node(self.getName(self.initState),
                     fillcolor="green",
                     style="filled")
        diagram.node("init", shape='point')
        diagram.edge("init", self.getName(self.initState))
        diagram.render(filename='diagram.gv',
                       directory='diagrams',
                       view=True,
                       cleanup=True)

    def showTransformMenu(self):
        while True:
            clearConsole()
            print("Transducto de Moore")
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

    def transform(self):
        mealyTransdurcer = mealy.Mealy()
        mealyTransdurcer.alphabetIn = self.alphabetIn
        mealyTransdurcer.alphabetOut = self.alphabetOut
        mealyTransdurcer.states = self.states
        mealyTransdurcer.initState = self.initState
        mealyTransdurcer.transitionIn = self.transitionIn
        mealyTransdurcer.transitionOut = self.transitionOut
        mealyTransdurcer.showTransformMenu()


if "__main__" == __name__:
    transductor = Moore()
    transductor.menu()
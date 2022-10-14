# Elaborado por Daniel Hernando Mantilla 
# Código: 1005040227
from afd import AFD
from graphviz import *


class AFND(AFD):
    def __init__(self,):
        super().__init__()
        self.alphabet = ["a", "b", "c", "λ"]
        self.states = ["s0", "s1", "s2", "s3"]
        self.initial_states = ["s0"]
        self.final_states = ["s3"]
        self.transitions = [
            {"current_state": "s0", "letter": "a", "next_state": "s1"},
            {"current_state": "s1", "letter": "b", "next_state": "s2"},
            {"current_state": "s1", "letter": "λ", "next_state": "s1"},
            {"current_state": "s2", "letter": "c", "next_state": "s3"},
            {"current_state": "s3", "letter": "λ", "next_state": "s1"},
        ]
        self.epsilon_transitions = []
        self.epsilon_closure = {}

    def showMenu(self):
        self.clearConsole()
        print("1. Ingresar alfabeto")
        print("2. Ingresar estados")
        print("3. Ingresar estados iniciales")
        print("4. Ingresar estados finales")
        print("5. Ingresar transiciones")
        print("6. Ingresar transiciones epsilon")
        print("7. Ver AFND")
        print("8. Ejecutar AFND")
        print("9. Ver diagrama de estados")
        print("0. Salir")
        option = input("Ingrese una opción: ")
        if option == "1":
            self.setAlphabet()
        elif option == "2":
            self.setStates()
        elif option == "3":
            self.setInitialStates()
        elif option == "4":
            self.setFinalStates()
        elif option == "5":
            self.setTransitions()
        elif option == "6":
            self.addEpsilonTransition()
        elif option == "7":
            self.showAFND()
        elif option == "8":
            self.executeAFND()
        elif option == "9":
            self.showAFNDDiagram()
        elif option == "0":
            exit()
        else:
            print("Opción inválida")
            input("")
            self.showMenu()
    
    def setInitialStates(self):
        self.clearConsole()
        print("Estados actuales: " + str(self.initial_states))
        initial_states = input("Ingrese los estados iniciales separados por coma: ")
        self.initial_states = initial_states.split(",")
        input("Estados iniciales actualizados")
        self.showMenu()

    def addEpsilonTransition(self):
        self.clearConsole()
        current_state = input("Ingrese el estado actual: ")
        next_state = input("Ingrese el estado siguiente: ")
        self.epsilon_transitions.append(
            {"current_state": current_state, "next_state": next_state})
        input("Transición agregada")
        self.showMenu()

    def getTransition(self, state, symbol):
        resp = []
        for transition in self.transitions:
            if transition["current_state"] == state and transition["letter"] == symbol:
                resp.append(transition["next_state"])
        for transition in self.epsilon_transitions:
            if transition["current_state"] == state and transition["letter"] == symbol:
                resp.append(transition["next_state"])
        if len(resp) == 0:
            return "∅"
        return resp

    def getTransitions(self, state):
        transitions = []
        for symbol in self.alphabet:
            transitions.append(self.getTransition(state, symbol))
        return transitions

    def showAllTransitions(self):
        print("Tabla de transiciones:")
        print("\t", end="")
        for symbol in self.alphabet:
            print(symbol + "\t", end="")
        print("")
        for state in self.states:
            print(state, end="\t")
            for transition in self.getTransitions(state):
                print(transition, end="\t")
            print()

    def showAFND(self):
        self.clearConsole()
        print("Alfabeto: " + str(self.alphabet))
        print("Estados: " + str(self.states))
        print("Estado inicial: " + str(self.initial_states))
        print("Estados finales: " + str(self.final_states))
        self.showAllTransitions()
        input("Regresar al menú")
        self.showMenu()

    def getEpsilonClosure(self, state):
        resp = [state]
        for transition in self.epsilon_transitions:
            if transition["current_state"] == state:
                resp.append(transition["next_state"])
        return resp

    def executeAFND(self):
        self.clearConsole()
        word = input("Ingrese la palabra a evaluar: ")
        current_states = self.initial_states
        for letter in word:
            if letter in self.alphabet:
                next_states = []
                for state in current_states:
                    next_states += self.getTransition(state, letter)
                current_states = next_states
            else:
                print("La palabra no pertenece al lenguaje")
                input("\nRegresar...")
                self.showMenu()
        for state in current_states:
            if state in self.final_states:
                print("La palabra pertenece al lenguaje")
                input("\nRegresar...")
                self.showMenu()
                break
        print("La palabra no pertenece al lenguaje")
        input("\nRegresar...")
        self.showMenu()
    def showAFNDDiagram(self):
        self.clearConsole()
        diagram = Digraph('G', filename='afnd.gv')
        diagram.attr(rankdir='LR', size='100,50')
        diagram.attr('node', shape='doublecircle')
        for state in self.final_states:
            diagram.node(state)
            diagram.attr('node', shape='circle')
        for transition in self.transitions:
            if transition["next_state"] in self.final_states:
                    diagram.edge(
                        transition["current_state"], transition["next_state"], label=transition["letter"], color="red")
            else: diagram.edge(transition["current_state"],
                             transition["next_state"], label=transition["letter"])
        for transition in self.epsilon_transitions:
            if transition["next_state"] in self.final_states:
                diagram.edge(
                        transition["current_state"], transition["next_state"], label=transition["letter"], color="red")
            else: diagram.edge(transition["current_state"],
                             transition["next_state"], label=transition["letter"])
        for state in self.initial_states:
            diagram.node(f's-{state}',shape='point')
            diagram.edge(f's-{state}', state)
        diagram.render(filename='diagram.gv', directory='diagrams',
                       view=True, cleanup=True, format='jpg')
        self.showMenu()

    
    
if __name__ == "__main__":
    afnd = AFND()
    afnd.showMenu()
# Elaborado por Daniel Hernando Mantilla 
# Código: 1005040227
from afd import AFD
from afnd import AFND
from graphviz import *
class Conversion(AFND):
    def __init__(self):
        super().__init__()
        self.afd = self.createBlankAFD()
    
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
        print("10. Convertir AFND a AFD")
        print("11. Ver AFD")
        print("12. Ejecutar AFD")
        print("13. Ver diagrama de estados AFD")
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
        elif option == "10":
            self.convertAFNDtoAFD()
        elif option == "11":
            self.afd.showAFD(self.showMenu)
        elif option == "12":
            self.afd.executeAFD(self.showMenu)
        elif option == "13":
            self.afd.showAFDDiagram(self.showMenu)
        elif option == "0":
            exit()

    def createBlankAFD(self):
        afd = AFD()
        afd.states = []
        afd.initial_states = []
        afd.final_states = []
        afd.transitions = []
        return afd
    
    def addStates(self, states, state):
        for letter in self.alphabet:
            nextStates = self.getNextStates(state, letter)
            for nextState in nextStates:
                if nextState not in states and nextState != "Ø":
                    states.append(nextState)
                    self.addStates(states, nextState)
        return states
    
    def getAFNDStates(self):
        states = self.initial_states[:]
        self.addStates(states, self.initial_states[0])
        return states
    
    def getNextStates(self, state, letter):
        nextStates = []
        add = False
        for transition in self.transitions:
            if transition["current_state"] == state and transition["letter"] == letter:
                nextStates.append(transition["next_state"])
                add = True
        if not add:
            nextStates.append("Ø")
        return nextStates

    def getAFNDTransitions(self):
        transitions = []
        for state in self.afd.states:
            for letter in self.alphabet:
                nextStates = self.getNextStates(state, letter)
                if len(nextStates) > 0:
                    transitions.append({"current_state": state, "letter": letter, "next_state": nextStates})
                else: # añade transicion al conjunto vacio
                    transitions.append({"current_state": state, "letter": letter, "next_state": "Ø"})
        return transitions

    def convertAFNDtoAFD(self):
        self.clearConsole()
        self.afd = self.createBlankAFD()
        self.afd.alphabet = self.alphabet
        self.afd.final_states = self.final_states
        self.afd.states = self.getAFNDStates()
        self.afd.initial_states = self.initial_states[0]
        self.afd.transitions = self.getAFNDTransitions()
        input("AFD generado")
        self.showMenu()


if __name__ == "__main__":
    conversion = Conversion()
    conversion.showMenu()
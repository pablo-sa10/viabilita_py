import models.viabilidade as Viabilidade

class viabilitaController:

    def __init__(self):
        #instancia da classe
        self.__model = Viabilidade()

    def initViabilities(self):
        
        # VERIFICA NO BANCO DE DADOS SE HA NOVAS VIABILIDADES
        # 
        viabilities = self.__model.latestViabilities();
        print(viabilities)

from models.viabilidade import Viabilitie  # Importar a classe corretamente

from selenium import webdriver  # para controlar o navegador
from selenium.webdriver.chrome.service import Service  # gerenciar o chromeDriver
from selenium.webdriver.chrome.options import Options  # configurar opções do chrome
from selenium.webdriver.common.by import By  # para localizar elementos página
# Para simular pressionamento de teclas
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time  # adicionar pausa no script
import logging  # Para salvar logs e debuggar código

# Configuração do logging para registrar eventos da automação
logging.basicConfig(filename='selenium.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')


class ViabilitieController:

    def __init__(self):
        # instancia da classe
        self.__model = Viabilitie()

    def initViabilities(self):

        # VERIFICA NO BANCO DE DADOS SE HA NOVAS VIABILIDADES
        #
        viabilities = self.__model.latestViabilities()
        print(viabilities)

    def createViabilitie(self):  # faz o processo de criar uma viabilidade

        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)

        try:
            print("abrindo o chrome")
            driver.get("https://vreredesim.sp.gov.br/home");

        except Exception as e:
            print(f"Ocorreu um erro: {e}")

        finally:
            time.sleep(5)
            driver.quit()
            print('navegador fechado')

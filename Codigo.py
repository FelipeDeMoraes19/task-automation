import time
import pyautogui
import pandas as pd

pyautogui.PAUSE = 0.3

def abrir_navegador(url):
    pyautogui.press("win")
    pyautogui.write("chrome")
    pyautogui.press("enter")
    time.sleep(5) 
    pyautogui.write(url)
    pyautogui.press("enter")
    time.sleep(3) 

def fazer_login(email, senha):
    pyautogui.click(x=685, y=451) 
    pyautogui.write(email)
    pyautogui.press("tab")
    pyautogui.write(senha)
    time.sleep(1) 
    pyautogui.click(x=955, y=660)
    time.sleep(3)

def importar_dados_produto():
    tabela = pd.read_csv("produtos.csv")
    print(tabela)
    return tabela

def cadastrar_produtos(tabela):
    for linha in tabela.index:
        time.sleep(0.5)  
        pyautogui.click(x=653, y=344)  
        time.sleep(1)  
        
        campos = ["codigo", "marca", "tipo", "categoria", "preco_unitario", "custo"]
        for campo in campos:
            dado = str(tabela.loc[linha, campo])
            pyautogui.write(dado)
            pyautogui.press("tab")
            print(f"Inserindo {campo}: {dado}")  
        pyautogui.press("tab")
        pyautogui.press("enter")
        pyautogui.scroll(5000)

def main():
    url = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
    email = "pythonimpressionador@gmail.com"
    senha = "sua senha"
    abrir_navegador(url)
    fazer_login(email, senha)
    tabela_produtos = importar_dados_produto()
    cadastrar_produtos(tabela_produtos)

if __name__ == "__main__":
    main()

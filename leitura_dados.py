from tkinter import filedialog
from tkinter import Tk
from tkinter import messagebox
import sys

class LeituraArquivos:
    def __init__(self):
        self.nome_arquivo = None
    
    def leitura_entrada(self):
        try:
            root = Tk()
            root.update()
            arquivo_entrada = filedialog.askopenfilename(initialdir = "/",title = "Selecione o arquivo de entrada",filetypes = (("txt files","*.txt"),("all files","*.*")))
            if arquivo_entrada:
                with open(arquivo_entrada, 'r') as arquivo:
                    print("Lendo o arquivo: {}".format(arquivo))
                    N = int(arquivo.readline().strip())
                    Q = int(arquivo.readline().strip())
                    # Inverter a ordem das camadas ao ler as pedras danificadas
                    pedras_danificadas = [tuple(map(int, linha.strip().split())) for linha in arquivo]
                    pedras_danificadas = [(N - C + 1, P) for C, P in pedras_danificadas]
                return N, Q, pedras_danificadas
            else:
                return None, None, None
        except Exception as e:
            messagebox.showerror("Erro", "Erro ao ler o arquivo de entrada: {}".format(e))
            sys.exit(1)

          

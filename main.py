from leitura_dados import LeituraArquivos
from problema_piramide import ProblemaPiramides
import sys

def main():
    try:
        leitura = LeituraArquivos()
        
        N, Q, pedras_danificadas = leitura.leitura_entrada()
        piramide = ProblemaPiramides(N, pedras_danificadas)
        numero_rotas = piramide.contar_rotas()
        print("Número de rotas: {}".format(numero_rotas))
    except Exception as e:
        print(f"Erro ao executar o programa: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()

import sys

class ProblemaPiramides:
    def __init__(self, N, pedras_danificadas):
        self.N = N
        self.piramide = self.inicializa_piramide(N, pedras_danificadas)

    def inicializa_piramide(self, N, pedras_danificadas):
        try:       
            piramide = [[True for _ in range(i)] for i in range(1, N + 1)]
            for C, P in pedras_danificadas:
            # Ajustar os índices para a indexação baseada em 0 do Python
            # e verificar se a posição existe na camada
                if 1 <= C <= N and 1 <= P and P <= len(piramide[C - 1]):
                    piramide[C - 1][P - 1] = False
            return piramide
        except Exception as e:
            print(f"Erro ao inicializar a pirâmide: {e}")
            sys.exit(1)

    def contar_rotas(self):
        try:
            dp = [[0 for _ in range(self.N)] for _ in range(self.N)]
            dp[0][0] = 1 if self.piramide[0][0] else 0

            for i in range(1, self.N):
                for j in range(i + 1):
                    if self.piramide[i][j]:
                        esquerda = dp[i - 1][j - 1] if j > 0 else 0
                        direita = dp[i - 1][j] if j < i else 0
                        dp[i][j] = esquerda + direita

            return sum(dp[self.N - 1])
        except Exception as e:  
            print(f"Erro ao contar as rotas: {e}")
            sys.exit(1)



        
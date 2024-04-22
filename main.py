class SlidingPuzzle:
    def __init__(self, puzzle):
        self.puzzle = puzzle  # Inicializa o quebra-cabeça com a configuração inicial
        self.size = 3  # Define o tamanho do quebra-cabeça (3x3)
        self.empty_pos = self.puzzle.index(0)  # Localiza a posição do espaço vazio (0)

    def move(self, direction):
        # A função move() permite mover o espaço vazio em uma das quatro direções: 'w' (cima), 's' (baixo), 'a' (esquerda), 'd' (direita)
        # A movimentação é feita trocando a posição do espaço vazio com o elemento na direção especificada
        # As condições garantem que o movimento é válido (por exemplo, não se pode mover para a esquerda se o espaço vazio já estiver na borda esquerda)
        if direction == 'w':
            if self.empty_pos >= self.size:
                self.puzzle[self.empty_pos], self.puzzle[self.empty_pos - self.size] = self.puzzle[self.empty_pos - self.size], self.puzzle[self.empty_pos]
                self.empty_pos -= self.size
        elif direction == 's':
            if self.empty_pos < self.size * (self.size - 1):
                self.puzzle[self.empty_pos], self.puzzle[self.empty_pos + self.size] = self.puzzle[self.empty_pos + self.size], self.puzzle[self.empty_pos]
                self.empty_pos += self.size
        elif direction == 'a':
            if self.empty_pos % self.size != 0:
                self.puzzle[self.empty_pos], self.puzzle[self.empty_pos - 1] = self.puzzle[self.empty_pos - 1], self.puzzle[self.empty_pos]
                self.empty_pos -= 1
        elif direction == 'd':
            if (self.empty_pos + 1) % self.size != 0:
                self.puzzle[self.empty_pos], self.puzzle[self.empty_pos + 1] = self.puzzle[self.empty_pos + 1], self.puzzle[self.empty_pos]
                self.empty_pos += 1

    def display(self):
        # A função display() imprime o estado atual do quebra-cabeça na tela linha por linha
        for i in range(self.size):
            print(self.puzzle[i*self.size:(i+1)*self.size])


def main():
    # A função main() controla o fluxo do jogo, inicialmente solicitando ao usuário a configuração inicial do quebra-cabeça
    # Em seguida, entra em um loop onde exibe o quebra-cabeça, solicita um movimento do usuário e executa o movimento
    # O loop continua até que o usuário digite 'sair'

    initialPositionInput = input("Digite um conjunto de 9 números para posição inicial ou 'enter' para utilziar a default (213804756): ")

    if  len(initialPositionInput) == 9:
      initialPostion = [int(char) for char in initialPositionInput]
    else:
      initialPostion = [2, 1, 3, 8, 0, 4, 7, 5, 6]

    slidingPuzzle = SlidingPuzzle(initialPostion)

    while True:
        slidingPuzzle.display()
        print("Use as teclas w a s d para jogar")
        directionInput = input("Digite uma direção (w, a, s, d) ou 'sair' para sair: ")

        if directionInput == 'sair':
            break
        elif directionInput in ['w', 'a', 's', 'd']:
            slidingPuzzle.move(directionInput)
        else:
            print("Movimento inválido. Tente novamente.")

if __name__ == "__main__":
    main()
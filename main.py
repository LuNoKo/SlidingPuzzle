from collections import deque

class SlidingPuzzle:
    def __init__(self):
        # Solicita ao usuário a configuração inicial do quebra-cabeça
        initialPositionInput = input("Digite um conjunto de 9 números para posição inicial ou 'enter' para utilziar a default (213804756): ")

        # Verifica se é valida
        if  len(initialPositionInput) == 9:
            self.puzzle = [int(char) for char in initialPositionInput]
        else:
            self.puzzle = [2, 1, 3, 8, 0, 4, 7, 5, 6]

        self.size = 3  # Define o tamanho do quebra-cabeça (3x3)
        self.empty_pos = self.puzzle.index(0)  # Localiza a posição do espaço vazio (0)
        self.solved = False # Define que não foi resolvido

    def move(self, direction):
        # A função move() permite mover o espaço vazio em uma das quatro direções: 'w' (cima), 's' (baixo), 'a' (esquerda), 'd' (direita)
        # A movimentação é feita trocando a posição do espaço vazio com o elemento na direção especificada
        # As condições garantem que o movimento é válido (por exemplo, não se pode mover para a esquerda se o espaço vazio já estiver na borda esquerda)
        if direction == 'w':
            if self.empty_pos >= self.size: # Valida se o 0 não esta na primeira linha
                self.puzzle[self.empty_pos], self.puzzle[self.empty_pos - self.size] = self.puzzle[self.empty_pos - self.size], self.puzzle[self.empty_pos]
                self.empty_pos -= self.size
        elif direction == 's':
            if self.empty_pos < self.size * (self.size - 1): # Valida se o 0 não esta na ultima linha
                self.puzzle[self.empty_pos], self.puzzle[self.empty_pos + self.size] = self.puzzle[self.empty_pos + self.size], self.puzzle[self.empty_pos]
                self.empty_pos += self.size
        elif direction == 'a':
            if self.empty_pos % self.size != 0: # Valida se o 0 não esta na coluna da esquerda
                self.puzzle[self.empty_pos], self.puzzle[self.empty_pos - 1] = self.puzzle[self.empty_pos - 1], self.puzzle[self.empty_pos]
                self.empty_pos -= 1
        elif direction == 'd':
            if (self.empty_pos + 1) % self.size != 0: # Valida se o 0 não esta na coluna da direita
                self.puzzle[self.empty_pos], self.puzzle[self.empty_pos + 1] = self.puzzle[self.empty_pos + 1], self.puzzle[self.empty_pos]
                self.empty_pos += 1

    def checkIfSolved(self, moves):
        if(self.puzzle == [1, 2, 3, 8, 0, 4, 7, 6, 5]):
            self.solved = True

            print("\n* * * * * Solucionado! * * * * *")
            print("\nMovimentos para a solução:", moves)
            print("\nEstado final:")
            self.display()

    def display(self):
        # A função display() imprime o estado atual do quebra-cabeça na tela linha por linha
        for i in range(self.size):
            print(self.puzzle[i*self.size:(i+1)*self.size])

    def manual(self):
        # Entra em um loop onde exibe o quebra-cabeça, solicita um movimento do usuário e executa o movimento
        # O loop continua até que o usuário digite 'sair' ou soluciona o jogo
        moves = []
        while not self.solved:
            print("\n")
            self.display()
            print("\nUse as teclas w a s d para jogar")
            directionInput = input("Digite uma direção (w, a, s, d) ou 'sair' para sair: ")

            if directionInput == 'sair':
                break
            elif directionInput in ['w', 'a', 's', 'd']:
                moves.append(directionInput)
                self.move(directionInput)
                self.checkIfSolved(moves)
            else:
                print("\nMovimento inválido. Tente novamente.")

    def breadthFirstSearch(self): # Busca em largura (amplitude) - Sem informação
        queue = deque([(self.puzzle, [])])  # Inicializa a fila com o estado inicial e uma lista vazia de movimentos
        visited = set()  # Conjunto para armazenar os estados visitados

        while queue:
            current_state, moves = queue.popleft()  # Pega o próximo estado e sua lista de movimentos
            self.puzzle = current_state  # Atualiza o estado do quebra-cabeça para o estado atual da fila
            self.empty_pos = self.puzzle.index(0)  # Atualiza a posição do espaço vazio

            # Verifica foi resolvido
            self.checkIfSolved(moves)
            if self.solved:
                break

            visited.add(tuple(self.puzzle))  # Adiciona o estado atual aos estados visitados

            # Gera todos os possíveis movimentos a partir do estado atual
            possible_moves = []
            if self.empty_pos >= self.size:  # Pode mover para cima
                possible_moves.append(('w', self.empty_pos - self.size))
            if self.empty_pos < self.size * (self.size - 1):  # Pode mover para baixo
                possible_moves.append(('s', self.empty_pos + self.size))
            if self.empty_pos % self.size != 0:  # Pode mover para a esquerda
                possible_moves.append(('a', self.empty_pos - 1))
            if (self.empty_pos + 1) % self.size != 0:  # Pode mover para a direita
                possible_moves.append(('d', self.empty_pos + 1))

            # Adiciona os novos estados gerados à fila, junto com os movimentos até esse estado
            for move, new_empty_pos in possible_moves:
                new_state = self.puzzle[:]  # Cria uma cópia do estado atual
                new_state[self.empty_pos], new_state[new_empty_pos] = new_state[new_empty_pos], new_state[self.empty_pos]
                if tuple(new_state) not in visited:  # Verifica se o novo estado não foi visitado antes
                    queue.append((new_state, moves + [move]))  # Adiciona o novo estado à fila com os movimentos até ele

        if not self.solved:
            print("\n* * * * * Não foi possível encontrar uma solução * * * * *")

    def bestFirsSearch(self): # Busca pela melhor escolha - Com informação
        queue = [(self.puzzle, [])]  # Inicializa a fila com o estado inicial e uma lista vazia de movimentos
        visited = set()  # Conjunto para armazenar os estados visitados

        while queue:
            queue.sort(key=lambda x: self.manhattanDistance(x[0]))  # Ordena a fila com base na heurística de Distância Manhattan
            current_state, moves = queue.pop(0)  # Pega o próximo estado e sua lista de movimentos
            self.puzzle = current_state  # Atualiza o estado do quebra-cabeça para o estado atual da fila
            self.empty_pos = self.puzzle.index(0)  # Atualiza a posição do espaço vazio

            # Verifica foi resolvido
            self.checkIfSolved(moves)
            if self.solved:
                break

            visited.add(tuple(self.puzzle))  # Adiciona o estado atual aos estados visitados

            # Gera todos os possíveis movimentos a partir do estado atual
            possible_moves = []
            if self.empty_pos >= self.size:  # Pode mover para cima
                possible_moves.append(('w', self.empty_pos - self.size))
            if self.empty_pos < self.size * (self.size - 1):  # Pode mover para baixo
                possible_moves.append(('s', self.empty_pos + self.size))
            if self.empty_pos % self.size != 0:  # Pode mover para a esquerda
                possible_moves.append(('a', self.empty_pos - 1))
            if (self.empty_pos + 1) % self.size != 0:  # Pode mover para a direita
                possible_moves.append(('d', self.empty_pos + 1))

            # Adiciona os novos estados gerados à fila, junto com os movimentos até esse estado
            for move, new_empty_pos in possible_moves:
                new_state = self.puzzle[:]  # Cria uma cópia do estado atual
                new_state[self.empty_pos], new_state[new_empty_pos] = new_state[new_empty_pos], new_state[self.empty_pos]
                if tuple(new_state) not in visited:  # Verifica se o novo estado não foi visitado antes
                    queue.append((new_state, moves + [move]))  # Adiciona o novo estado à fila com os movimentos até ele

        if not self.solved:
            print("\n* * * * * Não foi possível encontrar uma solução * * * * *")

    def manhattanDistance(self, state):
        # Calcula a heurística de Distância Manhattan para uma configuração de quebra-cabeça
        distance = 0
        for i in range(self.size):
            for j in range(self.size):
                value = state[i * self.size + j]
                if value != 0:  # Ignora o espaço vazio
                    target_row = (value - 1) // self.size  # Calcula a linha de destino para o número
                    target_col = (value - 1) % self.size  # Calcula a coluna de destino para o número
                    distance += abs(i - target_row) + abs(j - target_col)  # Calcula a Distância Manhattan
        return distance

    def mainResolutionMethods(self):
        # Controla o fluxo do jogo,, entra em um loop onde exibe os métodos para resolver o quebra-cabeça
        # Ao escolher um método direciona a execução para a função que resolve com o método selecionado
        # O loop continua até que o usuário escolha a opção de sair ou seja resolvido por um dos metodos
        while not self.solved:
            print("\nMétodos de resolução:")
            print("1 - Manual")
            print("2 - Busca em largura (amplitude) - Sem informação")
            print("3 - Busca pela melhor escolha - Sem informação (Ainda não desenvolvido)")
            print("4 - Sair")
            resolutionMethod = input("Informe o método de resolução: ")

            if resolutionMethod == '1':
                self.manual()
            elif resolutionMethod == '2':
                self.breadthFirstSearch()
            elif resolutionMethod == '3':
                self.bestFirsSearch()
            elif resolutionMethod == '4':
                break
            else:
                print("\nMétodo inválido, tente novamente")

def main():
    # Inicia uma instancia de SlidingPuzzle
    slidingPuzzle = SlidingPuzzle()

    # Chama a função de para selecionar método de resolução
    slidingPuzzle.mainResolutionMethods()

if __name__ == "__main__":
    main()
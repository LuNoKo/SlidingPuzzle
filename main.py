class SlidingPuzzle:
    def __init__(self, puzzle):
        self.puzzle = puzzle
        self.size = 3
        self.empty_pos = self.puzzle.index(0)

    def move(self, direction):
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
        for i in range(self.size):
            print(self.puzzle[i*self.size:(i+1)*self.size])


def main():
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
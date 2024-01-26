# Задача
# Написать игру в “Крестики-нолики”. Можете использовать любые парадигмы, которые посчитаете наиболее подходящими.
# Можете реализовать доску как угодно - как одномерный массив или двумерный массив (массив массивов).
# Можете использовать как правила, так и хардкод, на своё усмотрение. Главное, чтобы в игру можно было поиграть
# через терминал с вашего компьютера.

class NoughtsAndCrosses:
    def __init__(self):
        self.board = list(range(1, 10))

    def draw_board(self):
        print('-' * 10)
        for i in range(3):
            print(self.board[0 + i * 3], '|', self.board[1 + i * 3], '|', self.board[2 + i * 3])
            print('-' * 10)

    def make_move(self, cone):
        flag = False
        while not flag:
            answer = input('Куда ставим ' + cone + '? Введите число от 1 до 9: ')

            try:
                answer = int(answer)
            except:
                print('Введите число от 1 до 9: ')
                continue

            if answer >= 1 and answer <= 9:
                if str(self.board[answer - 1]) not in 'X0':
                    self.board[answer - 1] = cone
                    flag = True
                else:
                    print('Клетка занята')
            else:
                print('Введите число от 1 до 9: ')

    def check_win(self):
        win_combo = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
        for each in win_combo:
            if self.board[each[0]] == self.board[each[1]] == self.board[each[2]]:
                return self.board[each[0]]
        return False

    def play(self):
        count = 0
        win = False
        while not win:
            self.draw_board()
            if count % 2 == 0:
                self.make_move('X')
            else:
                self.make_move('0')
            count += 1

            if count > 4:
                check = self.check_win()
                if check:
                    print('Ура, это победа!')
                    win = True
                    break
            if count == 9:
                print('Это ничья!')
                break
        self.draw_board()


game = NoughtsAndCrosses()
game.play()

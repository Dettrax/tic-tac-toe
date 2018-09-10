from numpy import *
class data:
    c = [[9,9,9],[9,9,9],[9,9,9]]
    d = [[0.0,0.1,0.2],[1.0,1.1,1.2],[2.0,2.1,2.2]]
data_object = data()

class check_fill:
    @staticmethod
    def box_fill():
        for i in range(3):
            for j in range(3):
                if (data_object.c[i][j] == 9):
                    return 1
        return 0


class view:
   def view_box(self):
    print('Now the box is(Consider 9 as empty space ) : ', matrix(data_object.c), sep='\n')
    print('Location box is : ')
    for i in data_object.d:
        print(i)
view_object = view()

class intro:
    def start(self):
        print('           Welcome to the multiplayer tic-tac-toe game     ')
class exit_game:
    def bye(self):
        print()
        print('               Devloper Ashish Pandey   ')
        exit(1)

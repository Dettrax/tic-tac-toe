from com_class import*
from check import*
data_object = data()
fill_object = check_fill()
view_object = view()
view_object.view_box()
introduction = intro()
introduction.start()
game_exit = exit_game()
'''    object creation complete '''
def check_fill():
    global ret
    ret = 0
    for i in range(3):
        for j in range(3):
           if data_object.c[i][j]==9:
               ret = 1
    return ret
'''this is where 1 part ends '''
t = checkout()
t1 = checksid()
t2 = checkcros()
fill_flag=1
while(fill_flag==1):
    i,j= [int(x) for x in input('Enter place of 1(E.g:: 0.0 or 2.2 as per location box): ').split('.') ]
    data_object.c[i][j] = 1
    fill_flag = fill_object.box_fill()
    view_object.view_box()
    if (t.checkouter() == 3):
        print('\n1. won by outer  ')
        game_exit.bye()
    elif (t1.checkside() == 3):
        print('\n1. won by side ')
        game_exit.bye()
    elif (t2.checkcross() == 3):
        print('\n1. won by cross  ')
        game_exit.bye()

    if (fill_flag==1):
     i, j = [int(x) for x in input('Enter place of 0(E.g:: 0.0 or 2.2 as per location box): ').split('.')]
     data_object.c[i][j] = 0
     fill_flag = fill_object.box_fill()
     view_object.view_box()
     if (t.checkouter() == 3):
         print('\n0. won by outer')
         game_exit.bye()
         fill_flag=0
     elif (t1.checkside() == 3):
         print('\n0. wonb by side ')
         game_exit.bye()
     elif (t2.checkcross() == 3):
         print('\n0. won by cross ')
         game_exit.bye()
print()
print('                                       Draw')





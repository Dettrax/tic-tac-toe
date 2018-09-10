from com_class import*
data_object = data()
class checkout:
 
   count_1 = 0
   outer_list = [[[[0], [0]], [[0], [1]], [[0], [2]]], [[[0], [0]], [[1], [0]], [[2], [0]]],
                  [[[2], [0]], [[2], [1]], [[2], [2]]], [[[2], [2]], [[1], [2]], [[0], [2]]]]
   @staticmethod
   def checkouter():
     for q in range(4):
        for w in range(3):
            for i in range(3):
                for k in range(3):
                    if (data_object.c[i][k] == 1):
                        for fuc in checkout.outer_list[q][w][0]:
                            for fuc1 in checkout.outer_list[q][w][1]:
                                if (i == fuc and k == fuc1):
                                    checkout.count_1+=1
                                    if (checkout.count_1 == 3):
                                        return 3
        checkout.count_1=0
     checkout.count_1 = 0
     for q in range(4):
       for w in range(3):
           for i in range(3):
               for k in range(3):
                   if (data_object.c[i][k] == 0):
                       for fuc in checkout.outer_list[q][w][0]:
                           for fuc1 in checkout.outer_list[q][w][1]:
                               if (i == fuc and k == fuc1):
                                   checkout.count_1 += 1
                                   if (checkout.count_1 == 3):
                                       return 3
       checkout.count_1 = 0

class checkcros:
   count_1=0 
   cross_list = [[[[0], [0]], [[1], [1]], [[2], [2]]], [[[0], [2]], [[1], [1]], [[2], [0]]]]
   @staticmethod
   def checkcross():
    for q in range(2):
        for w in range(3):
            for i in range(3):
                for k in range(3):
                    if (data_object.c[i][k] == 1):
                        for fuc in checkcros.cross_list[q][w][0]:
                            for fuc1 in checkcros.cross_list[q][w][1]:
                                if (i == fuc and k == fuc1):
                                    checkcros.count_1+=1
                                    if (checkcros.count_1 == 3):
                                        return 3
        checkcros.count_1=0
    checkcros.count_1=0
    for q in range(2):
        for w in range(3):
            for i in range(3):
                for k in range(3):
                    if (data_object.c[i][k] == 0):
                        for fuc in checkcros.cross_list[q][w][0]:
                            for fuc1 in checkcros.cross_list[q][w][1]:
                                if (i == fuc and k == fuc1):
                                    checkcros.count_1+=1
                                    if (checkcros.count_1 == 3):
                                        return 3
        checkcros.count_1=0

class checksid:
   count_1 = 0
   side_list = [[[[1], [0]], [[1], [1]], [[1], [2]]], [[[0], [1]], [[1], [1]], [[2], [1]]]]
   @staticmethod
   def checkside():
    for q in range(2):
        for w in range(3):
            for i in range(3):
                for k in range(3):
                    if (data_object.c[i][k] == 1):
                        for fuc in checksid.side_list[q][w][0]:
                            for fuc1 in checksid.side_list[q][w][1]:
                                if (i == fuc and k == fuc1):
                                    checksid.count_1+=1
                                    if (checksid.count_1 == 3):
                                        return 3
        checksid.count_1=0
    checksid.count_1=0
    for q in range(2):
        for w in range(3):
            for i in range(3):
                for k in range(3):
                    if (data_object.c[i][k] == 0):
                        for fuc in checksid.side_list[q][w][0]:
                            for fuc1 in checksid.side_list[q][w][1]:
                                if (i == fuc and k == fuc1):
                                    checksid.count_1+=1
                                    if (checksid.count_1 == 3):
                                        return 3
        checksid.count_1=0



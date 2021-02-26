# -*- coding: utf-8 -*-
# @Time    : 
# @Author  : huoyanyang
# @Site    : 
# @File    : 
# @Software: PyCharm
def bubblesort(list):
    length = len(list)
    for index in range(length):
        print(index)
        for j in range(1,length-index):
            if list[j-1]>list[j]:
               list[j-1],list[j]=list[j],list[j-1]
               print(list)
    return list


def bubble_sort_flag(list):
    length = len(list)
    for index in range(length):
        flag = True
        for j in range(1,length-index):
            if list[j-1]>list[j]:
                list[j-1],list[j]=list[j],list[j-1]
                flag=False
        if flag:
            return list
    return list


def selection_sort(list):
    n=len(list)
    for i in range(0,n):
        min = i
        for j in range(i+1,n):
            if list[j]<list[min]:
                print(str(min)+"andj"+str(j)+"andi"+str(i))
                min = j
            if list[min] <list[i]:
                list[min],list[i]=list[i],list[min]
                print(str(list))
    return list

if __name__=="__main__":
    list=[9,6,3,8,4,2]
    # print("sortlist:"+str(bubblesort(list)))

    # print("bubble_sortlist_flag:"+str(bubble_sort_flag(list)))

    print( "selection_sort:" + str( selection_sort( list ) ) )
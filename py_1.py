box1 = 6
box2 = 6
box3 = 6
i_num = None
i_box = None

while True:
    print(box1, box2, box3)
    try:
        i_box, i_num = (int(x) for x in input(">>>").split())
    except IndexError:
        print("Error")
    except ValueError:
        print("Error")
    else:
        if i_box == 1 and i_num <= box1:
            box1 -= i_num
        if i_box == 2 and i_num <= box2:
            box2 -= i_num
        if i_box == 3 and i_num <= box3:
            box3 -= i_num
        if box1 == 0 and box2 == 0 and box3 == 0:
            break

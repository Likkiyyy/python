import random


lists = ["グー","チョキ","パー"]
cpu = None
cpu_num = None
i = None



while True:
    list = lists[i]
    cpu_num = random.randint(0,4)
    cpu = lists[cpu_num]
    while True:
        print("最初はグー、じゃんけん....")
        try:
            i = int(input("ポン！>>>"))
        except IndexError:
            print("Error")
        except ValueError:
            print("Error")
        else:
            if i == cpu_num:
                while True:
                    print("aikoで....")
                try:
                    i = int(input("しょ！>>>"))
                except IndexError:
                    print("Error")
                except ValueError:
                    print("Error")
                else:







                break



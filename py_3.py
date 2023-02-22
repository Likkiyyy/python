import random

lists = ["グー", "チョキ", "パー"]
cpu = None
cpu_num = None
i = None
list = None

# 勝ち１負け２あいこ３
def judge():
    if i == 0 and cpu_num == 1:
        jg = 1
        return jg
    if i == 0 and cpu_num == 2:
        jg = 2
        return jg
    if i == 1 and cpu_num == 0:
        jg = 2
        return jg
    if i == 1 and cpu_num == 2:
        jg = 1
        return jg
    if i == 2 and cpu_num == 0:
        jg = 1
        return jg
    if i == 2 and cpu_num == 1:
        jg = 2
        return jg
    if i == cpu_num:
        jg = 3
        return jg





while True:
    print("最初はグー、じゃんけん....")
    try:
        i = int(input("ポン！>>>"))
    except IndexError:
        print("Error")
    except ValueError:
        print("Error")
    else:
        if i == 1 or i == 2 or i == 3:
            break


list = lists[i]
cpu_num = random.randint(1, 3)
cpu = lists[cpu_num]
re = judge()
if re == 1:
    print("相手は"+cpu+"あなたの勝ち")
if re == 2:
    print("相手は"+cpu+"あなたの負け")


print(re)
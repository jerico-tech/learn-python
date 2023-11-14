"""
循环综合练习
"""

import random

number = 1
totle = 10000
while number <= 20:
    score = random.randint(1,10)
    if score > 5:
        if totle > 0:
            totle -= 1000
            print(f"员工{number}，绩效分{score}分，发放工资1000元，账户余额还剩{totle}元")
            number += 1
        else:
            print(f"工资发完了，下个月领吧。")
            break
    else:
        print(f"员工{number}，绩效分{score}分，低于5分，不发工资，下一位")
        number += 1
        continue
#coding:gbk
"""
第一个小项目：Rock-paper-scissors-lizard-Spock
作者：肖浩然
日期：2021.11.26
"""

import random
number=random.randint(0,4)



# 0 - 石头
# 1 - 史波克
# 2 - 纸
# 3 - 蜥蜴
# 4 - 剪刀

# 以下为完成游戏所需要用到的自定义函数

def name_to_number(name):
    if  name=="石头":
        num1=0
        print("您的选择为：石头")
        return num1
    elif name=="史波克":
        num1=1
        print("您的选择为：史波克")
        return num1
    elif name=="纸":
        num1=2
        print("您的选择为：纸")
        return num1
    elif name=="蜥蜴":
        num1=3
        print("您的选择为：蜥蜴")
        return num1
    elif name=="剪刀":
        num1=4
        print("您的选择为：剪刀")
        return num1
    else:
        print("Error: No Correct Name")
        num1=9
        return num1




    # 使用if/elif/else语句将各游戏对象对应到不同的整数
    # 不要忘记返回结果





def number_to_name(num2):
    if num2==0:
        name2="石头"
        print("计算机的选择为：石头")
        return name2
    elif num2==1:
        name2="史波克"
        print("计算机的选择为：史波克")
        return name2
    elif num2==2:
        name2="纸"
        print("计算机的选择为：纸")
        return name2
    elif num2==3:
        name2="蜥蜴"
        print("计算机的选择为：蜥蜴")
        return name2
    elif num2==4:
        name2="剪刀"
        print("计算机的选择为：剪刀")
        return name2





def rpsls(player_choice):
     i=name_to_number(player_choice)
     if i==0:
         nam = number_to_name(number)
         if nam=="石头":
             print("您和计算机出的一样呢")
         elif nam=="史波克":
             print("机器赢了")
         elif nam=="纸":
             print("机器赢了")
         elif nam=="蜥蜴":
             print("您赢了！")
         elif nam=="剪刀":
             print("您赢了！")
     elif i==1:
         nam = number_to_name(number)
         if nam=="石头":
             print("您赢了！")
         elif nam == "史波克":
             print("您和计算机出的一样呢")
         elif nam == "纸":
             print("机器赢了")
         elif nam == "蜥蜴":
             print("机器赢了")
         elif nam == "剪刀":
             print("您赢了！")
     elif i==2:
         nam = number_to_name(number)
         if nam=="石头":
             print("您赢了！")
         elif nam == "史波克":
             print("您赢了！")
         elif nam == "纸":
             print("您和计算机出的一样呢")
         elif nam == "蜥蜴":
             print("机器赢了")
         elif nam == "剪刀":
             print("机器赢了")
     elif i==3:
         nam = number_to_name(number)
         if nam=="石头":
             print("机器赢了")
         elif nam == "史波克":
             print("您赢了！")
         elif nam == "纸":
             print("您赢了！")
         elif nam == "蜥蜴":
             print("您和计算机出的一样呢")
         elif nam == "剪刀":
             print("机器赢了")
     elif i==4:
         nam = number_to_name(number)
         if nam=="石头":
             print("机器赢了")
         elif nam == "史波克":
             print("机器赢了")
         elif nam == "纸":
             print("您赢了！")
         elif nam == "蜥蜴":
             print("您赢了！")
         elif nam == "剪刀":
             print("您和计算机出的一样呢")
     elif i==9:
             print()









    # 输出"-------- "进行分割
    # 显示用户输入提示，用户通过键盘将自己的游戏选择对象输入，存入变量player_choice

    # 调用name_to_number()函数将用户的游戏选择对象转换为相应的整数，存入变量player_choice_number

    # 利用random.randrange()自动产生0-4之间的随机整数，作为计算机随机选择的游戏对象，存入变量comp_number

    # 调用number_to_name()函数将计算机产生的随机数转换为对应的游戏对象

    # 在屏幕上显示计算机选择的随机对象

    # 利用if/elif/else 语句，根据RPSLS规则对用户选择和计算机选择进行判断，并在屏幕上显示判断结果

    # 如果用户和计算机选择一样，则显示“您和计算机出的一样呢”，如果用户获胜，则显示“您赢了”，反之则显示“计算机赢了”

0

# 对程序进行测试
print("欢迎使用RPSLS游戏")
print("----------------")
print("请输入您的选择:")
choice_name=input()
rpsls(choice_name)



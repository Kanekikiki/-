#coding:gbk
"""
��һ��С��Ŀ��Rock-paper-scissors-lizard-Spock
���ߣ�Ф��Ȼ
���ڣ�2021.11.26
"""

import random
number=random.randint(0,4)



# 0 - ʯͷ
# 1 - ʷ����
# 2 - ֽ
# 3 - ����
# 4 - ����

# ����Ϊ�����Ϸ����Ҫ�õ����Զ��庯��

def name_to_number(name):
    if  name=="ʯͷ":
        num1=0
        print("����ѡ��Ϊ��ʯͷ")
        return num1
    elif name=="ʷ����":
        num1=1
        print("����ѡ��Ϊ��ʷ����")
        return num1
    elif name=="ֽ":
        num1=2
        print("����ѡ��Ϊ��ֽ")
        return num1
    elif name=="����":
        num1=3
        print("����ѡ��Ϊ������")
        return num1
    elif name=="����":
        num1=4
        print("����ѡ��Ϊ������")
        return num1
    else:
        print("Error: No Correct Name")
        num1=9
        return num1




    # ʹ��if/elif/else��佫����Ϸ�����Ӧ����ͬ������
    # ��Ҫ���Ƿ��ؽ��





def number_to_name(num2):
    if num2==0:
        name2="ʯͷ"
        print("�������ѡ��Ϊ��ʯͷ")
        return name2
    elif num2==1:
        name2="ʷ����"
        print("�������ѡ��Ϊ��ʷ����")
        return name2
    elif num2==2:
        name2="ֽ"
        print("�������ѡ��Ϊ��ֽ")
        return name2
    elif num2==3:
        name2="����"
        print("�������ѡ��Ϊ������")
        return name2
    elif num2==4:
        name2="����"
        print("�������ѡ��Ϊ������")
        return name2





def rpsls(player_choice):
     i=name_to_number(player_choice)
     if i==0:
         nam = number_to_name(number)
         if nam=="ʯͷ":
             print("���ͼ��������һ����")
         elif nam=="ʷ����":
             print("����Ӯ��")
         elif nam=="ֽ":
             print("����Ӯ��")
         elif nam=="����":
             print("��Ӯ�ˣ�")
         elif nam=="����":
             print("��Ӯ�ˣ�")
     elif i==1:
         nam = number_to_name(number)
         if nam=="ʯͷ":
             print("��Ӯ�ˣ�")
         elif nam == "ʷ����":
             print("���ͼ��������һ����")
         elif nam == "ֽ":
             print("����Ӯ��")
         elif nam == "����":
             print("����Ӯ��")
         elif nam == "����":
             print("��Ӯ�ˣ�")
     elif i==2:
         nam = number_to_name(number)
         if nam=="ʯͷ":
             print("��Ӯ�ˣ�")
         elif nam == "ʷ����":
             print("��Ӯ�ˣ�")
         elif nam == "ֽ":
             print("���ͼ��������һ����")
         elif nam == "����":
             print("����Ӯ��")
         elif nam == "����":
             print("����Ӯ��")
     elif i==3:
         nam = number_to_name(number)
         if nam=="ʯͷ":
             print("����Ӯ��")
         elif nam == "ʷ����":
             print("��Ӯ�ˣ�")
         elif nam == "ֽ":
             print("��Ӯ�ˣ�")
         elif nam == "����":
             print("���ͼ��������һ����")
         elif nam == "����":
             print("����Ӯ��")
     elif i==4:
         nam = number_to_name(number)
         if nam=="ʯͷ":
             print("����Ӯ��")
         elif nam == "ʷ����":
             print("����Ӯ��")
         elif nam == "ֽ":
             print("��Ӯ�ˣ�")
         elif nam == "����":
             print("��Ӯ�ˣ�")
         elif nam == "����":
             print("���ͼ��������һ����")
     elif i==9:
             print()









    # ���"-------- "���зָ�
    # ��ʾ�û�������ʾ���û�ͨ�����̽��Լ�����Ϸѡ��������룬�������player_choice

    # ����name_to_number()�������û�����Ϸѡ�����ת��Ϊ��Ӧ���������������player_choice_number

    # ����random.randrange()�Զ�����0-4֮��������������Ϊ��������ѡ�����Ϸ���󣬴������comp_number

    # ����number_to_name()����������������������ת��Ϊ��Ӧ����Ϸ����

    # ����Ļ����ʾ�����ѡ����������

    # ����if/elif/else ��䣬����RPSLS������û�ѡ��ͼ����ѡ������жϣ�������Ļ����ʾ�жϽ��

    # ����û��ͼ����ѡ��һ��������ʾ�����ͼ��������һ���ء�������û���ʤ������ʾ����Ӯ�ˡ�����֮����ʾ�������Ӯ�ˡ�

0

# �Գ�����в���
print("��ӭʹ��RPSLS��Ϸ")
print("----------------")
print("����������ѡ��:")
choice_name=input()
rpsls(choice_name)



check = float(input("�����̸� 1, �����̸� 0�� �Է��ϼ���: "))
weight = input("������: ")
waist = input("�㸮�ѷ�: ")
wrfm =76-(28* weight/waist)
mrfm = 64-(20* weight/waist)

if check == 0:
    print(wrfm)
else:
    print(mrfm)


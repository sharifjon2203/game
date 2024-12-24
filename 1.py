# L1 = ["share", "share", "share"]
# L2 = ["steal", "share", "steal"]

# L1 = ["steal"]
# L2 = ["steal"]

def game(lst1, lst2):
    l1_coin, l2_coin = 3,3
    for l1, l2 in zip(lst1,lst2):
        if l1.lower() == 'share':
            l1_coin-=1
            l2_coin+=3
        if l2.lower() == 'share':
            l2_coin-=1
            l1_coin+=3
    return [ l1_coin, l2_coin ]


def play():
    print("\nInputlarni Kirish Boshlandi !\nChiqish - q yoki x yoki xar qanday raqam bolmagan input\nQoidalar Inputlar soni tengligiga amal qilingan xolda natija chiqariladi agar L2-playerga Input berilmasdan chiqish kelsa L1-ni oxirgi inputi inobatga olinmaydi !!!\n")
    counter = 0
    L1 = []
    L2 = []
    while True:
        
        num=input(f"\nL1 - uchun \n[1]- Share yoki \n[2]- Steal tanlang...\n      ->-> ")
        
        if not num.isdigit():
            print("\n\n",game(L1,L2))
            print("\nDasturdan Chiqildi")
            break
        elif num.isdigit():
            choice1 = int(num)

        if 1 == choice1:
            L1.append("share")
        elif 2 == choice1:
            L1.append("steal")
        
        
        
        num=input(f"\nL2 - uchun \n[1]- Share yoki \n[2]- Steal tanlang...\n      ->-> ")

        if not num.isdigit():
            L1.pop()
            print("\n\n",game(L1,L2))
            print("\nDasturdan Chiqildi")
            break
        elif num.isdigit():
            choice1 = int(num)

        if 1 == choice1:
            L2.append("share")
        elif 2 == choice1:
            L2.append("steal")

        
    
play()


    


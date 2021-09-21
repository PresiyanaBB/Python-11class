money = float(input())
broi = 0
for i in range(0,21):
    enter = str(input())
    if enter == "mall.Enter":
        for i in range(0, 21):
            what = str(input())
            for x in what:
              if what != "mall.Exit" and money > 0:
                if x.isupper():
                    money -= ord(x) / 2
                    broi += 1
                elif x.islower():
                    money -= ord(x) * 0.3
                    broi += 1
                elif x == "%":
                    money = money / 2
                    broi += 1
                elif x == "*":
                    money += 10
                    broi += 1
                else:
                    money -= ord(x)
                    broi += 1
            else:
               break
        break
print("Number of purchases: " + str(broi))
print("Money left: " + str(money) + " lv.")

finger_dic = {"G":0, "C":2, "P":5}

win_dic = {"G":"P", "C":"G", "P":"C"}
lose_dic = {"G":"C", "C":"P", "P":"G"}
tie_dic = {"G":"G", "C":"C", "P":"P"}

hand_list = ("G", "C", "P")

pattern_list = []
pair_hand_list = list(input().upper())

for i in pair_hand_list:
    pattern_list.append(win_dic[i])

print(pattern_list)

import random
list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]

# индекс середины
#здесь уже было все выполнено


middle_index = len(list_players) // 2
first_team = list_players[:middle_index]
second_team = list_players[middle_index:]
print(first_team)
print(second_team)



#мое решение

# middle_index = len(list_players) // 2
# total_random = random.sample(range(0, len(list_players)), len(list_players))
# first_team_numbers =total_random[:middle_index]
# second_team_numbers=total_random[middle_index:]
#
# first_team=list(list_players[i] for i in first_team_numbers)
# second_team=list(list_players[i] for i in second_team_numbers)
#
# print(first_team)
# print(second_team)
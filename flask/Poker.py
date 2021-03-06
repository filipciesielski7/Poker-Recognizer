# Algorytm wyszukujący najlepszy układ w pokerze
def findSystem(cards_info):
    ranks = ['Dwojka', 'Trojka', 'Czworka', 'Piatka', 'Szostka', 'Siodemka',
                    'Osemka', 'Dziewiatka', 'Dziesiatka', 'Walet', 'Dama', 'Krol', 'As']
    results = []
    final_result = ""

    valid = True
    for i in range(len(cards_info)):
        if(cards_info[i][0] == "Nieznany" or cards_info[i][1] == "Nieznany"):
            valid = False

    if(valid):
        if(len(cards_info) < 7 or len(cards_info) > 7):
            final_result = "Niewlasciwa ilosc kart"
        else:
            for i in range(len(cards_info)):
                for j in range(len(cards_info)):
                    temp_cards_info = []
                    if(i != j):
                        for k in range(len(cards_info)):
                            if(k != i and k != j):
                                temp_cards_info.append(cards_info[k])

                        temp_cards_rank = []
                        temp_cards_color = []
                        for m in range(len(temp_cards_info)):
                            temp_cards_rank.append(temp_cards_info[m][0])
                            temp_cards_color.append(temp_cards_info[m][1])

                        all_same_color = False
                        color = ""
                        for l in range(len(temp_cards_color)):
                            temp_color = temp_cards_color[l]
                            number = 0
                            for v in range(len(temp_cards_color)):
                                if(l != v):
                                    if(temp_cards_color[v] == temp_color):
                                        number += 1
                            if(number == 4):
                                color = temp_color
                                all_same_color = True

                        if(all_same_color):
                            to_be_added = []
                            for i in range(len(temp_cards_info)):
                                if(temp_cards_info[i][1] == color):
                                    to_be_added.append(temp_cards_info[i])
                            results.append(["Kolor", to_be_added])
                        if(ranks[8] in temp_cards_rank and ranks[9] in temp_cards_rank and ranks[10] in temp_cards_rank and ranks[11] in temp_cards_rank and ranks[12] in temp_cards_rank):
                            if(all_same_color):
                                to_be_added = []
                                for i in range(len(temp_cards_info)):
                                    if(temp_cards_info[i][1] == color):
                                        to_be_added.append(temp_cards_info[i])
                                results.append(["Poker Krolewski", to_be_added])
                        for i in range(8):
                            if(ranks[i+1] in temp_cards_rank and ranks[i+2] in temp_cards_rank and ranks[i+3] in temp_cards_rank and ranks[i+4] in temp_cards_rank and ranks[i+5] in temp_cards_rank):
                                if(all_same_color):
                                    to_be_added = []
                                    for i in range(len(temp_cards_info)):
                                        if(temp_cards_info[i][1] == color):
                                            to_be_added.append(temp_cards_info[i])
                                    results.append(["Poker", to_be_added])
                                to_be_added = []
                                for j in range(len(temp_cards_info)):
                                    if(temp_cards_info[j][0] == ranks[i+1] or temp_cards_info[j][0] == ranks[i+2] or temp_cards_info[j][0] == ranks[i+3] or temp_cards_info[j][0] == ranks[i+4] or temp_cards_info[j][0] == ranks[i+5]):
                                        to_be_added.append(temp_cards_info[j])
                                results.append(["Strit", to_be_added])

                        four_same_rank = False
                        for n in range(len(temp_cards_rank)):
                            temp_rank = temp_cards_rank[n]
                            number = 0
                            for o in range(len(temp_cards_rank)):
                                if(n != o):
                                    if(temp_cards_rank[o] == temp_rank):
                                        number += 1
                            if(number == 3):
                                current_rank = temp_rank
                                four_same_rank = True
                            
                        if(four_same_rank):
                            to_be_added = []
                            best_rank = 0
                            index = -1
                            for i in range(len(temp_cards_info)):
                                if(temp_cards_info[i][0] == current_rank):
                                    to_be_added.append(temp_cards_info[i])
                                else:
                                    for j in range(len(ranks)):
                                        if(ranks[j] == temp_cards_info[i][0]):
                                            if(j >= best_rank):
                                                best_rank = j
                                                index = i

                            to_be_added.append(temp_cards_info[index])
                            results.append(["Kareta", to_be_added])
                        
                        three_same_rank = False
                        full_rank = False
                        three_rank = ""
                        full_rank_value =""
                        for n in range(len(temp_cards_rank)):
                            temp_rank = temp_cards_rank[n]
                            number = 0
                            for o in range(len(temp_cards_rank)):
                                if(n != o):
                                    if(temp_cards_rank[o] == temp_rank):
                                        number += 1
                            if(number == 2):
                                three_rank = temp_rank
                                three_same_rank = True
                                for p in range(len(temp_cards_rank)):
                                    temp_rank2 = temp_cards_rank[p]
                                    number2 = 0
                                    for r in range(len(temp_cards_rank)):
                                        if(r != p):
                                            if(temp_cards_rank[r] == temp_rank2 and temp_rank2 != temp_rank):
                                                number2 += 1
                                    if(number2 == 1):
                                        full_rank_value = temp_rank2
                                        full_rank = True
                            
                        if(three_same_rank):
                            to_be_added = []
                            for n in range(len(temp_cards_info)):
                                if(temp_cards_info[n][0] == three_rank):
                                    to_be_added.append(temp_cards_info[n])

                            for k in range(2):
                                index = -1
                                best_rank = 0
                                for p in range(len(temp_cards_info)):
                                    for q in range(len(ranks)):
                                        if(ranks[q] == temp_cards_info[p][0] and temp_cards_info[p] not in to_be_added):
                                            if(q >= best_rank):
                                                best_rank = q
                                                index = p
                                to_be_added.append(temp_cards_info[index])

                            results.append(["Trojka", to_be_added])
                        if(full_rank):
                            to_be_added = []
                            for n in range(len(temp_cards_info)):
                                if(temp_cards_info[n][0] == three_rank):
                                    to_be_added.append(temp_cards_info[n])
                            
                            for n in range(len(temp_cards_info)):
                                if(temp_cards_info[n][0] == full_rank_value):
                                    to_be_added.append(temp_cards_info[n])
                            
                            results.append(["Full", to_be_added])
                            
                        two_same_rank = False
                        pair = ""
                        for t in range(len(temp_cards_rank)):
                            temp_rank = temp_cards_rank[t]
                            number = 0
                            for q in range(len(temp_cards_rank)):
                                if(t != q):
                                    if(temp_cards_rank[q] == temp_rank):
                                        number += 1
                                        pair = temp_rank
                            if(number == 1):
                                two_same_rank = True

                        double_pair = ""
                        double = False
                        if(two_same_rank):
                            for e in range(len(temp_cards_rank)):
                                if(temp_cards_rank[e] != pair):
                                    temp_rank = temp_cards_rank[e]
                                    number = 0
                                    for d in range(len(temp_cards_rank)):
                                        if(e != d):
                                            if(temp_cards_rank[d] == temp_rank):
                                                number += 1
                                                double_pair = temp_rank
                                    if(number == 1):
                                        double = True

                        to_be_added = []
                        if(two_same_rank):
                            for i in range(len(temp_cards_info)):
                                if(temp_cards_info[i][0] == pair):
                                    to_be_added.append(temp_cards_info[i])
                            if(double):
                                for j in range(len(temp_cards_info)):
                                    if(temp_cards_info[j][0] == double_pair):
                                        to_be_added.append(temp_cards_info[j])

                        if(two_same_rank):
                            if(double):
                                best_rank = 0
                                index = -1
                                for i in range(len(temp_cards_info)):
                                    for j in range(len(ranks)):
                                        if(ranks[j] == temp_cards_info[i][0] and temp_cards_info[i] not in to_be_added):
                                            if(j >= best_rank):
                                                best_rank = j
                                                index = i
                                to_be_added.append(temp_cards_info[index])
                                results.append(["Dwie Pary", to_be_added])
                            else:
                                for i in range(3):
                                    best_rank = 0
                                    index = -1
                                    for i in range(len(temp_cards_info)):
                                        for j in range(len(ranks)):
                                            if(ranks[j] == temp_cards_info[i][0] and temp_cards_info[i] not in to_be_added):
                                                if(j >= best_rank):
                                                    best_rank = j
                                                    index = i
                                    to_be_added.append(temp_cards_info[index])
                                results.append(["Para", to_be_added])

        if(results == [] and final_result == ""):
            to_be_removed = []
            for i in range(len(cards_info)):
                temp_card_rank = ranks.index(cards_info[i][0])
                number = 0
                for j in range(len(cards_info)):
                    if(i != j):
                        if(ranks.index(cards_info[j][0]) > temp_card_rank):
                            number += 1
                if(number >= 5):
                    to_be_removed.append(cards_info[i][0])

            five_cards_list = []
            for i in range(len(cards_info)):
                if(cards_info[i] not in to_be_removed):
                    five_cards_list.append(cards_info[i])
            results.append(["Wysoka karta", five_cards_list])

        ranking = ["Poker Krolewski", "Poker", "Kareta", "Full", "Kolor", "Strit", "Trojka", "Dwie Pary", "Para", "Wysoka karta"]

        results2 = []
        for i in range(len(ranking)):
            if(results2 != []):
                continue
            else:
                for j in range(len(results)):
                    if(results[j][0] == ranking[i]):
                        results2.append(results[j])
        
        combinations = []
        for i in range(len(results2)):
            for j in range(len(results2[i][1])):
                if(len(results2[i][1]) == 5):
                    combinations.append(results2[i])
                elif(len(results2[i][1]) == 6):
                    cards_info = results2[i][1]
                    index = 0
                    for l in range(len(cards_info)):
                        temp_cards_info = []
                        for m in range(len(cards_info)):
                            if(m != index):
                                temp_cards_info.append(cards_info[m])
                        index += 1
                        combinations.append([results2[i][0], temp_cards_info])
                elif(len(results2[i][1]) == 7):
                    cards_info = results2[i][1]
                    for l in range(len(cards_info)):
                        for m in range(len(cards_info)):
                            temp_cards_info = []
                            if(l != m):
                                for k in range(len(cards_info)):
                                    if(k != l and k != m):
                                        temp_cards_info.append(cards_info[k])
                            combinations.append([results2[i][0], temp_cards_info])

        points_array = []
        for i in range(len(combinations)):
            points = 0
            for j in range(len(combinations[i][1])):
                if(len(combinations[i][1])==5):
                    for k in range(len(ranks)):
                        if(combinations[i][1][j][0] == ranks[k]):
                            points += (k + 1)
            points_array.append([combinations[i], points])
        
        sorted_points_array = sorted(points_array, key=lambda x: x[1], reverse=True)

        combination = []
        if(len(sorted_points_array) != 0):
            combination = sorted_points_array[0][0][1]

        if(final_result != "Niewlasciwa ilosc kart"):
           final_result = results2[0][0]
    else:
        combination = []
        final_result = "Nie odczytano poprawnie wszystkich kart"
    return final_result, combination
import cv2
import numpy as np
import time
import os
import Cards

# Wymiary obrazu
IM_WIDTH = 1280
IM_HEIGHT = 720

frame_rate_calc = 1

# Czcionka
font = cv2.FONT_HERSHEY_SIMPLEX

time.sleep(1)

# Załadowanie porównujących rang i kolorów
path = os.path.dirname(os.path.abspath(__file__))
train_ranks = Cards.load_ranks(path + '/Images/')
train_colors = Cards.load_colors(path + '/Images/')


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
                        current_rank = ""
                        current_rank2 = ""
                        for n in range(len(temp_cards_rank)):
                            temp_rank = temp_cards_rank[n]
                            number = 0
                            for o in range(len(temp_cards_rank)):
                                if(n != o):
                                    if(temp_cards_rank[o] == temp_rank):
                                        number += 1
                                        current_rank = temp_rank
                            if(number == 2):
                                three_same_rank = True
                                for p in range(len(temp_cards_rank)):
                                    temp_rank2 = temp_cards_rank[p]
                                    number2 = 0
                                    for r in range(len(temp_cards_rank)):
                                        if(r != p):
                                            if(temp_cards_rank[r] == temp_rank2 and temp_rank2 != temp_rank):
                                                number2 += 1
                                                current_rank2 = temp_rank2
                                    if(number2 == 1):
                                        full_rank = True
                            
                        to_be_added = []
                        best_rank = 0
                        index = -1
                        if(three_same_rank):
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

                            best_rank2 = 0
                            index2 = -1
                            for i in range(len(temp_cards_info)):
                                for j in range(len(ranks)):
                                        if(ranks[j] == temp_cards_info[i][0] and temp_cards_info[i] not in to_be_added):
                                                if(j >= best_rank2):
                                                    best_rank2 = j
                                                    index2 = i
                            to_be_added.append(temp_cards_info[index2])
                            results.append(["Trojka", to_be_added])

                        to_be_added = []
                        if(full_rank):
                            for i in range(len(temp_cards_info)):
                                    if(temp_cards_info[i][0] == current_rank):
                                        to_be_added.append(temp_cards_info[i])
                            for i in range(len(temp_cards_info)):
                                if(temp_cards_info[i][0] == current_rank2):
                                    to_be_added.append(temp_cards_info[i])
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
        combination = sorted_points_array[0][0][1]

        if(final_result != "Niewlasciwa ilosc kart"):
           final_result = results2[0][0]
    else:
        final_result = "Nie odczytano poprawnie wszystkich kart"
    return final_result, combination


# Funkcja zwracajaca informacje o przerobionym obrazie wejściowym
def drawImage(img):
    global frame_rate_calc
    dim = (IM_WIDTH, IM_HEIGHT)

    image = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
    
    # Wstępna obróbka obrazu (wyszarzenie, blurowanie i progowanie)
    pre_process = Cards.preprocess_image(image)

    # Znalezienio i posortowanie konturów wszystkich kart na obrazku
    contours_sort, contour_is_card = Cards.find_cards(pre_process)

    # Jeśli nie ma konturów, nie robimy nic
    if len(contours_sort) != 0:

        # Zmienne służące przechowaniu kart z obrazka
        cards = []
        cards_info = []
        k = 0

        # Dla każdego znalezionego konturu:
        for i in range(len(contours_sort)):
            if (contour_is_card[i] == 1):

                # Dodanie nowej karty ze znalezionego konturu
                cards.append(Cards.preprocess_card(contours_sort[i], image))

                # Znalezienie najlepszej rangi i koloru dla nowo znalezionej karty
                cards[k].best_rank_match, cards[k].best_color_match, cards[k].rank_diff, cards[
                    k].color_diff = Cards.match_card(cards[k], train_ranks, train_colors)

                # Narysowanie centroidu i wypisanie nazwy karty
                image, rank_name, color_name = Cards.draw_results(image, cards[k])
                cards_info.append([rank_name, color_name])
                k += 1

        # Wykorzystanie algorytmu wyszukującego najlepszy układ w pokerze
        final_result, combination = findSystem(cards_info)
        print(combination)

        # Wypisanie najlepszej mozliwej kombinacji podanych kart
        cv2.putText(image, final_result, (5, IM_HEIGHT//2 - 305), font, 1.95, (0, 0, 0), 3, cv2.LINE_AA)
        cv2.putText(image, final_result, (5, IM_HEIGHT//2 - 305), font, 1.95, (255, 255, 255), 2, cv2.LINE_AA)

        # Narysowanie konturu na wejściowym obrazku
        if (len(cards) != 0):
            temp_cnts = []
            for i in range(len(cards)):
                temp_cnts.append(cards[i].contour)
            cv2.drawContours(image, temp_cnts, -1, (255, 0, 0), 2)

    # Zwrócenie obrazka ze znalezionymi kartami
    return image
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
            final_result = "Niewłaściwa ilość kart"
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
                        for l in range(len(temp_cards_color)):
                            temp_color = temp_cards_color[l]
                            number = 0
                            for v in range(len(temp_cards_color)):
                                if(l != v):
                                    if(temp_cards_color[v] == temp_color):
                                        number += 1
                            if(number == 4):   
                                all_same_color = True

                        if(all_same_color):
                            results.append(["Kolor", temp_cards_info])
                        if(ranks[8] in temp_cards_rank and ranks[9] in temp_cards_rank and ranks[10] in temp_cards_rank and ranks[11] in temp_cards_rank and ranks[12] in temp_cards_rank):
                            if(all_same_color):
                                results.append(["Poker Krolewski", temp_cards_info])
                        for i in range(8):
                            if(ranks[i+1] in temp_cards_rank and ranks[i+2] in temp_cards_rank and ranks[i+3] in temp_cards_rank and ranks[i+4] in temp_cards_rank and ranks[i+5] in temp_cards_rank):
                                if(all_same_color):
                                        results.append(["Poker", temp_cards_info])
                                results.append(["Strit", temp_cards_info])

                        four_same_rank = False
                        for n in range(len(temp_cards_rank)):
                            temp_rank = temp_cards_rank[n]
                            number = 0
                            for o in range(len(temp_cards_rank)):
                                if(n != o):
                                    if(temp_cards_rank[o] == temp_rank):
                                        number += 1
                            if(number == 3):
                                four_same_rank = True
                            
                        if(four_same_rank):
                            results.append(["Kareta", temp_cards_info])
                            
                        three_same_rank = False
                        full_rank = False
                        for n in range(len(temp_cards_rank)):
                            temp_rank = temp_cards_rank[n]
                            number = 0
                            for o in range(len(temp_cards_rank)):
                                if(n != o):
                                    if(temp_cards_rank[o] == temp_rank):
                                        number += 1
                            if(number == 2):
                                three_same_rank = True
                                for p in range(len(temp_cards_rank)):
                                    temp_rank2 = temp_cards_rank[p]
                                    number2 = 0
                                    for r in range(len(temp_cards_rank)):
                                        if(r != p):
                                            if(temp_cards_rank[r] == temp_rank2 and temp_rank2 != temp_rank):
                                                number2 += 1
                                    if(number2 == 1):
                                        full_rank = True
                            
                        if(three_same_rank):
                            results.append(["Trojka", temp_cards_info])
                        if(full_rank):
                            results.append(["Full", temp_cards_info])

                        two_same_rank = False
                        pair = 'undefined'
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
                                results.append(["Para", temp_cards_info])

                        if(two_same_rank):
                            for e in range(len(temp_cards_rank)):
                                if(temp_cards_rank[e] != pair):
                                    temp_rank = temp_cards_rank[e]
                                    number = 0
                                    for d in range(len(temp_cards_rank)):
                                        if(e != d):
                                            if(temp_cards_rank[d] == temp_rank):
                                                number += 1
                                    if(number == 1):
                                        results.append(["Dwie Pary", temp_cards_info])

        if(results == []):
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
                
        final_result = results2[0][0]
    else:
        final_result = "Nie odczytano poprawnie wszystkich kart"
    return final_result


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
        final_result = findSystem(cards_info)
        print(final_result)

        # Wypisanie najlepszej mozliwej kombinacji podanych kart
        if(final_result != "Niewłaściwa ilość kart"):
            cv2.putText(image, final_result, (IM_WIDTH//2 - 150, IM_HEIGHT//2 - 300), font, 2, (0, 0, 0), 3, cv2.LINE_AA)
            cv2.putText(image, final_result, (IM_WIDTH//2 - 150, IM_HEIGHT//2 - 300), font, 2, (255, 0, 255), 2, cv2.LINE_AA)

        # Narysowanie konturu na wejściowym obrazku
        if (len(cards) != 0):
            temp_cnts = []
            for i in range(len(cards)):
                temp_cnts.append(cards[i].contour)
            cv2.drawContours(image, temp_cnts, -1, (255, 0, 0), 2)

    # Zwrócenie obrazka ze znalezionymi kartami
    return image
import cv2
import numpy as np
import time
import os
import Cards
import Poker

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
        final_result, combination = Poker.findSystem(cards_info)

        print(combination) # Wykorzystać znalezioną kombinacje kart do zaznaczenia na obrazku wynikowym

        # Wypisanie najlepszej mozliwej kombinacji podanych kart
        cv2.putText(image, final_result, (5, IM_HEIGHT//2 - 305), font, 1.95, (0, 0, 0), 3, cv2.LINE_AA)
        cv2.putText(image, final_result, (5, IM_HEIGHT//2 - 305), font, 1.95, (255, 255, 255), 2, cv2.LINE_AA)

        # Narysowanie konturu na wejściowym obrazku
        if (len(cards) != 0):
            temp_cnts = []
            for i in range(len(cards)):
                temp_cnts.append(cards[i].contour)
            cv2.drawContours(image, temp_cnts, -1, (0, 255, 0), 2)

    # Zwrócenie obrazka ze znalezionymi kartami
    return image
import cv2
import numpy as np
import time
import os
import Cards
import Poker
import copy

# Wymiary obrazu
IM_WIDTH = 1280
IM_HEIGHT = 720

# Czcionka
font = cv2.FONT_HERSHEY_COMPLEX

time.sleep(1)

# Załadowanie porównujących rang i kolorów
path = os.path.dirname(os.path.abspath(__file__))
train_ranks = Cards.load_ranks(path + '/Images/')
train_colors = Cards.load_colors(path + '/Images/')

# Funkcja sprawdzająca czy karta należy do systemu
def isInSystem(rank, color, combination):
    for c in combination:
        if rank == c[0] and color == c[1]:
            return True
    return False

# Funkcja zwracajaca informacje o przerobionym obrazie wejściowym
def drawImage(img):
    size = (IM_WIDTH, IM_HEIGHT)
    example_card = []
    zoom = []
    value = []
    symbol = []
    image = [] 
    grayed = [] 
    blurred = []
    pre_process = [] 

    image = cv2.resize(img, size, interpolation = cv2.INTER_AREA)
    
    # Wstępna obróbka obrazu (wyszarzenie, blurowanie i progowanie)
    image, grayed, blurred, pre_process = Cards.preprocess_image(image)

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
                card, example_card, zoom, value, symbol, valid = Cards.preprocess_card(contours_sort[i], image, blurred)

                if(not valid or example_card == []):
                    img2 = copy.copy(img)
                    cv2.putText(img, "Oryginalny obraz", (5, IM_HEIGHT//2 - 170), font, 6.2, (0, 0, 0), 8, cv2.LINE_AA)
                    cv2.putText(img, "Oryginalny obraz", (5, IM_HEIGHT//2 - 170), font, 6.2, (255, 255, 255), 5, cv2.LINE_AA)
                    cv2.putText(img2, "Nie odczytano poprawnie zdjecia", (5, IM_HEIGHT//2 - 170), font, 6.2, (0, 0, 0), 8, cv2.LINE_AA)
                    cv2.putText(img2, "Nie odczytano poprawnie zdjecia", (5, IM_HEIGHT//2 - 170), font, 6.2, (255, 255, 255), 5, cv2.LINE_AA)
                    return 0, 0, 0, 0, 0, 0, 0, 0, img, img2, False

                cards.append(card)

                # Znalezienie najlepszej rangi i koloru dla nowo znalezionej karty
                cards[k].best_rank_match, cards[k].best_color_match, cards[k].rank_diff, cards[
                    k].color_diff = Cards.match_card(cards[k], train_ranks, train_colors)

                # Wypisanie nazwy karty
                image, rank_name, color_name = Cards.draw_results(image, cards[k])
                cards_info.append([rank_name, color_name])
                k += 1

        # Wykorzystanie algorytmu wyszukującego najlepszy układ w pokerze
        final_result, combination = Poker.findSystem(cards_info)

        # Wypisanie najlepszej mozliwej kombinacji podanych kart
        cv2.putText(image, final_result, (5, IM_HEIGHT//2 - 305), font, 1.75, (0, 0, 0), 3, cv2.LINE_AA)
        cv2.putText(image, final_result, (5, IM_HEIGHT//2 - 305), font, 1.75, (255, 255, 255), 2, cv2.LINE_AA)

        # Narysowanie konturu na wejściowym obrazku (zielony dla kart nalezacych do ukladu, czerwony dla innych)
        if (len(cards) != 0):
            temp_cnts = []
            temp_cnts_red = []
            for i in range(len(cards)):
                if isInSystem(cards[i].best_rank_match, cards[i].best_color_match, combination):
                    temp_cnts.append(cards[i].contour)
                else:
                    temp_cnts_red.append(cards[i].contour)
            cv2.drawContours(image, temp_cnts_red, -1, (0, 0, 139), 2)
            cv2.drawContours(image, temp_cnts, -1, (0, 153, 0), 3)

        # Sprawdzenie, które karty należą do układu i pogrubienie czcionki ich nazw
        for card in cards:
            if isInSystem(card.best_rank_match, card.best_color_match, combination):
                Cards.thickBestSystem(image, card)

    # Zwrócenie obrazka ze znalezionymi kartami i poszczególnych etapów elagorytmu
    else:
        img2 = copy.copy(img)
        cv2.putText(img, "Oryginalny obraz", (5, IM_HEIGHT//2 - 170), font, 5.2, (255, 255, 255), 8, cv2.LINE_AA)
        cv2.putText(img, "Oryginalny obraz", (5, IM_HEIGHT//2 - 170), font, 5.2, (0, 0, 0), 5, cv2.LINE_AA)
        cv2.putText(img2, "Nie znaleziono konturow kart", (5, IM_HEIGHT//2 - 170), font, 5.2, (255, 255, 255), 8, cv2.LINE_AA)
        cv2.putText(img2, "Nie znaleziono konturow kart", (5, IM_HEIGHT//2 - 170), font, 5.2, (0, 0, 0), 5, cv2.LINE_AA)
        return 0, 0, 0, 0, 0, 0, 0, 0, img, img2, False

    if(example_card == [] or
    zoom == [] or
    value == [] or
    symbol == [] or
    image == [] or
    grayed == [] or
    blurred == [] or
    pre_process == [] ):
        img2 = copy.copy(img)
        cv2.putText(img, "Oryginalny obraz", (5, IM_HEIGHT//2 - 170), font, 5.2, (255, 255, 255), 8, cv2.LINE_AA)
        cv2.putText(img, "Oryginalny obraz", (5, IM_HEIGHT//2 - 170), font, 5.2, (0, 0, 0), 5, cv2.LINE_AA)
        cv2.putText(img2, "Nie znaleziono konturow kart", (5, IM_HEIGHT//2 - 170), font, 5.2, (255, 255, 255), 8, cv2.LINE_AA)
        cv2.putText(img2, "Nie znaleziono konturow kart", (5, IM_HEIGHT//2 - 170), font, 5.2, (0, 0, 0), 5, cv2.LINE_AA)
        return 0, 0, 0, 0, 0, 0, 0, 0, img, img2, False
    else:
        cv2.putText(grayed, "Wyszarzenie obrazu", (5, IM_HEIGHT//2 - 305), font, 1.95, (0, 0, 0), 3, cv2.LINE_AA)
        cv2.putText(grayed,"Wyszarzenie obrazu", (5, IM_HEIGHT//2 - 305), font, 1.95, (255, 255, 255), 2, cv2.LINE_AA)
        cv2.putText(blurred, "Rozmazanie obrazu", (5, IM_HEIGHT//2 - 305), font, 1.95, (0, 0, 0), 3, cv2.LINE_AA)
        cv2.putText(blurred,"Rozmazanie obrazu", (5, IM_HEIGHT//2 - 305), font, 1.95, (255, 255, 255), 2, cv2.LINE_AA)
        cv2.putText(pre_process, "Progowanie obrazu", (5, IM_HEIGHT//2 - 305), font, 1.95, (0, 0, 0), 3, cv2.LINE_AA)
        cv2.putText(pre_process,"Progowanie obrazu", (5, IM_HEIGHT//2 - 305), font, 1.95, (255, 255, 255), 2, cv2.LINE_AA)
        cv2.putText(img, "Oryginalny obraz", (5, IM_HEIGHT//2 - 170), font, 6.2, (0, 0, 0), 7, cv2.LINE_AA)
        cv2.putText(img, "Oryginalny obraz", (5, IM_HEIGHT//2 - 170), font, 6.2, (255, 255, 255), 5, cv2.LINE_AA)

        return grayed, blurred, pre_process, image, example_card, zoom, value, symbol, img, img, True
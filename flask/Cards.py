import cv2
import numpy as np
import time

# STAŁE

# Granice dla tła i kart
BACKGROUND_THRESHOLD = 60
CARDS_THRESHOLD = 30

# Szerokość i wysokość wyszukiwanych kart
CARDS_WIDTH = 32
CARDS_HEIGHT = 84

# Wymiary rang kart, które porównujemy
RANKS_WIDTH = 70
RANKS_HEIGHT = 125

# Wymiary kolorów kart, które porównujemy
COLORS_WIDTH = 70
COLORS_HEIGHT = 100

# Maksymalne dopuszczalne różnice pomiędzy rangami i kolorami, dla których może zachodzić algorytm sprawdzający
RANKS_MAX_DIFF = 2000
COLORS_MAX_DIFF = 700

# Maksymalne dopuszczalne pole kart, dla których może zachodzić algorytm sprawdzający
CARDS_MAX_AREA = 120000
CARDS_MIN_AREA = 25000

# Czcionka
font = cv2.FONT_HERSHEY_SIMPLEX


# Klasy przechowujące kolejkę kart do sprawdzenia oraz informacje o przechowywanych kolorach i rangach w folderze Images, które porównujemy

# Klasa przechowująca informacje o kolejce kart do sprawdzenia
class Query_card:

    def __init__(self):
        self.contour = []  # Kontury karty
        self.width, self.height = 0, 0  # Szerokość i wysokość karty
        self.corner_pts = []  # Punkty w narożnikach karty
        self.center = []  # Centroid karty
        self.warp = []  # Współrzędne spłaszczonego, wyszarzonego i zamazanego wejściowego obrazu o wymiarach 200x300
        self.rank_img = []  # Współrzędne wyciętej, przerobionej rangi
        self.color_img = []  # Współrzędne wyciętego, przerobionego koloru
        self.best_rank_match = "Nieznany"  # Najlepiej pasująca ranga
        self.best_color_match = "Nieznany"  # Najlepiej pasujący kolor
        self.rank_diff = 0  # Różnica pomiędzy wyciętą rangą a najlpiej pasującą z folderu Image
        self.color_diff = 0  # Różnica pomiędzy wyciętym kolorem a najlpiej pasującym z folderu Image

# Klasa przechowująca informacje o rangach z folderu Image
class Train_ranks:

    def __init__(self):
        self.img = []  
        self.name = "Placeholder"

# Klasa przechowująca informacje o kolorach z folderu Image
class Train_colors:

    def __init__(self):
        self.img = [] 
        self.name = "Placeholder"


# FUNKCJE

# Załadowanie obrazów rang z folderu Image
def load_ranks(filepath):

    train_ranks = []
    i = 0

    for rank in ['As', 'Dwojka', 'Trojka', 'Czworka', 'Piatka', 'Szostka', 'Siodemka',
                 'Osemka', 'Dziewiatka', 'Dziesiatka', 'Walet', 'Dama', 'Krol']:
        train_ranks.append(Train_ranks())
        train_ranks[i].name = rank
        filename = rank + '.jpg'
        train_ranks[i].img = cv2.imread(filepath + filename, cv2.IMREAD_GRAYSCALE)
        i += 1

    return train_ranks


# Załadowanie obrazów kolorów z folderu Image
def load_colors(filepath):

    train_colors = []
    i = 0

    for color in ['Pik', 'Karo', 'Trefl', 'Kier']:
        train_colors.append(Train_colors())
        train_colors[i].name = color
        filename = color + '.jpg'
        train_colors[i].img = cv2.imread(filepath + filename, cv2.IMREAD_GRAYSCALE)
        i += 1

    return train_colors

# Funkcja zwracająca wyszarzany, zamazany i przetworzony progowo wczytany obraz 
def preprocess_image(image):

    grayed = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(grayed, (5, 5), 0)

    # Zmienny poziom progowania w zależności od światła
    img_w, img_h = np.shape(image)[:2]
    bkg_level = grayed[int(img_h / 100)][int(img_w / 2)]
    thresh_level = bkg_level + BACKGROUND_THRESHOLD

    do_nothing, thresh = cv2.threshold(blurred, thresh_level, 255, cv2.THRESH_BINARY)

    return thresh

# Funkcja znajdująca kontury kart w progowanym obrazie zwracająca posortowaną listę konturów oraz listę identyfikującą, które kontury mogą być kartami 
def find_cards(thresh_image):

    # Znajdź kontury i posortuj je
    contours, hier = cv2.findContours(thresh_image, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    index_sort = sorted(range(len(contours)), key=lambda i: cv2.contourArea(contours[i]), reverse=True)

    # Jeśli nie ma konturów, zwróć 2 puste listy
    if len(contours) == 0:
        return [], []

    contours_sort = []
    hier_sort = []
    cnt_is_card = np.zeros(len(contours), dtype=int)

    for i in index_sort:
        contours_sort.append(contours[i])
        hier_sort.append(hier[0][i])


    # Identyfikacja karty na podstawie:
    # - mniejszego pola niż maksymalnego dopuszczalnego i większego pola niż minimalnego dopuszczalnego
    # - nie ma przodków (nie zawiera się w innym konturze)
    # - ma cztery rogi

    for i in range(len(contours_sort)):
        size = cv2.contourArea(contours_sort[i])
        perimeter = cv2.arcLength(contours_sort[i], True)
        approx = cv2.approxPolyDP(contours_sort[i], 0.01 * perimeter, True)

        if ((size < CARDS_MAX_AREA) and (size > CARDS_MIN_AREA)
                and (hier_sort[i][3] == -1) and (len(approx) == 4)):
            cnt_is_card[i] = 1

    return contours_sort, cnt_is_card

# Uzycie konturow do znalezienia informacji o kartach, oddzielenie rangi i koloru od karty
def preprocess_card(contour, image):

    qCard = Query_card()

    qCard.contour = contour

    # Znalezienie obwodu karty do wykrycia rogów
    perimeter = cv2.arcLength(contour, True)
    approx = cv2.approxPolyDP(contour, 0.01 * perimeter, True)
    points = np.float32(approx)
    qCard.corner_pts = points

    # Znalezienie wysokości i szerokości karty
    x, y, w, h = cv2.boundingRect(contour)
    qCard.width, qCard.height = w, h

    # Znalezienie punktu środkowego karty poprzez znalezienie średniej po współrzędnych punktów w rogach
    average = np.sum(points, axis=0) / len(points)
    qCard.center = [int(average[0][0]), int(average[0][1])]

    # Spłaszczenie oraz zmiana wymiarów karty do 200x300
    qCard.warp = flattener(image, points, w, h)

    # Czterokrotne przybliżenie do rogu karty
    Qcorner = qCard.warp[0:CARDS_HEIGHT, 0:CARDS_WIDTH]
    Qcorner_zoom = cv2.resize(Qcorner, (0, 0), fx=4, fy=4)

    # Znalezienie odpowiedniego poziomu progowania
    white_level = Qcorner_zoom[15, int((CARDS_WIDTH * 4) / 2)]
    thresh_level = white_level - CARDS_THRESHOLD
    if (thresh_level <= 0):
        thresh_level = 1
    retval, query_thresh = cv2.threshold(Qcorner_zoom, thresh_level, 255, cv2.THRESH_BINARY_INV)

    # Podzielenie rogu na 2 części (górna - ranga, dolna - kolor)
    Qrank = query_thresh[20:170, 0:128]
    Qcolor = query_thresh[171:336, 0:128]

    # Znalezienie konturu rangi, prostokątu ograniczającego i największego konturu
    Qrank_cnts, hier = cv2.findContours(Qrank, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    Qrank_cnts = sorted(Qrank_cnts, key=cv2.contourArea, reverse=True)

    # Znalezienie prostokąta ograniczającego dla największego konturu, dopasowanie do wymiarów rang z folderu Image 
    if len(Qrank_cnts) != 0:
        x1, y1, w1, h1 = cv2.boundingRect(Qrank_cnts[0])
        Qrank_roi = Qrank[y1:y1 + h1, x1:x1 + w1]
        Qrank_sized = cv2.resize(Qrank_roi, (RANKS_WIDTH, RANKS_HEIGHT), 0, 0)
        qCard.rank_img = Qrank_sized

    # # Znalezienie konturu koloru, prostokątu ograniczającego i największego konturu
    Qcolor_cnts, hier = cv2.findContours(Qcolor, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    Qcolor_cnts = sorted(Qcolor_cnts, key=cv2.contourArea, reverse=True)

    # Znalezienie prostokąta ograniczającego dla największego konturu, dopasowanie do wymiarów rang z folderu Image 
    if len(Qcolor_cnts) != 0:
        x2, y2, w2, h2 = cv2.boundingRect(Qcolor_cnts[0])
        Qcolor_roi = Qcolor[y2:y2 + h2, x2:x2 + w2]
        Qcolor_sized = cv2.resize(Qcolor_roi, (COLORS_WIDTH, COLORS_HEIGHT), 0, 0)
        qCard.color_img = Qcolor_sized

    return qCard

# Znalezienie najlepszej rangi i koloru dla karty z kolejki.
def match_card(qCard, train_ranks, train_colors):

    best_rank_match_diff = 10000
    best_color_match_diff = 10000
    best_rank_match_name = "Nieznany"
    best_color_match_name = "Nieznany"

    # Jeśli nie ma znalezionych konturów z funkcji preprocess_card, zakończ przetwarzanie
    if (len(qCard.rank_img) != 0) and (len(qCard.color_img) != 0):

        # Znalezienie najmniej różniącej się rangi i koloru z folderu Image od odciętej karty
        for train in train_ranks:

            diff_img = cv2.absdiff(qCard.rank_img, train.img)
            rank_diff = int(np.sum(diff_img) / 255)

            if rank_diff < best_rank_match_diff:
                best_rank_match_diff = rank_diff
                best_rank_name = train.name

        for color in train_colors:

            diff_img = cv2.absdiff(qCard.color_img, color.img)
            color_diff = int(np.sum(diff_img) / 255)

            if color_diff < best_color_match_diff:
                best_color_match_diff = color_diff
                best_color_name = color.name

    # Zidentyfikowanie znalezionej karty. Jeśli pomiędzy rangami i kolorami różnice są nadal zbyt duże, znaleziona karta pozostaje nierozpoznana
    if (best_rank_match_diff < RANKS_MAX_DIFF):
        best_rank_match_name = best_rank_name

    if (best_color_match_diff < COLORS_MAX_DIFF):
        best_color_match_name = best_color_name

    return best_rank_match_name, best_color_match_name, best_rank_match_diff, best_color_match_diff

# Rysowanie nazwy karty, centoidu i konturów
def draw_results(image, qCard):

    x = qCard.center[0]
    y = qCard.center[1]
    # cv2.circle(image, (x, y), 5, (255, 0, 0), -1)

    rank_name = qCard.best_rank_match
    color_name = qCard.best_color_match

    # Wypisanie nazwy dwukrotnie w celu pozostawienia czarnego konturu napisu 
    cv2.putText(image, rank_name, (x - 60, y - 10), font, 1, (0, 0, 0), 4, cv2.LINE_AA)
    cv2.putText(image, rank_name, (x - 60, y - 10), font, 1, (0, 0, 139), 2, cv2.LINE_AA)

    cv2.putText(image, color_name, (x - 60, y + 25), font, 1, (0, 0, 0), 3, cv2.LINE_AA)
    cv2.putText(image, color_name, (x - 60, y + 25), font, 1, (0, 0, 139), 2, cv2.LINE_AA)

    return image, rank_name, color_name

# Funkcja pogrubiajaca czcionke nazw kart należących do układu
def thickBestSystem(image, qCard):
    x = qCard.center[0]
    y = qCard.center[1]

    rank_name = qCard.best_rank_match
    color_name = qCard.best_color_match

    cv2.putText(image, rank_name, (x - 60, y - 10), font, 1, (0, 0, 0), 7, cv2.LINE_AA)
    cv2.putText(image, rank_name, (x - 60, y - 10), font, 1, (255, 255, 255), 4, cv2.LINE_AA)

    cv2.putText(image, color_name, (x - 60, y + 25), font, 1, (0, 0, 0), 7, cv2.LINE_AA)
    cv2.putText(image, color_name, (x - 60, y + 25), font, 1, (255, 255, 255), 4, cv2.LINE_AA)

# Spłaszczenie i wyszarzenie obrazu do wymiarów 200x300 do perspektywy góra-dół - www.pyimagesearch.com/2014/08/25/4-point-opencv-getperspective-transform-example/
def flattener(image, points, w, h):
    rect = np.zeros((4, 2), dtype="float32")

    sum = np.sum(points, axis=2)

    tl = points[np.argmin(sum)]
    br = points[np.argmax(sum)]

    diff = np.diff(points, axis=-1)
    tr = points[np.argmin(diff)]
    bl = points[np.argmax(diff)]
    
    # Stworzenie tablicy [lewy górny, prawy górny, prawy dolny, lewy dolny]

    # Jeśli karta jest położona pionowo
    if w <= 0.8 * h:  
        rect[0] = tl
        rect[1] = tr
        rect[2] = br
        rect[3] = bl

    # Jeśli karta jest położona poziomo
    if w >= 1.2 * h:  
        rect[0] = bl
        rect[1] = tl
        rect[2] = tr
        rect[3] = br

    # Jeśli karta jest ułożona na ukos, następujący algorytm odnajduje jej odpowiednie rogi:

    # Karta jest ułożona na ukos
    if w > 0.8 * h and w < 1.2 * h:  
        # Jeśli najbardziej oddalony lewy punkt jest wyżej niż najbardziej oddalony prawy punkt, karta jest przesunięta w lewo
        if points[1][0][1] <= points[3][0][1]:
            rect[0] = points[1][0]  
            rect[1] = points[0][0]  
            rect[2] = points[3][0]  
            rect[3] = points[2][0]  

        else:
            rect[0] = points[0][0]  
            rect[1] = points[3][0]  
            rect[2] = points[2][0]  
            rect[3] = points[1][0]  

    maxWidth = 200
    maxHeight = 300

    # Wyliczenie macierzy transformacji perspektywy i zwrócenie współrzędnych karty w perspektywie góra-dół
    dest = np.array([[0, 0], [maxWidth - 1, 0], [maxWidth - 1, maxHeight - 1], [0, maxHeight - 1]], np.float32)
    Matrix = cv2.getPerspectiveTransform(rect, dest)
    warp = cv2.warpPerspective(image, Matrix, (maxWidth, maxHeight))
    warp = cv2.cvtColor(warp, cv2.COLOR_BGR2GRAY)

    return warp
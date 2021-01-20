# pythonproject
Użyte biblioteki:

tkinter (latest version) - biblioteka umożliwiająca tworzenie interfejsu graficznego;
cv2 (4.4.0) - biblioteka funkcji wykorzystywanych podczas obróbki obrazu;
numpy (1.19.4) - biblioteka dodająca obsługę dużych, wielowymiarowych tablic i macierzy;
os - systemowa biblioteka dla pracy ze ścieżkami;
PIL (6.2.0)  - rozszerzenie dla Pythona, które dodaje obsługę grafiki;
tensorflow (2.4.0) - biblioteka wykorzystywana w uczeniu maszynowym i głębokich sieciach neuronowych;
skimage (0.16.2) - zbiór algorytmów przetwarzania obrazu;
sklearn (0.20.3) - darmowa biblioteka pythona która zawiera różne algorytmy uczenia maszynowego i metod do przetwarzania, wykorzystaliśmy z niej metodę do obliczania wagi klas.
signs (skrypt lokalny) -  posiada słownik z kluczami jakie odpowiadają konkretnej nazwie znaku drogowego


Pliki:

signs.py - zawiera słownik road_signs dla wypisania rozpoznanego znaku drogowego;
main.py - GUI oraz funkcje wykorzystywane do rozpoznawania znaku;
train.py - ładowanie etykiet, konwersja, wszycztywanie danych testowych oraz treningowych, trenowanie modelu.


Autorzy:

-Kamil Weselski
-Aleksander Kowalski
-Aleksandra Dębska
-Marcin Nowak
-Anton Mekh
-Marcin Górny
-Adam Wojnarowski


Opis działania programu:

Program używa nauczonej sieci neuronowej do rozpoznawania konkretnego znaku drogowego. W okienku startowym wgrywamy obrazek z znakiem drogowym i po przejściu przez sieć neuronową uzyskujemy nazwę tego znaku. 

Aby uruchomić proces trenowania należy wpisać w konsoli folderu komendę:
python train.py --dataset gtsrb-german-traffic-sign --model signnet.model

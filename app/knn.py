import numpy as np


class KNNRecommender:
    def __init__(self, k=5):
        # domyslnie szukamy 5 sasiadow
        self.k = k
        self.dane = None
        self.info = None

    def fit(self, cechy, meta):
        # wrzucamy dane do pamieci
        self.dane = cechy
        self.info = meta

    def policz_dystans(self, wektor1, wektor2):
        # zwykly wzor na odleglosc euklidesowa bez zbednych kombinacji
        roznica = wektor1 - wektor2
        return np.sqrt(np.sum(roznica ** 2))

    def get_recommendations(self, id_ksiazki):
        szukana_ksiazka = self.dane[id_ksiazki]
        odleglosci = []

        # lecimy po wszystkich ksiazkach w bazie
        for i in range(len(self.dane)):
            if i == id_ksiazki:
                continue # pomijamy sama siebie
            
            dystans = self.policz_dystans(szukana_ksiazka, self.dane[i])
            odleglosci.append((i, dystans))

        # sortujemy wyniki od najmniejszego dystansu
        odleglosci.sort(key=lambda x: x[1])
        
        # wybieramy tylko k najlepszych wynikow (zwykla petla zamiast one-linera)
        najlepsze_indeksy = []
        for j in range(self.k):
            najlepsze_indeksy.append(odleglosci[j][0])
        
        # zwracamy wiersze z tabeli z informacjami o ksiazkach
        return self.info.iloc[najlepsze_indeksy].copy()
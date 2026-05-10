import numpy as np

from app.knn import KNNRecommender


def test_inicjalizacji_modelu():
    # Sprawdzamy czy klasa poprawnie zapisuje parametr k
    model = KNNRecommender(k=3)
    assert model.k == 3
    assert model.dane is None
    assert model.info is None

def test_obliczania_odleglosci_euklidesowej():
    # Testujemy naszą matematykę na prostych wektorach z lekcji geometrii
    # Wektor [0, 0] i [3, 4] - z twierdzenia Pitagorasa odległość to 5
    model = KNNRecommender()
    wektor_a = np.array([0, 0])
    wektor_b = np.array([3, 4])
    
    dystans = model.policz_dystans(wektor_a, wektor_b)
    
    # Sprawdzamy, czy algorytm poprawnie policzył
    assert dystans == 5.0

def test_zapisywania_danych():
    # Sprawdzamy czy metoda fit() poprawnie "zapamiętuje" dane
    model = KNNRecommender()
    przykładowe_cechy = np.array([[1, 2], [3, 4]])
    przykładowe_info = ["Ksiazka A", "Ksiazka B"]
    
    model.fit(przykładowe_cechy, przykładowe_info)
    
    assert len(model.dane) == 2
    assert model.info[0] == "Ksiazka A"
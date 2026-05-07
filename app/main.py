import pandas as pd

from app.knn import KNNRecommender

def przygotuj_dane(sciezka):
    # wczytuje dane i olewam zepsute linijki z kaggle
    df = pd.read_csv(sciezka, on_bad_lines="skip")
    
    # te kolumny wezmiemy do liczenia odleglosci
    kolumny = ["average_rating", "  num_pages", "ratings_count"]
    
    # wywalamy puste wartosci zeby nie wywalilo bledu
    df_czyste = df.dropna(subset=kolumny + ["title", "authors"]).copy()
    
    # na wszelki wypadek wymuszam liczby
    for k in kolumny:
        df_czyste[k] = pd.to_numeric(df_czyste[k], errors="coerce")
    
    df_czyste = df_czyste.dropna(subset=kolumny)
    
    # resetujemy indeksy, zeby numery wierszy znowu szly po kolei od 0
    df_czyste = df_czyste.reset_index(drop=True)
    dane_liczbowe = df_czyste[kolumny].values
    
    # NORMALIZACJA
    minimum = dane_liczbowe.min(axis=0)
    maksimum = dane_liczbowe.max(axis=0)
    roznica = maksimum - minimum
    roznica[roznica == 0] = 1 
    
    znormalizowane = (dane_liczbowe - minimum) / roznica
    
    return znormalizowane, df_czyste

def uruchom():
    print("Odpalam system rekomendacji...")
    
    try:
        dane_norm, df_info = przygotuj_dane("data/books.csv")
        
        model = KNNRecommender(k=5)
        model.fit(dane_norm, df_info[["title", "authors", "average_rating"]])
        
        # Pytamy uzytkownika o ksiazke:
        wpisany_tekst = input("\nWpisz tytul ksiazki (lub jego fragment), do ktorej szukasz podobnych: ").lower()
        
        szukane_id = -1
        tytuly = df_info["title"].tolist()
        
        # Proste przeszukiwanie bazy
        for i in range(len(tytuly)):
            # sprawdzamy czy wpisany tekst znajduje sie w tytule z bazy
            if wpisany_tekst in str(tytuly[i]).lower():
                szukane_id = i
                break
                
        # Sprawdzamy, czy znalezlismy jakas ksiazke
        if szukane_id == -1:
            print(f"\nNiestety, nie znalazlem w bazie ksiazki pasujacej do: '{wpisany_tekst}'")
            print('Sprobuj odpalic program ponownie i wpisac cos innego (np. "hobbit" albo "twilight").')
        else:
            tytul_znaleziony = df_info.iloc[szukane_id]["title"]
            autor_znaleziony = df_info.iloc[szukane_id]["authors"]
            
            print(f"\nZnaleziono w bazie: '{tytul_znaleziony}' (Autor: {autor_znaleziony})")
            print("Szukam podobnych...")
            
            wyniki = model.get_recommendations(szukane_id)
            
            print("\nWyniki:")
            print("--------------------------------------------------")
            print(wyniki.to_string(index=False))
            print("--------------------------------------------------")
        
    except Exception as e:
        print("Cos poszlo nie tak. Sprawdz czy plik books.csv na pewno jest w folderze data!")
        print("Opis bledu:", e)

if __name__ == "__main__":
    uruchom()
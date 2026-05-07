# System Rekomendacji Książek (k-NN)

Projekt zrealizowany w ramach zaliczenia przedmiotu Sztuczna Inteligencja.
Aplikacja jest interaktywnym systemem rekomendacji opartym na algorytmie k-Najbliższych Sąsiadów (k-NN), zaimplementowanym samodzielnie od zera.

## Wymagania

- Python 3.12+
- Menedżer pakietów `uv`

## Instalacja

1. Sklonuj repozytorium na swój komputer.
1. Pobierz zbiór danych *Goodreads-books* z serwisu Kaggle: [Link do datasetu](https://www.kaggle.com/datasets/jealousleopard/goodreadsbooks)
1. Wypakowany plik CSV nazwij `books.csv` i umieść go w nowo utworzonym folderze `data/` w głównym katalogu projektu.
1. Zainstaluj wymagane zależności komendą:

```bash
uv sync

## Uruchomienie aplikacji

Aby uruchomić interaktywną wyszukiwarkę książek, wpisz w terminalu:

'''bash
uv run python -m app.main

Program poprosi o wpisanie tytułu książki (w języku angielskim, np. hobbit, potter, silence), a następnie wyświetli 5 najbardziej podobnych do niej pozycji na podstawie cech fizycznych i ocen.

## Uruchomienie testów

Aby zweryfikować poprawność działania rdzenia matematycznego algorytmu, uruchom testy jednostkowe:

'''bash
uv run pytest

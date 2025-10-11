# Coffee Machine (Day 16)

Prosty symulator automatu do kawy napisany w Pythonie jako część kursu Udemy "100 Days of Code" — dzień 16.

Opis:
- Program symuluje maszynę do przygotowywania kawy z trzema rodzajami napojów: `latte`, `espresso` i `cappuccino`.
- Obsługuje sprawdzenie zasobów (woda, mleko, kawa), płatność monetami oraz wydawanie reszty.

Pliki:
- `main.py` — główny skrypt uruchamiający interakcję z użytkownikiem (wybór napoju, raport, wyłączenie).
- `coffee_maker.py` — klasa `CoffeeMaker` zarządzająca zasobami i przygotowaniem napojów.
- `menu.py` — klasy `Menu` i `MenuItem` definiujące dostępne napoje i ich składniki.
- `money_machine.py` — klasa `MoneyMachine` obsługująca przyjmowanie monet i płatności.

Jak uruchomić:
1. Upewnij się, że masz zainstalowanego Pythona 3.7+.
2. Otwórz terminal w folderze `day_16`.
3. Uruchom:

```bash
python main.py
```

Użytkowanie:
- Wpisz nazwę napoju (`latte`, `espresso`, `cappuccino`) aby go zamówić.
- Wpisz `report` aby zobaczyć aktualne zasoby i stan pieniędzy.
- Wpisz `off` aby wyłączyć maszynę.

Uwagi:
- Projekt jest prosty i służy nauce OOP w Pythonie. Możesz rozszerzyć projekt dodając zapis stanu do pliku, obsługę większej liczby monet, lub interfejs graficzny.

Autor: kod z kursu Udemy (dostosowany lokalnie)

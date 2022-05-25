PL

Projekt REST API dla książek

Opcje:

- api_spec/ - wyświetla statyczną informacje o wersji api
- books/ - lista książek z pobranych z bazy danych, dostępna jest opcja filtrowania (trzeba wpisywać dokładne nazwy), możliwość dodawania książek do bazy
- books/<int:pk>/ - podląd widoku konkretnej książki, dostępna jest opcja modyfikowania lub usunięcia danej pozycji
- search/ - alternatywne filtrowanie listy książek - wyszukuje tylko autrów, nie trzeba podawać dokładnych danych autora
- import/ - importuje dane o książkach do bazy danych z podanego w prostym formularzu linku url 

Technologie użyte w pojekcie: Python, Dajngo, REST Framework, HTML oraz baza SQLite (nie dołączona do rezpozytorium)

wkrótce: dodanie do api testów, poprawa fitru zabezpieczającego przed dodaniem duplikatów książek do bazy.


ENG
...

# Løsningsbeskrivelse – Login med Flask

## Hva er dette?
En enkel nettside med login. Laget med Flask, HTML, CSS og SQLite.
Du kan logge inn, lage ny bruker og se alle brukerne.

## Filer
- `app.py` – hovedprogrammet, har alle sidene og kobler nettsiden med databasen
- `db.py` – lager databasen og tabellen `login`
- `database.db` – databasen med brukerne
- `templates/index.html` – startside med loginskjema
- `templates/student.html` – skjema for ny bruker
- `templates/list.html` – tabell med alle brukerne
- `templates/result.html` – viser melding av resultatet
- `static/css/index.css` – skrift og stil

## Hvordan det virker
1. **Login:** Du skriver brukernavn og passord. `app.py` leter etter brukeren i databasen. Finner den brukeren, vises «Welcome». Ellers vises «Wrong username or password».
2. **Ny bruker:** Du fyller ut skjemaet. `app.py` legger brukeren til i databasen.
3. **Liste:** `app.py` leser alle brukerne og viser dem i en tabell.

## Kjøre programmet
1. `pip install flask`
2. `flask run`
3. Åpne `http://127.0.0.1:5000/`
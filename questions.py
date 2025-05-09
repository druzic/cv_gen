form_steps = [
    {
        "key": "ime_prezime",
        "label": "Unesi svoje ime i prezime",
        "type": "text"
    },
    {
        "key": "email",
        "label": "Unesi svoj email",
        "type": "text"
    },
    {
        "key": "telefon",
        "label": "Unesi svoj broj telefona",
        "type": "text"
    },
    {
        "key": "obrazovanje",
        "label": "Unesi obrazovanje (možeš dodati više zapisa)",
        "type": "list",
        "fields": [
            {"name": "institucija", "label": "Naziv obrazovne institucije", "type": "text"},
            {"name": "titula", "label": "Stečena titula", "type": "text"},
            {"name": "pocetak", "label": "Datum početka", "type": "text"},
            {"name": "kraj", "label": "Datum završetka", "type": "text"},
            {"name": "opis", "label": "Kratki opis", "type": "textarea"},
        ]
    },
    {
        "key": "iskustvo",
        "label": "Unesi radno iskustvo (možeš dodati više zapisa)",
        "type": "list",
        "fields": [
            {"name": "pozicija", "label": "Naziv pozicije", "type": "text"},
            {"name": "tvrtka", "label": "Naziv tvrtke", "type": "text"},
            {"name": "pocetak", "label": "Datum početka", "type": "text"},
            {"name": "kraj", "label": "Datum završetka", "type": "text"},
            {"name": "opis", "label": "Opis posla", "type": "textarea"},
        ]
    },
    {
        "key": "projekti",
        "label": "Unesi projekte (možeš dodati više zapisa)",
        "type": "list",
        "fields": [
            {"name": "naziv", "label": "Naziv projekta", "type": "text"},
            {"name": "opis", "label": "Kratki opis", "type": "textarea"},
            {"name": "link", "label": "Link na projekt (ako postoji)", "type": "text"},
        ]
    },
    {
        "key": "vjestine",
        "label": "Koje vještine i alate poznaješ?",
        "type": "textarea"
    },
    {
        "key": "jezici",
        "label": "Koje jezike govoriš?",
        "type": "text"
    },
    {
        "key": "interesi",
        "label": "Napiši nešto o svojim interesima i hobijima",
        "type": "textarea"
    }
]

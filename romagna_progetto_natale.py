class Libro:
    def __init__(self, titolo, autore, anno):
        self.titolo = titolo
        self.autore = autore
        self.anno = anno

    def __str__(self):
        return f"'{self.titolo}' di {self.autore} ({self.anno})"

class Libreria:
    def __init__(self):
        self.libri = []

    def aggiungi_libro(self, libro):
        self.libri.append(libro)
        print(f"libro aggiunto: {libro}")

    def rimuovi_libro(self, titolo):
        libro_da_eliminare = None
        for libro in self.libri:
            if libro.titolo == titolo:
                libro_da_eliminare = libro
                break 
        if libro_da_eliminare:
            self.libri.remove(libro_da_eliminare)
            print(f"libro rimosso: {libro_da_eliminare}")
        else:
            print(f"libro non trovato '{titolo}'")

    def lista_libri(self):
        if self.libri:
            print("libri nella libreria:")
            for libro in self.libri:
                print(libro)
        else:
            print("libreria vuota")

    def trova_libro_autore(self, autore):
        libri_trovati = []
        for libro in self.libri:
            if libro.autore == autore:
                libri_trovati.append(libro)
        if libri_trovati:
            print(f"libri di {autore}:")
            for libro in libri_trovati:
                print(libro)
        else:
            print(f"nessun libro di {autore}")

def main():
    libreria = Libreria()

    scelta = 1
    while scelta !=5 :
        print("\n menu libreria:")
        print("1. aggiungi libro")
        print("2. rimuovi libro")
        print("3. lista di tutti i libri")
        print("4. trova i libri dell'autore")
        print("5. uscire")

        scelta = input("chegli un'opzione (1-5): ")

        if scelta == '1':
            titolo = input("inserisci libro titolo: ")
            autore = input("inserisci libro autore: ")
            anno = input("inserisci anno di pubblicazione: ")
            libro = Libro(titolo, autore, anno)
            libreria.aggiungi_libro(libro)
        elif scelta == '2':
            titolo = input("inserisci titolo del libro da rimuovere: ")
            libreria.rimuovi_libro(titolo)
        elif scelta == '3':
            libreria.lista_libri()
        elif scelta == '4':
            autore = input("inserisi nome autore: ")
            libreria.trova_libro_autore(autore)
        elif scelta == '5': 
            print("Esco")
            break
        else:
            print("codice non valido. inserisci un numero tra 1 e 5")

if __name__ == "__main__":
    main()

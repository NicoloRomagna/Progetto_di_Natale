```mermaid
classDiagram
    class Libro{
        -titolo: str
        -autore: str
        -anno: int
    }

    class Libreria{

    }
 
Libro"1" --> "1*"Libreria : contenuto
Libreria"1" --> "0..*"Libro : contiene  
# Knapsack-Problem-Checker

### Team
* Militaru Ionut - Marius
* Popa Filip Andrei
* Visanescu Bogdan
## Descriere generală
Acest proiect implementează 3 algoritmi pentru rezolvarea problemei rucsacului (Knapsack):
1. **Bruteforce** – verifică toate combinațiile posibile (complexitate mare).
2. **Greedy** – sortează obiectele după un anumit criteriu (ex: raport valoare/greutate) și ia cât încape.
3. **Dinamic** – folosește programare dinamică pentru a construi soluția optimă pe subprobleme.

## Implementarea algoritmilor
- **Bruteforce**: Rulare recursivă care testează toate subseturile de obiecte. Returnează valoarea maximă obținută.
- **Greedy**: Sortează obiectele descrescător după raportul valoare/greutate și le alege în ordinea respectivă până se umple rucsacul.
- **Dinamic**: Folosește un vector unidimensional `dp` de mărime `W + 1`. Pentru fiecare obiect, se parcurge vectorul descrescător, actualizând valoarea maximă la greutatea `w` cu formula:

## Generarea testelor (generate_tests.py)
- Generează automat mai multe fișiere de intrare `.in` cu diferite seturi de date (dimensiune rucsac, număr de obiecte, greutăți și valori).
- Primele teste sunt simple (fără diferențe mari între variante), iar ultimele teste sunt mai lungi

## main_py și Checker
- În fișierul `main_py` se apelează **checker-ul** care rulează toate testele, colectează timpii de execuție și rezultatele obținute de bruteforce, greedy și dinamic.
- Rezultatele (valori și timpi) se salvează în fișiere JSON (ex: `times.json`, `values.json`, `ratios.json`), pentru a fi folosite ulterior în grafice.

## Log file și Out
- **Log file**: este un fișier text în care se salvează testele la care s-a obținut WA (Wrong Answer).
- **Out**: fișierele `.out` conțin rezultatele fiecărui algoritm pentru un test (valoare maximă găsită).

## Plotarea graficelor (plot_values.py, plot_differences.py)
- Pentru a compara rezultate, se afișează:
  - **Un grafic** cu valorile obținute de Dinamic vs. Greedy pentru fiecare test.
  - **Un al doilea grafic** cu raportul dintre cele două rezultate, ilustrand cat de aproape este greedy de valaorea exacta
- Se folosesc datele din JSON-uri și se generează imagini (PNG) în folderul `plots`.

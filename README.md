# parking_app

Simularea unei intrări în parcare pe baza numărului de înmatriculare. 

Membrii echipei: Bobernac Lucia, Berkes Edina, Gyenes Emőke-Anita

Tehnologii folosite: Arduino, Python

Componente hardware: Arduino Uno, senzor de distanta, motor cu bariera, camera CCTV

Componente software:
-Modul detectare numar inmatriculare (localization.py, cca2.py, segmentation.py, machine_train.py, prediction.py): prelucrarea imaginii si extragerea numarului de inmatriculare sub forma unui sir de caractere)
-Modul Arduino(license_plate.ino): conectarea senzorului de distanta si a barierei la placuta Arduino
-Modul bridge(serial.py, snap.sh): componenta de legatura intre sistem si placuta Arduino, conexiunea este realizata prin port serial
-Modul baza de date(db_management): conectarea la baza de date si cautarea numarului de inmatriculare corespunzator (daca exista)

Activitatea din zona parcarii este monitorizata de camera CCTV. Senzorul de distanta transmite date continuu catre Arduino Uno.
In momentul detectarii unui obiect in apropiere, se transmite un trigger prin portul serial catre modulul bridge.
La primirea semnalului, modulul bridge realizeaza un snapshot din inregistrarea camerei.
Imaginea este prelucrata in modulul detectarii numarului de inmatriculare.
In cazul in care a fost extras un numar de inmatriculare, acesta este cautat in baza de date.
Modulul bazei de date returneaza o valoare booleana in modulul bridge.
Daca valoarea este pozitiva, se transmite prin serial un trigger inapoi catre placuta Arduino, care declanseaza ridicarea barierei.


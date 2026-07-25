# 05 — La lettura ancorata

*Voce di diario. I dati vengono da un uso della pipeline precedente a questo progetto,
riportati in forma generica.*

---

## Un'ottimizzazione che sembrava ovvia

Il prompt che manda una funzione a rileggere una formula deve dirle **dove guardare**:
quale pagina, quale equazione, quale riga. Fin qui è necessario.

A un certo punto ci si è messo dentro anche **cosa aspettarsi**. Non per distrazione: per
efficienza. Incollare nel prompt la stringa presa dalla nota sembrava un miglioramento
netto — chi rilegge sa esattamente cosa confrontare, non perde tempo, il verdetto è
mirato, si spendono meno token.

Il ragionamento è corretto. La conclusione è sbagliata, e per un motivo che si vede solo
dopo averlo pagato.

## L'episodio

Il caso è emerso su una coppia di termini tecnici quasi sinonimi — due espressioni che si
somigliano al punto che, lette di fretta, si scambiano senza accorgersene. La nota ne
riportava una. Nel prompt del **ri-trascrittore — il gate di livello base** — era stata
incollata **quella della nota**.

Il ri-trascrittore l'ha confermata, restituendola come verbatim del testo stampato.

Sulla stampa c'era l'altra.

Non aveva letto male la pagina: **non aveva davvero avuto bisogno di leggerla**. Gli era
stata data la risposta insieme alla domanda, e ha fatto la cosa che chiunque farebbe —
ha verificato che la risposta fosse coerente con sé stessa.

Lo stesso meccanismo è ricomparso altrove, su un errore di sigla: la nota riportava uno
scenario sperimentale al posto di un altro, e il verificatore di livello pieno — quello
che guarda l'immagine ad alta risoluzione, il presidio più forte della pipeline — **ha
confermato la nota**. A prendere l'errore sono stati il layer-testo e l'aritmetica interna
della fonte. Il canale più costoso, neutralizzato dal modo in cui gli era stata posta la
domanda.

## Perché è un difetto strutturale e non una svista

L'indipendenza della verifica era già un principio del progetto: chi giudica la formula
**non vede la prima lettura e non ha interessi in essa**. È scritto, ed è il cuore
dell'[ADR-0001](../architecture/decisions/0001-formula-verification-from-image.it.md).

Ed era già applicato — in un punto. Chi arbitra rifà l'analisi dimensionale **a mano,
prima di aprire il verdetto** di chi ha verificato, esplicitamente per non farsene
condizionare. La parola *anti-ancoraggio* compariva già nelle istruzioni operative.

Il buco stava altrove, e questa è la parte che rende l'episodio istruttivo. La regola
proteggeva l'arbitro dal verdetto del verificatore. **Nessuno proteggeva il verificatore
dalla nota.** L'indipendenza era stata garantita all'ultimo anello e data per scontata al
penultimo — dove si può annullare con una singola riga di prompt.

E si è annullata **senza lasciare traccia**. Una lettura ancorata non produce un errore
visibile: produce una **conferma**. Nel registro è indistinguibile da un controllo riuscito.
La pipeline continua a mostrare gate verdi mentre uno dei suoi canali ha, di fatto, smesso
di essere un canale.

## La regola che ne è nata

La formulazione è semplice, e più difficile da rispettare di quanto sembri:

> **Il bersaglio si indica per posizione e grandezza. Mai per valore.**

*«L'equazione 12 a pagina 7, il coefficiente al primo membro»* — legittimo. *«L'equazione 12
dovrebbe riportare X»* — vietato, in qualunque forma, anche parafrasata, anche come
"contesto utile".

Se c'è un sospetto da comunicare, si comunica **il punto conteso**, non la conclusione
attesa: *«su questo rigo c'è un dubbio, rileggilo»*, non *«su questo rigo dovrebbe esserci
questo»*. E chi ha riletto elenca poi le **differenze**, a trascrizione ormai chiusa — ma
a giudicarle è **un terzo attore**, mai chi ha riletto.

## Una nota di onestà

Nel materiale d'origine questo emendamento **è stato fatto** — su un prompt solo, e il
giorno stesso in cui l'episodio è stato messo a verbale.

Il divieto di incollare la stringa attesa è entrato nel prompt canonico del
ri-trascrittore, il gate di livello base, con la motivazione scritta accanto alla regola.
È rimasto in vigore: le sessioni successive lo citano nei rapporti come procedura corrente.

Sul verificatore di livello pieno — quello che guarda l'immagine ad alta risoluzione — non
è stato scritto. Il suo prompt continua a ricevere «le equazioni e i valori dichiarati per
questa nota», più una riga libera per i sospetti: due porte da cui la risposta attesa
rientra.

Due giorni dopo è rientrata. L'errore di sigla raccontato qui sopra è **successivo** alla
correzione dell'altro prompt: la regola c'era già, e non ha protetto nulla, perché era
scritta sull'anello sbagliato.

Vale la pena dirlo invece di nasconderlo. Una regola applicata a un solo anello di una
catena non è una regola applicata: è una convinzione di essere protetti. Qui la decisione
si prende per intero — è l'[ADR-0006](../architecture/decisions/0006-reader-must-not-know-the-expected-answer.it.md).

## Il principio, fuori da questo progetto

Vale per qualunque catena in cui un componente ne controlla un altro, con o senza modelli
di linguaggio in mezzo.

**Un verificatore che sa cosa dovrebbe trovare non è un verificatore.** È un secondo
lettore della stessa risposta — con il costo di un controllo indipendente e il valore di
nessuno.

E l'errore è tanto più facile da commettere quanto più il sistema è curato: nasce dal
desiderio ragionevole di essere precisi, di non far perdere tempo, di dare contesto. Il
contesto che si dà a chi verifica è **esattamente ciò che smette di essere verificato**.

---

**Decisione nata da qui:** [ADR-0006 — Chi rilegge la fonte non deve conoscere la risposta attesa](../architecture/decisions/0006-reader-must-not-know-the-expected-answer.it.md)

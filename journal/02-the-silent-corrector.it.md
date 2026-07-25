# 02 — Il correttore silenzioso

*Voce di diario. I dati vengono da un uso della pipeline precedente a questo progetto,
riportati in forma generica.*

---

## Un difetto che non sembra un difetto

La voce [01](01-the-typo-that-was-not-there.it.md) racconta la pipeline che accusa la
fonte di errori inesistenti. Questa racconta il difetto opposto — e peggiore.

Qui la pipeline **non accusa nessuno**. Legge una formula stampata con un errore, capisce
che c'è un errore, **lo corregge** e scrive nella nota la forma giusta. Senza dirlo.

Il risultato è una nota **corretta**. Ed è precisamente questo il problema.

## Perché è il caso peggiore

Una nota sbagliata, prima o poi, stona. Un'unità che non torna, un ordine di grandezza
fuori posto, un simbolo che non c'entra: qualcosa attira l'occhio, e si va a controllare.

Una nota **silenziosamente corretta** non stona mai. È matematicamente ineccepibile,
dimensionalmente coerente, plausibile in ogni suo punto. Nessuna rilettura del testo la
smaschera, perché **non c'è niente di sbagliato da vedere**. L'unico modo per accorgersene
è confrontarla con **ciò che la fonte stampa davvero** — e quel confronto o lo fai per
protocollo, o non lo fai mai.

Il danno non è nella nota. È nel fatto che la nota **non è più la fonte**. Chi la userà
crederà di star citando l'articolo, e starà citando l'interpretazione che qualcuno ne ha
dato per conto suo, in un passaggio di cui non resta traccia.

## Il conto

Su un **singolo articolo**, il gate ha intercettato **tre** correzioni silenziose. Tre
punti in cui la nota riportava la forma *corretta* al posto di quella *stampata*, senza
una riga che lo segnalasse: due equazioni **normalizzate in silenzio** — la forma stampata
sostituita da quella "pulita" — e una percentuale riscritta nella lettura sensata, perché
quella stampata non tornava con le figure dello stesso articolo.

Su un altro articolo, due errori di trascrizione presi al gate — con un dettaglio che
merita: nessuno dei due è stato preso dalla lettura dell'immagine. Li ha presi il
**layer-testo insieme all'aritmetica interna della fonte**. E su uno dei due il verificatore
di livello pieno aveva **confermato la nota**, perché guardava la nota mentre giudicava.
*(Quella storia è la voce [05](05-the-anchored-reading.it.md).)*

## La distinzione che ha risolto il problema

La formulazione che ha sbloccato tutto è una sola riga, e sta nella scheda di chi estrae:

> **Fedeltà ≠ correttezza.**

La trascrizione verbatim garantisce che la nota è **fedele alla stampa**. Non garantisce
che la formula stampata sia **giusta**. Sono due proprietà diverse, e una pipeline che le
confonde le perde entrambe.

Da qui la regola. Quando chi estrae si accorge che la fonte sbaglia, **non ha il permesso
di correggere**. Ha l'obbligo di fare tre cose insieme:

1. **trascrivere verbatim ciò che è stampato** — la nota resta fedele;
2. **dichiarare il sospetto**, con accanto la forma coerente attesa;
3. **marcarne la natura**: la riga d'uso dice esplicitamente *questa contraddice la fonte,
   ed ecco perché*.

Così la correzione non sparisce: **diventa visibile, tracciabile e discutibile**. Chi
legge la nota vede sia cosa dice l'articolo, sia cosa se ne è concluso, sia chi ha concluso
cosa.

## Il principio generale

C'è una lezione che vale ben oltre le formule, ed è il motivo per cui questa voce esiste.

Un gate che chiede **«è giusto?»** non può prendere il correttore silenzioso: la risposta,
in quel caso, è onestamente *sì*. L'unico gate che lo prende è quello che chiede
**«da dove viene?»** — cioè che tratta il verdetto come una questione di **provenienza**,
non di verità.

La domanda utile non è *questa formula è corretta*. È: **questa riga è ciò che la fonte
stampa, o è ciò che qualcuno ha pensato che la fonte volesse dire?**

---

**Decisione nata da qui:** [ADR-0002 — Il verdetto obbligatorio è esso stesso una sorgente di errore](../architecture/decisions/0002-verdict-as-source-of-error.it.md)

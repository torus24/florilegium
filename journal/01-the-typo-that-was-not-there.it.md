# 01 — Il refuso che non c'era

*Voce di diario. Racconta un episodio reale e cosa ne è cambiato nel metodo. I dati vengono
da un uso della pipeline precedente a questo progetto, riportati in forma generica.*

---

## Il sospetto sbagliato

La domanda con cui è nato tutto era: **la pipeline sta trascrivendo bene le formule?**

Era la domanda sbagliata. Non perché fosse inutile, ma perché dava per scontato il verso
dell'errore. Cercavamo formule trascritte male. Quello che stava succedendo era un'altra
cosa, e più insidiosa: la pipeline trascriveva la formula in un modo, **non trovava
corrispondenza con la fonte, e concludeva che a sbagliare fosse la fonte.**

Nelle note prodotte questo lasciava una traccia inconfondibile: una riga marcata
**«refuso di fonte»**, con tanto di prescrizione operativa allegata — *l'articolo stampa
così, ma è sbagliato: usa quest'altra forma*. Una nota del genere non è un errore passivo.
È un errore **che dà istruzioni**.

## Quattro su cinque

Quando siamo andati a ricontrollare quelle righe una per una, rendendo la pagina come
**immagine** e rileggendo il rigo contestato ad alta risoluzione, il risultato è stato
questo: su **cinque** accuse alla fonte, **quattro erano false**. La fonte stampava
esattamente ciò che doveva stampare. A sbagliare la lettura era stata la pipeline — e poi
ci aveva costruito sopra una regola d'uso.

Il caso più netto non era nemmeno una lettura imprecisa: era un'accusa **fabbricata**. La
verifica contestava a un'equazione un errore che coinvolgeva **simboli mai stampati in
quella formula**. Non aveva letto male: aveva prodotto un verdetto perché gliene era stato
chiesto uno. *(Da lì nasce l'[ADR-0002](../architecture/decisions/0002-verdict-as-source-of-error.it.md).)*

## Il quarto caso — quello che ha deciso tutto

I primi tre li avevamo trovati perché **qualcuno aveva un dubbio**. Un'equazione sembrava
strana, si andava a controllare, saltava fuori la falsa accusa. Un processo che funziona,
ma che dipende interamente dal fatto che il dubbio arrivi.

Il quarto è arrivato in un altro modo. Si stava lavorando su una nota per una questione
del tutto diversa — sbloccare un elemento rimasto in sospeso — e nel farlo si è passati
sopra un'equazione **che nessuno aveva messo in discussione**. Nessun sospetto, nessuna
segnalazione, nessuna anomalia apparente. Sotto resa ad alta risoluzione, il glifo stampato
dalla fonte era diverso da quello trascritto nella nota, e su quella differenza inesistente
la nota aveva fondato l'ennesima riga «refuso di fonte».

Il conto di quella nota, alla fine: portava **quattro** righe «refuso di fonte», e i
refusi **reali** erano **due**. Sono due conti diversi e **non si sommano**: le cinque
accuse ricontrollate una per una stanno su tre articoli diversi — due dei quali ne portavano
più di una — mentre queste quattro stanno tutte sulla stessa nota, e i due conti si
sovrappongono. Vanno letti come due sguardi sullo stesso materiale, non come due conteggi
indipendenti.

Questo è il punto che ha cambiato il metodo, ed è più importante del numero. Se il quarto
caso è emerso **per caso**, mentre si guardava altro, allora la domanda non è più *quanti
ne abbiamo trovati*. È: **quanti ne restano dove nessuno guarderà mai?**

Il dato dice che il dubbio non arriva.

## Cosa è cambiato

La regola precedente era ragionevole e sbagliata: *la resa ad alta risoluzione si fa quando
c'è un dubbio.* Costava poco proprio perché scattava di rado — ma scattava di rado per la
ragione peggiore, cioè che l'errore silenzioso, per definizione, non genera dubbi.

La regola nuova è ottusa e funziona: **ogni riga che accusa la fonte richiede la resa
dell'immagine a ≥400 dpi del rigo contestato, prima di essere firmata.** A qualunque
livello di gate. Senza eccezioni, senza sospetto, senza discrezionalità.

Non è una micro-ottimizzazione: è l'inversione dell'onere della prova. Prima la pipeline
poteva accusare la fonte **e** farla franca. Adesso, per accusare la fonte, deve
**dimostrarlo con un canale diverso da quello che ha generato l'accusa.**

## Perché è la voce fondativa

Tutto il resto del progetto discende da qui.

- Che il verdetto non basti, e vada pesato invece che creduto → [ADR-0002](../architecture/decisions/0002-verdict-as-source-of-error.it.md).
- Che la verifica debba essere di **terza parte** — chi giudica non è chi ha estratto →
  [ADR-0001](../architecture/decisions/0001-formula-verification-from-image.it.md).
- Che una catena di funzioni separate valga più di un solo prompt bravo →
  [ADR-0004](../architecture/decisions/0004-chain-vs-single-prompt.it.md).
- Che il costo in più sia **intrinseco alla qualità**, non uno spreco da ottimizzare →
  [ADR-0005](../architecture/decisions/0005-cost-is-intrinsic-to-quality.it.md).

E soprattutto: una knowledge base che sbaglia **in silenzio** è peggio di una che non
esiste. Chi non ha la base, va a leggere l'articolo. Chi ha la base sbagliata, si fida.

---

**Decisione nata da qui:** [ADR-0001 — L'OCR-testo non è affidabile per le formule](../architecture/decisions/0001-formula-verification-from-image.it.md)

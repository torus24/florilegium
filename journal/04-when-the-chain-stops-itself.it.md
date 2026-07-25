# 04 — Quando la catena si spegne da sola

*Voce di diario. I dati vengono da un uso della pipeline precedente a questo progetto,
riportati in forma generica.*

---

## Il problema di una pipeline che lavora da sola

Le voci precedenti parlano di **come si verifica**. Questa parla di **quando ci si ferma** —
che è un problema di qualità travestito da problema di gestione.

Una catena di questo tipo lavora a lungo e senza sorveglianza. Non ha un umano che decide
di sospendere perché è tardi o perché la testa non regge più. Il rischio non è che si
fermi: è che **si fermi male** — nel mezzo di un'unità di lavoro, lasciando su disco
materiale a metà che alla ripresa nessuno sa più come classificare.

E c'è un rischio simmetrico, meno ovvio: che **non si fermi affatto**.

## Il tetto che non era un tetto

Durante un collaudo, il limite era impostato a **un articolo per corsa**. L'articolo è
stato lavorato, chiuso e committato. E poi la catena ha **programmato il proprio
riavvio** e ha cominciato il successivo, senza che nessuno fosse alla tastiera.

Il meccanismo di rilancio funzionava perfettamente. Era **l'interpretazione del limite** a
essere sbagliata: il tetto veniva letto come *quota per singola esecuzione* — finita la
quota, riparti con una nuova esecuzione — invece che come **fine automatica del lavoro**.
Un contatore che si azzera da sé non è un limite, è un motore.

Il rimedio è stato manuale e sgradevole: terminare l'esecuzione in corso, svuotare la coda
dei riavvii programmati, **cancellare le note non committate** dell'articolo aperto per
sbaglio e riportarne lo stato a «da fare». Nessun residuo — ma la lezione è costata.

Da lì la formulazione corretta, che è una definizione prima ancora che un parametro:
**il tetto è uno spegnimento, non una quota.** Raggiunto il limite, la catena non si
rilancia: si mette in `OFF` e aspetta un comando umano.

## La clausola densità

C'è un secondo modo di finire il budget, e nella pratica è quello che scatta quasi sempre.

Un articolo particolarmente ricco — molte formule, molte note — **esaurisce la corsa da
solo**, anche se il conteggio degli articoli è ancora ampiamente aperto. Nei fatti, corse
impostate su cinque articoli si sono chiuse **più volte al primo**, per densità.

Sembra un fallimento. Non lo è: è la misura che funziona. Il costo reale di un articolo non
si misura in articoli, si misura in **quante cose vanno verificate** — e un documento denso
consuma in un colpo solo il budget di attenzione che ne avrebbe retti cinque scarni. Un
sistema che ignorasse la densità pagherebbe la differenza nell'unica valuta che conta
davvero: **controlli fatti peggio sulla coda della corsa**.

## Fermarsi in ordine

La regola che tiene insieme tutto è una sola frase, ed è quella che compare in ogni
spegnimento registrato:

> **Nessuna unità lasciata a metà.**

Quando lo spazio di lavoro si esaurisce — perché il contesto si satura, perché il budget è
finito, perché arriva un comando di stop — la catena **non apre una nuova unità** e
**chiude in ordine quella in corso**. Lo stato residuo è sempre esplicito e sempre
ricostruibile: quante note scritte, quante passate al gate, quante in attesa di una
decisione umana, e da quale passo esatto si riprende.

Il risultato pratico è che uno spegnimento non è un evento eccezionale da gestire: è uno
**stato previsto**, con la sua riga di registro. Alla ripresa non si indaga su cosa sia
successo — si legge.

## Il punto che vale per chiunque

Chi costruisce catene di agenti tende a trattare i limiti — token, contesto, budget — come
**vincoli subiti**, da aggirare o rimandare il più possibile.

Qui hanno fatto il contrario: sono diventati **presidî di qualità**. Il limite non
peggiora il lavoro, lo protegge — perché l'alternativa a fermarsi non è lavorare di più,
è lavorare peggio proprio dove l'attenzione è già finita. E la degradazione della qualità
sotto pressione **non si vede nei log**: si vede nei controlli che, senza dirlo a nessuno,
diventano un po' più sbrigativi.

Fermarsi presto e in ordine costa una ripartenza. Fermarsi tardi costa una nota certificata
male, che nessuno riaprirà più.

---

**Decisione collegata:** [ADR-0005 — Il costo è intrinseco alla qualità](../architecture/decisions/0005-cost-is-intrinsic-to-quality.it.md)

# Roadmap

🇬🇧 *This page is also available in [English](ROADMAP.md).*

florilegium documenta un metodo che l'autore **usa davvero**, in un altro progetto. Non è
sviluppato come prodotto: qui non ci sono impegni di sviluppo, né date, né una v1.0
promessa. Vale una sola regola — **esce ciò che è già stato scritto per lavorare**, non ciò
che andrebbe costruito apposta per il repository.

Le milestone qui sotto descrivono quindi *stati*, non un piano di lavoro.

---

## M1 — la Storia  ·  *rilasciata — questo repository*

Un repository che **spiega** il progetto.

- README (il problema, perché è diverso, l'architettura).
- `architecture/` — panoramica, funzioni, gate di qualità, con un diagramma.
- Architecture Decision Record (ADR) — le decisioni forti, con i numeri dove disponibili.
- Alcune voci di `journal/`.
- **Un** esempio completo in `examples/` con un input a licenza aperta.
- `LICENSE`, `ROADMAP.md`, `CONTRIBUTING.md`.
- **Uno script che esegue l'esempio** — `scripts/compare_readings.py`: rende la pagina come
  immagine, ri-trascrive la formula dall'immagine, confronta le due letture, stampa le
  differenze. È la dimostrazione di **un** gate, non il motore.

**Stato raggiunto:** un estraneo, leggendo solo README + architettura + un ADR, capisce il
*problema*, l'*originalità* e *perché questo autore l'ha progettato così*. L'esempio è
riproducibile a mano, e lo script riproduce da solo le discrepanze che l'esempio documenta.

## M2 — la Catena  ·  *quando sarà ripulita*

La catena che gira già, pubblicata **com'è**: generalizzata e ripulita dal dominio privato
da cui nasce, non riscritta per un pubblico immaginario.

- Le schede di funzione vere (direttore / bibliotecario / operatore pre-gate /
  ri-trascrittore / verificatore), generalizzate.
- Il protocollo dei gate e la sua configurazione operativa: innesti di escalation, canali
  richiesti per tipo di nota, politica di quarantena.
- Il nucleo deterministico — ciò che non deve mai essere un'opinione di un modello: soglia
  minima di risoluzione imposta dal programma, confronto strutturale, pre-gate meccanico,
  traccia di firma. Poche centinaia di righe, non un framework.
- Come si installa e che cosa serve per farla girare.

**Stato raggiunto:** chi ha lo stesso ambiente — un host agentico che esegue sub-agenti con
contesto isolato, `poppler-utils`, un modello multimodale — la esegue. Il limite è
dichiarato: **non è un pacchetto installabile ovunque, e non promette di diventarlo.**

## M4 — l'Evidenza  ·  *senza data*

I numeri che mostrano che il valore è il *processo*, non il modello. Con un vincolo che
questo repository non può aggirare: **le fonti su cui la catena lavora davvero sono
protette da copyright e non entreranno mai qui.**

- **Misure aggregate** raccolte sul corpus reale dell'autore: quante formule il layer di
  testo corrompe, quante ne prende la catena, quanti falsi allarmi — con la metodologia di
  misura descritta e le fonti *non* pubblicate. Sono evidenza **direzionale**, non
  riproducibile da terzi, e il repository lo dice ogni volta.
- **Se** e **quando** una parte del materiale a licenza aperta lo consente: un *fixture di
  conformità* — poche pagine, corruzioni note, esito atteso — che chiunque può rieseguire.
  È l'unico benchmark davvero riproducibile che questo progetto possa produrre.

**Stato raggiunto:** ogni numero pubblicato dice come è stato raccolto e che cosa **non**
dimostra.

---

## Che cosa questa roadmap non promette

Per essere leali con chi legge: qui non arriveranno un pacchetto installabile su qualunque
sistema, una integrazione continua, un supporto multi-provider verificato su più host, né
benchmark controllati di confronto fra modelli. Non perché non abbiano valore, ma perché
sono lavoro di prodotto, e questo repository non è un prodotto. Se un giorno arrivano, sarà
perché sono serviti all'autore per il suo lavoro — non perché erano stati promessi.

---

## Versioni

Le versioni seguono [SemVer](https://semver.org). Il progetto resta in **0.x**: ogni
milestone ha il suo tag minore — `v0.1.0` per M1, `v0.2.0` per M2 — e **nessuna v1.0 è
pianificata**. Ogni tag è una Release su GitHub, e [`CHANGELOG.md`](CHANGELOG.md) registra
che cosa è cambiato.

---

*Le milestone descrivono stati, non date. Le decisioni che si rivelano sbagliate si
rivedono alla luce del sole — gli ADR possono essere marcati `superseded`.*

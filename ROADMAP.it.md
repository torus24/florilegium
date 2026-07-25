# Roadmap

florilegium viene rilasciato **a livelli**. Ogni milestone ha un deliverable pubblicabile e
una **definition of done** (DoD): la successiva non parte finché la DoD non è verde. È una
scelta deliberata — qui il valore sono il metodo e le decisioni, quindi la *storia* esce
prima del *codice*.

---

## M1 — la Storia  ·  *in corso*

Un repository che **spiega** il progetto, ancora senza codice eseguibile.

- README (il problema, perché è diverso, l'architettura).
- `architecture/` — panoramica, funzioni, gate di qualità, con un diagramma.
- Architecture Decision Record (ADR) — le decisioni forti, con i numeri dove disponibili.
- Alcune voci di `journal/`.
- **Un** esempio completo in `examples/` con un input a licenza aperta.
- `LICENSE`, `ROADMAP.md`, `CONTRIBUTING.md`.

**DoD:** un estraneo, leggendo solo README + architettura + un ADR, capisce il *problema*,
l'*originalità* e *perché questo autore l'ha progettato così*. L'esempio è riproducibile
a mano.

## M2 — il Motore  ·  *pianificata*

Rendere il progetto eseguibile nel suo nucleo utile-ma-difficile-da-copiare.

- L'orchestratore, i batch e la gestione delle sessioni.
- `config/config.example.yaml`, documentazione di installazione e primi passi.

**DoD:** un utente Linux esegue la pipeline su un PDF d'esempio seguendo la guida ai primi
passi, senza altro aiuto.

## M3 — i Gate  ·  *pianificata*

La parte metodologicamente originale, in forma eseguibile. Il *metodo* è già pubblicato a
M1 (vedi `architecture/` e gli ADR); ciò che M3 aggiunge è la macchina che lo esegue.

- I prompt di funzione generalizzati (direttore / bibliotecario / operatore pre-gate /
  ri-trascrittore / verificatore).
- La configurazione operativa dei gate: gli innesti di escalation, i canali richiesti per
  tipo di nota, la politica di quarantena.

**DoD:** i gate girano sull'esempio e producono un rapporto di qualità riproducibile.

## M4 — Benchmark & v1.0  ·  *pianificata*

I dati che mostrano che il valore è il *processo*, non il modello.

- `benchmark/`: singolo prompt vs. catena; robustezza OCR; costo/token; densità di note —
  con dati riproducibili.
- Test (unitari + funzionali + di regressione), CI.
- Tag **v1.0.0**, `CHANGELOG.md` completo.

**DoD:** i benchmark sono riproducibili dal repository; la CI è verde; il README punta ai
risultati.

---

*Le milestone descrivono intenzioni, non date. Le decisioni che si rivelano sbagliate si
rivedono alla luce del sole — gli ADR possono essere marcati `superseded`.*

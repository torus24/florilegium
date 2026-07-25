# ADR-0003 — Un modello per funzione: il forte dove si giudica, l'economico dove si esegue

**Status:** accepted

---

## Contesto

La pipeline usa più modelli linguistici. La tentazione naturale — per contenere i costi —
è usarne **uno economico ovunque**. Ma le funzioni non sono uguali: alcune **estraggono e
giudicano** (serve accuratezza), altre fanno **lavoro meccanico** (eseguire uno script,
riportare un output). Assegnare lo stesso modello a tutte spreca denaro dove non serve e
sbaglia dove serve.

## Ipotesi (cosa credevamo prima)

Che un modello di **fascia media** potesse reggere anche l'estrazione, riducendo i costi
senza perdere qualità; e che per i compiti meccanici bastasse sempre il modello **più
economico**.

## Esperimento (cosa abbiamo misurato)

> **Dato reale**, da un uso della pipeline precedente a questo progetto, riscritto in
> forma generica. Nell'implementazione di riferimento i modelli sono di famiglia Claude
> (vedi il README, *Stato & implementazione*). **Campione piccolo → evidenza direzionale, non
> benchmark** (quello è M4). Avvertenza dichiarata: la baseline è stata raccolta in parte
> con un regime di gate diverso ⇒ **non è un A/B pienamente controllato**.

- **Estrazione con il modello forte (Opus) — baseline:** **≈ 0,163 errori sostanziali per
  nota** (8 errori sostanziali su 49 note, 3 articoli).
- **Estrazione con un modello di fascia media (Sonnet), un articolo:** **≈ 0,50 errori
  sostanziali per nota** (~3× peggio). In più il **gate base non ha intercettato 2 errori
  gravi**, e un **refuso di fonte fabbricato** è passato (preso solo dal gate pieno).
- **Ritorno al modello forte, articolo successivo:** **≈ 0,00**.
- **Su una funzione puramente meccanica** (eseguire uno script e riportare l'output
  verbatim), il modello **più economico (Haiku) ha fallito due volte** — *interpretava*
  invece di *eseguire* — ed è stato alzato di fascia.

## Decisione

1. **Modello forte dove si estrae e dove si giudica al livello pieno** (estrazione,
   verifica dall'immagine).
2. **Modello medio dove si ri-legge senza emettere verdetto** (gate base) e dove il
   compito è un mestiere ripetibile.
3. **Non "il più economico ovunque":** anche un compito meccanico richiede un modello che
   sappia *non* interpretare.
4. Il modello di ciascuna funzione è **fissato nella sua scheda**, indipendente dal
   modello con cui gira la sessione.

**Assegnazione nell'implementazione di riferimento (Claude):** estrazione = Opus ·
verifica livello pieno = Opus · ri-trascrizione livello base = Sonnet (senza verdetto) ·
operatore meccanico pre-gate = Sonnet (alzato da Haiku).

## Conseguenze

- **Cosa risolve:** costo speso dove ripaga (il giudizio), risparmiato dove non serve
  (lettura base, lavoro meccanico).
- **Cosa NON è:** un benchmark. I numeri sono **direzionali** e vanno riconfermati in
  condizioni controllate (M4).
- **Cosa NON risolve:** non elimina gli errori; li sposta sul modello giusto per ogni
  funzione. La rete resta il gate a due livelli più l'arbitro (ADR-0001).
- **Quando rivederla:** l'ADR fissa il **criterio** ("il forte dove si giudica"), non i
  *nomi* dei modelli. Se un modello economico futuro raggiungesse il forte
  sull'estrazione, l'assegnazione cambia senza toccare il criterio.

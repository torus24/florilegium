# ADR-0001 — L'OCR-testo non è affidabile per le formule → verifica indipendente dall'immagine

**Status:** accepted

---

## Contesto

Una pipeline che estrae conoscenza da PDF tecnici si appoggia al **layer di testo** (OCR,
o testo incorporato nel PDF). Sul corpo del testo funziona bene. **Sulle formule no.**

Le corruzioni tipiche sono di **un solo glifo** — un pedice scambiato, un esponente perso
o raddoppiato, un simbolo alterato — e sono **silenziose**: l'output si legge benissimo,
quindi nessuno controlla. In un contesto ingegneristico il danno non si ferma alla nota:
quelle formule **finiscono nel codice di calcolo**, e un errore silenzioso diventa un
**risultato sbagliato a valle**, prodotto da uno script che non mette mai in dubbio il
numero che ha ricevuto.

Il problema ha **due facce**, non una:
- **falso negativo** — un errore reale della trascrizione che non viene visto;
- **falso positivo** — un controllo solo-testo che *accusa* la fonte di un refuso che
  nella fonte **non c'è**, e propone una "correzione" sbagliata.

## Ipotesi (cosa credevamo prima dell'esperimento)

Che un modello grande, leggendo il testo OCR, riuscisse a **rilevare da sé** le formule
sospette; e che la **resa ad alta risoluzione** dell'immagine servisse solo nei casi
dubbi, da attivare **"a richiesta"**, quando qualcuno avesse un dubbio esplicito.

## Esperimento (cosa abbiamo misurato)

> **Dato reale**, da un uso della pipeline precedente a questo progetto, riscritto in
> forma generica — nessun riferimento al corpus. È un **campione piccolo**: va letto come
> evidenza *direzionale* che ha motivato la decisione, non come benchmark controllato
> (quello è M4).

Su un lotto di **5 formule** che il controllo testuale aveva marcato come **"refuso di
fonte"** (cioè: la fonte sbaglia, uso la versione corretta), abbiamo reso il **solo rigo
conteso** ad **alta risoluzione (≥400 dpi)** e ri-letto la formula **dall'immagine**, in
modo indipendente. Esito:

- **4 casi su 5 erano falsi allarmi:** la fonte era corretta, l'errore stava
  nell'OCR/resa a bassa risoluzione. La "correzione" sarebbe stata un peggioramento.
- **Il 5º era un errore di fonte reale,** confermato per la stessa via.

**Dato chiave:** il "dubbio" che, in teoria, avrebbe dovuto far scattare la resa ad alta
risoluzione — lasciato alla discrezione — **non arrivava**. La resa "a richiesta" era, di
fatto, una resa che non si faceva.

## Decisione

1. **Le formule non si verificano dal testo, ma dall'immagine.** Render ad alta
   risoluzione della pagina/rigo → **ri-trascrizione indipendente** dall'immagine →
   **confronto incrociato** con la lettura testuale.
2. **La verifica è di terza parte.** La funzione che giudica la formula **non vede** la prima
   lettura e **non ha interesse** in essa: un agente non-terzo non può far passare il
   proprio errore come giusto.
3. **La resa ad alta risoluzione del rigo conteso è obbligatoria, non "a richiesta"**, per
   ogni formula segnalata, *prima* di firmarla come verificata.
4. **Due livelli di gate, più un arbitro:** *base* (ri-trascrizione indipendente
   dall'immagine, **senza verdetto**) su ogni nota che porti una formula o un valore a
   punto d'uso; *pieno* (verifica dall'immagine a ≥400 dpi, **con** verdetto) **solo dove
   un verdetto accusa la fonte**, o la nota è un anchor di benchmark — perché un errore
   silenzioso non produce nessuna segnalazione. Una discrepanza trovata al livello base
   apre l'**adjudication dell'arbitro**, non il gate costoso.

## Conseguenze

- **Cosa risolve:** cattura errori di formula silenziosi che un singolo prompt non vede;
  e — altrettanto importante — **azzera i falsi allarmi**, evitando di "correggere" fonti
  che erano già giuste.
- **Cosa costa:** più token e più passaggi. È il compromesso dichiarato del progetto —
  *knowledge quality over token efficiency*.
- **Cosa NON risolve:** le formule dove **nemmeno l'immagine** è leggibile (pagina troppo
  degradata). In quei casi il sistema **segnala**, non indovina.
- **Quando rivederla:** se un modello futuro leggesse le formule dall'immagine in modo
  affidabile in un **solo passaggio**, i due livelli di gate potrebbero fondersi (allora
  questo ADR passerebbe a `superseded`).

# ADR-0005 — Il costo in token è in gran parte intrinseco alla qualità (un'ottimizzazione respinta)

**Status:** accepted *(documenta una proposta di ottimizzazione **respinta**)*

---

## Contesto

La catena usa più token di un'estrazione one-shot, e questo attira ottimizzazioni. Una
proposta concreta: spostare la parte "motivazioni/verbale" (il *perché* delle regole,
episodi, regole superate) in file caricati **on-demand**, per alleggerire la grossa
lettura iniziale che precede ogni lotto di lavoro.

## Ipotesi (cosa credevamo)

Che alleggerire quella lettura iniziale tagliasse una **quota significativa** del costo.

## Esperimento (l'analisi che l'ha respinta)

> **Dato reale**, da un uso della pipeline precedente a questo progetto, in forma generica
> e direzionale.

- **Sposta poco.** Gran parte delle "motivazioni" è in realtà **operativa** (*quale canale
  di verifica cattura quale errore* è un "come", non un "perché") e deve restare. Il taglio
  reale è **~10%**, non il ~50% sperato.
- **Colpisce il costo sbagliato.** Ciò che fa saturare il lavoro su un documento denso non
  è la lettura iniziale: è il **costo di verifica per-nota**, che **scala col numero di
  note** e che la proposta non tocca. Alleggerire la lettura iniziale comprava **meno di
  una nota in più**.
- **Nessuna vera semplificazione.** Il materiale spostato avrebbe comunque richiesto una
  protezione (contiene regole superate in forma imperativa) → solo un file in più.

## Decisione

Ottimizzazione **respinta**. Il costo in token è **in gran parte intrinseco alla
qualità**: nasce dalla **verifica ridondante multi-canale**, che è il valore, non lo
spreco. Non si combatte il compromesso da cui il progetto prende il nome. L'unico
intervento tenuto è stato uno che **aumenta l'affidabilità a costo maggiore** (un canale
di verifica sempre tentato), non uno che risparmia.

## Conseguenze

- **Cosa dice:** la pipeline opera **vicino alla sua frontiera qualità/costo**; il lavoro
  che si estende su più sessioni è **atteso**, non un'inefficienza.
- **Cosa rafforza:** *knowledge quality over token efficiency*, con un caso concreto.
- **Insegnamento riusabile:** prima di ottimizzare, misura **quale** costo domina — spesso
  non è quello che sembra (qui: la verifica per-nota, non la lettura iniziale).
- **Quando rivederla:** se cambiasse il costo dominante (es. la verifica per-item
  diventasse molto più economica), l'analisi andrebbe rifatta.

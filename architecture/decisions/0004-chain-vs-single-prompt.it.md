# ADR-0004 — Una catena multi-agente, non un singolo prompt

🇬🇧 *This page is also available in [English](0004-chain-vs-single-prompt.md).*

**Status:** accepted

---

## Contesto

Estrarre conoscenza verificabile da PDF tecnici si potrebbe fare con **un singolo prompt**
su un modello capace: "leggi il PDF, scrivi le note". È la via più semplice e più
economica in token — ed è la scelta di default della maggior parte degli strumenti.

## Ipotesi (cosa credevamo possibile)

Che un modello abbastanza capace, in un solo prompt, potesse **estrarre e ricontrollarsi
da sé** a un livello sufficiente.

## Esperimento / ragionamento

Un singolo prompt ha **una sola lettura** della pagina e **nessuna seconda sorgente
indipendente** che la contraddica. Da qui due fallimenti *strutturali*, misurati negli
altri ADR:

- non vede gli **errori di formula silenziosi** — serve la seconda lettura dall'immagine
  ([ADR-0001](0001-formula-verification-from-image.it.md));
- sotto l'obbligo di giudicare, **fabbrica verdetti** su evidenza ambigua
  ([ADR-0002](0002-verdict-as-source-of-error.it.md)).

Nessuno dei due si risolve rendendo il prompt "più bravo": mancano la **seconda sorgente**
e la **terzietà**, non l'intelligenza.

## Decisione

La pipeline è una **catena di funzioni a responsabilità singola**, dove chi verifica non
ha prodotto ciò che verifica e non ne vede il ragionamento. La verifica indipendente non è
una scelta di stile: è ciò che un singolo prompt, **per costruzione**, non può fare.

## Conseguenze

- **Cosa risolve:** cattura errori che un singolo prompt, strutturalmente, non prende.
- **Cosa costa:** più token e più passaggi — è il compromesso dichiarato, e quel costo è
  in gran parte **intrinseco alla qualità** ([ADR-0005](0005-cost-is-intrinsic-to-quality.it.md)).
- **Cosa NON risolve:** non rende infallibile ogni funzione; la rete resta il gate a due
  livelli più l'arbitro.
- **Quando rivederla:** se un singolo modello riuscisse a produrre una seconda lettura
  **indipendente, da una sorgente diversa, in un colpo solo** — cosa difficile per
  costruzione: resterebbe comunque una sola lettura.

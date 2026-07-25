# Journal — note di campo

Un ADR registra una **decisione**: contesto, ipotesi, misura, conseguenza. Una voce di
journal registra l'**episodio che l'ha imposta** — cosa è andato storto, come è stato
trovato, e spesso quanto poco è mancato perché non lo si trovasse mai.

| # | Voce | Cosa è successo | Decisione che ne è nata |
|---|---|---|---|
| 01 | [Il refuso che non c'era](01-the-typo-that-was-not-there.it.md) | Quattro accuse alla fonte su cinque erano false — e la quarta è emersa per caso, senza che nessuno sospettasse niente | [ADR-0001](../architecture/decisions/0001-formula-verification-from-image.it.md) |
| 02 | [Il correttore silenzioso](02-the-silent-corrector.it.md) | Tre "correzioni" non dichiarate a una fonte: fedeltà non è correttezza | [ADR-0002](../architecture/decisions/0002-verdict-as-source-of-error.it.md) |
| 03 | [Il terzo canale](03-the-third-channel.it.md) | Due canali hanno concordato sullo stesso errore — e un canale dichiarato morto è stato decisivo tre volte su tre | [ADR-0001](../architecture/decisions/0001-formula-verification-from-image.it.md) · [ADR-0005](../architecture/decisions/0005-cost-is-intrinsic-to-quality.it.md) |
| 04 | [Quando la catena si spegne da sola](04-when-the-chain-stops-itself.it.md) | Il tetto è uno spegnimento, non una quota: nessuna unità lasciata a metà | [ADR-0005](../architecture/decisions/0005-cost-is-intrinsic-to-quality.it.md) |
| 05 | [La lettura ancorata](05-the-anchored-reading.it.md) | La stringa attesa, incollata nelle istruzioni di chi rilegge | [ADR-0006](../architecture/decisions/0006-reader-must-not-know-the-expected-answer.it.md) |

Sono scritte a posteriori e tenute oneste, anche dove il metodo prima era sbagliato e poi
è diventato giusto. I dati vengono da un uso della pipeline precedente a questo progetto,
riportati in forma generica.

Gli episodi provengono da circa **35 corse armate** su una **diciottina di documenti**:
abbastanza per dire che sono modi di guasto ricorrenti e non incidenti isolati, non
abbastanza per chiamarli una misura. I totali esatti arrivano coi benchmark di **M4**.

---

*Vedi anche: [architecture/overview](../architecture/overview.it.md) per come queste regole
sono finite nel disegno.*

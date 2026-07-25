# ADR-0007 — I limiti di corsa sono arresti, non quote

**Stato:** accettata

---

## Contesto

Una pipeline che lavora senza sorveglianza deve decidere **da sola** quando fermarsi. Nella
catena che ha preceduto questo progetto si sono viste due modalità di guasto opposte, ed
entrambe si sono pagate:

- **Non si ferma.** Un tetto di un documento per corsa è stato letto come *quota per singola
  esecuzione*: quota esaurita, la catena ha programmato il proprio riavvio e ha aperto il
  documento successivo con nessuno alla tastiera. Un contatore che si azzera da solo non è un
  limite, è un motore.
- **Si ferma male.** Interrompersi a metà di un'unità di lavoro lascia sul disco materiale
  che alla ripresa nessuno sa classificare — note scritte ma non verificate, verificate ma
  non firmate.

Sotto entrambe c'è la ragione per cui i limiti esistono: il decadimento della qualità sotto
pressione **non compare nei registri**. Compare in controlli che verso la fine della corsa
diventano un po' più sbrigativi, ed è invisibile proprio a chi sta finendo l'attenzione.
→ [journal/04](../../journal/04-when-the-chain-stops-itself.it.md).

## Decisione

**I limiti di corsa sono arresti, non quote**, e si formulano in cinque punti.

1. **Al raggiungimento del limite la pipeline si spegne e attende.** Non si rilancia, non si
   rimette in coda, non apre l'unità successiva. Il riarmo è un **atto umano** — una decisione
   presa fuori dalla corsa, non uno stato che la corsa possa raggiungere da sé.
2. **Il limite che governa è il contesto occupato, non il conteggio degli elementi.** Un tetto
   in documenti descrive medie passate; ciò che finisce davvero è lo spazio di lavoro. Due
   soglie, quindi: sotto la prima si può aprire un documento nuovo; sopra, la corsa prosegue
   **un'unità atomica alla volta**, ristimando a ognuna; oltre un **margine duro** non si apre
   più alcuna unità. Nella catena d'origine le due soglie erano il **65%** e l'**85%** del
   contesto — manopole, non leggi di natura. Proseguire oltre il limite *per finire il
   gruppo* è vietato.
3. **Nessuna unità lasciata a metà.** Un'unità già aperta si finisce; tutto ciò che non è
   stato lavorato diventa esplicitamente **sospeso** — un marcatore visibile nella nota
   stessa, che dichiara la verifica non completata e vieta l'uso a punto d'uso, il campo di
   verifica lasciato vuoto, e l'elenco delle note sospese scritto **sia** nel rapporto della
   corsa **sia** nella coda di lavoro. Uno stato che vive solo nella sessione che l'ha
   prodotto non esiste.
4. **Sospesa non è trattenuta.** La sospensione viene dal limite e si scioglie riprendendo il
   lavoro; la **trattenuta** viene da un verdetto non risolto e si scioglie con l'arbitrato o
   con la quarantena. Due stati diversi con due uscite diverse: confonderli farebbe sparire un
   controllo fallito dentro un evento di pianificazione.
5. **Il limite è imposto, non raccomandato.** Nella catena d'origine la dichiarazione di
   occupazione del contesto è rimasta *sulla carta* finché una corsa non ha firmato sei note
   senza una sola stima scritta. Da allora la dichiarazione è meccanica: un hook di sistema
   **rifiuta** di compilare il campo di verifica di una nota finché il rapporto corrente non
   porta almeno una riga di occupazione, con la stima e il modo in cui è stata fatta. Una
   regola che nessuno impone non è in vigore — è lo stesso ragionamento dell'
   [ADR-0006](0006-reader-must-not-know-the-expected-answer.it.md).

## Conseguenze

- **Cosa dice:** un arresto non è un evento eccezionale da gestire — è uno **stato previsto**,
  con la sua riga nel registro. Alla ripresa non si indaga su cosa è successo: lo si legge.
- **Cosa costa:** ripartenze, e lavoro che si distende su più sessioni. È il compromesso
  dell'[ADR-0005](0005-cost-is-intrinsic-to-quality.it.md) visto dal lato della
  pianificazione: fermarsi presto e in ordine costa una ripartenza, fermarsi tardi costa una
  nota mal certificata che nessuno riaprirà mai.
- **Cosa NON risolve:** il dato di occupazione è una **stima**, e come tale si dichiara. La
  regola non la rende esatta — la obbliga a essere **scritta e motivata** prima di poter
  autorizzare qualcosa. Né protegge da un limite tarato male: le soglie sono calibrazione, e
  la calibrazione è rivedibile.
- **Lezione riutilizzabile:** un limite che la funzione a cui si applica può **reinterpretare**
  non è un limite. Va scritto esplicitamente chi chiude la corsa, cosa la riarma, e cosa alla
  pipeline è vietato fare una volta raggiunto il limite.
- **Quando rivederla:** se l'orchestrazione smettesse di assumere sessioni con contesto
  limitato (vedi il vincolo di portabilità dichiarato nel README), queste soglie andrebbero
  riscritte nei termini di qualunque cosa diventi la risorsa scarsa.

## Voce di diario collegata

[journal/04 — Quando la catena si spegne da sola](../../journal/04-when-the-chain-stops-itself.it.md)

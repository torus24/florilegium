# Architettura — le funzioni della pipeline

La pipeline è una sequenza di **funzioni**, ognuna con un **unico compito** e
requisiti di inizio e fine ben definiti. Regola di fondo:

> Le funzioni **non condividono informazioni nascoste**. Una funzione successiva non
> accede mai al processo logico di quella precedente: riceve **solo il suo output**.

È questa separazione a rendere la verifica *indipendente* (di **terza parte**) invece che
auto-confermante: chi giudica non ha prodotto ciò che giudica, e non ne ha visto il
ragionamento.

Ogni funzione è descritta con lo stesso schema: **Missione · Input · Output · Cosa NON fa
· Perché esiste**.

---

## Direttore (orchestratore e arbitro)

- **Missione:** **orchestra e firma, non produce.** Dà il ritmo alla pipeline — sceglie cosa
  lavorare, in che ordine, e manda ogni nota attraverso le fasi. Ma è anche il **terzo
  attore che decide**: rifà i conti degli altri, esegue la **terza lettura dal layer di
  testo**, scioglie le divergenze fra estrazione e gate, esegue le rese ad alta risoluzione
  del rigo conteso, ed è **l'unico** che può certificare una nota (vedi
  [quality-gates](quality-gates.it.md)).
- **Input:** la coda di lavoro (Discovery), lo stato della pipeline, e gli esiti dei gate —
  le differenze del livello base, i verdetti del livello pieno.
- **Output:** la terza lettura sul rigo conteso, le analisi rifatte, la decisione sulle
  divergenze, la **firma** della nota — oppure la trattenuta o la quarantena, con il motivo.
- **Cosa NON fa:** **non distilla** (chi scrive una nota non la certifica). **Non apre il
  verdetto altrui prima di aver rifatto il conto per conto proprio**, partendo dalla sola
  nota: se il proprio conto e il verdetto divergono, si apre l'arbitrato *anche quando il
  verdetto dice «fedele»*. Non tratta un verdetto come una verità in nessuna delle due
  direzioni — né la conferma né l'accusa. E non corregge **mai** in silenzio: se scopre un
  proprio errore lo dichiara e riapre la nota.
- **Perché esiste:** perché **l'ultima firma sbaglia come tutte le altre funzioni — solo
  che nessuno la controlla.** Le fasi precedenti si controllano a vicenda; chi firma no. Il
  contrappeso non può che essere una procedura scritta che quella funzione deve eseguire su
  sé stessa, prima di ogni certificazione.

## Bibliotecario (estrazione)

- **Missione:** legge il layer di testo e produce **note atomiche** — una nota per un
  singolo concetto o formula — con il frontmatter di provenienza (fonte, pagina).
- **Input:** il documento sorgente (layer di testo) e l'elemento da estrarre.
- **Output:** una nota Markdown atomica, con i campi di provenienza compilati.
- **Cosa NON fa:** non "verifica" la propria estrazione (lo fanno i gate); non scrive a
  memoria — se la fonte non è verificabile, segnala la lacuna invece di inventare.
- **Perché esiste:** l'estrazione e la verifica devono stare in **funzioni diverse**,
  altrimenti la verifica non è indipendente.

## Operatore pre-gate

- **Missione:** prepara meccanicamente le note prima dei gate (normalizzazioni,
  precondizioni, controlli di esistenza pagina). Anche il **triage dei canali** si esegue qui:
  prima dell'estrazione legge il layer di testo pagina per pagina e riferisce, pagina per
  pagina, dove è scarno, vuoto o corrotto sui simboli. Riferisce e basta: **leggere quella
  tabella e stilare l'elenco finale delle pagine da leggere a immagine resta del
  direttore**.
- **Input:** le note appena estratte.
- **Output:** note pronte per il gate, oppure scartate con motivo.
- **Come lavora:** lancia uno script deterministico e ne riporta l'esito così com'è. Il
  controllo è dello script, non del modello: la funzione esiste perché qualcuno deve
  eseguirlo dentro la catena e riferire senza aggiustare nulla — e anche un compito
  meccanico richiede un modello che non improvvisi (ADR-0003).
- **Cosa NON fa:** non entra nel merito della correttezza dei contenuti; fa lavoro
  meccanico e ripetibile.
- **Perché esiste:** togliere il lavoro meccanico dai gate li mantiene focalizzati sul
  giudizio.

## Ri-trascrittore (gate — livello base)

- **Missione:** ri-legge il contenuto in modo **indipendente** e lo confronta con
  l'estrazione. È il controllo base, e gira su ogni **nota da gate** — quelle che portano
  una formula o un valore a punto d'uso; le esclusioni si dichiarano una per una, mai in
  blocco.
- **Input:** la nota da controllare (senza il ragionamento di chi ha estratto) e le pagine
  rese a immagine. I bersagli gli sono indicati per posizione e grandezza, mai per valore.
- **Output:** l'elenco delle **differenze** rispetto alla nota, oppure "nessuna differenza".
  Una differenza apre l'**adjudication dell'arbitro**, non il livello pieno. Più, per ogni
  glifo di cui non è sicuro, un
  **dubbio dichiarato**: un dubbio dichiarato vale più di una lettura sicura sbagliata.
- **Cosa NON fa:** **non emette verdetti.** Non dice "fedele" né "non fedele", non giudica
  e non accusa: una differenza fra due letture non è un'accusa, e a giudicarla è un terzo
  che dispone anche del layer di testo. Non normalizza ciò che legge: il bersaglio è lo
  **stampato**, anche quando è insensato.
- **Perché esiste:** perché è nato *togliendo* il verdetto alla seconda lettura. Quando la
  seconda lettura emetteva verdetti, sbagliava in entrambe le direzioni — conferme
  correlate su note malate e accuse a note sane. Ciò che restava utile, misurato, era la
  **ri-trascrizione indipendente**: il valore che questa funzione porta è la trascrizione,
  non l'opinione (vedi [ADR-0002](decisions/0002-verdict-as-source-of-error.it.md)).

## Verificatore (gate — livello pieno, dall'immagine)

- **Missione:** quando un verdetto **accusa la fonte**, o la nota è un **anchor di
  benchmark** — in particolare sulle **formule** — verifica dall'**immagine** della pagina,
  non dal testo OCR. La resa ad alta risoluzione del rigo conteso è **obbligatoria** prima
  di firmare (vedi [ADR-0001](decisions/0001-formula-verification-from-image.it.md)).
- **Input:** la nota contesa e l'immagine ad alta risoluzione della pagina/rigo.
- **Output:** un **verdetto motivato** — *fedele*, *fedele con rilievi* oppure *non fedele*
  — insieme a che cosa servirebbe per chiudere il caso. Non firma: il verdetto torna
  all'arbitro, che rifà i conti e firma; un *non fedele* che l'adjudication non riesce a
  sciogliere è ciò che manda la nota in quarantena (vedi
  [gate di qualità](quality-gates.it.md)).
- **Cosa NON fa:** non "corregge" una fonte senza prova indipendente più forte; non
  indovina dove nemmeno l'immagine è leggibile — segnala. E **non riceve la risposta
  attesa**: il prompt indica i bersagli per **posizione e grandezza**, mai per valore, e
  non contiene la forma attesa — né nelle istruzioni, né attraverso campi liberi che la
  fanno rientrare. La nota gli viene consegnata *per il confronto*, che però si apre solo
  **dopo** che la sua trascrizione è chiusa: è la separazione fra chi legge e chi giudica
  a reggere il presidio, non la buona volontà di non guardare (vedi
  [ADR-0006](decisions/0006-reader-must-not-know-the-expected-answer.it.md)).
- **Perché esiste:** è il punto in cui florilegium chiude il punto cieco dell'OCR sulle
  formule. È la feature-eroe.

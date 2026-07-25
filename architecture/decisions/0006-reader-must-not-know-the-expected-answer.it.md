# ADR-0006 — Chi rilegge la fonte non deve conoscere la risposta attesa

🇬🇧 *This page is also available in [English](0006-reader-must-not-know-the-expected-answer.md).*

**Status:** accepted

---

## Contesto

L'[ADR-0001](0001-formula-verification-from-image.it.md) stabilisce che la verifica è **di
terza parte**: la funzione che giudica una formula non vede la prima lettura e non ha
interessi in essa. È il principio su cui poggia l'intera catena.

Ma «non vedere la nota» non basta come garanzia, perché l'indipendenza non si perde solo
mostrando il documento: si perde **con un frammento di documento dentro il prompt**. E il
prompt di verifica deve necessariamente dire *dove* guardare. Il confine fra indicare il
bersaglio e suggerire la risposta è sottile, e sta esattamente lì che si rompe.

Questo ADR chiude il lato scoperto dell'ADR-0001. Il principio proteggeva **l'arbitro** dal
verdetto altrui — era già prassi rifare i conti a mano *prima* di aprire il verdetto del
verificatore, dichiaratamente per non farsene condizionare. Nessuna regola proteggeva **il
verificatore** dalla nota che doveva mettere in discussione.

C'è un motivo in più per cui il perimetro non può fermarsi a chi emette verdetti. Nella
catena d'origine il gate di livello base **non giudica affatto**: è una funzione nata
*togliendo* il verdetto alla seconda lettura, dopo che i verdetti si erano rivelati
sbagliati in entrambe le direzioni — conferme correlate su note malate e accuse a note
sane (è la stessa constatazione dell'[ADR-0002](0002-verdict-as-source-of-error.it.md)).
Quella funzione rilegge dall'immagine ed elenca le differenze; a giudicarle è un terzo,
che dispone di un canale in più. **Eppure si è ancorata lo stesso.** Togliere il potere
di giudizio non ha tolto l'ancoraggio, perché l'ancoraggio non colpisce il giudizio:
colpisce **la lettura**. Per questo l'ADR parla di *chi rilegge la fonte*, e non di *chi
verifica*.

## Ipotesi (cosa credevamo prima)

Che incollare nel prompt di verifica la stringa attesa — presa dalla nota — rendesse il
controllo **più preciso ed economico**: bersaglio inequivocabile, nessun tempo perso a
cercare, verdetto mirato, meno token.

## Esperimento (cosa abbiamo osservato)

> **Dato reale**, da un uso della pipeline precedente a questo progetto, in forma generica.
> Campione piccolo → evidenza *direzionale*, non benchmark (quello è M4).

Due episodi indipendenti, stesso meccanismo.

1. Su una coppia di termini tecnici quasi sinonimi, la stringa della nota è stata incollata
   nel prompt del **ri-trascrittore — il gate di livello base**, la funzione che rilegge
   dall'immagine e non emette verdetti. L'ha **restituita come verbatim del testo
   stampato**; sulla stampa c'era l'altro termine. Non aveva letto male la pagina: non
   aveva avuto bisogno di leggerla, perché la risposta gli era arrivata insieme alla
   domanda. Sul dato non ci fu conseguenza — il valore reggeva su altri due canali — ma
   il canale che doveva controllarlo aveva smesso di controllare.
2. Su un errore di sigla (uno scenario sperimentale riportato al posto di un altro), il
   verificatore di **livello pieno** — quello che rende l'immagine ad alta risoluzione, il
   presidio più costoso della catena — si è **ancorato alla nota** e l'ha confermata.
   L'errore è stato preso da altri due canali (layer-testo e aritmetica interna alla fonte).

Il tratto comune, ed è ciò che rende il difetto grave: una lettura ancorata **non produce
un errore, produce una conferma**. Nei registri è indistinguibile da un controllo riuscito,
e il canale risulta attivo mentre ha smesso di funzionare. Vale a ogni livello di gate:
nel primo episodio la conferma arriva da una funzione che non ha nemmeno il potere di
emettere verdetti.

C'è un secondo dato, ed è quello che detta il perimetro di questo ADR. Dopo il primo
episodio la regola **è stata scritta** — ma sul solo prompt che l'aveva generata, quello
del gate di livello base. Il prompt del livello pieno è rimasto com'era. Il secondo
episodio è avvenuto **due giorni dopo**, su quel prompt. Una regola giusta, applicata a un
anello solo, non ha spostato nulla: ha prodotto la convinzione di essere protetti.

## Decisione

1. **Il prompt di verifica non contiene la forma attesa.** In nessuna forma: né verbatim,
   né parafrasata, né come "contesto utile", né come esempio.
2. **Il bersaglio si indica per POSIZIONE e GRANDEZZA, mai per valore.** *«Equazione 12,
   pagina 7, il coefficiente al primo membro»* è legittimo; *«l'equazione 12 dovrebbe
   riportare X»* è vietato.
3. **Un sospetto si comunica come punto conteso, non come conclusione attesa:** *«su questo
   rigo c'è un dubbio, rileggilo»*, mai *«su questo rigo dovrebbe esserci questo»*.
4. **Prima si trascrive, poi si confronta — e chi rilegge non giudica.** La ri-lettura si
   chiude *prima* di aprire la nota. Chi ha riletto può poi elencare le **differenze** —
   una differenza fra due letture non è un'accusa — ma il giudizio su quelle differenze
   spetta a un terzo, che dispone di un canale in più. È questo punto, non il punto 1, a
   coprire il caso in cui a chi rilegge la nota è consegnata per intero. E va detto:
   l'ordine, da solo, è un'istruzione, e vale quanto valgono le istruzioni (vedi
   *Conseguenze*); il presidio strutturale è la **separazione fra chi legge e chi giudica**.
5. **Chi arbitra rifà i conti prima di aprire i verdetti altrui** (analisi dimensionale e
   aritmetica): regola già in essere, qui confermata come parte della stessa famiglia.
6. **La regola vale su OGNI prompt di OGNI funzione che rilegge la fonte, a ogni livello
   di gate** — che quella funzione sia autorizzata a giudicare oppure no.
   Non è un rimedio all'episodio che l'ha generata: è un requisito del perimetro. Un prompt
   di verifica che non la porta scritta è **fuori norma** anche se nessuno vi ha ancora
   incollato nulla — la regola sta nel testo del prompt, non nella diligenza di chi lo
   compila.
7. **I campi liberi sono la via di rientro, e vanno normati per primi.** Le voci del tipo
   *«valori dichiarati per questa nota»* o *«sospetti da giudicare»* sono punti in cui la
   forma attesa rientra senza che nessuno abbia deciso di farla rientrare. Vanno vincolati
   a posizione e numero nel testo stesso del prompt, come tutto il resto.
8. **L'adozione si verifica sui prompt, uno per uno.** Il controllo è meccanico: si apre
   ogni prompt di verifica in vigore e si cerca la regola. Fin quando c'è un prompt scoperto
   la decisione non è applicata, per quanto sia applicata altrove.

## Conseguenze

- **Cosa risolve:** impedisce la modalità di guasto più insidiosa dei gate — un canale che
  produce conferme invece di controlli, restando verde nei registri.
- **Cosa costa:** ri-letture meno mirate, quindi più token e qualche verdetto fuori
  bersaglio da rilanciare. È lo stesso compromesso dell'[ADR-0005](0005-cost-is-intrinsic-to-quality.it.md):
  la qualità della conoscenza prima dell'efficienza dei token.
- **Cosa NON risolve:** l'ancoraggio di una funzione **alla propria** lettura precedente
  (se rilegge due volte, la seconda è contaminata dalla prima) — per quello serve la
  separazione in funzioni distinte dell'[ADR-0004](0004-chain-vs-single-prompt.it.md). E non
  risolve i falsi negativi: un verificatore non ancorato può comunque mancare un errore.
- **Perché non basta chiedere di diffidare.** Il presidio, nella catena d'origine, esisteva
  già — in forma di **istruzione**. Il prompt del livello pieno si apre con *«non fidarti
  della nota né del report di chi ha estratto»*; la scheda della funzione prescrive di
  trascrivere **prima** dall'immagine e di confrontare **dopo**, e di ignorare i giudizi
  della nota finché non si è arrivati a una conclusione autonoma. L'ancoraggio è avvenuto
  lo stesso. Un'esortazione alla diffidenza vale finché l'informazione non è già sotto gli
  occhi: dopo, chiedere di non usarla è chiedere di non aver letto. **Il rimedio non è
  istruire a diffidare dell'informazione: è non fornirla.** Questa è la ragione per cui la
  decisione è scritta come vincolo sul **testo del prompt** e non come raccomandazione di
  condotta.
- **Esposizione residua, proprio dove il metodo è più forte.** Al livello pieno chi legge è
  anche chi giudica, e la nota contesa gli viene di norma fornita per il confronto: è
  esattamente la configurazione che questa decisione dichiara insufficiente in linea di
  principio. I contrappesi non stanno dentro il gate, stanno attorno — la terza lettura dal
  layer di testo che l'arbitro esegue comunque su ogni nota-formula, anche quando il gate
  non ha trovato nulla; la resa ad alta risoluzione che l'arbitro fa di persona prima di
  ogni firma che accusa la fonte; le condizioni formali di validità del verdetto, senza le
  quali il gate si considera non avvenuto e si rifà; e la regola per cui nessun verdetto è
  fonte di verità, in nessuna delle due direzioni. Nella catena d'origine il livello pieno
  ha, in una stessa corsa, confermato un errore reale e smentito a torto una nota giusta: a
  reggere furono la ri-trascrizione di base e la terza lettura. La separazione strutturale
  fra chi legge e chi giudica, a questo livello, resta un **obiettivo di M2** — due chiamate
  isolate, trascrizione senza la nota e giudizio sulle due trascrizioni — non un risultato
  già acquisito.
- **Rischio residuo da sorvegliare:** la regola è facile da violare **in buona fede**,
  perché nasce dal desiderio legittimo di essere precisi e di non far perdere tempo. Va
  verificata sui **prompt**, non sulle intenzioni: il contesto che si dà a chi verifica è
  esattamente ciò che smette di essere verificato.
- **Rischio residuo, secondo tipo — la correzione parziale:** una regola scritta sull'anello
  dove il difetto si è manifestato, e non sugli altri, è più pericolosa dell'assenza di
  regola: chiude il caso nei registri e lascia il difetto in esercizio. È il secondo dato
  dell'esperimento qui sopra. Ogni volta che una regola di questa famiglia entra in vigore,
  l'ultimo passo non è scriverla — è **enumerare gli anelli e verificarli tutti**.
- **Quando rivederla:** se si potesse dimostrare che una funzione di verifica **non si
  ancora** a un'informazione fornita — misurandolo, non assumendolo — il vincolo potrebbe
  essere allentato per i casi in cui il bersaglio è genuinamente ambiguo.

## Voce di diario collegata

[05 — La lettura ancorata](../../journal/05-the-anchored-reading.it.md)

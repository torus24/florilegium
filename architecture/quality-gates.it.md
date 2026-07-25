# Architettura — i gate di qualità

I **gate di qualità** sono il cuore metodologico di florilegium: il punto in cui una nota
estratta viene messa alla prova prima di entrare nel vault. Sono progettati intorno a
quattro idee, ognuna con un registro alle spalle — un ADR, una voce di journal, o entrambi.

## 1. Due livelli, più un arbitro

Un unico gate "pesante" su ogni nota sarebbe costoso e lento; un unico gate "leggero"
mancherebbe gli errori che contano. florilegium usa **due livelli di gate** e, sopra di
essi, **un arbitro** che è l'unico a firmare:

| Livello | Chi | Quando | Cosa fa |
|---|---|---|---|
| **Base** | Ri-trascrittore | Solo sulle **note da gate**: formule e valori numerici a punto d'uso | Ri-trascrive dall'**immagine** ed **elenca le differenze** — non giudica |
| **Pieno ★** | Verificatore | Solo quando un verdetto **accusa la fonte**, o la nota è un **anchor di benchmark** | Verifica dall'immagine a **≥400 dpi**; qui il verdetto c'è |
| **Arbitro** | Direttore | **Sempre**, su tutto ciò che passa | Rifà i conti prima di aprire i verdetti altrui, esegue la terza lettura dal layer di testo, scioglie le divergenze, **firma** |

Il gate base non gira «su ogni nota»: gira sulle **note da gate**. Le altre sono **escluse
una per una, con la motivazione a verbale** — mai un'esclusione in blocco.

L'escalation ha **due innesti**, e portano in due posti diversi:

- **per segnalazione** — uno o più scarti al livello base non fanno scattare il controllo
  costoso: aprono l'**adjudication dell'arbitro**, con lettura dal layer di testo
  obbligatoria. Chi ha trovato la differenza non è chi la giudica.
- **per accusa** — qualunque verdetto che dica *la fonte sbaglia* impone la resa del rigo
  conteso a **≥400 dpi** prima che si possa firmare. A qualsiasi livello, senza bisogno di
  sospetto e senza discrezionalità. È un'**inversione dell'onere della prova**: per
  accusare la fonte, la pipeline deve provarlo attraverso un canale diverso da quello che
  ha prodotto l'accusa. È anche l'unico innesto, insieme agli anchor di benchmark, che fa
  salire al livello pieno.

Il secondo innesto esiste perché il primo non basta: un errore silenzioso non genera
dubbio, quindi un controllo che scatta solo sul dubbio non scatta proprio nei casi per cui
esiste. Il terzo canale (§3) è incondizionato per la stessa ragione — sulle note di formula
gira **anche quando il gate non ha trovato nulla**. Soprattutto allora.

## 2. Verifica di terza parte

Chi giudica non ha prodotto ciò che giudica, e non vede il suo ragionamento (vedi
[roles](roles.it.md)). Sulle formule questo diventa concreto: il livello pieno non si fida
del testo OCR — rende la pagina come **immagine** ad alta risoluzione, ri-trascrive la
formula in modo **indipendente**, e la confronta in modo incrociato con la lettura
testuale.

- L'accordo tra le due letture è **evidenza, non prova**: due canali possono sbagliare
  insieme (vedi §3).
- Il disaccordo non promuove né boccia: apre l'**adjudication dell'arbitro** — e, se resta
  irrisolto, la quarantena.
- La resa ad alta risoluzione del rigo conteso è **obbligatoria**, non "a richiesta":
  lasciata alla discrezione, non si faceva mai. → motivazione e dati nell'
  [ADR-0001](decisions/0001-formula-verification-from-image.it.md).
- L'indipendenza è **informativa**, non solo organizzativa: a chi verifica non va
  consegnata la risposta che deve verificare. Un verificatore che sa già cosa deve
  trovare, lo trova. →
  [ADR-0006](decisions/0006-reader-must-not-know-the-expected-answer.it.md).

Questo taglia in **due direzioni**: cattura gli errori silenziosi *e* azzera i falsi
allarmi (non "corregge" fonti che erano già giuste).

## 3. Tre canali, non due

Due letture indipendenti possono concordare **sullo stesso errore**. Quando succede, il
gate non vede alcuna discrepanza — e l'errore non viene catturato, viene *certificato*.
Perciò il controllo non poggia su due canali ma su **tre**, scelti in base a **quanto
diversamente sbagliano**:

| Canale | Cosa legge | Come sbaglia |
|---|---|---|
| **Layer di testo** | i caratteri incorporati nel PDF | perde o riordina caratteri — un operatore che sparisce, un indice invertito |
| **Immagine della pagina** | la pagina resa ad alta risoluzione | confonde **glifi** che si somigliano |
| **Aritmetica interna alla fonte** | un valore che la formula deve riprodurre, un caso limite, il bilancio dimensionale | non sbaglia *leggendo*: o il conto torna, o non torna |

Il terzo passaggio lo esegue **l'arbitro**, e lo esegue **sempre** su ogni nota di formula:
una **terza lettura dal layer di testo**, anche quando il gate non ha trovato niente. Dove
la fonte pubblica un numero che la formula deve riprodurre, **l'aritmetica interna è la
forma da preferire** — chiude la questione **senza guardare nessuna delle due letture**. E
quando *quel rigo* è illeggibile nel layer, l'aritmetica interna lo **surroga**: riga per
riga, mai per pagina. Un caso svolto: [examples/01](../examples/01/README.it.md).

Ne discendono tre regole, e sono regole, non consigli:

- **Nessun canale si dichiara morto in blocco.** L'indisponibilità si decide **riga per
  riga** e si motiva nel rapporto — mai come esclusione a priori di una pagina o di un
  documento.
- **Alzare la risoluzione non risolve un errore di glifo.** Se due simboli si somigliano,
  guardarli più da vicino non aiuta: bisogna guardarli **da un'altra parte**.
- **Il layer di testo non basta mai, da solo, a un verdetto.** È un canale, non una prova:
  qualunque conclusione che poggi solo su di lui resta aperta.

→ gli episodi da cui nasce: [journal/03](../journal/03-the-third-channel.it.md).

## 4. Il verdetto è evidenza, non una verità assoluta

Obbligare un verdetto netto (passa/non passa) su **ogni** elemento fabbrica falsa
sicurezza: su evidenza ambigua, la funzione produce comunque un verdetto — spesso
sbagliato. Perciò:

- È ammesso — e a volte richiesto — l'esito **"non determinabile → escalation"**.
- Un verdetto ad **alto impatto** (es. "la fonte sbaglia") non è firmabile senza una prova
  indipendente più forte.
- Il gate **premia il dubbio onesto**: un'escalation non è un fallimento, è il
  comportamento corretto. → [ADR-0002](decisions/0002-verdict-as-source-of-error.it.md).

## Il percorso di un elemento

```
Estrazione  (canale 1 · layer di testo)
   │
   ├─ pre-gate MECCANICO ... uno script, non un modello: verifica che il numero d'equazione
   │                         e le stringhe distintive stiano sulla pagina dichiarata
   │
   └─ gate BASE ........... solo note da gate ..... ri-trascrizione dall'IMMAGINE  (canale 2)
                                                   elenca le differenze, non giudica
             ↓
   ARBITRO — il direttore, sempre
      ├─ rifà i conti PRIMA di aprire i verdetti altrui
      ├─ terza lettura dal LAYER DI TESTO su ogni nota-formula, anche a zero scarti
      └─ aritmetica interna dove la fonte pubblica un numero                       (canale 3)
             │
             ├─ tutto coerente ──────────────────────────────────────────────► Vault
             │
             └─ il verdetto accusa la fonte  ·oppure·  la nota è un anchor
                       ↓
                  gate PIENO ★ ... IMMAGINE ≥400 dpi, con verdetto                (canale 2)
                       │
                       ├─ conferma / correzione ─────────────────────────────► Vault
                       └─ irrisolvibile ──► Quarantena  (né promosso né perso, con motivo)
```

## Quarantena

Ciò che nessun livello riesce a risolvere **non viene né promosso né buttato**: finisce in
**quarantena**, con la motivazione. È un meccanismo di prima classe, non un errore: rende
esplicito ciò che il sistema non sa, invece di indovinare. La cartella di quarantena esiste
per convenzione anche quando è vuota.

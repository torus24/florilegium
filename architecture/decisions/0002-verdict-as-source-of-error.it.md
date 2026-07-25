# ADR-0002 — Il verdetto obbligatorio è esso stesso una sorgente di errore

**Status:** accepted

---

## Contesto

In un gate di qualità sembra naturale — e rigoroso — chiedere alla funzione di verifica un
**verdetto netto** su ogni elemento: passa / non passa, corretto / refuso. L'intuizione è
"niente vie di mezzo, decidi".

Ma obbligare un verdetto **definitivo su OGNI item** ha un effetto collaterale non ovvio:
di fronte a evidenza **ambigua o insufficiente**, la funzione produce **comunque** un
verdetto — perché glielo si è chiesto. Quel verdetto non misura la realtà: misura la
**pressione a decidere**. È così che nasce la falsa sicurezza.

Questo ADR è strettamente legato all'[ADR-0001](0001-formula-verification-from-image.it.md):
lì il verdetto obbligatorio "refuso di fonte" produceva accuse infondate; qui se ne trae
il principio generale.

## Ipotesi (cosa credevamo prima)

Che un verdetto **obbligatorio e binario** rendesse i gate più severi e più affidabili —
che "costringere a decidere" equivalesse a "decidere meglio".

## Esperimento (cosa abbiamo osservato)

> **Dato reale**, da un uso della pipeline precedente a questo progetto, in forma
> generica. Campione piccolo → evidenza *direzionale*, non benchmark (quello è M4).

Costringere la funzione di verifica a emettere un verdetto "refuso di fonte" sulle formule
contese ha prodotto una quota **alta di accuse infondate** (vedi
[ADR-0001](0001-formula-verification-from-image.it.md): **4 casi su 5** erano falsi
allarmi). Un caso lo mostra in modo netto: la verifica ha **fabbricato** un refuso,
accusando un'equazione di un errore che usava **simboli mai stampati** in quella formula
— un verdetto prodotto dalla *pressione a decidere*, non dall'evidenza. Sui casi ambigui
il verdetto obbligatorio tendeva, **in tutti i casi osservati**, verso la decisione **più forte**
(accusare la fonte) invece che verso il "non so, serve altro".

## Decisione

1. **Il verdetto è evidenza da pesare, non una verità assoluta.** "La funzione ha espresso
   un giudizio" e "il giudizio è vero" sono due cose distinte: la prima non implica la
   seconda.
2. **È ammesso — e a volte richiesto — l'esito "non determinabile → escalation"**, invece
   di forzare un pass/fail su evidenza insufficiente.
3. **Un verdetto ad alto impatto** (es. "la fonte sbaglia") **non è firmabile senza una
   prova indipendente più forte** — la resa ad alta risoluzione dell'ADR-0001.
4. Il gate è progettato per **premiare il dubbio onesto**, non per punirlo: un'escalation
   non è un fallimento della funzione, è il comportamento corretto.

## Conseguenze

- **Cosa risolve:** meno falsi positivi; le ambiguità diventano **escalation** invece di
  decisioni sbagliate firmate.
- **Cosa costa:** richiede un **percorso di escalation esplicito** (costo di processo) e
  un livello di gate che lo raccolga.
- **Cosa NON risolve:** i falsi negativi. Una funzione può ancora *mancare* un errore reale;
  per quello restano i **due livelli di gate più l'arbitro** (ADR-0001), non basta
  togliere l'obbligo di verdetto.
- **Quando rivederla:** se si trovasse un modo per **calibrare in modo affidabile la
  confidenza** del verdetto, parte dell'escalation potrebbe automatizzarsi (questo ADR
  passerebbe a `superseded` o verrebbe raffinato).

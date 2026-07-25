# 03 — Il terzo canale

*Voce di diario. I dati vengono da un uso della pipeline precedente a questo progetto,
riportati in forma generica.*

---

## Due letture non bastano

L'architettura nasce con due canali: chi **estrae** legge il testo, chi **verifica** rilegge
l'immagine. Due letture indipendenti, una per sorgente. Sembrava sufficiente, e per un po'
lo è sembrato davvero.

Poi sono arrivati due episodi che dicono la stessa cosa da direzioni opposte.

## Episodio uno — quando i due canali sbagliano insieme

Su una correzione, il ri-trascrittore da immagine e la nota hanno dato la **stessa risposta
sbagliata**. Non è un caso fortunato per la pipeline: è il caso che manda in pezzi l'idea
che due canali bastino. Se concordano, il gate passa. Nessuno scarto, nessun dubbio,
nessuna segnalazione — e l'errore è certificato.

A dare il verdetto giusto è stato il **terzo canale**: la rilettura del layer-testo, che
sbaglia in un modo **strutturalmente diverso** dagli altri due. L'immagine può sbagliare
sul **glifo** (un simbolo somiglia a un altro). Il layer-testo sbaglia sull'**estrazione**
(perde un carattere, ne inverte l'ordine). Sono guasti che non si sovrappongono: ed è
esattamente per questo che il terzo canale paga.

Il corollario operativo è ruvido: **alzare i DPI non risolve un errore di glifo.** Se il
problema è che due simboli si somigliano, guardarli più da vicino non aiuta — serve
guardarli **da un'altra parte**.

## Episodio due — quando il canale viene dichiarato morto

Il caso opposto, ed è quello che ha prodotto la regola più severa.

Su un articolo con il layer-testo malmesso, il terzo canale è stato dichiarato
**«indisponibile in blocco»** su tutte le pagine con formule. Decisione ragionevole: la
pagina era corrotta sui simboli, sembrava inutile insistere.

Alla verifica successiva, sullo stesso materiale, quel canale è risultato **dirimente su
tre righi su tre**.

Il motivo è che «pagina corrotta sui simboli» non significa «pagina inutile». La corruzione
colpisce i **simboli**; sopravvivono il testo in chiaro, i numeri d'equazione e — soprattutto
— **l'aritmetica interna della fonte**. Buttare la pagina intera per salvare tempo significa
buttare anche quello che era rimasto buono.

Da qui il divieto, scritto com'è giusto che sia scritto un divieto: **è vietato dichiarare
il layer-testo indisponibile in blocco.** L'indisponibilità è **sempre per singolo rigo**,
sempre motivata nel rapporto, mai un'esclusione di canale a priori. Il terzo canale **si
tenta sempre** — anche su una pagina che si è già data per persa.

## L'aritmetica della fonte non è un ripiego

Merita una precisazione, perché è controintuitivo e viene facile capirlo al contrario.

Quando la fonte pubblica un **numero che la formula deve riprodurre** — un valore in
tabella, un esempio applicativo, un risultato numerico — allora **rifare quel conto** vale
come terzo canale. E non è un surrogato di seconda scelta: è il canale **da preferire**.

La ragione è che un conto che torna è una prova di natura diversa da una lettura. Due
letture possono concordare nell'errore, come si è visto. Un'aritmetica che chiude non
concorda con nessuno: **o torna o non torna**, e non le interessa cosa hanno letto gli
altri due.

Con lo stesso spirito, chi estrae confronta ogni formula con le sue **gemelle nella stessa
fonte** — lo stesso termine in un'altra equazione, un caso limite fisico noto — e controlla
che i due membri **bilancino** dimensionalmente prima ancora di scrivere la nota. Sono
canali interni al documento, gratuiti, e sistematicamente sottovalutati.

## E quando nessuno ha un dubbio

C'era un'ultima falla, e stava nella parola *condizionata*.

La terza lettura, in origine, scattava **quando qualcuno aveva un dubbio**: gate con scarto,
verdetto contestato, anomalia visibile. Poi si è visto un caso in cui il gate base aveva
detto «nessuno scarto» — quindi nessun dubbio era nato, quindi la terza lettura non era
scattata — e sotto ci stavano due errori della classe più grave.

La lettura condizionata al dubbio **non scatta proprio nei casi in cui servirebbe**, perché
l'errore silenzioso non genera dubbi. È lo stesso meccanismo della voce
[01](01-the-typo-that-was-not-there.it.md), sotto un altro nome.

Oggi la regola è incondizionata: su ogni nota-formula, il terzo canale **si esegue sempre**,
anche quando il gate non ha trovato nulla. Soprattutto quando il gate non ha trovato nulla.

## Cosa portarsi via

- Due canali che concordano **non sono una conferma**: possono essere lo stesso errore due
  volte.
- Un canale vale in proporzione a **quanto sbaglia in modo diverso** dagli altri, non a
  quanto è accurato da solo.
- Nessun canale è **una verità assoluta** — nemmeno l'immagine ad alta risoluzione, che
  pure è il presidio più forte che abbiamo.
- Un controllo che si attiva **solo in caso di dubbio** è un controllo che manca proprio la
  classe di errori per cui esiste.

---

**Decisioni collegate:** [ADR-0001](../architecture/decisions/0001-formula-verification-from-image.it.md) · [ADR-0005](../architecture/decisions/0005-cost-is-intrinsic-to-quality.it.md)

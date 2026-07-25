# Esempio 01 — una formula che il layer-testo ha rotto in silenzio

Questo è l'esempio di **M1**. Il motore non c'è ancora (è M2), quindi tutto qui è
**riproducibile a mano** con due comandi di `poppler-utils` — niente chiave API, niente
modello, niente account. Quello che la pipeline automatizza si può fare a mano in cinque
minuti e vedere la stessa cosa.

Il punto non è che la pipeline sia intelligente. Il punto è che **il layer-testo perde un
operatore senza dirlo a nessuno**, e che una seconda lettura dall'immagine lo prende.

---

## La fonte

| | |
|---|---|
| **Titolo** | Distributed fiber optic sensors for tunnel monitoring: A state-of-the-art review |
| **Autori** | Xuehui Zhang et al. |
| **Rivista** | Journal of Rock Mechanics and Geotechnical Engineering (2024) |
| **DOI** | [10.1016/j.jrmge.2024.01.008](https://doi.org/10.1016/j.jrmge.2024.01.008) |
| **Licenza** | **CC-BY 4.0** — stampata a pagina 1 dell'articolo e registrata nei metadati Crossref |

Il PDF **non è nel repository** e non ci entrerà mai — vedi la nota sulle fonti nel
[README](../../README.it.md). Scaricalo dal DOI qui sopra: è libero.

> **Una nota sui numeri di pagina.** Questo esempio individua il bersaglio per **dove sta
> nella struttura del documento — §2.1, Eq. (1)** — e tratta il numero di pagina come un
> aiuto alla ricerca, non come un identificativo: l'articolo è circolato prima come *bozza
> corretta* dell'editore, con intestazione `xxx (xxxx) xxx` e una paginazione **non**
> definitiva. Indirizzare un bersaglio per struttura invece che con un numero che cambia fra
> le versioni è la stessa disciplina dell'
> [ADR-0006](../../architecture/decisions/0006-reader-must-not-know-the-expected-answer.it.md).

Nella **versione definitiva pubblicata** (23 pagine), la §2.1 cade a **pagina PDF 2**,
stampata **3842**. I comandi qui sotto usano `-f 2 -l 2`; se la tua copia è la bozza, la
§2.1 sta a pagina PDF 3 e i flag vanno corretti.

---

## Prerequisiti

Un sistema Unix-like (Linux, macOS, WSL) e `poppler-utils` — i due comandi usati sotto,
`pdftotext` e `pdftoppm`, vengono da quel pacchetto:

```bash
sudo apt install poppler-utils     # Debian/Ubuntu
brew install poppler               # macOS
```

Scarica l'articolo dal DOI qui sopra e salvalo in questa cartella come **`paper.pdf`**: è
il nome che i comandi si aspettano.

---

## Canale 1 — il layer-testo

```bash
pdftotext -f 2 -l 2 paper.pdf - | grep -A 4 'relationship can be expressed'
```

Quello che esce:

```
nðT; εÞ ¼ Cε ðε  ε0 Þ þ CT ðT  T0 Þ þ n0 ðT0 ; ε0 Þ
```

Una parte di questo danno è rumorosa e innocua: `ð` per `(`, `Þ` per `)`, `¼` per `=`, `þ`
per `+` — una codifica di font sbagliata che qualunque lettore riconosce all'istante, e che
un modello linguistico ripara correttamente senza esitare.

Due pezzi di danno non sono né rumorosi né innocui:

1. **`ν` è diventato `n`.** Lo scostamento di frequenza di Brillouin è un ni greco. Come `n`
   latino sembra un conteggio, o un indice.
2. **Tutti e due i segni meno sono spariti.** `ðε  ε0 Þ` è `ε`, due spazi, `ε0`. L'operatore
   di sottrazione non è diventato un carattere sbagliato: **ha smesso di esistere**.

È il modo di guasto attorno a cui è costruito il progetto. Niente qui sembra corrotto
abbastanza da meritare un controllo: chi ripara il rumore evidente di `ð`/`Þ`/`¼`/`þ` arriva
a una formula pulita, plausibile, difendibile sul piano dimensionale — e sbagliata.
`C_ε(ε ε₀)` invita a ricostruire un prodotto, o una somma. Entrambi sarebbero silenziosamente
e usabilmente scorretti.

---

## Canale 2 — l'immagine

Rendi la pagina ad alta risoluzione e leggi l'equazione dalla figura, senza guardare cosa ha
prodotto il canale 1:

```bash
pdftoppm -r 400 -f 2 -l 2 -png paper.pdf page
```

L'equazione stampata è:

> **ν(T, ε) = C_ε(ε − ε₀) + C_T(T − T₀) + ν₀(T₀, ε₀)**  (1)

Tutti e due i segni meno ci sono e a 400 dpi non sono ambigui. Nemmeno il `ν` greco lo è.

**Il confronto incrociato:** due letture indipendenti, due differenze — un operatore perso
(due volte) e un simbolo scambiato. Nessuna delle due era stata segnalata da niente: l'uscita
del layer-testo non portava alcun marcatore di danno in quei due punti.

---

## Canale 3 — l'aritmetica interna alla fonte

Le due letture qui sopra sono in disaccordo, e l'immagine è l'evidenza più forte. Ma
*evidenza più forte* non è *prova*, ed è qui che il metodo fa una cosa che una pipeline a due
canali non può fare: chiude la questione **senza guardare nessuna delle due letture**.

L'articolo definisce i propri simboli nella frase subito dopo l'equazione: `ν₀(T₀, ε₀)` è il
BFS **di riferimento** alla temperatura di riferimento `T₀` e alla deformazione di
riferimento `ε₀`.

Ora imponi quella definizione alla formula. Poni `T = T₀` e `ε = ε₀` — la misura *è* il
riferimento. L'equazione deve allora ridursi a `ν = ν₀`, per la definizione che la fonte
stessa dà di `ν₀`. Questo obbliga i primi due termini ad **annullarsi** nel punto di
riferimento:

- con una **differenza**, `C_ε(ε₀ − ε₀) = 0` e `C_T(T₀ − T₀) = 0` → `ν = ν₀` ✅
- con un **prodotto**, `C_ε·ε₀·ε₀ ≠ 0` → il riferimento non è il riferimento ❌
- con una **somma**, `C_ε(ε₀ + ε₀) ≠ 0` → idem ❌

L'operatore mancante può essere solo un meno. Questo è il **terzo canale**: non una terza
lettura, ma il documento che controlla sé stesso. Sbaglia in un modo che gli altri due non
possono — non gli interessa cosa hanno letto gli altri, solo se il conto chiude.

La coerenza dimensionale concorda: ogni termine deve essere una frequenza, quindi `C_ε` è Hz
per unità di deformazione e `C_T` è Hz per grado — che è esattamente ciò che l'articolo dice
che siano.

---

## La nota che ne esce

→ [`notes/dfos-brillouin-frequency-shift.md`](notes/dfos-brillouin-frequency-shift.md)

Una nota atomica: una formula, la provenienza nel frontmatter, e il registro di **quali
canali l'hanno verificata e come**. È quest'ultima parte a fare la differenza fra una nota
che puoi usare e una nota che devi ricontrollare.

---

## Cosa mostra questo esempio — e cosa non mostra

**Mostra:**

- una perdita reale, silenziosa, di un singolo operatore in un layer-testo, su un articolo a
  licenza aperta che chiunque può scaricare;
- che una seconda lettura dall'immagine la prende;
- che un terzo canale, non visivo, può chiuderla in modo indipendente — vedi
  [journal/03](../../journal/03-the-third-channel.it.md).

**Non mostra:**

- un tasso d'errore misurato. Questa è **una formula in un articolo**: una dimostrazione, non
  un benchmark. I benchmark arrivano con M4, e fino ad allora questo repository non cita
  numeri che non sia in grado di riprodurre.
- la pipeline in funzione. Qui non ci sono ancora né il motore né i prompt delle
  funzioni (entrambi M2): questo esempio è volutamente eseguibile a mano, che è anche il modo onesto
  di verificare che il metodo non dipenda da un modello particolare.

---

## Attribuzione

L'equazione e le definizioni dei simboli discusse qui sopra vengono da Zhang, X. et al.
(2024), *Distributed fiber optic sensors for tunnel monitoring: A state-of-the-art review*,
Journal of Rock Mechanics and Geotechnical Engineering,
[doi:10.1016/j.jrmge.2024.01.008](https://doi.org/10.1016/j.jrmge.2024.01.008), usati in
regime [CC-BY 4.0](https://creativecommons.org/licenses/by/4.0/).

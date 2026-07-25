# Contribuire a florilegium

🇬🇧 *This page is also available in [English](CONTRIBUTING.md).*

Grazie dell'interesse. florilegium è, prima di tutto, una **metodologia pubblicata** —
quindi i contributi più preziosi, in questo momento, sono idee, critiche al metodo e
riproduzioni, non solo codice.

## Dove si trova il progetto

Vedi la [Roadmap](ROADMAP.it.md). Oggi il repository è a **M1 — la Storia**: README,
architettura e registri delle decisioni. Il motore eseguibile, i prompt generalizzati e i
benchmark arrivano nelle milestone successive.

## Come proporre una modifica

1. Apri prima una **issue** per discutere qualunque cosa non banale — soprattutto le
   modifiche al metodo o all'architettura.
2. Per testi e documentazione, le pull request piccole e mirate sono le più facili da
   rivedere.
3. Spiega il *perché*, non solo il *cosa*. Questo progetto dà valore al ragionamento: una
   modifica a una decisione dovrebbe leggersi come una breve argomentazione.

## Convenzioni

- **Documentazione bilingue.** L'inglese è la versione canonica; lo specchio italiano porta
  il suffisso `.it.md` (es. `README.md` ↔ `README.it.md`). Lo specchio è **best-effort**:
  può restare indietro, tranne `README` e `ROADMAP`, che si mantengono allineati. Se
  modifichi un file inglese, segnala lo specchio così può recuperare.
- **Le decisioni vanno negli ADR.** Una scelta di progetto significativa si registra in
  `architecture/decisions/` con il template esistente: *Contesto · Ipotesi · Esperimento ·
  Decisione · Conseguenze*. Un ADR può diventare `superseded` — è normale.
- **Le affermazioni devono essere oneste.** I numeri sono etichettati come evidenza
  direzionale oppure come benchmark; le due cose non coincidono. I benchmark controllati
  arrivano con M4.
- **Il diagramma della pipeline vive in quattro file.** Lo stesso flowchart Mermaid è
  duplicato in `README.md`, `README.it.md`, `architecture/overview.md` e
  `architecture/overview.it.md` — GitHub non ha un meccanismo di include, quindi la
  duplicazione è obbligata. **Si toccano tutti e quattro, o nessuno.** Un diagramma che dice
  una cosa diversa dagli altri tre è esattamente la divergenza silenziosa che questo
  progetto esiste per intercettare.

## Due regole ferree

- **Nessun PDF sorgente.** I documenti sorgente (articoli, normative, libri) sono protetti
  da copyright e non vanno mai committati. Gli esempi usano **solo** materiale a licenza
  aperta (es. arXiv CC-BY, o un PDF sintetico).
- **Nessun segreto o dato personale.** Niente chiavi, token, percorsi personali assoluti o
  configurazioni private.

## Licenza

Contribuendo accetti che i tuoi contributi siano licenziati secondo i termini del progetto:
**[Apache-2.0](LICENSE)** per il codice e **CC-BY-4.0** per la documentazione.

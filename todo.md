# Sprint 1 — TODO

## Avant de partir

- [ ] Créer la branche `feature/issue-5-and-6`
- [ ] Commit

```text
Implement MassIVE dataset discovery and metadata indexing
```

- [ ] Push
- [ ] Ouvrir une **Draft Pull Request**

---

# Demain

## Issue #5 — Dataset Discovery

### 5.1 Resume robuste

**Fichier :**

`src/foundation/data/download/downloader.py`

À implémenter :

- [ ] Requête `HEAD`
- [ ] Lire `Content-Length`
- [ ] Comparer avec la taille locale
- [ ] Si tailles identiques → `SKIP`
- [ ] Sinon → supprimer puis retélécharger

---

### 5.2 Retry robuste

**Fichier :**

`src/foundation/data/download/downloader.py`

À implémenter :

- [ ] Retry automatique
- [ ] Backoff exponentiel
- [ ] Gestion du header `Retry-After`
- [ ] Logs :
  - `RETRY`
  - `FAILED`
  - `SKIPPED`

---

### 5.3 Validation

Lancer :

```bash
python scripts/download_dataset.py
```

Tester :

- [ ] `Ctrl+C`
- [ ] Relancer le script

Vérifier :

- [ ] reprise correcte
- [ ] pas de redownload inutile
- [ ] pas de fichiers incomplets

---

## Issue #6 — Metadata Index

### 6.1 CSV idempotent

**Fichier :**

`src/foundation/data/metadata/writer.py`

À implémenter :

- [ ] empêcher les doublons dans `metadata.csv`
- [ ] empêcher les doublons dans `metadata.parquet`

---

### 6.2 Enrichir les métadonnées

**Fichier :**

`src/foundation/data/metadata/extractor.py`

Ajouter :

- [ ] TIC total
- [ ] TIC MS1
- [ ] TIC MS2
- [ ] BPI
- [ ] Nombre total de pics MS1
- [ ] Nombre total de pics MS2
- [ ] Statistiques après seuils :
  - [ ] 1 %
  - [ ] 2 %
  - [ ] 5 %
  - [ ] 10 %
- [ ] Percentiles :
  - [ ] P90
  - [ ] P95
  - [ ] P99

---

### 6.3 Dataset summary

Créer :

- [ ] `dataset_summary.json`

ou

- [ ] `summary.csv`

avec :

- [ ] Nombre de fichiers
- [ ] Taille totale
- [ ] Nombre total de scans
- [ ] Nombre de scans MS1
- [ ] Nombre de scans MS2
- [ ] Statistiques globales

---

# Télécharger le dataset complet

```bash
python scripts/download_dataset.py
```

---

# Vérifications

Nombre de fichiers :

```bash
find /temporary/2025-2026/21316700/lcms-fm/data/MSV000096884 -name "*.mzML" | wc -l
```

Attendu :

```text
826
```

Nombre de lignes du CSV :

```bash
wc -l data/MSV000096884/metadata.csv
```

Attendu :

```text
827
```

(header + 826 fichiers)

---

# Compression

```bash
cd /temporary/2025-2026/21316700/lcms-fm/data/MSV000096884/jzemlin/U19

XZ_OPT="-9e -T0" tar -cJf dataset.tar.xz 20240323_ADRC_serum_mzML_NA_rm
```

---

# Sauvegarde

```bash
cp dataset.tar.xz \
~/projects/lcms-fm/data/MSV000096884/
```

---

# État du Sprint 1

## ✅ Fermées

- [x] #1 Initial project structure
- [x] #2 Development environment
- [x] #3 Hydra configuration
- [x] #4 Architecture documentation

---

## 🟡 Issue #5 — Implement dataset discovery (~90 %)

### Fait

- [x] Parser `params.xml`
- [x] Génération des URLs MassIVE
- [x] Téléchargement HTTPS
- [x] Organisation des dossiers
- [x] Logging
- [x] Retry (v1)

### Reste

- [ ] Resume basé sur `Content-Length`
- [ ] Validation des téléchargements
- [ ] Nettoyage des fichiers incomplets

---

## 🟡 Issue #6 — Create dataset metadata index (~75 %)

### Fait

- [x] Extraction pyOpenMS
- [x] `metadata.csv`
- [x] `metadata.parquet`
- [x] Extraction pendant le téléchargement

### Reste

- [ ] Éviter les doublons
- [ ] Ajouter les statistiques scientifiques
- [ ] Générer un résumé global du dataset

---

# Prochaines issues

- [ ] #7 Benchmark des bibliothèques mzML
- [ ] #8 Preprocessing design
- [ ] #9 Tests
- [ ] #10 Logging global
- [ ] #11 CI
- [ ] #12 Documentation
- [ ] #13 Documentation
- [ ] #14 Documentation

---

# Objectif de demain

- [ ] Fermer les issues #5 et #6
- [ ] Télécharger les 826 fichiers mzML
- [ ] Générer un index complet des données
- [ ] Créer `dataset.tar.xz`
- [ ] Préparer le Sprint 2 (PyTorch Dataset + Foundation Model)

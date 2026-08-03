# Project Architecture

## Overview

This repository is organized around four main components:

- `configs/` : Hydra configuration files.
- `scripts/` : executable entry points.
- `src/foundation/` : reusable Python package.
- `data/` : datasets (never committed).

---

## Repository Layout

```
configs/
data/
docs/
notebooks/
scripts/
src/
tests/
```

---

## configs/

Hydra configuration tree.

Contains experiment, preprocessing, optimizer, model and runtime configuration.

---

## data/

Contains LC-MS datasets.

Ignored by Git.

---

## scripts/

Executable entry points.

Examples:

- train.py
- discover_dataset.py
- index_dataset.py

---

## src/foundation/

Main Python package.

Contains:

- data/
- models/
- training/
- evaluation/
- utils/

---

## notebooks/

Exploration only.

Never imported by the package.

---

## tests/

Unit and integration tests.

---

## docs/

Project documentation.

Architecture, roadmap and design decisions.

# Amazon Top 50 Bestselling Books (2009–2019) — Exploratory Data Analysis

An exploratory data analysis and market intelligence project examining a decade of Amazon bestselling books to extract actionable consumer trends, pricing dynamics, and author market share.

[![Kaggle Notebook](https://img.shields.io/badge/Kaggle-Notebook-20BEFF?logo=kaggle&logoColor=white)](https://www.kaggle.com/code/lazer999/top-selling-books-amazon)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Python 3.10+](https://img.shields.io/badge/Python-3.10+-blue.svg?logo=python&logoColor=white)](https://www.python.org/downloads/)
[![Field](https://img.shields.io/badge/Field-Exploratory%20Data%20Analysis%20/%20Business%20Intelligence-brightgreen)](#)

---

## Table of Contents
- [Project Overview](#project-overview)
- [Key Highlights & Results](#key-highlights--results)
- [System Architecture & Workflow](#system-architecture--workflow)
- [Repository Structure](#repository-structure)
- [Quickstart & Reproduction](#quickstart--reproduction)
- [Dataset Details](#dataset-details)
- [Author & Acknowledgments](#author--acknowledgments)

---

## Project Overview

This repository provides the complete, production-structured implementation of the **[Amazon Top 50 Bestselling Books (2009–2019) — Exploratory Data Analysis](https://www.kaggle.com/code/lazer999/top-selling-books-amazon)** project originally published on Kaggle. 

The primary focus of this work is translating complex data into actionable machine learning solutions using disciplined data engineering, rigorous validation strategies, and clean, leak-free preprocessing pipelines.

---

## Key Highlights & Results

- Analyzed 550 bestselling titles across 10 years of commercial performance.
- Fiction vs. Non-Fiction segmentation: pricing elasticity, average user review scores, and count distributions.
- Author dominance ranking identifying prolific bestsellers (Jeff Kinney, Rick Riordan, J.K. Rowling).
- Temporal trend evaluation revealing year-over-year pricing shifts and consumer rating dynamics.

---

## System Architecture & Workflow

The pipeline follows a structured, modular execution path:

```mermaid
flowchart LR
    A[Amazon Bestsellers Dataset] --> B[Data Cleansing & Type Casting]
    B --> C[Genre Segmentation: Fiction vs Non-Fiction]
    C --> D[Longitudinal Trend Analysis: 2009-2019]
    D --> E[Price Elasticity & Rating Studies]
    E --> F[Publishing Market Intelligence]
```

---

## Repository Structure

```plaintext
amazon-bestselling-books-eda/
├── notebooks/
│   └── amazon-bestselling-books-eda.ipynb      # Original Jupyter notebook with full exploratory visuals
├── src/
│   └── main.py                # Modular, executable Python pipeline
├── .gitignore                 # Standard Python/Jupyter ignores
├── LICENSE                    # MIT License
├── README.md                  # Human-friendly documentation
└── requirements.txt           # Verified Python dependencies
```

---

## Quickstart & Reproduction

### 1. Clone the Repository
```bash
git clone https://github.com/musaoc/amazon-bestselling-books-eda.git
cd amazon-bestselling-books-eda
```

### 2. Set Up a Virtual Environment
```bash
# Linux / macOS
python3 -m venv venv
source venv/bin/activate

# Windows
python -m venv venv
.\venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### 4. Run the Pipeline
You can run the end-to-end script directly:
```bash
python src/main.py
```

Or open and run the interactive notebook:
```bash
jupyter lab notebooks/amazon-bestselling-books-eda.ipynb
```

---

## Dataset Details

- **Dataset / Competition**: [Amazon Top 50 Bestselling Books 2009-2019](https://www.kaggle.com/datasets/sootersaalu/amazon-top-50-bestselling-books-2009-2019)
- **Origin Platform**: Kaggle
- For automated dataset downloading via Kaggle CLI:
  ```bash
  kaggle datasets download -d sootersaalu/amazon-top-50-bestselling-books-2009-2019
  ```

---

## Author & Acknowledgments

- **Author**: **Muhammad Musa Khan** (Kaggle Master)
- **Kaggle Profile**: [@lazer999](https://www.kaggle.com/lazer999)
- **GitHub**: [@musaoc](https://github.com/musaoc)
- **Original Kaggle Solution**: [Amazon Top 50 Bestselling Books (2009–2019) — Exploratory Data Analysis](https://www.kaggle.com/code/lazer999/top-selling-books-amazon)

If you found this project helpful or insightful, please consider starring the repository ⭐!

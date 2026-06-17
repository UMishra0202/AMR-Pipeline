## Overview

This project implements a bioinformatics workflow for processing antimicrobial resistance (AMR) gene sequences stored in FASTA format.

The pipeline currently performs:

- FASTA sequence parsing
- Sequence length analysis
- Summary statistics generation
- Command-line execution using Python

The repository is being developed incrementally and will be expanded to include additional AMR sequence analysis features.

---

## Project Structure

AMR-Pipeline/

├── data/
│ └── sample.fasta

├── scripts/
│ └── fasta_stats.py

├── README.md

└── .gitignore

---

## Input Data

The pipeline currently uses a FASTA file containing representative antimicrobial resistance genes:

* blaTEM_1
* blaSHV_1
* blaCTXM_1

---

## Current Features

### FASTA Statistics Script

The script:

* Reads FASTA files
* Counts sequences
* Calculates sequence lengths
* Identifies longest sequence
* Identifies shortest sequence
* Computes average sequence length

---

## Usage

Run:

python scripts/fasta_stats.py

---

## Example Output

Sequence Summary

blaTEM_1: 108 bp

blaSHV_1: 87 bp

blaCTXM_1: 26 bp

Overall Statistics

Number of sequences: 3

Longest sequence: 108

Shortest sequence: 26

Average length: 73.67

---

## Technologies Used

* Python 3
* Linux Command Line
* Git
* GitHub
* FASTA File Format

---

## Future Development

Planned improvements include:

* GC content calculation
* Sequence quality checks
* AMR gene summary reports
* Results export to text files
* Data visualization
* Integration of real AMR datasets

---

## Author

Utkarsh Mishra

M.Tech Bioinformatics

Delhi Technological University (DTU)


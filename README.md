\# Bioinformatics Project: Healthy vs Breast Cancer Classification



\## Project Purpose

This project analyzes FASTQ sequencing data to distinguish between healthy individuals and breast cancer patients using GC content and quality scores.



\## Dataset

\- 5 FASTQ files total

\- Cancer: cancer.fastq, cancer2.fastq, cancer3.fastq (3 files)

\- Healthy: healthy.fastq, healthy2.fastq (2 files)



\## Results

| Sample | Class | GC% | Quality |

|--------|-------|-----|---------|

| cancer.fastq | Cancer | 50.76 | 36.83 |

| cancer2.fastq | Cancer | 50.44 | 36.55 |

| cancer3.fastq | Cancer | 50.59 | 36.89 |

| healthy.fastq | Healthy | 49.03 | 34.63 |

| healthy2.fastq | Healthy | 56.01 | 36.51 |



\## Quick Start

python -m venv bioinfo\_env

bioinfo\_env\\Scripts\\activate

pip install -r requirements.txt

python parse\_fastq\_fast.py



\## Dataset Source

Data provided from sequencing experiment.



\## Repository

https://github.com/mariiamhosny/bioinformatics\_project


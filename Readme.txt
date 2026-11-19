###LiMiT — Linker Multi-condition Iterative Screening Tool

A molecular linker design tool built with RDKit + PyQt5.

Quick Start

conda env create -f environment.yml

conda activate my-rdkit-env

python LiMIt_4.1_en.py

###Required Files

Place these two files in the same directory as LiMIt_cn.py:

fpscores.pkl.gz — fingerprint scores
linker-f-smiles_new_202609.xlsx — linker fragment library (SMILES)

Warning: Missing either file will cause the program to fail.

Environment: Python 3.10 · RDKit 2022.03.5 · PyQt5

LiMIt is protected by Patent CN117373562A (owned by Zhuhai Hengqin Haomai Technology Co., Ltd) and is available for academic and non-commercial use only.


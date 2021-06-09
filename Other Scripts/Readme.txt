README

The files in this directory represent the scripts required to support the generation of microbiome abundance data using Qiime2.

1. The 16S amplification primers were removed using the primertrim.py script which uses Cutadapt and requires the 16Sprimers.txt file.

2. The QCreports.py script will generate quality report files (using FastQC) for all fast data in a directory.

3. Trimming of the fastq data using the QCtrimming.smk Snakemake workflow file.

4. Manifest.py automatically generates a manifest file for Qiime2 data importation.
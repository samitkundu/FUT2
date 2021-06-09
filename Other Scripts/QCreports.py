"""Script for running Fastqc to generate QC reports on all fastq data in a folder.
Fastq files are assumed to be gzipped
"""

import subprocess
import glob
import argparse
import os

parser = argparse.ArgumentParser(description='Generate quality reports for multiple files (Fastqc must be installed). ".fq.gz" is assumed to be the file suffix')
parser.add_argument("--threads", default=1, required=False, type=str, help="number of threads")
args = parser.parse_args()
td = args.threads

os.mkdir('QCReports')
for fq in glob.glob("*.fq.gz"):
    qcargs = ['fastqc', fq, "-t", td, "-o", 'QCReports']
    subprocess.call(qcargs)

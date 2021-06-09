"""Script for trimming primer sequences from paired end read data.
"""
#include extra argument for primer file (including it's path) and make multithreaded
import subprocess
import glob
import argparse
import sys
import itertools

parser = argparse.ArgumentParser(description='16S primer trimming')
parser.add_argument("--primers", required=True, type=str, help="comma delimited list of primers")
args = parser.parse_args()
pl = args.primers

primer = []
primer_seq = []
primer_dir = []

primer_file = open("16Sprimers.txt","r")
for row in primer_file.readlines():
    row = row.rstrip()
    l_row = row.split("\t")
    primer.append(l_row[0])
    primer_seq.append(l_row[1])
    primer_dir.append(l_row[2])

primer_s_dict = dict(zip(primer,primer_seq))
primer_dict = dict(zip(primer,primer_dir))

primer_list = pl.split(",")

inp_f = []
inp_r = []
for p in primer_list:
    try:
        p_dir = primer_dict[p]
        p_seq = primer_s_dict[p]
        if p_dir == 'r':
            inp_r.append(p_seq)
        else:
            inp_f.append(p_seq)
    except KeyError:
        print('primer not found in primer file')
        sys.exit()

f_count_p = len(inp_f)
f_com = ['-g']*f_count_p
f_iters = [iter(f_com), iter(inp_f)]
fwd_fin_comm = list(it.next() for it in itertools.cycle(f_iters))

r_count_p = len(inp_r)
r_com = ['-g']*r_count_p
r_iters = [iter(r_com), iter(inp_r)]
rev_fin_comm = list(it.next() for it in itertools.cycle(r_iters))

fwd_seq_files = glob.glob("*R1.fastq")
rev_seq_files = glob.glob("*R2.fastq")

for fd in fwd_seq_files:
    print(fd)
    id_f = fd[:-6]
    outname = 'ptrim_' + id_f + '.fastq'
    ftrim_args = ['cutadapt'] + fwd_fin_comm + ['-o', outname, fd]
    subprocess.call(ftrim_args)

for rv in rev_seq_files:
    print(rv)
    id_r = rv[:-6]
    outname = 'ptrim_' + id_r + '.fastq'
    rtrim_args = ['cutadapt'] + rev_fin_comm + ['-o', outname, rv]
    subprocess.call(rtrim_args)

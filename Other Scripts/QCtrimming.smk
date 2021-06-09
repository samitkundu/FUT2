import glob
SAMPLES = []
for s in glob.glob("*-R1.fastq"):
    sample_name = s[:-9]
    SAMPLES.append(sample_name)

rule all:
    input:
        expand("{sample}-R1_val_1.fq", sample=SAMPLES),
        expand("{sample}-R2_val_2.fq", sample=SAMPLES)

rule trim:
    input:
        rdf="{sample}-R1.fastq",
        rdr="{sample}-R2.fastq"
    output:
        fwd="{sample}-R1_val_1.fq",
        rev="{sample}-R2_val_2.fq"
    shell:
        "TrimGalore --paired {input.rdf} {input.rdr} --quality 20"

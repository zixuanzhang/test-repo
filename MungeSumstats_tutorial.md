### Install on HPC

#### Switch to conda compiler

If you have file `~/.R/Makevar` configured based on mancusolab github
[HPC.md](https://github.com/mancusolab/LabInfo/blob/main/HPC.md) page,
please move this file outside `~/.R` such that R will use conda
compiler. Log off and back on to start a new cluster session when you
done so.

If you have R installed in current env, type in command line
`R CMD config CC` to check and see the output should be:
x86_64-conda-linux-gnu-cc

#### Create new env

1.  Create a new conda env by: `conda create --name gwas_munge`

2.  Activate this env: `conda activate gwas_munge`

3.  Use conda to install MungeSumstats:
    `conda install -c bioconda bioconductor-mungesumstats`

Note: No need to install R in this env by yourself because R with the
correct dependency version will be handled implicitly by above conda
command

1.  Start R session and try load: `library(MungeSumstats)`

**Tips**:

-   Downloading data from web need internet access so we can only do so
    on login node.

-   I recommend to stick with one package manager: either BiocManager or
    conda. For example, Install other R packages using conda such that
    conda can manage the environment consistently (although not sure if
    anything will break if cross using)

-   Several repetitive installing and removing of env can disrupt conda
    installing (eg. installed R corrupted or other failure). You can try
    cleaning up all unused packages and cache by `conda clean -a`
    (**Warning**: this can be life saver or devil). Just to be safe, I
    highly recommend output each of your existing env to env.yml file
    for future restore.

#### Install human reference genome (on login node)

MungeSumstats need this to format gwas files. So we can install
GRCh37/hg19 and GRCh38/hg38 using:

-   `conda install -c bioconda bioconductor-snplocs.hsapiens.dbsnp144.grch38`

-   `conda install -c bioconda bioconductor-bsgenome.hsapiens.ncbi.grch38`

-   `conda install -c bioconda bioconductor-snplocs.hsapiens.dbsnp144.grch37`

-   `conda install -c bioconda bioconductor-bsgenome.hsapiens.1000genomes.hs37d5`

### Standardize GWAS sumstats format

vignette:
<https://neurogenomics.github.io/MungeSumstats/articles/MungeSumstats.html>

### Work with Open Gwas (Download GWAS data)

vignette:
<https://bioconductor.org/packages/release/bioc/vignettes/MungeSumstats/inst/doc/OpenGWAS.html>

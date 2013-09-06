Identify Immune Cell Genes
==========================
So this is just a microarray analysis
-------------------------------------


A standalone repository to make publically available a microarray analysis for identifying immune-related genes in Affymextrix Mouse 2.0 Microarrays. Cell types involved are Th1, Th2, Th17, and Tfh.


0. Quickstart
-------------

Virtual Machine and provisioning files are provided to provide identical computation environment for re-computing this analysis. Script `run.sh` automates the running of the three scripts.


1. More Information
-------------------

All datasets were publically available and taken from [GEO Omnibus][geo]. After data-normalization to prevent bias across arrays, Testing consists of independent sample T-tests for each cell type.


2. References
-------------

 - [An Opinionated Guide to Microarray Analysis][ogma]
 - [Global mapping of H3K4me3 and H3K27me3 reveals specificity and plasticity in lineage fate determination of differentiating CD4+ T cells.][tcell]
 - [Germinal center T follicular helper cell IL-4 production is dependent on signaling lymphocytic activation molecule receptor (CD150).][tfh]


3. Authors
----------

 - [Andy Chiang][andy] (Columbia University)
 - Rebecca Mathew (The University of Chicago)



[geo]: http://www.ncbi.nlm.nih.gov/geo/
[tfh]: http://www.ncbi.nlm.nih.gov/pubmed/20525889
[andy]: http://www.andy-chiang.com
[ogma]: http://discover.nci.nih.gov/microarrayAnalysis/Microarray.Home.jsp
[tcell]: http://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE14308
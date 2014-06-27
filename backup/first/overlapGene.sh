windowBed -a non-targeting/non-targeting_exp.bed -b repeat/ell3_filtered_ERVK.bed -w 1000 -u |closestBed -a stdin -b mm9genes.bed -d -t first|cut -f1,2,3,4,8,9,11|sort -k7 -g >temp
windowBed -a transcript/ell3RawERVK_knock.tab -b transcript/ell3RawERVK_nt.tab -w 1 |cut -f1-4,11-14 >temp

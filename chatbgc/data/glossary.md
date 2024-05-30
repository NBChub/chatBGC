# Protocluster Types

antiSMASH uses some abbreviations internally and in outputs to refer to the different
types of secondary metabolite clusters detected.

There are three strictness levels for cluster detection: strict, relaxed, and loose.
Each level includes the more strict levels.
The types of cluster within each ruleset are given below:

## Current Types


### Strict
|Label|Description|Added|Last updated|
|-----|-----------|:---:|:----------:|
|2dos|2-deoxy-streptamine aminoglycoside|7.0|7.0|
|acyl_amino_acids|N-acyl amino acid|4.0|4.1|
|amglyccycl|Aminoglycoside/aminocyclitol|&lt;= 3.0|&lt;= 3.0|
|aminocoumarin|Aminocoumarin|&lt;= 3.0|&lt;= 3.0|
|aminopolycarboxylic-acid|Aminopolycarboxylic acid metallophores (doi:10.1039/C8MT00009C)|7.0|7.0|
|archaeal-RiPP|Archaeal RiPPs (doi:10.1021/jacs.2c00521 supplemental)|7.1|7.1|
|arylpolyene|Aryl polyene|&lt;= 3.0|&lt;= 3.0|
|betalactone|Beta-lactone containing protease inhibitor|5.0|5.0|
|blactam|&beta;-lactam|&lt;= 3.0|&lt;= 3.0|
|bottromycin|Bottromycin|&lt;= 3.0|&lt;= 3.0|
|butyrolactone|Butyrolactone|&lt;= 3.0|&lt;= 3.0|
|CDPS|tRNA-dependent cyclodipeptide synthases|5.0|5.0|
|crocagin|Crocagin-like|7.0|7.0|
|cyanobactin|Cyanobactins like patellamide (AY986476)|&lt;= 3.0|7.0|
|cyclic-lactone-autoinducer|agrD-like cyclic lactone autoinducer peptides (AF001782)|6.0|6.0|
|darobactin|Darobactin-like compounds|7.1|7.1|
|ectoine|Ectoine|&lt;= 3.0|&lt;= 3.0|
|epipeptide|D-amino-acid containing RiPPs such as yydF (D78193)|6.0|6.0|
|fungal-RiPP|Fungal RiPP with POP or UstH peptidase types and a modification|5.0|5.0|
|furan|Furan|&lt;= 3.0|5.0|
|glycocin|Glycocin|&lt;= 3.0|&lt;= 3.0|
|guanidinotides|Pheganomycin-style protein ligase-containing cluster|4.0|6.0|
|hglE-KS|Heterocyst glycolipid synthase-like PKS|5.0|5.0|
|HR-T2PKS|Highly reducing type II PKS like ishigamide and skyllamycin|7.1|7.1|
|hserlactone|Homoserine lactone|&lt;= 3.0|&lt;= 3.0|
|hydrogen-cyanide|Hydrogen cyanide (AF208523, doi:10.1128/jb.182.24.6940-6949.20)|7.1|7.1|
|HR-T2PKS|Highly reducing type II PKS like ishigamide and skyllamycin|7.1|7.1|
|indole|Indole|&lt;= 3.0|4.0|
|isocyanide|Isocyanides (doi:10.1093/nar/gkad573)|7.1|7.1|
|NRP with isocyanide|Isocyanides (doi:0.1128/mBio.00785-18)|7.1|7.1|
|LAP|Linear azol(in)e-containing peptides|&lt;= 3.0|6.0|
|ladderane|Ladderane|&lt;= 3.0|7.1|
|lanthipeptide class I|Class I lanthipeptides like nisin|4.2|6.0|
|lanthipeptide class II|Class II lanthipeptides like mutacin II (U40620)|4.2|6.0|
|lanthipeptide class III|Class III lanthipeptides like labyrinthopeptin (FN178622)|4.2|6.0|
|lanthipeptide class IV|Class IV lanthipeptides like venezuelin (HQ328852)|4.2|6.0|
|lanthipeptide class V|Glycosylated lanthipeptide/linaridin hybrids like MT210103|5.1|6.0|
|lassopeptide|Lasso peptide|&lt;= 3.0|5.0|
|linaridin|Linear arid peptide such as cypemycin (HQ148718) and salinipeptin (MG788286)|&lt;= 3.0|&lt;= 3.0|
|lipolanthine|Lanthipeptide class containing N-terminal fatty acids such as MG673929|5.0|5.0|
|melanin|Melanin|&lt;= 3.0|&lt;= 3.0|
|methanobactin|Copper-chelating/transporting peptides (doi:10.1126/science.aap9437)|7.0|7.0|
|microviridin|Microviridin|&lt;= 3.0|&lt;= 3.0|
|mycosporine-like|Molecules containing mycosporine-like amino acid|7.0|7.0|
|NAGGN|N-acetylglutaminylglutamine amide|5.0|5.0|
|NAPAA|Non-alpha poly-amino acids like e-Polylysin|6.0|7.0|
|NI-siderophore|NRPS-independent, IucA/IucC-like siderophores (*siderophore* prior to 7.0)|7.0|7.1|
|NRPS|Non-ribosomal peptide synthetase|&lt;= 3.0|6.0|
|NRP-metallophore|Non-ribosomal peptide metallophores|7.0|7.0|
|nucleoside|Nucleoside|&lt;= 3.0|5.0|
|oligosaccharide|Oligosaccharide|&lt;= 3.0|&lt;= 3.0|
|opine-like-metallophore|Opine-like zincophores like staphylopine (doi:10.1128/mSystems.00554-20)|7.0|7.0|
|other|Cluster containing a secondary metabolite-related protein that does not fit into any other category|4.0|5.0|
|PBDE|Polybrominated diphenyl ether|4.1|4.1|
|phenazine|Phenazine|&lt;= 3.0|&lt;= 3.0|
|phosphoglycolipid|Phosphoglycolipid|&lt;= 3.0|&lt;= 3.0|
|phosphonate|Phosphonate|&lt;= 3.0|7.0|
|PpyS-KS|PPY-like pyrone|4.2|4.2|
|prodigiosin|Serratia-type non-traditional PKS prodigiosin biosynthesis pathway|6.0|6.0|
|proteusin|Proteusin|&lt;= 3.0|&lt;= 3.0 |
|PUFA|Polyunsaturated fatty acid|&lt;= 3.0|&lt;= 3.0|
|pyrrolidine|Pyrrolidines like described in BGC0001510|6.0|6.0|
|ranthipeptide|Cys-rich peptides (aka. SCIFF: six Cys in fourty-five) like in CP001581:3481278-3502939|6.0|6.0|
|RaS-RiPP|Streptide-like thioether-bond RiPPs|5.0|5.0|
|RCDPS|Fungal Arginine-containing cyclic dipeptides|7.0|7.0|
|redox-cofactor|Redox-cofactors such as PQQ (NC_021985:1458906-1494876)|6.0|6.0|
|resorcinol|Resorcinol|&lt;= 3.0|&lt;= 3.0|
|saccharide|Saccharide (loose strictness, likely from primary metabolism)|&lt;= 3.0|&lt;= 3.0|
|sactipeptide|Sactipeptide|&lt;= 3.0|6.0|
|spliceotide|RiPPs containing plpX type spliceases (NZ_KB235920:17899-42115)|6.0|6.0|
|T1PKS|Type I PKS (Polyketide synthase)|&lt;= 3.0|&lt;= 3.0|
|T2PKS|Type II PKS|&lt;= 3.0|5.0|
|T3PKS|Type III PKS|&lt;= 3.0|&lt;= 3.0|
|terpene|Terpene|&lt;= 3.0|4.1|
|thioamitides|Thioamitide RiPPs as found in JOBF01000011|5.1|6.0|
|thioamide-NRP|Thioamide-containing non-ribosomal peptide|5.0|5.0|
|thiopeptide|Thiopeptide|4.2|5.0|
|transAT-PKS|Trans-AT PKS|&lt;= 3.0|5.0|
|triceptide|Triceptides|7.1|7.1|
|tropodithietic-acid|Tropodithietic acid|5.0|5.0|

### Relaxed
|Label|Description|Added|Last updated|
|-----|-----------|:---:|:----------:|
|fungal-RiPP-like|Fungal RiPP-likes|7.0|7.0|
|NRPS-like|NRPS-like fragment|5.0|5.0|
|phosphonate-like|Phosphonate-like (prior to 7.0 this was the phosphonate rule)|7.0|7.0|
|PKS-like|Other types of PKS|5.0|5.0|
|RiPP-like|Other unspecified ribosomally synthesised and post-translationally modified peptide product (RiPP)|4.1|7.1|
|RRE-containing|RRE-element containing cluster|6.0|6.0|
|transAT-PKS-like|Trans-AT PKS fragment, with trans-AT domain not found|&lt;= 5.0|5.0|

### Loose
|Label|Description|Added|Last updated|
|-----|-----------|:---:|:----------:|
|fatty_acid|Fatty acid (loose strictness, likely from primary metabolism)|&lt;= 3.0|4.2|
|halogenated|Halogenase-containing cluster, potentially generating a halogenated product|5.0|5.0|


## Obsolete / Previous Types

|Label|Description|Added|Removed|Notes|
|-----|-----------|:---:|:-----:|-----|
|siderophore|Siderophore|&lt;= 3.0|7.0|Renamed to *NI-siderophore*|
|bacteriocin|Bacteriocin or other unspecified ribosomally synthesised and  post-translationally modified peptide product (RiPP)|4.1|6.0|Renamed to *RiPP-like*|
|fused|Pheganomycin-style protein ligase-containing cluster|4.0|6.0|Renamed to *guanidinotides*|
|head_to_tail|Head-to-tail cyclised RiPP (subtilosin-like)|&lt;= 3.0|6.0|Merged into *sactipeptides*|
|lanthidin|Glycosylated lanthipeptide/linaridin hybrids like MT210103|5.1|6.0|Renamed to *lanthipeptide class V*|
|lanthipeptide|Lanthipeptides|4.2|6.0|Split into subclasses, e.g. *lanthipeptide class I*|
|TfuA-related|TfuA-related RiPPs|5.1|6.0|Renamed to *thioamitides*|
|otherks|Other types of PKS|&lt;= 3.0|5.0|Split into *PKS-like* and *hglE-KS*|
|microcin|Microcin|&lt;= 3.0|5.0|Merged into *lasso peptide*|
|cf_saccharide|Possible saccharide|&lt;= 3.0|5.0|Renamed to *saccharide*|
|cf_fatty_acid|Possible fatty acid|&lt;= 3.0|5.0|Renamed to *fatty_acid*|
|cf_putative|Putative cluster of unknown type identified  with the ClusterFinder algorithm|&lt;= 3.0|5.0|These predictions are now subregions, not clusters|

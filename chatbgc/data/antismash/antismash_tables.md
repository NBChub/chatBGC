# AntiSMASH DuckDB Database Documentation
This documentation describes the table in the duckDB antiSMASH database.
It covers the structure and purpose of each table and column in the database schema, making it easier to understand and use the database for querying and analysis.

## Table: antismash.as_domain_profiles
This table stores information about domain profiles.
A functional secondary metabolite domain profile predicted by antiSMASH.

- **as_domain_profile_id**: Identifier for the domain profile.
- **name**: Name of the domain profile.
- **description**: Description of the domain profile.
- **DATABASE**: Database associated with the domain profile.
- **TYPE**: Type of the domain profile.

## Table: antismash.as_domain_subtypes
This table stores information about domain subtypes.
Possible subtypes of domains predicted by antiSMASH, e.g. TransAT-KS.

- **subtype**: Identifier for the domain subtype.
- **description**: Description of the domain subtype.

## Table: antismash.bgc_categories
This table stores information about BGC categories.
Biosynthetic gene cluster categories according to MIBiG spec.

- **category**: Identifier for the BGC category. Values could be pks, nrps, ripp, terpene, saccharide, alkaloid, or other.
- **description**: Description of the BGC category. The following are the categories and its description: 'pks' is 'Polyketide', 'nrps' is 'Nonribosomal peptide', 'ripp' is 'Ribosomally synthesized and post-translationally modified peptide', 'terpene' is 'Terpene', 'saccharide' is'Saccharide', 'alkaloid' is 'Alkaloid', and 'other' is 'Other'.

## Table: antismash.candidate_types
This table stores information about candidate types.
Candidate cluster types as used by antiSMASH.

- **candidate_type_id**: Identifier for the candidate type.
- **description**: Description of the candidate type. Can be 'chemical hybrid', 'interleaved', 'neighbouring', or 'single'.

## Table: antismash.clusterblast_algorithms
This table stores information about clusterblast algorithms.
Available *ClusterBlast algorithms.

- **algorithm_id**: Identifier for the algorithm.
- **name**: Name of the algorithm. Value could be 'clusterblast','knownclusterblast', or 'subclusterblast'.


## Table: antismash.comparippson_mibig_references
This table stores references to MIBIG entries used in comparative analysis.

- **comparippson_mibig_id**: Identifier for the MIBIG reference.
- **accession**: Accession number of the MIBIG entry.
- **name**: Name of the MIBIG entry.
- **product**: Product associated with the MIBIG entry.
- **compound**: Compound associated with the MIBIG entry.

## Table: antismash.filenames
This table stores information about filenames associated with assemblies.
Tracking a number of interesting filenames for an assembly id.

- **assembly_id**: Identifier for the assembly.
- **base_filename**: Base filename for the assembly.

## Table: antismash.functional_classes
This table stores information about functional classes.
An index of possible functional classes.

- **functional_class_id**: Identifier for the functional class.
- **name**: Name of the functional class. Values for basic functional classes are 'biosynthetic', 'regulator', 'transporter', or 'other'. Advanced classes are 'bgc_seed' and 'biosynthetic_smcog', which are the child of parent class 'biosynthetic'.
- **parent_id**: Identifier for the parent functional class, if applicable.

## Table: antismash.gene_ontologies
This table stores information about gene ontologies.

- **go_id**: Identifier for the gene ontology.
- **identifier**: Unique identifier for the gene ontology.
- **description**: Description of the gene ontology.

## Table: antismash.module_domain_functions
This table stores information about functions associated with module domains in table antismash.modules.

- **function_id**: Identifier for the function.
- **FUNCTION**: Description of the function. Values could be 'starter','loader', 'carrier_protein', 'modification', 'finalisation', or 'other'.

## Table: antismash.pfams
This table stores information about Pfam entries.
pfam domain metadata.

- **pfam_id**: Identifier for the Pfam entry.
- **name**: Name of the Pfam entry.
- **description**: Description of the Pfam entry.
- **trusted_cutoff**: Trusted cutoff value for the Pfam entry.

## Table: antismash.profiles
This table stores information about HMM profiles.
HMM profiles used during cluster detection.

- **name**: Name of the profile.
- **description**: Description of the profile.
- **cutoff**: Cutoff value for the profile.
- **filename**: Filename associated with the profile.

## Table: antismash.regulators
This table stores information about regulators, part of the antiSMASH TFBS (transcription factor binding site) finder feature.

- **regulator_id**: Identifier for the regulator.
- **name**: Name of the regulator.
- **description**: Description of the regulator.

## Table: antismash.regulator_confidence
This table stores information about regulator confidence levels, part of the antiSMASH TFBS (transcription factor binding site) finder feature.

- **confidence_id**: Identifier for the confidence level.
- **name**: Name of the confidence level. Can be 'weak', 'medium', or 'strong'.
- **strength**: Strength of the confidence level.

## Table: antismash.resfams
This table stores information about Resfam entries.

- **resfam_id**: Identifier for the Resfam entry.
- **accession**: Accession number of the Resfam entry.
- **name**: Name of the Resfam entry.
- **description**: Description of the Resfam entry.

## Table: antismash.sampling_sites
This table stores information about sampling sites.
A site where a biological sample was taken.

- **site_id**: Identifier for the sampling site.

## Table: antismash.substrates
This table stores information about substrates.

- **substrate_id**: Identifier for the substrate.
- **name**: Name of the substrate.
- **description**: Description of the substrate.

## Table: antismash.t2pks_products
This table stores information about T2PKS products.

- **product_type**: Type of the product.
- **product_function**: Function of the product.

## Table: antismash.t2pks_profiles
This table stores information about T2PKS profiles.

- **profile_id**: Identifier for the profile.
- **name**: Name of the profile.
- **description**: Description of the profile.

## Table: antismash.taxa
This table stores NCBI taxonomic classification information.

- **tax_id**: Identifier for the taxonomic entry.
- **ncbi_taxid**: NCBI taxonomic identifier.
- **superkingdom**: Superkingdom classification.
- **kingdom**: Kingdom classification.
- **phylum**: Phylum classification.
- **class**: Class classification.
- **taxonomic_order**: Order classification.
- **family**: Family classification.
- **genus**: Genus classification.
- **species**: Species classification.
- **strain**: Strain classification.
- **name**: Name of the taxonomic entry.

## Table: antismash.tigrfams
This table stores information about TIGRFAM entries.
tigrfam domain metadata.

- **tigrfam_id**: Identifier for the TIGRFAM entry.
- **name**: Name of the TIGRFAM entry.
- **description**: Description of the TIGRFAM entry.
- **trusted_cutoff**: Trusted cutoff value for the TIGRFAM entry.

## Table: antismash.bgc_types
This table stores information about BGC types.
Biosynthetic gene cluster types.

- **bgc_type_id**: Identifier for the BGC type.
- **term**: Term associated with the BGC type.
- **description**: Description of the BGC type.
- **category**: Category associated with the BGC type.

## Table: antismash.monomers
This table stores information about monomers.

- **monomer_id**: Identifier for the monomer.
- **substrate_id**: Identifier for the substrate associated with the monomer.
- **name**: Name of the monomer.
- **description**: Description of the monomer.

## Table: antismash.rel_as_domain_to_subtype
This table stores relationships between domain subtypes and domains.
Relationships between a specific aSDomain and subtypes.

- **as_domain_id**: Identifier for the domain.
- **subtype**: Identifier for the subtype.

## Table: antismash.samples
This table stores information about samples.
A biological sample.

- **sample_id**: Identifier for the sample.
- **habitat**: Habitat where the sample was collected.
- **TIME**: Time when the sample was collected.
- **site_id**: Identifier for the sampling site.

## Table: antismash.smcogs
This table stores information about SMCOG entries.
Secondary Metabolite specific Clusters of Orthologous Groups (smCoGs).

- **smcog_id**: Identifier for the SMCOG entry.
- **name**: Name of the SMCOG entry.
- **description**: Description of the SMCOG entry.
- **functional_class_id**: Identifier for the functional class associated with the SMCOG entry.

## Table: antismash.bgc_rules
This table stores information about BGC rules.
The detection rule used for a specific BGC type.

- **bgc_rule_id**: Identifier for the BGC rule.
- **RULE**: Description of the rule.
- **bgc_type_id**: Identifier for the BGC type associated with the rule.

## Table: antismash.isolates
This table stores information about isolates.
A single biological isolate, sample or strain.

- **isolate_id**: Identifier for the isolate.
- **sample_id**: Identifier for the sample associated with the isolate.

## Table: antismash.genomes
This table stores information about genomes.
Information on a genome.

- **genome_id**: Identifier for the genome.
- **tax_id**: Identifier for the taxonomic entry associated with the genome.
- **bio_project**: BioProject associated with the genome.
- **bio_sample**: BioSample associated with the genome.
- **isolate_id**: Identifier for the isolate associated with the genome.
- **assembly_id**: Identifier for the assembly associated with the genome.

## Table: antismash.dna_sequences
This table stores information about DNA sequences.

- **dna**: DNA sequence.
- **md5**: MD5 checksum of the DNA sequence.
- **accession**: Accession number for the DNA sequence.
- **definition**: Definition of the DNA sequence.
- **contig_type**: Type of the contig.
- **chromosome_type**: Type of the chromosome.
- **record_number**: Record number for the DNA sequence.
- **VERSION**: Version of the DNA sequence.
- **genome_id**: Identifier for the genome associated with the DNA sequence.

## Table: antismash.regions
This table stores information about regions in the DNA sequences containing Biosynthetic Gene Clusters as predicted by antiSMASH. People commonly refers to region when mentioning a BGC.
A region of interest as predicted by antiSMASH.

- **region_id**: Identifier for the region.
- **accession**: Accession number for the DNA sequence associated with the region.
- **region_number**: Number of the region.
- **LOCATION**: Location of the region.
- **start_pos**: Start position of the region.
- **end_pos**: End position of the region.
- **contig_edge**: Indicates if the region is at the contig edge.
- **best_mibig_hit_acc**: Best MIBIG hit accession number.
- **best_mibig_hit_description**: Best MIBIG hit description.
- **best_mibig_hit_similarity**: Best MIBIG hit similarity.

## Table: antismash.rel_regions_types
This table stores relationships between regions and BGC types.

- **region_id**: Identifier for the region.
- **bgc_type_id**: Identifier for the BGC type.

## Table: antismash.tta_codons
This table stores information about TTA codons. This codon are quite rare in GC-rich organism such as Streptomyces. While genes involved in primary metabolism almost exclusively use CTC codons to code for Leu, key genes in secondary metabolism and cell differentiation often contain TTA codons.
A TTA codon record.

- **tta_codon_id**: Identifier for the TTA codon.
- **seq_id**: Identifier for the DNA sequence.
- **LOCATION**: Location of the TTA codon in the DNA sequence.

## Table: antismash.binding_sites
This table stores information about binding sites of regulators, part of the antiSMASH TFBS (transcription factor binding site) finder feature.

- **binding_site_id**: Identifier for the binding site.
- **regulator_id**: Identifier for the regulator.
- **region_id**: Identifier for the region.
- **score**: Score of the binding site.
- **START**: Start position of the binding site.
- **confidence_id**: Identifier for the confidence level.

## Table: antismash.candidates
This table stores information about candidates cluster.
A candidate cluster as predicted by antiSMASH.

- **candidate_id**: Identifier for the candidate.
- **region_id**: Identifier for the region.
- **LOCATION**: Location of the candidate in the region.
- **candidate_type_id**: Identifier for the candidate type.
- **smiles**: SMILES notation for the candidate.
- **polymer**: Polymer information for the candidate.

## Table: antismash.cdss
This table stores information about coding sequences (CDSs).
A CDS record.

- **cds_id**: Identifier for the CDS.
- **functional_class_id**: Identifier for the functional class associated with the CDS.
- **locus_tag**: Locus tag of the CDS.
- **name**: Name of the CDS.
- **product**: Product encoded by the CDS.
- **protein_id**: Protein identifier for the CDS.
- **TRANSLATION**: Translation of the CDS.
- **LOCATION**: Location of the CDS in the region.
- **region_id**: Identifier for the region.

## Table: antismash.clusterblast_hits
This table stores information about clusterblast hits.
ClusterBlast hit storage, also for Sub- and KnownClusterblast.

- **clusterblast_hit_id**: Identifier for the clusterblast hit.
- **region_id**: Identifier for the region.
- **rank**: Rank of the clusterblast hit.
- **acc**: Accession number of the clusterblast hit.
- **description**: Description of the clusterblast hit.
- **similarity**: Similarity of the clusterblast hit.
- **algorithm_id**: Identifier for the algorithm used.

## Table: antismash.comparippson_asdb_references
This table stores references to ASDB entries used in comparative analysis.

- **comparippson_asdb_id**: Identifier for the ASDB reference.
- **cds_id**: Identifier for the CDS.
- **product**: Product associated with the ASDB reference.

## Table: antismash.comparippson_hits
This table stores information about comparippson hits.
CompaRiPPson hits storage for both MIBiG and aS-DB.

- **comparippson_hit_id**: Identifier for the comparippson hit.
- **cds_id**: Identifier for the CDS.
- **similarity**: Similarity of the comparippson hit.
- **region_id**: Identifier for the region.
- **comparippson_mibig_id**: Identifier for the MIBIG reference.
- **comparippson_asdb_id**: Identifier for the ASDB reference.

## Table: antismash.genes
This table stores information about genes.
A gene record.

- **gene_id**: Identifier for the gene.
- **locus_tag**: Locus tag of the gene.
- **LOCATION**: Location of the gene in the region.
- **region_id**: Identifier for the region.

## Table: antismash.modules
This table stores information about modules.
An NRPS/PKS module with multiple child domains, the loaded substrate and resulting modified monomer.

- **module_id**: Identifier for the module.
- **LOCATION**: Location of the module.
- **TYPE**: Type of the module.
- **trans_at**: Indicates if the module is trans-AT.
- **complete**: Indicates if the module is complete.
- **iterative**: Indicates if the module is iterative.
- **multi_gene**: Indicates if the module is multi-gene.
- **region_id**: Identifier for the region.

## Table: antismash.pfam_domains
This table stores information about Pfam domains.
A PFAM domain prediction.

- **pfam_domain_id**: Identifier for the Pfam domain.
- **DATABASE**: Database associated with the Pfam domain.
- **detection**: Detection method for the Pfam domain.
- **score**: Score of the Pfam domain.
- **evalue**: E-value of the Pfam domain.
- **TRANSLATION**: Translation of the Pfam domain.
- **pfam_id**: Identifier for the Pfam entry.
- **LOCATION**: Location of the Pfam domain.
- **cds_id**: Identifier for the CDS.

## Table: antismash.pfam_go_entries
This table stores relationships between Pfam domains and gene ontologies.

- **pfam_domain_id**: Identifier for the Pfam domain.
- **go_id**: Identifier for the gene ontology.

## Table: antismash.profile_hits
This table stores information about profile hits.

- **profile_hit_id**: Identifier for the profile hit.
- **cds_id**: Identifier for the CDS.
- **name**: Name of the profile.
- **evalue**: E-value of the profile hit.
- **bitscore**: Bit score of the profile hit.
- **seeds**: Number of seeds for the profile hit.

## Table: antismash.protoclusters
This table stores information about protoclusters.
A protocluster as predicted by antiSMASH.

- **protocluster_id**: Identifier for the protocluster.
- **region_id**: Identifier for the region.
- **LOCATION**: Location of the protocluster.
- **bgc_type_id**: Identifier for the BGC type.

## Table: antismash.rel_candidates_modules
This table stores relationships between candidates and modules.
Many to many relation for compounds to modules.

- **candidate_id**: Identifier for the candidate.
- **module_id**: Identifier for the module.

## Table: antismash.rel_candidates_protoclusters
This table stores relationships between candidates and protoclusters.
Many to many relation for candidates to protoclusters

- **candidate_id**: Identifier for the candidate.
- **protocluster_id**: Identifier for the protocluster.

## Table: antismash.rel_candidates_types
This table stores relationships between candidates and BGC types.
Many to many relation for candidates and bgc_types.

- **candidate_id**: Identifier for the candidate.
- **bgc_type_id**: Identifier for the BGC type.

## Table: antismash.rel_cds_candidates
This table stores relationships between CDSs and candidates.
Many to many relation for CDSs to candidates.

- **candidate_id**: Identifier for the candidate.
- **cds_id**: Identifier for the CDS.

## Table: antismash.rel_cds_protoclusters
This table stores relationships between CDSs and protoclusters.
Many to many relation for CDSs to protoclusters.

- **protocluster_id**: Identifier for the protocluster.
- **cds_id**: Identifier for the CDS.

## Table: antismash.rel_modules_monomers
This table stores relationships between modules and monomers.
Many to many relation for modules to substrates and monomers.

- **module_id**: Identifier for the module.
- **substrate**: Identifier for the substrate.
- **monomer**: Identifier for the monomer.

## Table: antismash.resfam_domains
This table stores information about Resfam domains.

- **resfam_domain_id**: Identifier for the Resfam domain.
- **score**: Score of the Resfam domain.
- **evalue**: E-value of the Resfam domain.
- **resfam_id**: Identifier for the Resfam entry.
- **cds_id**: Identifier for the CDS.

## Table: antismash.ripps
This table stores information about RiPPs (Ribosomally synthesized and Post-translationally modified Peptides).
A (predicted) ribosomally preduced peptide compound.

- **protocluster_id**: Identifier for the protocluster.
- **peptide_sequence**: Peptide sequence of the RiPP.
- **molecular_weight**: Molecular weight of the RiPP.
- **monoisotopic_mass**: Monoisotopic mass of the RiPP.
- **alternative_weights**: Alternative weights of the RiPP.
- **bridges**: Number of bridges in the RiPP.
- **CLASS**: Class of the RiPP.
- **subclass**: Subclass of the RiPP.
- **score**: Score of the RiPP.
- **locus_tag**: Locus tag associated with the RiPP.
- **cds_id**: Identifier for the CDS.

## Table: antismash.smcog_hits
This table stores information about SMCOG hits.
Metadata about an smCoG hit.

- **smcog_id**: Identifier for the SMCOG entry.
- **cds_id**: Identifier for the CDS.
- **score**: Score of the SMCOG hit.
- **evalue**: E-value of the SMCOG hit.
- **image_path**: Path to the image associated with the SMCOG hit.

## Table: antismash.t2pks
This table stores information about T2PKS (Type II Polyketide Synthases).
Predicted compound details for a Type II PKS.

- **t2pks_id**: Identifier for the T2PKS.
- **protocluster_id**: Identifier for the protocluster.

## Table: antismash.t2pks_cds_domain
This table stores information about T2PKS CDS domains.

- **domain_id**: Identifier for the domain.
- **t2pks_id**: Identifier for the T2PKS.
- **cds_id**: Identifier for the CDS.
- **profile_id**: Identifier for the profile.
- **protein_type**: Type of the protein.
- **protein_function**: Function of the protein.
- **evalue**: E-value of the domain.
- **bitscore**: Bit score of the domain.

## Table: antismash.t2pks_product_classes
This table stores relationships between T2PKS and product classes.

- **t2pks_id**: Identifier for the T2PKS.
- **product_class**: Product class associated with the T2PKS.

## Table: antismash.t2pks_starters
This table stores information about T2PKS starters.
A Type II PKS-specific starter domain.

- **domain_id**: Identifier for the domain.
- **t2pks_id**: Identifier for the T2PKS.
- **name**: Name of the starter.
- **evalue**: E-value of the starter.
- **bitscore**: Bit score of the starter.

## Table: antismash.t2pks_starter_elongation
This table stores information about T2PKS starter elongation combinations.

- **combo_id**: Identifier for the combination.
- **domain_id**: Identifier for the domain.
- **elongation**: Elongation value.
- **weight**: Weight of the elongation combination.

## Table: antismash.tigrfam_domains
This table stores information about TIGRFAM domains.
A TIGRFAM domain prediction.

- **tigrfam_domain_id**: Identifier for the TIGRFAM domain.
- **DATABASE**: Database associated with the TIGRFAM domain.
- **detection**: Detection method for the TIGRFAM domain.
- **score**: Score of the TIGRFAM domain.
- **evalue**: E-value of the TIGRFAM domain.
- **TRANSLATION**: Translation of the TIGRFAM domain.
- **tigrfam_id**: Identifier for the TIGRFAM entry.
- **LOCATION**: Location of the TIGRFAM domain.
- **cds_id**: Identifier for the CDS.

## Table: antismash.as_domains
This table stores information about domains.
A functional domain on a gene as predicted by antiSMASH.

- **as_domain_id**: Identifier for the domain.
- **detection**: Detection method for the domain.
- **score**: Score of the domain.
- **evalue**: E-value of the domain.
- **TRANSLATION**: Translation of the domain.
- **pks_signature**: PKS signature of the domain.
- **minowa**: Minowa score of the domain. This score predicts the specificity of adenylation domains in nonribosomal peptide synthetases (NRPS).
- **nrps_predictor**: NRPS predictor score.
- **stachelhaus**: Stachelhaus score. This score predicts the specificity of adenylation domains in nonribosomal peptide synthetases (NRPS).
- **consensus**: Consensus sequence of the domain.
- **kr_activity**: Indicates if the domain has (keto reductase) KR activity.
- **kr_stereochemistry**: Stereochemistry of the (keto reductase) KR activity.
- **as_domain_profile_id**: Identifier for the domain profile.
- **LOCATION**: Location of the domain.
- **cds_id**: Identifier for the CDS.
- **module_id**: Identifier for the module.
- **function_id**: Identifier for the function.
- **follows**: Indicates if the domain follows another domain.

## Table: antismash.cluster_compare_hits
This table stores information about cluster comparison hits.
ClusterCompare hit storage.

- **hit_id**: Identifier for the cluster comparison hit.
- **region_id**: Identifier for the region.
- **protocluster_id**: Identifier for the protocluster.
- **reference_accession**: Reference accession number.
- **description**: Description of the cluster comparison hit.
- **score**: Score of the cluster comparison hit.
- **identity_metric**: Identity metric of the cluster comparison hit.
- **order_metric**: Order metric of the cluster comparison hit.
- **components_metric**: Components metric of the cluster comparison hit.

## Table: antismash.rel_as_domains_substrates
This table stores relationships between AS domains and substrates.
Many to many relation for as_domains to substrate.

- **as_domain_id**: Identifier for the AS domain.
- **substrate_id**: Identifier for the substrate.
- **position_in_domain**: Position of the substrate in the domain.

## Table: antismash.sequence_gc_content
This view stores GC content information for sequences.

- **accession**: Accession number for the DNA sequence.
- **gc_content**: GC content percentage of the DNA sequence.

## Table: antismash.sequence_lengths
This view stores sequence length information.

- **accession**: Accession number for the DNA sequence.
- **seq_length**: Length of the DNA sequence.

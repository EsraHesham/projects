your_djangoproject_home="/home/esraa/Test_loading/website/"
import sys,os
import django
sys.path.append(your_djangoproject_home)
os.environ['DJANGO_SETTINGS_MODULE'] = 'website.settings'
django.setup()
from variants.models import Variant , Annotation, Population
from django.db import connection

os.system("bcftools query -f '%CHROM\t%POS\t%ID\t%REF\t%ALT\t%QUAL\t%FILTER\t%INFO/BaseQRankSum,%INFO/CCC,%INFO/ClippingRankSum,%INFO/DB,%INFO/DS,%INFO/END,%INFO/FS,%INFO/HWP,%INFO/HaplotypeScore,%INFO/MLEAC,%INFO/MLEAF,%INFO/MQ,%INFO/MQ0,%INFO/MQRankSum,%INFO/NCC,%INFO/NEGATIVE_TRAIN_SITE,%INFO/POSITIVE_TRAIN_SITE,%INFO/QD,%INFO/ReadPosRankSum,%INFO/VQSLOD,%INFO/culprit,%INFO/DOUBLETON_DIST,%INFO/AC_MALE,%INFO/AC_FEMALE,%INFO/AN_MALE,%INFO/AN_FEMALE,%INFO/AC_CONSANGUINEOUS,%INFO/AN_CONSANGUINEOUS,%INFO/Hom_CONSANGUINEOUS,%INFO/AC_POPMAX,%INFO/AN_POPMAX,%INFO/POPMAX,%INFO/clinvar_measureset_id,%INFO/clinvar_conflicted,%INFO/clinvar_pathogenic,%INFO/clinvar_mut,%INFO/K1_RUN,%INFO/K2_RUN,%INFO/K3_RUN,%INFO/ESP_AF_POPMAX,%INFO/ESP_AF_GLOBAL,%INFO/ESP_AC,%INFO/KG_AF_POPMAX,%INFO/KG_AF_GLOBAL,%INFO/KG_AC\n' EXAC_Data_20M.vcf > variants.vcf")

os.system("bcftools query -f '%INFO/AC\t%INFO/AC_AFR\t%INFO/AC_AMR\t%INFO/AC_Adj\t%INFO/AC_EAS\t%INFO/AC_FIN\t%INFO/AC_Hemi\t%INFO/AC_Het\t%INFO/AC_Hom\t%INFO/AC_NFE\t%INFO/AC_OTH\t%INFO/AC_SAS\t%INFO/AF\t%INFO/AN\t%INFO/AN_AFR\t%INFO/AN_AMR\t%INFO/AN_Adj\t%INFO/AN_EAS\t%INFO/AN_FIN\t%INFO/AN_NFE\t%INFO/AN_OTH\t%INFO/AN_SAS\t%INFO/DP\t%INFO/GQ_MEAN\t%INFO/GQ_STDDEV\t%INFO/Hemi_AFR\t%INFO/Hemi_AMR\t%INFO/Hemi_EAS\t%INFO/Hemi_FIN\t%INFO/Hemi_NFE\t%INFO/Hemi_OTH\t%INFO/Hemi_SAS\t%INFO/Het_AFR\t%INFO/Het_AMR\t%INFO/Het_EAS\t%INFO/Het_FIN\t%INFO/Het_NFE\t%INFO/Het_OTH\t%INFO/Het_SAS\t%INFO/Hom_AFR\t%INFO/Hom_AMR\t%INFO/Hom_EAS\t%INFO/Hom_FIN\t%INFO/Hom_NFE\t%INFO/Hom_OTH\t%INFO/Hom_SAS\t%INFO/InbreedingCoeff\t%INFO/DP_HIST\t%INFO/GQ_HIST\n' EXAC_Data_20M.vcf > population.vcf")


os.system("bcftools query -f '%INFO/CSQ\n' EXAC_Data_20M.vcf > Annotation.vcf")

cursor = connection.cursor()
from itertools import izip
with open('variants.vcf') as file1, open('population.vcf') as file2 , open('Annotation.vcf') as file3 :
	for line,line2,line3 in izip(file1,file2,file3):
		s=line.split()
		insert_stmt = ("INSERT INTO variants_variant (Chromosome_Number, Position, Var_ID, Reference, Alternate, Quality, Filter, Info)" "VALUES (%s, %s, %s, %s, %s , %s, %s, %s)")
		data = (s[0], s[1], s[2] , s[3] ,s[4] ,s[5] ,s[6],s[7])
		cursor.execute(insert_stmt, data)

		s2=line2.split('\t')
		insert_stmt2 = ("INSERT INTO variants_population (Variant_id , Allele_Count ,AC_African_American , AC_American ,AC_Adjusted, AC_East_Asian , AC_Finnish ,AC_Hemizygous ,AC_Heterozygous, AC_Homozygous, AC_Non_Finnish_European ,AC_Other ,AC_South_Asian,Allele_Frequency,Allele_Number ,AN_African_American,AN_American,AN_Adjusted,AN_East_Asian,AN_Finnish, AN_Non_Finnish, AN_Other ,AN_South_Asian , Read_Depth , Genotype_Quality_MEAN,GQ_Standard_Deviation, Hemi_African_American , Hemi_American, Hemi_East_Asian,Hemi_Finnish ,Hemi_Non_Finnish_European, Hemi_Other, Hemi_South_Asian , Het_African_American , Het_American, Het_East_Asian,Het_Finnish ,Het_Non_Finnish_European, Het_Other, Het_South_Asian, Hom_African_American , Hom_American, Hom_East_Asian,Hom_Finnish ,Hom_Non_Finnish_European_Homozygous, Hom_Other, Hom_South_Asian,InbreedingCoef,DP_HIST ,GQ_HIST)" "VALUES (%s, %s, %s, %s, %s,%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s, %s, %s, %s, %s, %s, %s, %s, %s)")
		select=	("SELECT id FROM variants_variant WHERE Position= %s ")	
		cursor.execute(select, (s[1],))
		result_set = cursor.fetchone()[0]
		data2 = (result_set, s2[0],s2[1],s2[2],s2[3],s2[4],s2[5],s2[6],s2[7],s2[8],s2[9], s2[10],s2[11],s2[12],s2[13],s2[14],s2[15],s2[16],s2[17],s2[18],s2[19],s2[20],s2[21],s2[22],s2[23],s2[24],s2[25],s2[26],s2[27],s2[28], s2[29],s2[30],s2[31],s2[32],s2[33],s2[34],s2[35],s2[36],s2[37],s2[38], s2[39],s2[40],s2[41],s2[42],s2[43],s2[44],s2[45],s2[46],s2[47],s2[48] )
		cursor.execute(insert_stmt2, data2)


		s3=line3.split(',')
		for x in s3:
			c=x.split('|')
			insert_stmt3 = ("INSERT INTO variants_annotation (Variant_id ,Allele,Consequence,Impact,Gene_Symbol,Gene,Feature_type,Feature,Biotype,Exon,Intron,HGVS_DNA,HGVS_Protein,cDNA_position,CDS_position,Protein_position,Amino_acids,Codons,Existing_variation,ALLELE_NUM,DISTANCE,STRAND,VARIANT_CLASS,MINIMISED,SYMBOL_SOURCE,HGNC_ID,CANONICAL,TSL,CCDS,ENSP,SWISSPROT,TREMBL,UNIPARC,SIFT,PolyPhen,DOMAINS,HGVS_OFFSET,GMAF,AFR_MAF,AMR_MAF,ASN_MAF,EAS_MAF,EUR_MAF,SAS_MAF,AA_MAF,EA_MAF,CLIN_SIG,SOMATIC,PHENO,PUBMED,MOTIF_NAME,MOTIF_POS,HIGH_INF_POS,MOTIF_SCORE_CHANGE,LoF_info,LoF_flags,LoF_filter,LoF,context,ancestral )" "VALUES (%s , %s, %s, %s,%s, %s, %s , %s, %s, %s,%s , %s, %s, %s,%s, %s, %s , %s, %s, %s,%s , %s, %s, %s,%s, %s, %s , %s, %s, %s,%s , %s, %s, %s,%s, %s, %s , %s, %s, %s,%s , %s, %s, %s,%s, %s, %s , %s, %s, %s,%s , %s, %s, %s,%s, %s, %s , %s, %s, %s)")
			select2=	("SELECT id FROM variants_variant WHERE Position= %s ") 
			cursor.execute(select2, (s[1],))
			result_set2 = cursor.fetchone()[0]
			data3 = (result_set2, c[0],c[1],c[2],c[3],c[4],c[5],c[6],c[7],c[8],c[9], c[10],c[11],c[12],c[13],c[14],c[15],c[16],c[17],c[18],c[19],c[20],c[21],c[22],c[23],c[24],c[25],c[26],c[27],c[28], c[29],c[30],c[31],c[32],c[33],c[34],c[35],c[36],c[37],c[38], c[39],c[40],c[41],c[42],c[43],c[44],c[45],c[46],c[47],c[48], c[49],c[50],c[51],c[52],c[53],c[54],c[55],c[56],c[57],c[58] )
			cursor.execute(insert_stmt3, data3)

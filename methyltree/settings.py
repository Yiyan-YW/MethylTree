import os

default_feature_dir = ''  # directory of selected genomic regions (bed format)
source_script_dir = ''

map_context = {"GC": "Acc", "CG": "Met"}

help_function_dir, this_filename = os.path.split(__file__)

#lambda-pUC19
bismark_mm10_ref = (
    "/storage/wangshouwenLab/shared_folder/reference/refdata-gex-mm10-lambda-pUC19/fasta"
)
bismark_hg38_ref = (
    "/storage/wangshouwenLab/shared_folder/reference/refdata-gex-GRCh38-lambda-pUC19/fasta"
)
# transcriptome reference
RNA_mm10_ref = "/storage/wangshouwenLab/shared_folder/reference/refdata-gex-mm10-2020-A"
RNA_hg38_ref = (
    "/storage/wangshouwenLab/shared_folder/reference/refdata-gex-GRCh38-2020-A"
)

CpG_ref_location='/storage/wangshouwenLab/shared_folder/reference/CpG'

color_list = [
    "#1f78b4",
    "#ff7f00",
    "#33a02c",
    "#e31a1c",
    "#6a3d9a",
    "#8c564b",
    "#e377c2",
    "#969696",  #
    "#17becf",
    "#253494",
    #'#ffffcc',
    "#a6cee3",
    "#b2df8a",
    "#fb9a99",
    # '#fdbf6f',
    "#cab2d6",
    #'#ffff99',
    "#99d8c9",
    "#8c96c6",
    "#66c2a5",
    "#636363",
    "#ffd92f",
    "#b3b3b3",
    "#db5f57",
]


color_list_2 = [
    "#8dd3c7",
    "#bebada",
    "#fb8072",
    "#80b1d3",
    "#fdb462",
    "#b3de69",
    "#fccde5",
    "#d9d9d9",
    "#bc80bd",
    "#ccebc5",
    "#ffed6f",
    "#ffffb3",
    "#99d8c9",
    "#8c96c6",
    "#66c2a5",
    "#636363",
    "#ffd92f",
    "#b3b3b3",
    "#db5f57",
]

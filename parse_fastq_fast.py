import os
import pandas as pd
from Bio import SeqIO

data_dir = "data"
results = []
MAX_READS = 1000  # نقرأ بس 1000 read لكل ملف عشان السرعة

for filename in os.listdir(data_dir):
    if filename.endswith(".fastq"):
        filepath = os.path.join(data_dir, filename)
        
        total_reads = 0
        total_length = 0
        total_gc = 0
        total_quality = []
        
        for i, record in enumerate(SeqIO.parse(filepath, "fastq")):
            if i >= MAX_READS:
                break
            
            total_reads += 1
            total_length += len(record.seq)
            seq = record.seq
            gc_count = seq.count('G') + seq.count('C')
            gc_percent = (gc_count / len(seq)) * 100
            total_gc += gc_percent
            
            qualities = record.letter_annotations['phred_quality']
            avg_qual = sum(qualities) / len(qualities)
            total_quality.append(avg_qual)
        
        if total_reads > 0:
            avg_length = total_length / total_reads
            avg_gc = total_gc / total_reads
            avg_quality = sum(total_quality) / total_reads
            
            if "healthy" in filename.lower():
                class_label = 0
                disease = "healthy"
            else:
                class_label = 1
                disease = "breast_cancer"
            
            results.append({
                "filename": filename,
                "class": class_label,
                "disease": disease,
                "total_reads": total_reads,
                "avg_length": round(avg_length, 2),
                "avg_gc_percent": round(avg_gc, 2),
                "avg_quality": round(avg_quality, 2)
            })
            
            print(f"✅ {filename}: {total_reads} reads, GC={avg_gc:.2f}%, Quality={avg_quality:.2f}")

df = pd.DataFrame(results)
df.to_csv("parsing_results.csv", index=False)
print("\n📊 تم حفظ النتائج في parsing_results.csv")
print(df)

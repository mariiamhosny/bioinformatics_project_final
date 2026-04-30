import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("parsing_results.csv")

# الألوان: أحمر للسرطان، أخضر للسليم
colors = ['red' if 'cancer' in x else 'green' for x in df['filename']]

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

# GC Content
ax1.bar(df['filename'], df['avg_gc_percent'], color=colors)
ax1.axhline(y=50, color='blue', linestyle='--', label='50% Reference')
ax1.set_ylabel('GC Content (%)')
ax1.set_title('GC Content by Sample')
ax1.tick_params(axis='x', rotation=45)

# Quality
ax2.bar(df['filename'], df['avg_quality'], color=colors)
ax2.set_ylabel('Average Quality Score')
ax2.set_title('Quality Score by Sample')
ax2.tick_params(axis='x', rotation=45)

plt.tight_layout()
plt.savefig('parsing_plot.png', dpi=150)
print("✅ تم حفظ الرسمة في parsing_plot.png")
plt.show()
import pandas as pd
from mlxtend.frequent_patterns import fpgrowth, association_rules
# STEP 2: LOAD DATASET
df = pd.read_csv('fp_train_disease.csv')
print("\n DATASET SHAPE:")
print("before drop",df.shape)
# data cleaning
df = df.dropna()
print("after drop",df.shape)
print("\nCOLUMNS:")
print(df.columns.tolist())
#findout frequent symptom 
frequent_itemsets = fpgrowth(df,min_support=0.05,use_colnames=True)
print("\nFREQUENT SYMPTOM ITEMSETS")
print("-" * 60)
# sorting
frequent_itemsets = frequent_itemsets.sort_values("support",ascending=False)
print(frequent_itemsets.head(50))
# exit(1)
rules = association_rules(frequent_itemsets,metric="confidence",min_threshold=0.20)
rules = rules[rules['lift']>1]
rules = rules.sort_values("lift",ascending=False)
# print(rules.columns)
for index,rule in rules.iterrows():
    print(f"{' '.join(rule['antecedents'])} -> {' '.join(rule['consequents'])} {round(rule['support'],2)} {round(rule['confidence'],2)} {round(rule['lift'],2)}")

#task export result into excel.

# ==========================================
# STEP 4: EXPORT RESULTS INTO EXCEL FILE
# ==========================================

# 1. Convert frozensets to comma-separated strings for Excel compatibility
rules['antecedents'] = rules['antecedents'].apply(lambda item: ', '.join(list(item)))
rules['consequents'] = rules['consequents'].apply(lambda item: ', '.join(list(item)))

# 2. Round the numerical metrics to 2 decimal places
numeric_columns = ['support', 'confidence', 'lift']
for col in numeric_columns:
    if col in rules.columns:
        rules[col] = rules[col].round(2)

# 3. Write selected columns into Excel file
file_name = "association_rules_disease.xlsx"
rules[['antecedents', 'consequents', 'support', 'confidence', 'lift']].to_excel(file_name, index=False)

print(f"\nSuccessfully exported association rules to {file_name}")
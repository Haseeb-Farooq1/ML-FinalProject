from pathlib import Path
p=Path('notebooks/heart_disease_pipeline.ipynb')
out=Path('notebooks/diabetes_pipeline.ipynb')
if not p.exists():
    print('Source not found:', p)
    raise SystemExit(1)
s=p.read_text(encoding='utf-8')
# Basic replacements
s=s.replace('# Heart Disease Dataset Pipeline','# Diabetes Dataset Pipeline')
s=s.replace('Heart Disease Classification Pipeline','Diabetes Classification Pipeline')
s=s.replace("DATA_PATH = ROOT / 'data' / 'heart.csv'","DATA_PATH = ROOT / 'data' / 'diabetes.csv'")
s=s.replace("TARGET = 'target'","TARGET = 'Outcome'")
# Replace continuous cols list (approx)
s=s.replace("CONTINUOUS_COLS = ['age', 'trestbps', 'chol', 'thalach', 'oldpeak']",
"CONTINUOUS_COLS = ['Glucose','BloodPressure','SkinThickness','Insulin','BMI','DiabetesPedigreeFunction','Age']")
# Ensure target mention in overview
s=s.replace("**Target variable:** `target` — `0` = No Heart Disease, `1` = Heart Disease",
"**Target variable:** `Outcome` — `0` = No Diabetes, `1` = Diabetes")
out.write_text(s, encoding='utf-8')
print('Wrote', out)

import pandas as pd
from calculator_app import Calculator

cal = Calculator()

results = []

for i in range(1,11):
    cal.a = 3
    cal.b = i
    results.append(
        {
            'Values':f"3*{i}",
            'Results':cal.do_product()
        }
    )

df = pd.DataFrame(results)

print(df)
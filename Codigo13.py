import re
import pandas as pd

# DataFrame.
data = {'Usuario': ['@ v#a :l, d?o', 'vñ¿a /l@e r%ia_', 'v& a/l,i (e)n,te@', '_v@ i,c_t,o@r_']}
df = pd.DataFrame(data)

# Caracteres no deseados
caracteres_no_deseados = ['@', '_', ',',':','ñ','?','¿','#','$','%','&','/','()','=',' ']
patron= f"[{''.join(caracteres_no_deseados)}]"

# Eliminar caracteres no deseados.
df['Usuario'] = df['Usuario'].apply(lambda x: re.sub(patron,"",x))

# DataFrame actualizado.
print(df)
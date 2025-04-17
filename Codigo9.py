import pandas as pd
import numpy as np
from faker import Faker
import random
from datetime import datetime


fake = Faker()
Faker.seed(42)
np.random.seed(42)
random.seed(42)

num_registros = 5000


datos_generados = {
    'id': np.arange(1, num_registros + 1),
    'edad': np.random.randint(18, 80, size=num_registros),
    'salario': np.round(np.random.uniform(20000, 100000, size=num_registros), 2),
    'puntaje_credito': np.round(np.random.uniform(300, 850, size=num_registros), 1),
    'años_experiencia': np.random.randint(0, 40, size=num_registros),
    'departamento': [random.choice(['Ventas', 'IT', 'HR', 'Finanzas']) for _ in range(num_registros)],
    'nivel_educativo': [random.choice(['Secundaria', 'Pregrado', 'Posgrado']) for _ in range(num_registros)],
    'fecha_contratacion': [fake.date_between(start_date='-10y', end_date='today') for _ in range(num_registros)],
    'direccion': [fake.address().replace('\n', ', ') for _ in range(num_registros)],
    'comentarios': [fake.text(max_nb_chars=200) for _ in range(num_registros)],
}


df = pd.DataFrame(datos_generados)
df['fecha_contratacion'] = pd.to_datetime(df['fecha_contratacion'])


pd.set_option('display.max_columns', None)

print("Vista previa de los primeros 10 registros:\n")
print(df.head(10))
print("\nCorreos de Teyvat\n")

registros = [
    ['Ei', 'EternidadxSiempre@mail.com', '1500-06-26', 'Inactivo'],
    ['Mavuika', 'SolInvictus@mail.com', '1800-08-28', 'Activo'],
    ['Aether', 'SisterFound@mail.com', '2004-07-26', 'Activo'],
    ['Jean', 'Chambeadora3000@mail.com', '1985-03-14', 'Inactivo'],
    ['Furina', 'NoFocalors?@mail.com', '1525-10-13', 'Inactivo'],
    ['Itto', 'TheOneandOni@mail.com', '1910-06-01', 'Inactivo'],
    ['Nahida', 'SabiduriaesPoder@mail.com', '1750-10-27', 'Activo'],
    ['Klee', 'MasterJeanisaBi...@mail.com', '1990-07-27', 'Activo'],
    ['Paimon', 'Food_Emergency@mail.com', '1000-06-01', 'Activo'],
    ['Sara', 'ShogunSimp@mail.com', '1989-07-14', 'Inactivo'],
    ['Zhongli', 'NoMoney@mail.com', '2023-12-31', 'Activo'],
    ['Roronoa Zoro', 'Donde_Estoy?@mail.com', '2006-11-11', 'Inactivo'],

    # Duplicados
    ['Ei', 'EternidadxSiempre@mail.com', '1500-06-26', 'Inactivo'],
    ['Furina', 'NoFocalors?@mail.com', '1525-10-13', 'Inactivo'],
    ['Nahida', 'SabiduriaesPoder@mail.com', '1750-10-27', 'Activo'],
]

# Eliminar los duplicados (basado en todos los campos)
registros_sin_duplicados = [list(x) for x in set(tuple(x) for x in registros)]

# Mostrar la lista sin duplicados
print("Lista sin duplicados:")
for registro in registros_sin_duplicados:
    print(registro)

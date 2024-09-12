def calcular_pago(cantidad_nutricion, cantidad_estetica):
    # Definir costos por estudio
    costo_nutricion = 10000
    costo_estetica = 5000
    
    # Calcular costo total
    total_nutricion = cantidad_nutricion * costo_nutricion
    total_estetica = cantidad_estetica * costo_estetica
    total = total_nutricion + total_estetica
    
    # Calcular descuento si aplica
    if total > 80000:
        descuento = total * 0.20
    else:
        descuento = 0
    
    # Calcular monto final a pagar
    monto_final = total - descuento
    
    return monto_final, descuento

# Ejemplo de uso:
pacientes = [
    {"nutricion": 8, "estetica": 5},
    {"nutricion": 1, "estetica": 8},
    {"nutricion": 0, "estetica": 1},
]

for i, paciente in enumerate(pacientes):
    monto, descuento = calcular_pago(paciente["nutricion"], paciente["estetica"])
    print(f"Paciente {i + 1}:")
    print(f"  Total a pagar: {monto} pesos")
    print(f"  Descuento aplicado: {descuento} pesos")


costo_nutricion = 10000
costo_estetica = 5000
num_estudios_nutricion = 3  # Entero
num_estudios_estetica = 2  # Entero
costo_total = (costo_nutricion * num_estudios_nutricion) + (costo_estetica * num_estudios_estetica)  # Aritmético


if costo_total > 80000:
    descuento = costo_total * 0.20
    costo_final = costo_total - descuento
else:
    descuento = 0
    costo_final = costo_total

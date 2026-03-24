# unidades = int(input("Ingresa el número de unidades vendidas: "))
# valor_venta = float(input("Ingresa el valor de venta por unidad: "))

# costo_produccion = 100
# costo_total = costo_produccion * unidades
# ingreso_total = valor_venta * unidades
# ganancia = ingreso_total - costo_total
# porcentaje = (ganancia / costo_total) * 100

# print("=" * 45)
# print(f"  Unidades vendidas      : {unidades}")
# print(f"  Costo de producción    : ${costo_total:,.2f}")
# print(f"  Ingreso total          : ${ingreso_total:,.2f}")
# print(f"  Ganancia/Pérdida       : ${ganancia:,.2f}")
# print(f"  Porcentaje             : {porcentaje:,.0f}%")


"""Escriba un programa en python que tome el valor total de una venta 
introducida por entrada standard aplicarle iva, impuesto a la utilidad 
y retención en la fuente."""

valor_total = float(input("Ingrese el valor total de la venta: "))

impuesto_iva = valor_total * 0.19
utilidad = valor_total * 0.10
retencion = valor_total * 0.035

total_pagar = valor_total + impuesto_iva + utilidad - retencion

print(f"  El valor de la venta es      : ${valor_total:,.2f}")
print(f"  IVA (19%)                    : ${impuesto_iva:,.2f}")
print(f"  Utilidad (10%)               : ${utilidad:,.2f}")
print(f"  Retención en la fuente (3.5%): ${retencion:,.2f}")
print(f"  Total a pagar                : ${total_pagar:,.2f}")













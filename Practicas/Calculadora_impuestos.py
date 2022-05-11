def Calculadora(pago, impuesto):
    pago_total = pago + pago * (impuesto/21)
    return pago_total

pago = float(input('Proporcione el pago sin impuestos: '))
impuesto = float(input('Proporcione el monto del impuesto a aplicar: '))
pago_impuesto = Calculadora(pago, impuesto)

print(f'Pago con impuesto: {pago_impuesto}')
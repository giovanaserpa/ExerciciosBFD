valor_hora = float(input("Informe o valor recebido por hora trabalhada: R$ "))
horas_trabalhadas = float(input("Informe a quantidade de horas trabalhadas no mês: "))

salario_bruto = valor_hora * horas_trabalhadas
desconto_ir = salario_bruto * 0.11
desconto_inss = salario_bruto * 0.09
desconto_sindicato = salario_bruto * 0.04
salario_liquido = salario_bruto - (desconto_ir + desconto_inss + desconto_sindicato)

print(f"+ Salário Bruto    : R$ {salario_bruto:.2f}")
print(f"- IR (11%)         : R$ {desconto_ir:.2f}")
print(f"- INSS (9%)        : R$ {desconto_inss:.2f}")
print(f"- Sindicato (4%)   : R$ {desconto_sindicato:.2f}")
print(f"= Salário Líquido  : R$ {salario_liquido:.2f}")

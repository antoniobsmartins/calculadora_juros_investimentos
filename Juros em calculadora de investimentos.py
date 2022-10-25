
    montante = capital + rendimento

    print("O valor do rendimento após {1} anos é de R$ {0:.2f}".format(rendimento, periodo))
    print("O montante final após o investimento é de R$ {:.2f} após {} anos".format(montante, periodo))

elif (tipos_de_juros == 2 and periodo_de_juros_m_ou_a == 1):
    capital = float(input("Qual o valor do capital a ser aplicado?"))
    taxa = float(input("Qual a porcentagem do Juros?"))
    taxa_percentual = taxa / 100
    periodo = int(input("Qual o tempo do investimento?"))

    montante = capital * ((1+ taxa_percentual) ** periodo)

    print("O montante final após o investimento é de R$ {:.2f} após {} meses".format(montante, periodo))

elif (tipos_de_juros == 2 and periodo_de_juros_m_ou_a == 2):
    capital = float(input("Qual o valor do capital a ser aplicado?"))
    taxa = float(input("Qual a porcentagem do Juros?"))
    taxa_percentual = taxa / 100
    periodo = int(input("Qual o tempo do investimento?"))

    montante = capital * ((1 + taxa_percentual) ** periodo)

    print("O montante final após o investimento é de R$ {:.2f} após {} anos".format(montante, periodo))
else:
    print("Tente Novamente")
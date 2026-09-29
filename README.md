# 13DOF Sensor Excel

Registro em **Microsoft Excel** dos dados do sensor **13DOF**
(acelerómetro, giroscópio, magnetómetro, temperatura, humidade, pressão e gás).

## Descrição

Este projeto permite [receber / registar / visualizar] no Excel
os dados de um sensor de 13 graus de liberdade, ligado através de Arduino por porta série

## Sensores

O 13DOF integra três circuitos da Bosch:

| Sensor | Medições |
|--------|----------|
| BMI088 | Acelerómetro 3 eixos + giroscópio 3 eixos |
| BMM150 | Magnetómetro 3 eixos |
| BME680 | Temperatura, humidade, pressão e gás |

## Funcionalidades

- Aquisição de dados dos 13 canais
- Registo automático numa folha de Excel
- [Exportação para CSV]

## Estrutura do repositório

    13DOF_Sensor_Excel/
    ├── [13DOF]     # Código para configuração do sensor
    ├── [Receive/]  # Código para receber e gravar os dados
    └── README.md

**Jonhi7139** — [https://github.com/Jonhi7139](https://github.com/Jonhi7139)

## Licença

[MIT / GPL / outra]

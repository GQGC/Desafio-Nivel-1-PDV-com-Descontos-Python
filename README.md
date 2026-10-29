# Sistema de Caixa e Calculadora de Descontos

Script em Python desenvolvido para automatizar o registro de vendas diárias em um ponto de caixa. O sistema calcula descontos progressivos com base na idade do cliente e no valor total do carrinho, gerando um relatório consolidado ao final do expediente.

---

## Como Funciona

O programa roda em loop contínuo permitindo a inserção de sucessivas vendas. As regras de desconto são aplicadas em cascata:

1. **Desconto por idade:** Clientes com 65 anos ou mais recebem 20% de desconto sobre o valor inicial da compra.
2. **Desconto por valor:** Caso o valor da compra (já considerando o desconto de idade, se houver) seja superior a R$ 100,00, é aplicado um desconto adicional de 10%.
3. **Validação de entrada:** Valores negativos para idade ou preço são recusados, solicitando nova digitação sem interromper o fluxo.
4. **Encerramento e Relatório:** Ao digitar '0' no valor da compra, o caixa é fechado e o sistema exibe o total de operações, o faturamento bruto, o volume de descontos concedidos e o valor final arrecadado.

---

## Pré-requisitos

- Python 3.6 ou superior instalado.

---

## Execução

1. Clone este repositório:
	```bash
	git clone [https://github.com/seu-usuario/nome-do-repositorio.git](https://github.com/seu-usuario/nome-do-repositorio.git)

2. Acesse a pasta do projeto:
cd nome-do-repositorio

3.Execute o script "pdv.py"
	python pdv.py

import os
from google.generativeai import Gemini

# *Configurar a sua API Key usando variáveis de ambiente*
os.environ["GOOGLE_API_KEY"] = "AIzaSyD3PRHFREj9u7TogX5Rpu1Go3oGt7XoZ-A" 
Gemini.api_key = os.environ["GOOGLE_API_KEY"]

# Função para calcular o IMC
def calcular_imc(peso, altura):
  return peso / (altura ** 2)

# Função para obter informações do usuário
def obter_informacoes_usuario():
  idade = int(input("Qual a sua idade? "))

  # Verificação de idade
  if idade < 18:
    print("Este serviço só pode ser utilizado por pessoas com 18 anos ou mais.")
    return None

  conhece_bioimpedancia = input("Você conhece suas informações de bioimpedância (percentual de gordura, etc.)? (s/n) ")

  if conhece_bioimpedancia.lower() == 's':
    # Obter informações detalhadas de bioimpedância
    percentual_gordura = float(input("Qual o seu percentual de gordura? "))
    gordura_visceral = float(input("Qual a sua gordura visceral? "))
    percentual_musculo = float(input("Qual o seu percentual de tecido muscular? "))
    percentual_osseo = float(input("Qual o seu percentual de tecido ósseo? "))
  else:
    # Obter informações básicas para calcular o IMC
    peso = float(input("Qual o seu peso (em kg)? "))
    altura = float(input("Qual a sua altura (em metros)? "))
    percentual_gordura = None
    gordura_visceral = None
    percentual_musculo = None
    percentual_osseo = None

  print("\nQual o seu objetivo principal? Escolha uma opção:")
  print("1. Perder peso")
  print("2. Ganhar massa muscular")
  print("3. Manter-se em forma")
  print("4. Ganhar flexibilidade")
  print("5. Ganhar resistência")
  print("6. Outro")
  opcao_objetivo = input("Digite o número da opção ou descreva seu objetivo: ")

  if opcao_objetivo.isdigit():
    objetivo = {
      "1": "Perder peso",
      "2": "Ganhar massa muscular",
      "3": "Manter-se em forma",
      "4": "Ganhar flexibilidade",
      "5": "Ganhar resistência"
    }.get(opcao_objetivo, "Outro")
  else:
    objetivo = opcao_objetivo

  return {
    "idade": idade,
    "peso": peso,
    "altura": altura,
    "percentual_gordura": percentual_gordura,
    "gordura_visceral": gordura_visceral,
    "percentual_musculo": percentual_musculo,
    "percentual_osseo": percentual_osseo,
    "objetivo": objetivo
  }

# Função para gerar insights de treinamento e alimentação com Gemini
def gerar_insights(informacoes_usuario):
  prompt = f"""
  Com base nas informações do usuário, gere insights personalizados de treinamento e alimentação:
  Idade: {informacoes_usuario['idade']}
  Peso: {informacoes_usuario['peso']}
  Altura: {informacoes_usuario['altura']}
  Percentual de gordura: {informacoes_usuario['percentual_gordura']}
  Gordura visceral: {informacoes_usuario['gordura_visceral']}
  Percentual de músculo: {informacoes_usuario['percentual_musculo']}
  Percentual de osso: {informacoes_usuario['percentual_osseo']}
  Objetivo: {informacoes_usuario['objetivo']}

  Inclua:
  * Análise do estado atual do usuário (se possível, com base nas informações fornecidas).
  * Sugestões de treino personalizadas, considerando o objetivo do usuário.
  * Recomendações de alimentação saudável.
  """

  # Utilize o Gemini para gerar os insights
  response = Gemini.generate_text(prompt)
  return response.text

# Fluxo principal do programa
informacoes_usuario = obter_informacoes_usuario()

if informacoes_usuario:
  if informacoes_usuario['peso'] and informacoes_usuario['altura']:
    imc = calcular_imc(informacoes_usuario['peso'], informacoes_usuario['altura'])
    print(f"\nSeu IMC é: {imc:.2f}")

  insights = gerar_insights(informacoes_usuario)
  print("\n## Insights personalizados para você:")
  print(insights)

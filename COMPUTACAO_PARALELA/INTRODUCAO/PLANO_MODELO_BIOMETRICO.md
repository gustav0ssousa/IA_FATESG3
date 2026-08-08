# Plano de implementação para modelo biométrico

## 1. Contexto do dataset

O dataset presente na pasta Real contém 6.000 imagens BMP organizadas em um padrão biométrico:

- identificador da pessoa
- sexo: M ou F
- lado da mão: Left ou Right
- tipo de dedo: index, middle, ring, little, thumb

### Características observadas
- 600 indivíduos
- 10 imagens por pessoa
- 3.000 imagens para cada lado da mão
- 1.200 imagens para cada tipo de dedo
- desbalanceamento entre sexos: 4.770 imagens masculinas e 1.230 femininas

## 2. Objetivo do projeto

Construir um pipeline completo para tratamento, treinamento e avaliação de um modelo biométrico capaz de:

- preprocessar imagens de impressões digitais
- aprender padrões discriminativos
- produzir métricas objetivas de desempenho
- ser expandido para reconhecimento ou verificação biométrica

## 3. Etapas de implementação

### Etapa 1 — Coleta e organização dos dados

- localizar todas as imagens BMP na pasta Real
- extrair metadados a partir do nome do arquivo
- criar um dataset estruturado com colunas:
  - caminho da imagem
  - id da pessoa
  - sexo
  - lado da mão
  - tipo de dedo

### Etapa 2 — Pré-processamento das imagens

Aplicar uma rotina padrão para padronizar as entradas:

- leitura das imagens em escala de cinza ou RGB
- redimensionamento para tamanho fixo, por exemplo 224x224
- normalização de pixel para intervalo [0,1]
- remoção de ruído simples
- equalização de contraste para destacar estruturas
- padronização da iluminação quando necessário

### Etapa 3 — Divisão do dataset

A separação deve ser feita por pessoa, não de forma aleatória, para evitar vazamento de informação.

Sugestão:
- treino: 70%
- validação: 15%
- teste: 15%

### Etapa 4 — Definição do modelo

#### Versão inicial (MVP)
- usar uma CNN simples ou rede pré-treinada como ResNet18 ou MobileNet
- objetivo: classificação de identidade ou atributo biométrico

#### Versão mais robusta
- usar embeddings com triplet loss ou contrastive loss
- objetivo: comparar duas amostras e decidir se pertencem à mesma pessoa

### Etapa 5 — Treinamento

- carregar batches das imagens preprocessadas
- aplicar aumentação leve para aumentar robustez
- usar otimizador como Adam
- monitorar perda em validação
- salvar checkpoints do melhor modelo

### Etapa 6 — Avaliação

Avaliar com métricas clássicas e métricas biométricas:

#### Métricas de classificação
- accuracy
- precision
- recall
- F1-score
- matriz de confusão

#### Métricas biométricas
- FAR: False Acceptance Rate
- FRR: False Rejection Rate
- EER: Equal Error Rate
- ROC-AUC

#### Métricas operacionais
- tempo de inferência por imagem
- uso de memória
- throughput

## 4. Pipeline recomendado

1. carregar imagens
2. extrair labels
3. pré-processar
4. dividir por pessoa
5. treinar modelo
6. validar
7. calcular métricas
8. salvar resultados em CSV/JSON e gerar gráficos

## 5. Recomendação prática

Para este projeto, a melhor abordagem é:

- começar com um modelo de classificação simples para validar o pipeline
- depois evoluir para um modelo baseado em embeddings para cenários reais de biometria

Isso permite provar a ideia rapidamente e, em seguida, aumentar a qualidade do sistema.

## 6. Entregáveis esperados

- script de preprocessamento
- script de treinamento
- script de avaliação
- relatório com métricas
- gráficos de desempenho
- modelo treinado e checkpoints

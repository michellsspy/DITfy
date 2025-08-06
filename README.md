# 📝 Conversor Automatizado de Notebooks Jupyter para Documentos Técnicos (DIT)

**Solução Inteligente para Documentação Técnica Padronizada em Times de Dados**

![Interface DITfy](img\Captura de tela 2025-08-04 213554.png)
*(Imagem ilustrativa)*

## 🌟 Visão Geral

Desenvolvemos uma solução inovadora que transforma notebooks Jupyter/Databricks em Documentos de Implementação Técnica (DIT) completos e padronizados, utilizando inteligência artificial para automatizar até 90% do processo de documentação.

**Problema resolvido:** Elimina os desafios de documentação manual em projetos de dados, que costumam ser:
- Demorados e propensos a erros
- Despadronizados entre membros do time
- Difíceis de manter atualizados
- Pouco eficientes para auditorias e transferência de conhecimento

## 🚀 Principais Funcionalidades

### 🔄 Conversão Inteligente
- Transformação automática de `.ipynb` para Markdown e Word (.docx)
- Extração inteligente de código e textos dos notebooks
- Geração automática de resumos técnicos por seção

### 📑 Estruturação Automatizada
- Criação de documentos completos com:
  - Capa profissional personalizável
  - Sumário automático
  - Introdução técnica contextual
  - Seções organizadas por notebook
  - Rodapé institucional padrão

### 🤖 IA Avançada
- Processamento com GPT-3.5/GPT-4 para:
  - Explicação de trechos complexos de código
  - Geração de documentação contextual
  - Padronização de tom técnico
- Modelos de linguagem configuráveis para diferentes necessidades

## 💡 Benefícios Chave

- **⏱️ Economia de tempo:** Redução de até 80% no tempo de documentação
- **📊 Padronização:** Documentos consistentes seguindo templates corporativos
- **🔍 Rastreabilidade:** Facilita auditorias e compliance
- **🔄 Manutenção:** Atualização simplificada da documentação
- **🧑‍💻 Onboarding:** Acelera a integração de novos membros no time

## 🛠️ Tecnologias Utilizadas

### 💻 Stack Principal
- **Python 3.10+** (Estrutura modular e orientada a objetos)
- **OpenAI API** (GPT-3.5-turbo e GPT-4 para geração de conteúdo)
- **LangChain** (Orquestração de modelos de IA)
- **nbconvert** (Conversão de notebooks Jupyter)
- **python-docx** (Geração de documentos Word profissionais)

### 📚 Bibliotecas Complementares
```python
dependencies = [
        'ipykernel',
        'langchain==0.1.16',
        'langchain-community==0.0.33',
        'langchain-openai==0.1.3',
        'openai==1.55.3',
        'huggingface_hub==0.22.2',
        'transformers==4.39.3',
        'jinja2==3.1.3',
        'tiktoken==0.6.0',
        'pypdf==4.2.0',
        'yt_dlp==2024.4.9',
        'pydub==0.25.1',
        'beautifulsoup4==4.12.3',
        'python-dotenv',
        'sentence-transformers==2.7.0',
        'langchain-chroma',
        'faiss-cpu',
        'lark',
        'python-docx',
        'gradio==5.39.0',
        'psutil',
        'pypandoc',
        'python-docx',
        'markdown',
        'nbconvert'
]
```

## 🏗️ Arquitetura do Projeto

```
project-root/
│
├── .venv/                      # Ambiente virtual
├── doc/                        # Documentos carregados
├── .env                        # Variáveis de ambiente
├── functions/                  # Funções do sistema   
│   ├── __init__.py             # Inicialização do módulo
│   ├── log.py                  # Configuração do logger 
│   ├── estrutura.py            # Criação de pastas
│   ├── conversao.py            # Conversão de arquivos
│   ├── upsert_key_gpt.py       # Inserção de chave da API OpenAI
│   ├── create_key_gpt.py       # Criação/atualização da chave da API OpenAI
│   ├── esta_em_venv.py         # Verificação do ambiente virtual
|   ├── garantir_venv.py        # Garantia do ambiente virtual        
├── log/                        # Logs do sistema
├── markdown/                   # Arquivos convertidos para Markdown
├── notebooks/                  # Notebooks Jupyter
├── docdit_app.exe              # Executável do sistema (se aplicável)
├── installer.py                # Script de instalação automática
└── README.md                   # 
```

## 🛠️ Configuração e Uso

### Pré-requisitos
- Python 3.10+ instalado
- Chave de API da OpenAI configurada no `.env`
- Ambiente virtual recomendado (venv, conda ou similar)

### Instalação Automática
```bash
python installer.py
```

### Processamento de Notebooks
```python
from src.main import convert_notebooks_to_dit

convert_notebooks_to_dit(
    input_dir="notebooks",
    output_dir="docs",
    template="corporate"
)
```

## 📈 Casos de Uso Típicos

1. **Documentação para Auditorias**  
   Geração rápida de documentação técnica completa para processos de compliance

2. **Transferência de Conhecimento**  
   Criação automática de manuais quando projetos mudam de equipe

3. **Padronização em Grandes Equipes**  
   Garantia de que todos os membros documentam seguindo o mesmo padrão

4. **Atualização de Documentação**  
   Sincronização fácil entre mudanças no código e na documentação

## 📌 Próximos Passos

- [ ] Suporte a mais formatos de saída (PDF, HTML)
- [ ] Integração com plataformas de CI/CD
- [ ] Versão CLI para uso em pipelines
- [ ] Dashboard de acompanhamento de documentação

## 🤝 Contribuição

Contribuições são bem-vindas! Siga o processo:
1. Abra uma issue descrevendo a melhoria
2. Faça fork do repositório
3. Crie um branch para sua feature (`git checkout -b feature/AmazingFeature`)
4. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
5. Push para o branch (`git push origin feature/AmazingFeature`)
6. Abra um Pull Request

## 📄 Licença
     ```markdown
     ## 📄 Licença
     Este projeto está licenciado sob a licença MIT - veja o arquivo [LICENSE](LICENSE) para detalhes.
     ```
    Distribuído sob a licença MIT. Veja `LICENSE` para mais informações.

## ✉️ Contato

Equipe prosite - [michellss.py@gmail.com](michel.prosite@gmail.com)  
Projeto Link: [https://github.com/michellsspy/DITfy.git](https://github.com/michellsspy/DITfy.git)

---

**Transforme sua documentação técnica de obrigação para vantagem competitiva!** 🚀
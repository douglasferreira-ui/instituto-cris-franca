# Instituto Cris França — Site em Streamlit

Site institucional profissional para **Psicologia & Terapias Integrativas**, com:

- página inicial responsiva;
- foco em Psicologia e Dependência Emocional;
- áreas de atuação;
- catálogo pesquisável de Florais de Saint Germain e fórmulas;
- botões individuais para compra/consulta via WhatsApp;
- formulário que monta a mensagem para o WhatsApp;
- seção de Instagram;
- visual alinhado à identidade verde oliva, dourado, bege e marrom;
- aviso de uso complementar para florais e terapias integrativas;
- versão responsiva para celular.

## 1. Rodar no Windows

Abra o CMD dentro da pasta do projeto e execute:

```bat
python -m pip install -r requirements.txt
python -m streamlit run app.py
```

Se o Windows disser **"Python was not found"**, tente:

```bat
py -m pip install -r requirements.txt
py -m streamlit run app.py
```

Depois o navegador abrirá o site localmente.

## 2. Personalizar o CRP

No início do `app.py`, altere:

```python
CRP = ""
```

para o número profissional correto, por exemplo:

```python
CRP = "CRP 06/000000"
```

Não foi inventado nenhum número de registro no projeto.

## 3. WhatsApp e Instagram

Já configurados no `app.py`:

- WhatsApp: **(11) 94571-4554**
- Instagram: **@crisfrancah**

## 4. Publicar no Streamlit Community Cloud

1. Crie um repositório no GitHub.
2. Envie `app.py`, `requirements.txt`, `.streamlit/` e `assets/`.
3. No Streamlit Community Cloud, crie um novo app.
4. Selecione o repositório e use `app.py` como arquivo principal.
5. Faça o deploy.

## Estrutura

```text
instituto_cris_franca_streamlit/
├── app.py
├── requirements.txt
├── README.md
├── .streamlit/
│   └── config.toml
└── assets/
    ├── logo_full.png
    ├── logo_icon.png
    ├── cris_avatar.jpg
    ├── cris_post.jpg
    └── instagram_profile.png
```

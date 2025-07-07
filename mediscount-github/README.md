# MediSCOUNT

MediSCOUNT é um app Streamlit que permite ao usuário comparar produtos médicos com base em:
- Preço
- Distância
- Avaliação
- Custo-benefício (score)

Ideal para clínicas, hospitais e consumidores.

## 🚀 Rodar localmente

```bash
pip install -r requirements.txt
streamlit run app.py
```

Crie um `.env` com suas credenciais:

```
EMAIL_MEDISCOUNT=seuemail@gmail.com
SENHA_MEDISCOUNT=sua_senha_de_app
```

## ☁️ Deploy no Streamlit Cloud

1. Suba este projeto no GitHub
2. Acesse https://streamlit.io/cloud
3. Clique em "New App"
4. Configure o repositório, branch e `app.py`
5. Em Settings > Secrets, adicione:

```
EMAIL_MEDISCOUNT=seuemail@gmail.com
SENHA_MEDISCOUNT=sua_senha_de_app
```

✅ Seu app estará no ar!

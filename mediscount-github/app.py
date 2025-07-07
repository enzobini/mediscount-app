import streamlit as st
import pandas as pd
import geopy.distance
import base64
import requests
import folium
from streamlit_folium import st_folium
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os
from dotenv import load_dotenv
from collections import defaultdict
from operator import itemgetter

# Carrega variáveis de ambiente
load_dotenv()

# Notificações e estado
if 'alertas' not in st.session_state:
    st.session_state.alertas = []
if 'historico' not in st.session_state:
    st.session_state.historico = []
if 'carrinho' not in st.session_state:
    st.session_state.carrinho = []

# Mock de dados
farmacias = [
    {"nome": "FarmaCentro", "produto": "Digoxina 0,25 mg, 30 comprimidos", "preco": 55.50, "coordenadas": (-23.561684, -46.625378), "avaliacao": 5},
    {"nome": "Drogaria São José", "produto": "Sonda vesical de demora nº 14", "preco": 7.50, "coordenadas": (-23.564123, -46.650123), "avaliacao": 4},
    {"nome": "Farmácia Popular", "produto": "Luvas cirúrgicas estéreis tamanho M - par", "preco": 3.90, "coordenadas": (-23.570000, -46.630000), "avaliacao": 3.5},
    {"nome": "SaúdeMais", "produto": "Seringa descartável 5ml com agulha", "preco": 1.30, "coordenadas": (-23.568700, -46.628000), "avaliacao": 4.5},
    {"nome": "Clínica Farma", "produto": "Esparadrapo hospitalar 10cm x 4,5m", "preco": 8.90, "coordenadas": (-23.566000, -46.620000), "avaliacao": 4.7},
    {"nome": "FarmaCentro", "produto": "Termômetro digital clínico", "preco": 22.00, "coordenadas": (-23.561684, -46.625378), "avaliacao": 4.2},
    {"nome": "OrtoFarma", "produto": "Andador articulado dobrável alumínio", "preco": 280.00, "coordenadas": (-23.563000, -46.629000), "avaliacao": 4.8},
    {"nome": "Saúde Total", "produto": "Oxímetro de dedo portátil", "preco": 139.90, "coordenadas": (-23.562500, -46.632000), "avaliacao": 4.4},
    {"nome": "Cirúrgica Brasil", "produto": "Máscara N95 hospitalar - unidade", "preco": 6.50, "coordenadas": (-23.560300, -46.626800), "avaliacao": 4.9},
    {"nome": "Hospitalar Express", "produto": "Bisturi lâmina nº 15 estéril descartável", "preco": 2.10, "coordenadas": (-23.559000, -46.624500), "avaliacao": 4.3},
    {"nome": "VitalMed", "produto": "Aparelho de pressão digital de pulso", "preco": 119.00, "coordenadas": (-23.565500, -46.627000), "avaliacao": 4.6},
    {"nome": "Vida Farma", "produto": "Gaze estéril compressa 7,5x7,5cm - pct 10un", "preco": 4.70, "coordenadas": (-23.567800, -46.630900), "avaliacao": 4.1},
    {"nome": "MedExpress", "produto": "Bomba de infusão portátil hospitalar", "preco": 1490.00, "coordenadas": (-23.568900, -46.631700), "avaliacao": 4.9}
]

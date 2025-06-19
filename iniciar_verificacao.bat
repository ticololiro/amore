@echo off
cd /d "%~dp0"
echo Iniciando Verificação de Amor...
python -m streamlit run verificacao_amor_local.py
pause

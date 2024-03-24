import time
import bs4
from bs4 import BeautifulSoup
#raspágem
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
#requisição de dados de uma API
import selenium
from selenium.webdriver.chrome.service import Service
#automação
from webdriver_manager.chrome import ChromeDriverManager
from googlesearch import search
import webbrowser
import requests

print('Digite algo a ser buscado: ')
termosBuscados = input()

print('Buscando os termos... ' + termosBuscados)

# faz a requisição ao buscar do google
res=requests.get('https://www.google.com/maps/search/'+ termosBuscados)
#verifica se a requisição foi bem sucedida
res.raise_for_status()

#bs4 analisa o html da página google retornada

parserSoup= bs4.BeautifulSoup(res.text, features='lxml')
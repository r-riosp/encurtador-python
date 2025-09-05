# 🔗 Encurtador de URL com Python & Flask

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white) ![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white) ![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black) ![SQLite](https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white) ![Render](https://img.shields.io/badge/Render-46E3B7?style=for-the-badge&logo=render&logoColor=white)

<!-- ### 🚀 [Acesse a aplicação ao vivo!](https://link_do_projeto.onrender.com) -->

---

## 📋 Índice

- [Sobre o Projeto](#-sobre-o-projeto)
- [✨ Features](#-features)
- [🛠️ Stack de Tecnologias](#-stack-de-tecnologias)
- [🔌 Endpoints da API](#-endpoints-da-api)

---

## 📖 Sobre o Projeto

Este é um projeto de um encurtador de URL completo, desenvolvido para demonstrar habilidades em desenvolvimento **Full Stack**, desde a criação da lógica de backend com **Python** e **Flask**, passando pela manipulação de um banco de dados **SQLite**, até a construção de uma interface de usuário reativa com **JavaScript** puro e, finalmente, o deploy da aplicação na nuvem utilizando **Render**.

O objetivo foi construir uma aplicação funcional, robusta e com boas práticas de desenvolvimento, servindo como uma peça de portfólio sólida e um campo de aprendizado prático.

---

## ✨ Features

- ✅ **API RESTful** para criação de links curtos.
- ✅ **Redirecionamento** rápido e eficiente de links encurtados.
- ✅ **Interface de usuário** simples e intuitiva para interação com a API.
- ✅ **Frontend reativo** que consome a API sem recarregar a página (SPA-like).
- ✅ **Deploy contínuo** configurado para a plataforma Render.

---

## 🛠️ Stack de Tecnologias

As seguintes ferramentas e tecnologias foram utilizadas na construção do projeto:

| Stack | Ferramenta |
|-------|------------|
| **Backend** | Python, Flask, Gunicorn |
| **Banco de Dados** | SQLite |
| **Frontend** | HTML5, CSS3, JavaScript |
| **Infra/Deploy** | Render, Git, GitHub |

---

## 🔌 Endpoints da API

A API possui os seguintes endpoints:

#### `POST /encurtar`
Cria um novo link encurtado.

- **Request Body:**
```json
{
  "link_original": "[https://www.google.com](https://www.google.com)"
}


# Solouse

Solouse is a private online learning platform designed to deliver an efficient and organized educational experience. With a robust backend built on Node.js and an intuitive frontend built on React, Solouse allows administrators (teachers) to create courses, assign exercises, manage students, and more. The platform includes support for teaching materials, video lessons, and quizzing features, making it a complete solution for managing and disseminating educational content.

## Installation

Steps to configure the environment and install dependencies:

```bash
git clone https://github.com/eliasabrell/Solouse.git
cd Solouse
npm install
```

## Configuration

Instructions for configuring environment variables, database, etc.

```bash
cp .env.example .env
npm run db:migrate
```

## Usage

How to start the project and access main features:

Start backend

```bash
cd backend
npm start
```

Start frontend

```bash
cd frontend
npm start
```

## Project Structure

```bash
solouse/
├── backend/
│   ├── app.py                  # Instância principal do Flask, registro de Blueprints
│   ├── config.py               # Configurações da aplicação (database, secrets, etc.)
│   ├── extensions.py           # Instâncias de extensões (SQLAlchemy, JWT, etc.)
│   ├── models/
│   │   ├── __init__.py
│   │   ├── user.py             # Modelo de usuário
│   │   ├── product.py          # Modelo de produto
│   │   └── order.py            # Modelo de pedido
│   ├── routes/
│   │   ├── __init__.py
│   │   ├── auth.py             # Rotas de autenticação (login, register)
│   │   ├── users.py            # Rotas de usuários (CRUD)
│   │   ├── products.py         # Rotas de produtos (CRUD)
│   │   └── orders.py           # Rotas de pedidos (CRUD)
│   ├── services/
│   │   ├── __init__.py
│   │   ├── user_service.py     # Lógica de negócio para usuários
│   │   ├── product_service.py  # Lógica de negócio para produtos
│   │   └── auth_service.py     # Lógica de negócio para autenticação
│   ├── utils/
│   │   ├── __init__.py
│   │   ├── decorators.py       # Decoradores personalizados (ex: @jwt_required)
│   │   └── validators.py       # Funções de validação
│   ├── migrations/             # Alembic migrations (se usar)
│   │   ├── versions/
│   │   └── env.py
│   ├── tests/
│   │   ├── __init__.py
│   │   ├── test_auth.py
│   │   └── test_users.py
│   ├── .env
│   └── run.py                  # Script para rodar a aplicação
├── frontend/
│   ├── node_modules/
│   ├── public/
│   │   └── index.html
│   ├── src/
│   │   ├── components/
│   │   ├── App.js
│   │   ├── App.css
│   │   └── index.js
│   └── package.json
├── .gitignore
└── README.md

```

## License

[MIT License](LICENSE).
See the `LICENSE` file for more details.

---

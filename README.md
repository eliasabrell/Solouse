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

```
solouse/
├── backend/
│   ├── node_modules/
│   ├── src/
│   │   ├── config/
│   │   ├── controllers/
│   │   ├── middleware/
│   │   ├── models/
│   │   └── routes/
│   ├── app.js
│   ├── server.js
│   ├── package.json
│   ├── .env
│   └── .nvmrc
├── frontend/
│   ├── node_modules/
│   ├── public/
│   │   └── index.html
│   ├── src/
│   │   ├── components/
│   │   ├── App.js
│   │   ├── App.css
│   │   ├── index.css
│   │   └── index.js
│   └── package.json
├── .gitignore
└── README.md
```

## License

[MIT License](LICENSE).
See the `LICENSE` file for more details. 

---
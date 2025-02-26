const express = require("express");
const app = express();
const port= process.env.PORT || 3000;
const massage = process.env.MESSAGE || "Hello World!";

app.get("/", (req, res) => {
    res.send(massage);
});

app.listen(port, () => {
    console.log(`Servidor rodando na porta ${port}`);
});

//Solouse is a Node.js app for creating courses and lessons. Teacher administrators can create courses, assign exercises and manage students. The app offers an intuitive interface and features to organize educational content efficiently.
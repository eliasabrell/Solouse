const express = require("express");
const app = express();
const massage = process.env.MESSAGE || "Hello World!";

app.get("/", (req, res) => {
    res.send(massage);
});

module.exports = app;

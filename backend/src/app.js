const express = require("express");
const homeRoutes = require("./routes/homeRoute");
const loginRoutes = require("./routes/loginRoute");
const signupRoutes = require("./routes/signupRoute");
const perfilRoutes = require("./routes/perfilRoute");
const coursesRoutes = require("./routes/coursesRoute");
const essaysRoutes = require("./routes/essaysRoute");
const supportRoutes = require("./routes/supportRoute");
const emailRoutes = require("./routes/emailRoute");
const databaseRoutes = require("./routes/databaseRoute");
//const cors = require("cors");

const app = express();


app.use(express.json());
app.use(express.urlencoded({ extended: false }));
//app.use(cors());

app.use("/", homeRoutes);
app.use("/", loginRoutes);
app.use("/", signupRoutes);
app.use("/", perfilRoutes);
app.use("/", coursesRoutes);
app.use("/", essaysRoutes);
app.use("/", supportRoutes);
app.use("/", emailRoutes);
app.use("/", databaseRoutes);

module.exports = app;

exports.getDatabase = async function (req, res) {
  const mysql = require('mysql2');
  const connection = mysql.createConnection({
    host: process.env.DB_HOST,
    user: process.env.DB_USER,
    password: process.env.DB_PASS,
    database: process.env.DB_NAME
  });
  connection.connect((err) => {
      if (err) {
          console.error("Error connecting:", err);
          res.status(500).send("Erro ao conectar ao banco de dados.");
          return;
      }
      res.send("Conexão bem-sucedida!");
      console.log("Connection sucessful!");
  });
};

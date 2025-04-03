const express = require("express");
const router = express.Router();
const databaseController = require("../controllers/databaseController");

router.get("/db", databaseController.getDatabase);

module.exports = router;
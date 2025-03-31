const express = require("express");
const router = express.Router();
const essaysController = require("../controllers/essaysController");

router.get("/essays", essaysController.getEssays);

module.exports = router;
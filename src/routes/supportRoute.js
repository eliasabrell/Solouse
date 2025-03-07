const express = require("express");
const router = express.Router();
const supportController = require("../controllers/supportController");

router.get("/support", supportController.getSupport);
router.post("/support", supportController.postSupport);

module.exports = router;
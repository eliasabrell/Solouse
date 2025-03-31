const express = require("express");
const router = express.Router();
const perfilController = require("../controllers/perfilController");

router.get("/perfil", perfilController.getPerfil);
router.put("/perfil", perfilController.putPerfil);

module.exports = router;
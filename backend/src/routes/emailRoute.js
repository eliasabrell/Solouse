const { validateEmail } = require('../middleware/validateEmail');
const { authenticate } = require('../middleware/authenticate');
const express = require('express');
const router = express.Router();
const emailController= require('../controllers/emailController');

router.post('/send-email', authenticate, validateEmail, emailController.postEmail);
router.get('/email', emailController.getEmail);

module.exports = router;
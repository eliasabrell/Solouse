const { validateEmail } = require('../middleware/validateEmail');
const { authenticate } = require('../middleware/authenticate');
const express = require('express');
const router = express.Router();
const sendEmail= require('../controllers/emailController');

router.post('/send-email', authenticate, validateEmail, emailController.postEmail);

module.exports = router;
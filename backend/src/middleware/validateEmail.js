const validateEmail = (req, res, next) => {
    const { to, subject, text } = req.body;
  
    if (!to || !subject || !text) {
      return res.status(400).json({ error: 'Todos os campos são obrigatórios.' });
    }
  
    next();
  };
  
  module.exports = { validateEmail };
const authenticate = (req, res, next) => {
  const token = req.headers['authorization'];

  if (!token || token !== 'seu-token') {
    return res.status(403).json({ error: 'Access denied!' });
  }

  next();
};

module.exports = { authenticate };
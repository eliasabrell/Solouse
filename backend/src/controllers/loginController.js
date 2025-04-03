exports.getLogin = (req, res) => {
  res.send("Login!");
};
exports.postLogin = (req, res) => {
  try {
    res.status(200).json({ message: 'Login successful!' });
  } catch (error) {
    res.status(500).json({ message: 'Failed to login.', error });
  }
};
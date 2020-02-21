const express = require('express');
const router = express.Router();

const checkAuth = require('../middleware/check-auth');

router.get('/', (req, res, next) => {
  res.status(200).json({ 'message': 'events API' });
});
router.get('/protected', checkAuth, (req, res, next) => {
  res.status(200).json({ 'message': 'events API' });
});


module.exports = router;

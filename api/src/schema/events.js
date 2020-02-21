const mongoose = require('mongoose');

const eventsSchema = new mongoose.Schema({
  title: String,
  desc: String,
  price: String,
}, { collection: 'events' });

module.exports = mongoose.model('Events', eventsSchema);

const mongoose = require('mongoose');

const profileSchema = new mongoose.Schema({
  displayName: String,
  username: String,
  bio: String,
  homeTown: String,
  events: [mongoose.Schema.ObjectId],
  genres: [
    { name: String, endorsedBy: Number },
  ],
}, { collection: 'profile' });

module.exports = mongoose.model('Profile', profileSchema);

const mongoose = require('mongoose');

const eventSchema = mongoose.Schema({
  _id: mongoose.Schema.Types.ObjectId,
  venue: {
    type: mongoose.Schema.Types.ObjectId,
    ref: 'User',
    required: true
  },
  title: {
    type: String,
    required: true
  },
  description: {
    type: String,
    required: true
  },
  startDate: {
    type: Date,
    required: true
  },
  endDate: {
    type: Date,
    required: true
  },
  price: {
    type: Number,
    required: true
  },
  bands: [
    {
      type: mongoose.Schema.Types.ObjectId,
      ref: 'User',
      required: true
    }
  ],
  createdBy: {
    type: mongoose.Schema.Types.ObjectId,
    required: true
  }

});
module.exports = mongoose.model('Event', eventSchema);
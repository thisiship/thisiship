const mongoose = require('mongoose');
const Event = require('../models/event');

exports.events_get_all = (req, res, next) => {
  Event.find()
  .select('title description startDate endDate price bands venue createdBy')
  .populate('venue', 'username _id')
  .populate('bands', 'username _id')
  .exec()
  .then(docs => {
    res.status(200).json({
      count: docs.length,
      events: docs.map(doc => {
        return {
          _id: doc._id,
          title: doc.title,
          description: doc.description,
          startDate: doc.startDate,
          endDate: doc.endDate,
          price: doc.price,
          bands: doc.bands,
          venue: doc.venue,
          createdBy: doc.createdBy,
          request: {
            type: 'GET',
            url: 'http://localhost:3001/events/' + doc._id
          }
        };
      })
    });
  })
  .catch(err => {
    res.status(500).json({
      error: err
    });
  });
};

exports.events_create_event = (req, res, next) => {
  const event = new Event({
    _id: new mongoose.Types.ObjectId(),
    title: req.body.title,
    description: req.body.description,
    price: req.body.price,
    bands: req.body.bands,
    venue: req.body.venue,
    startDate: req.body.startDate,
    endDate: req.body.endDate,
    createdBy: req.userData.userId
  });
  event.save().then(result => {
    console.log(result);
    res.status(201).json({
      createdEvent: {
        title: result.title,
        description: result.description,
        price: result.price,
        _id: result._id,
        bands: result.bands,
        venue: result.venue,
        startDate: result.startDate,
        endDate: result.endDate,
        createdBy: result.createdBy,
      },
      request: {
        type: 'GET',
        url: 'http://localhost:3001/events/' + result._id
      }
    });
  })
  .catch(err => {
    console.log(err)
    res.status(500).json({
      error: err
    });
  });
};

exports.events_get_event = (req, res, next) => {
  Event.findById(req.params.eventId)
  .populate('venue', 'username _id')
  .populate('bands', 'username _id')
  .exec()
  .then(event => {
    if (!event) {
      return res.status(404).json({
        message: 'Event Not Found'
      });
    }
    res.status(200).json({
      event: {
        title: event.title,
        description: event.description,
        price: event.price,
        _id: event._id,
        bands: event.bands,
        venue: event.venue,
        startDate: event.startDate,
        endDate: event.endDate,
        createdBy: event.createdBy,
      },
      request: {
        type: 'GET',
        url: 'http://localhost:3001/events'
      }
    });
  })
  .catch(err => {
    res.status(500).json({
      error: err
    });
  });
};

exports.events_delete_event = (req, res, next) => {
  Event.remove({_id: req.params.eventId})
  .exec()
  .then(result => {
    res.status(200).json({
      message: 'Event Deleted',
      request: {
        type: 'POST',
        url: 'http://localhost:3001/events',
        body: {
          title: 'String',
          description: 'String',
          price: 'Number',
          bands: '[ID]',
          venue: 'ID',
          startDate: 'Date',
          endDate: 'Date'
        }
      }
    });
  })
  .catch(err => {
    res.status(500).json({
      error: err
    });
  });
};

exports.events_get_event_by_user_id = (req, res, next) => {
  Event.find({createdBy: req.params.userId})
  .select('title description startDate endDate price bands venue createdBy')
  .populate('venue', 'username _id')
  .populate('bands', 'username _id')
  .exec()
  .then(docs => {
    res.status(200).json({
      count: docs.length,
      events: docs.map(doc => {
        return {
          _id: doc._id,
          title: doc.title,
          description: doc.description,
          startDate: doc.startDate,
          endDate: doc.endDate,
          price: doc.price,
          bands: doc.bands,
          venue: doc.venue,
          request: {
            type: 'GET',
            url: 'http://localhost:3001/events/' + doc._id
          }
        };
      })
    });
  })
  .catch(err => {
    res.status(500).json({
      error: err
    });
  });
};
const express = require('express');
const router = express.Router();
const mongoose = require('mongoose');

const Profile = require('./schema/profile.js');

mongoose.connect('mongodb://localhost/thisiship', { useNewUrlParser: true, useUnifiedTopology: true });

router.get('/', (req, res, next) => {
  res.status(200).json({message: 'Hello World'});
});

router.post('/profile', (req, res, next) => {
  Profile.create({
    displayName: req.body.displayName,
    username: req.body.username,
    bio: req.body.bio,
    homeTown: req.body.homeTown,
    events: [],
    genres: []
  })
    .then(response => {
      res.status(200).json(response);
    })
    .catch(err => {
      res.status(500).json(err);
    });

});

router.get('/profile', (req, res, next) => {
  Profile.find({})
    .then(docs => {
      res.status(200).json(docs);
    })
    .catch(err => {
      res.status(500).json(err);
    });
});

router.get('/profile/:username', (req, res, next) => {
  Profile.find({username: req.params.username})
    .then(docs => {
      res.status(200).json(docs);
    })
    .catch(err => {
      res.status(500).json(err);
    });
})

module.exports = router;

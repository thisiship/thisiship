const express = require('express');
const app = express();
const morgan = require('morgan');
const bodyParser = require('body-parser');
const mongoose = require('mongoose');

const indexRoutes = require('./routes/index');
const authRoutes = require('./routes/auth');
const eventsRoutes = require('./routes/events');

mongoose.connect('mongodb://localhost:27017/thisiship', {
  useNewUrlParser: true,
  useUnifiedTopology: true,
  useCreateIndex: true
})
  .then(() => console.log('Connected to MongoDB!'))
  .catch((err) => console.log(err));

app.use(morgan('dev'));
app.use(bodyParser.urlencoded({ extended: false }));
app.use(bodyParser.json());

// handle cors errors
app.use((req, res, next) => {
  res.header('Access-Control-Allow-Origin', '*');
  res.header('Access-Control-Allow-Headers', 'Origin, X-Requested-With, Content-Type, Accept, Authorization');
  if (req.method === 'OPTIONS') {
    res.header('Access-Control-Allow-Methods', 'PUT, POST, PATCH, DELETE, GET');
    return res.status(200).json({});
  }
  next();
});

// routing
app.use('/', indexRoutes);
app.use('/auth', authRoutes);
app.use('/events', eventsRoutes);

app.use((req, res, next) => {
  const error = new Error('Not Found');
  error.status = 404;
  next(error);
});

// this middleware will catch any errors sent through and return the error to the UI
app.use((err, req, res, next) => {
  res.status(err.status || 500);
  res.json({
    error: err,
    message: err.message
  });
});

module.exports = app;

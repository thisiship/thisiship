const express = require('express');
const app = express();
const morgan = require('morgan');
const bodyParser = require('body-parser');
const mongoose = require('mongoose');

/*
const productRoutes = require('./api/routes/products');
const orderRoutes = require('./api/routes/orders');
*/
const userRoutes = require('./api/routes/user');

mongoose.connect(
  `mongodb+srv://tonisbones:${process.env.MONGO_ATLAS_PW}@thisiship-5gtlj.mongodb.net/thisiship?retryWrites=true`,
  {
    useNewUrlParser: true
  });
mongoose.Promise = global.Promise;

// middleware
app.use(morgan('dev'));
app.use(bodyParser.urlencoded({extended: false}));
app.use(bodyParser.json());

// CORS middleware
app.use((res, req, next) => {
  res.header('Access-Control-Allow-Origin', '*');
  res.header('Access-Control-Allow-Headers', 'Origin, X-Requested-With, Content-Type, Accept, Authorization');
  if (req.method === 'OPTIONS') {
    res.header('Access-Control-Allow-Methods', 'PUT, POST, PATCH, DELETE, GET');
    return res.status(200).json({});
  }
  next();
});

// routes
/*
app.use('/products', productRoutes);
app.use('/orders', orderRoutes);
*/
app.use('/user', userRoutes)

// handle any requests that aren't mapped in any routers 
app.use((req, res, next) => {
  const error = new Error('Not Found');
  error.status = 404;
  next(error);
});

// cascade any errors back to requester
app.use((error, req, res, next) => {
  res.status(error.status || 500);
  res.json({
    error: {
      message: error.message
    }
  });
});

module.exports = app;
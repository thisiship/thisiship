const express = require('express');
const router = express.Router();
const checkAuth = require('../middleware/check-auth');

const EventsController = require('../controllers/events');

router.get('/', EventsController.events_get_all);

router.post('/', checkAuth, EventsController.events_create_event);

router.get('/:eventId', EventsController.events_get_event);

router.delete('/:eventId', checkAuth, EventsController.events_delete_event);

router.get('/user/:userId', EventsController.events_get_event_by_user_id);

module.exports = router;
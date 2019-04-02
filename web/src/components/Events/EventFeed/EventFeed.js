import React, { useEffect, useReducer } from 'react';
import axios from 'axios';

import Event from '../Event/Event';
import { useFormInput } from '../../../hooks/forms';
import classes from './EventFeed.module.css';

const eventFeed = (props) => {
  const titleInput = useFormInput();
  const priceInput = useFormInput();
  const venueInput = useFormInput();

  const eventFeedReducer = (state, action) => {
    switch(action.type) {
      case 'ADD':
        return state.concat(action.payload);
      case 'SET':
        return action.payload;
      case 'REMOVE':
        return state.filter((event) => event.id !== action.payload);
      default:
        return state;
    }
  }

  const [eventFeed, dispatch] = useReducer(eventFeedReducer, []);

  const createEventHandler = () => {
    const eventTitle = titleInput.value;
    const eventPrice = priceInput.value;
    const eventVenue = venueInput.value;
    axios.post('https://mock-thisiship.firebaseio.com/events.json', {
      title: eventTitle,
      price: eventPrice,
      venue: eventVenue,
      userId: 'tonisbones',
    })
    .then((response) => {
      console.log(response);
      const eventData = response.data;
      const events = [];
      for (let key in eventData) {
        events.push({
          id: key,
          title: eventTitle,
          venue: eventVenue,
          price: eventPrice,
        });
      }
      dispatch({
        type: 'ADD',
        payload: events,
      });
    })
    .catch((error) => {
      console.log(error);
    });
  };

  useEffect(() => {
    axios.get('https://mock-thisiship.firebaseio.com/events.json')
    .then(response => {
      const eventData = response.data;
      const events = [];
      for (const key in eventData) {
        events.push({
          id: key,
          title: eventData[key].title,
          price: eventData[key].price,
          venue: eventData[key].venue,
        });
      }
      dispatch({
        type: 'SET',
        payload: events,
      });
    })
  }, []);

  return (
    <div>
      <h3>Event Feed</h3>
      <div className={classes.EventFeed}>
        {eventFeed.map(event => (
          <Event
            key={event.id}
            title={event.title}
            price={event.price}
            venue={event.venue} />
        ))}
      </div>
      <h4>Create Event</h4>
      <input
        type="text"
        placeholder="Event Title"
        onChange={titleInput.onChange}
        value={titleInput.value} />
      <input
        type="text"
        placeholder="Event Price"
        onChange={priceInput.onChange}
        value={priceInput.value} />
      <input
        type="text"
        placeholder="Event Venue"
        onChange={venueInput.onChange}
        value={venueInput.value} />
      <button
        type="button"
        onClick={createEventHandler}>Create Event</button>
    </div>
  )
};

export default eventFeed;

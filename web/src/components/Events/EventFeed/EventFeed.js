import React, { useEffect, useReducer } from 'react';
import axios from 'axios';

import Event from '../Event/Event';
import classes from './EventFeed.module.css';
import CreateEvent from '../CreateEvent/CreateEvent';

const eventFeed = (props) => {
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
      <CreateEvent dispatch={dispatch}/>
    </div>
  )
};

export default eventFeed;

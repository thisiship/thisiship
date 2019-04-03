import React from 'react';
import axios from 'axios';
import Input from '@material-ui/core/Input';
import Button from '@material-ui/core/Button';

import { useFormInput } from '../../../hooks/forms';

const createEvent = (props) => {
  const titleInput = useFormInput();
  const priceInput = useFormInput();
  const venueInput = useFormInput();

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
      props.dispatch({
        type: 'ADD',
        payload: events,
      });
    })
    .catch((error) => {
      console.log(error);
    });
  };
  return (
    <div>
      <h4>Create Event</h4>
      <Input
        type="text"
        required
        placeholder="Event Title"
        onChange={titleInput.onChange}
        value={titleInput.value} />
      <Input
        type="text"
        required
        placeholder="Event Price"
        onChange={priceInput.onChange}
        value={priceInput.value} />
      <Input
        type="text"
        required
        placeholder="Event Venue"
        onChange={venueInput.onChange}
        value={venueInput.value} />
      <Button
        variant="contained"
        color="primary"
        onClick={createEventHandler}>Create Event</Button>
    </div>
  );
};

export default createEvent;

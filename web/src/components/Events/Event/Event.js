import React from 'react';

import classes from './Event.module.css';

const event = (props) => {
  return (
    <div className={classes.Event}>
      <h4 className={classes.Title}>{props.title}</h4>
      <p className={classes.Price}>${props.price}</p>
      <p>{props.venue}</p>
    </div>
  );
};

export default event;

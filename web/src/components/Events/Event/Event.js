import React from 'react';
import Card from '@material-ui/core/Card';
import CardActions from '@material-ui/core/CardActions';
import CardContent from '@material-ui/core/CardContent';
import Button from '@material-ui/core/Button';
import Typography from '@material-ui/core/Typography';
import Divider from '@material-ui/core/Divider';

import classes from './Event.module.css';

const event = (props) => {
  return (
    <Card className={classes.Event}>
      <CardContent>
        <Typography variant="h5" gutterBottom>{props.title}</Typography>
        <hr />
        <Typography gutterBottom>${props.price}</Typography>
        <Typography gutterBottom>{props.venue}</Typography>
      </CardContent>
      <Divider variant="middle" />
      <CardActions>
        <Button
          size="small"
          color="primary"
          variant="contained">SHOUT</Button>
        <Button
          size="small"
          color="secondary"
          variant="contained">ENDORSE</Button>
      </CardActions>
    </Card>
  );
};

export default event;

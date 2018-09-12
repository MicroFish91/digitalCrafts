import React, { Component } from 'react';
import Products from './Products';
import Rating from './Rating';
import {Button} from 'react-bootstrap';


class App extends Component {
  render() {
    return (
      <div>

        <Products />

        <Rating rating="1" />
        <Rating rating="2" />
        <Rating rating="3" />
        <Rating rating="4" />
        <Rating rating="5" />

        <Button bsStyle="danger">My Button</Button>
        
      </div>
    );
  }
}

export default App;

import React, { Component } from 'react';

import {Media} from 'react-bootstrap';
import Product from './Product';

class Product extends Component {
  render() {
    return (
      <div>
          <Media>
              <Media.Left>
                  <img />
              </Media.Left>
              
              <Media.Body>
                  <Media.Heading>Media Heading</Media.Heading>
              </Media.Body>


          </Media>
      </div>
    );
  }
}

export default Product;

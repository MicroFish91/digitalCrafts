import React, { Component } from 'react';


class Products extends Component {
  render() {

    let productList = ['soap', 'shoes', 'rum', 'chicken'];
    let newProductList = productList.map((product) => {
        return <li key={product}>{product}</li>;
    });

    return (
      <div>
        <ul>

            {newProductList}

        </ul>
      </div>
    );
  }
}

export default Products;

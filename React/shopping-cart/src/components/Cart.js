import React, {Component} from 'react';
import ReactDOM from 'react-dom';

import AddProduct from './AddProduct';

class Cart extends Component {

    constructor(props){
        super(props);
    }

  render() {
    return (
      <div>

        <AddProduct addProduct={this.props.onAddProduct} />

        <table>
            <thead>
                <tr>
                    <th>Product Name</th>
                    <th>Product Price</th>
                    <th>#</th>
                </tr>
            </thead>
            <tbody>
                {
                    this.props.productCart.map(productData => {
                        return <tr key={productData.productName}>
                            <td>{productData.productName}</td>
                            <td>{productData.productPrice}</td>
                            <td onClick={() => {
                                {this.props.onRemoveProduct(productData)}
                            }}>X</td>
                        </tr>
                    })
                }
            </tbody>
        </table>
      </div>
    )
  }

}

export default Cart;

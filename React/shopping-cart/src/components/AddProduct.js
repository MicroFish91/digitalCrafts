import React, {Component} from 'react';

class AddProduct extends Component {

    constructor(props){
        super(props);
        this.state = {
            productName: "",
            productPrice: 0
        }
    }

    nameUpdate(event){

        this.setState({productName: event.target.value});

    }

    priceUpdate(event){

        this.setState({productPrice: event.target.value});

    }

    render() {
        return (

            <div>

                <input type="text" placeholder="Product Name" value={this.state.productName} onChange={this.nameUpdate.bind(this)} />

                <input type="text" placeholder="Product Price" value={this.state.productPrice} onChange={this.priceUpdate.bind(this)} />

                <button onClick={() => this.props.addProduct({
                    productName: this.state.productName,
                    productPrice: this.state.productPrice
                })}
                >Add Product</button>
                
            </div>
        )
    }
}

export default AddProduct;

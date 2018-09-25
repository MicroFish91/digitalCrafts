import {connect} from 'react-redux';

import Cart from './components/Cart';
import addProduct from './actions/addProduct';
import removeProduct from './actions/removeProduct';

function mapStateToProps(state){

  return {
    totalCost: state.totalCost,
    productCart: state.productCart
  }

}

function mapDispatchToProps(dispatch){

  return {
    onAddProduct: (productData) => dispatch(addProduct(productData)),
    onRemoveProduct: (productData) => dispatch(removeProduct(productData))
  }

}

var connectedComponent = connect(
  mapStateToProps,
  mapDispatchToProps,
)(Cart);

export default connectedComponent;

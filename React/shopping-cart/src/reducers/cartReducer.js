function cartReducer(state, action){

    if (state === undefined){

        return {
            totalCost: 0,
            productCart: []
        }
    }

    switch(action.type){

        case "addProduct":
            
            return {
                totalCost: state.totalCost + parseInt(action.productData.productPrice),
                productCart: state.productCart.concat(
                    {
                        productName: action.productData.productName,
                        productPrice: action.productData.productPrice
                    }
                )
            };

        case "removeProduct":

            return {

                totalCost: state.totalCost - parseInt(action.productData.productPrice),
                productCart: state.productCart.filter(productData => {
                    return (productData.productName !== action.productData.productName);
                })
                
            };

        default:
            return state;
    }

}

export default cartReducer;
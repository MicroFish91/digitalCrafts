function removeProduct(item){

    return {
        type: "removeProduct",
        productData: item
    };

}

export default removeProduct;
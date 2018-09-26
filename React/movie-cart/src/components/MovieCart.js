import React, { Component } from 'react';

class MovieCart extends Component {

    constructor(props){
        super(props);
    }

    render() {

        var cart = [];

        if (this.props.userCart !== undefined){

            if(this.props.userCart.length > 0){

                cart = this.props.userCart.map(movie => {

                    return <div>

                        Title: {movie.title}
                        Price: {movie.price}
                        <img src={movie.image}></img>
                        <button onClick={() => this.props.onRemoveMovie(movie)}>Remove Movie</button>

                    </div>

                })
            }
        }

        return (

            <div>

                <b><u>USER CART</u></b>: <br></br>

                Total Cost: {this.props.cost}

                {cart}
        
            </div>
        )
    }
}

export default MovieCart;

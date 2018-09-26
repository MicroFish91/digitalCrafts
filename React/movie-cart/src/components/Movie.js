import React, { Component } from 'react';

import DisplayMovies from './DisplayMovies';
import MovieCart from './MovieCart';

class Movie extends Component {

    constructor(props){
        super(props);
    }

    render() {

        return (

            <div>

                <MovieCart cost={this.props.cost} onRemoveMovie={this.props.onRemoveMovie} userCart={this.props.userCart} />

                <DisplayMovies onFetch={this.props.onFetch} movies={this.props.movies} onAddMovie={this.props.onAddMovie} />
        
            </div> 
        )
    }
}

export default Movie;
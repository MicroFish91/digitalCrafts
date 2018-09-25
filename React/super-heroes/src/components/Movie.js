import React, { Component } from 'react';

// Material UI
import Card from '@material-ui/core/Card';
import CardActionArea from '@material-ui/core/CardActionArea';
import CardActions from '@material-ui/core/CardActions';
import CardContent from '@material-ui/core/CardContent';
import CardMedia from '@material-ui/core/CardMedia';

import AddMovie from './AddMovie';

class Movie extends Component {
  
    render() {

        return (
            <div>

                <AddMovie addMovie={this.props.onAddMovie} />

                {this.props.movies.map(movie => {

                    return <div>

                        <div>

                            {movie.title} 

                            <img src={movie.image}></img> 

                            <button onClick={() => {
                                this.props.onRemoveMovie(movie)
                            }}> X </button>  

                        </div>

                    </div>

                })}


            </div>
    )
  }
}

export default Movie;

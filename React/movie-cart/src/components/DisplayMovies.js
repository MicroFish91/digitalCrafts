import React, { Component } from 'react'

class DisplayMovies extends Component {

    constructor(props){
        super(props);
    }

    componentWillMount(){
        fetch('http://www.omdbapi.com/?s=batman&apikey=c4995339')
        .then(results => results.json())
        .then(results => this.props.onFetch(results))
    }
    
    render() {

        var movies = [];

        if (this.props.movies !== undefined){

            if (this.props.movies.length > 0) {

                movies = this.props.movies.map(movie => {

                    return <div key={movie.title}>
                        
                            Title: {movie.title}
                            Price: {movie.price}
                            Click to Add
                            <img src={movie.image} onClick={() => this.props.onAddMovie(movie)}
                            ></img>

                        </div>

                    })
                }
            }

        return (

            <div>

                <b><u>MOVIE CHOICES</u></b>:   <br></br>

                {movies}
        
            </div>
        )
    }
}

export default DisplayMovies;

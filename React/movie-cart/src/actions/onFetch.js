function onFetch(movieList){

    var newList = movieList.Search.map(movie => {
        let newMovie = {};
        newMovie.title = movie.Title;
        newMovie.price = Math.random() * 60;
        newMovie.image = movie.Poster;

        return newMovie;
    })

    return {
        type: "onFetch",
        movieList: newList
    }

}

export default onFetch;
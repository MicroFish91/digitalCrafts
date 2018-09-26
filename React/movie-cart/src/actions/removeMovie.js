function removeMovie(movie){

    return {
        type: "removeMovie",
        movieData: {
            title: movie.title,
            price: movie.price,
            image: movie.image
        }
    }

}

export default removeMovie;
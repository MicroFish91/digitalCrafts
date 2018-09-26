function addMovie(movie){

    return {
        type: "addMovie",
        movieData: {
            title: movie.title,
            price: movie.price,
            image: movie.image
        }
    }

}

export default addMovie; 
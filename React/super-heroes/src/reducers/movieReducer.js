function movieReducer(state, action){

    if (state === undefined){

        return {
            movies: []
        }

    }

    switch(action.type){

        case "addMovie":
        
            return {
                ...state,
                movies: state.movies.concat({
                    title: action.movieData.title,
                    image: action.movieData.image
                })
            };

        case "removeMovie":
            return {
                ...state,
                movies: state.movies.filter(movie => {
                    return (movie.title !== action.movieData.title);
                })
            }

        default:
            return state;

    }

}

export default movieReducer;
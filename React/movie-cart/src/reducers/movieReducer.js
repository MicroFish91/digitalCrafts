function movieReducer(state, action){

    if (state === undefined){
        return {
            cost: 0,
            movies: [],
            userCart: []
        }
    }

    switch(action.type){

        case "addMovie":

            return {
                ...state,
                userCart: state.userCart.concat(action.movieData),
                cost: state.cost + parseInt(action.movieData.price)
            }

        case "removeMovie":

            return {
                ...state,
                userCart: state.userCart.filter(movie => {
                    return (movie.title !== action.movieData.title);
                }),
                cost: state.cost - parseInt(action.movieData.price)
            }

        case "onFetch":

            return {
                ...state,
                movies: action.movieList
            }

        default:

            return state;


    }

}

export default movieReducer;
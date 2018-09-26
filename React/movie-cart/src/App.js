import {connect} from 'react-redux';

import addMovie from './actions/addMovie';
import removeMovie from './actions/removeMovie';
import onFetch from './actions/onFetch';
import Movie from './components/Movie';

function mapStateToProps(state){
    
    return {
        cost: state.cost,
        movies: state.movies,
        userCart: state.userCart
    }

}

function mapDispatchToProps(dispatch){

    return {
        onAddMovie: (movieData) => dispatch(addMovie(movieData)),
        onRemoveMovie: (movieData) => dispatch(removeMovie(movieData)),
        onFetch: (movieData) => dispatch(onFetch(movieData))
    }

}

var connectedComponent = connect(
    mapStateToProps,
    mapDispatchToProps,
)(Movie);

export default connectedComponent;

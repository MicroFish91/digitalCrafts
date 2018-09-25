import {connect} from 'react-redux';

import addMovie from './actions/addMovie';
import removeMovie from './actions/removeMovie';
import Movie from './components/Movie';

function mapStateToProps(state){

    return {
        movies: state.movies
    }

}

function mapDispatchToProps(dispatch){

    return {
        onAddMovie: (movieData) => dispatch(addMovie(movieData)),
        onRemoveMovie: (movieData) => dispatch(removeMovie(movieData))
    }
}

var connectedComponent = connect(
    mapStateToProps,
    mapDispatchToProps
)(Movie);


export default connectedComponent;

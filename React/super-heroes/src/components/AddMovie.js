import React, { Component } from 'react';

import Button from '@material-ui/core/Button';
import MenuItem from '@material-ui/core/MenuItem';
import TextField from '@material-ui/core/TextField';

class AddMovie extends Component {

    constructor(props){
        super(props);
        this.state = {
            movieName: "",
            movieURL: ""
        }
    }

    addName(event){
        this.setState({movieName: event.target.value});
    }

    addURL(event){
        this.setState({movieURL: event.target.value});
    }

    render() {

    return (

      <div>

        <TextField placeholder="Movie Title" value={this.state.movieName} onChange={this.addName.bind(this)}></TextField>
        <TextField placeholder="Movie Image" value={this.state.movieURL} onChange={this.addURL.bind(this)}></TextField>

        <Button color="primary" onClick={() => {
            this.props.addMovie({
                title: this.state.movieName,
                image: this.state.movieURL
            })
        }}>Add Movie</Button>
        
      </div>
    )
  }
}

export default AddMovie;
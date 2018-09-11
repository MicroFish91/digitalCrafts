import React, { Component } from 'react';

class MyState extends Component {
  
    constructor(props){
        super(props);
        this.state = {
            txt: "hello world",
            count: 1
        }
    }

    update(e){
      this.setState({txt: e.target.value});
    }

    render() {
    return (
      <div>
        {/* {this.state.txt} */}
        <h1>{this.state.txt} {this.state.count}</h1>
        <input type="text" onChange={this.update.bind(this)}></input>

      </div>
    );
  }
}

export default MyState;

import React, { Component } from 'react';

class Name extends Component {
  
    formatName(user){
        return user.firstName + ' ' + user.lastName;
    }
  
    render() {

    let user = {firstName: 'Veronica', lastName: 'Lino'};

    return (

      <div>
        <h2>Hello, {this.formatName(user)}</h2>
      </div>
    );
  }
}

export default Name;

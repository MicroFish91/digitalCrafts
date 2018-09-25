import React, { Component } from 'react';
import ReactDOM from 'react-dom';


class ContactItem extends Component {

  render() {

    var myContacts = [];

    console.log(this.props.contact);

    myContacts = this.props.contact.map(contact => {
        return <div>
          Name: {contact.name}, Email: {contact.email}, Phone Number: {contact.number}, Address: {contact.address}, City: {contact.city}, State: {contact.state}, Zip Code: {contact.zip}
           <a href="#" onClick="">X</a>
          </div>;
    })


    return (
      <div>

        {myContacts}
        
      </div>
    );
  }
}

export default ContactItem;

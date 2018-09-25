import React, { Component } from 'react';
import ReactDOM from 'react-dom';

import ContactItem from './ContactItem';
import PropTypes from 'prop-types';


class Form extends Component {

  constructor(props) {
    super(props)
  
    this.state = {
      contacts: [
        {
          name: "Joe",
          email: "joe@joe.com",
          number: 1,
          address: "myaddress on Baker St.",
          city: "Houston",
          state: "TX",
          zip: 77000
        },
        {
          name: "push",
          email: "push@joe.com",
          number: 1,
          address: "myaddress on Baker St.",
          city: "Houston",
          state: "TX",
          zip: 77000
        },
        {
          name: "Matt",
          email: "matt@joe.com",
          number: 1,
          address: "myaddress on Baker St.",
          city: "Houston",
          state: "TX",
          zip: 77000
        }
      ]
    }
  }

  // Pass current state of contacts and returns sorted array of contacts
  sortAlphabetically(contactList){
    
    var sortedNames = contactList.map(word => (word.name.toLowerCase()));
    var unsortedNames = sortedNames.slice();
    var sortedList = [];

    sortedNames.sort();

    sortedNames.forEach((word) => {

      sortedList.push(contactList[unsortedNames.indexOf(word)]);

    })

    return sortedList;

  }

  // Take value of contacts and push into this.state.contacts
  makeContact(e){

    e.preventDefault();

    var newContacts = this.state.contacts;

    var contacts = {};

    contacts.name = this.refs.Name.value;
    contacts.email = this.refs.Email.value;
    contacts.number = this.refs.Phone.value;
    contacts.address = this.refs.Address.value;
    contacts.city = this.refs.City.value;
    contacts.state = this.refs.State.value;
    contacts.zip = this.refs.Zip.value;

    newContacts.push(contacts);

    this.setState({contacts: newContacts});

  }

  onDelete(){

    

  }
  

  render() {

    // Field Parameters
    var contactInfo = ["Name", "Email", "Phone", "Address", "City", "State", "Zip"];

    var sortedContacts = [];

    // If array exists, map it to show below form
    if (this.state.contacts.length > 0){

      // Sort
      sortedContacts = this.sortAlphabetically(this.state.contacts);

    }

    console.log(sortedContacts);

    // Converts to Array of Search Fields
    var contactFields = contactInfo.map(value => {
        return (

            <div>

            <label>
            {value}:
            <input type="text" ref={value} key={value} />
            </label>

            <br></br>

            </div>
        )
    })

    

    return (
      <div>
        <form>
            
            {/* Posts via Array of Search Fields */}
            {contactFields}
            
            <input type="submit" value="Submit" onClick={this.makeContact.bind(this)} />
        </form>

        <div>

          <ContactItem key={sortedContacts.name} contact={sortedContacts}  />

        </div>


      </div>
    );
  }
}

export default Form;

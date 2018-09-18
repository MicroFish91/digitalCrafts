import React, { Component } from 'react';
import ReactDOM from 'react-dom';


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
          email: "joe@joe.com",
          number: 1,
          address: "myaddress on Baker St.",
          city: "Houston",
          state: "TX",
          zip: 77000
        },
        {
          name: "Matt",
          email: "joe@joe.com",
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
    
    var contactNames = contactList.map(word => (word.name));
    var sortedList = [];
    
    contactNames.sort();

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
  

  render() {

    // Field Parameters
    var contactInfo = ["Name", "Email", "Phone", "Address", "City", "State", "Zip"];

    var myContacts = [];
    var sortedContacts = [];

    // If array exists, map it to show below form
    if (this.state.contacts.length > 0){

      // Sort
      sortedContacts = this.sortAlphabetically(this.state.contacts);

      // Map
      myContacts = sortedContacts.map(contact => {
      return <p> Name: {contact.name}, Email: {contact.email}, Phone Number: {contact.number}, Address: {contact.address}, City: {contact.city}, State: {contact.state}, Zip Code: {contact.zip}</p>;
      })

    }

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

          {myContacts}

        </div>


      </div>
    );
  }
}

export default Form;

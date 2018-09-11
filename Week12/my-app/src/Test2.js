import React, { Component } from 'react';
import PropTypes from 'prop-types';

class Test2 extends Component {
  render() {

    let students = ['Matt', 'Eric', 'Travis', 'Hussein', 'Tracy', 'Melissa', 'Skylar'];

    return (
      <div>
          <ul>
              {students.map(student => {
                  return <li key={student}>{student}</li>;
              })}
          </ul>
      </div>
    );
  }
}

Test2.propTypes = {
    txt: PropTypes.string,
    cat: PropTypes.number.isRequired
}

export default Test2;

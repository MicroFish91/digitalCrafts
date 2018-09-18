import React, { Component } from 'react';

import MemoryCard from './MemoryCard';
import './App.css';

class App extends Component {
  render() {
    return (
      <div className="App">
        <header className="App-header">
          <h1 className="App-title">Memory Game</h1>
          <h3>Match Cards to Win</h3>
        </header>
        <div>
        <MemoryCard />
        <MemoryCard />
        <MemoryCard />
        <MemoryCard />
        </div>
        <div>
        <MemoryCard />
        <MemoryCard />
        <MemoryCard />
        <MemoryCard />
        </div>
        <div>
        <MemoryCard />
        <MemoryCard />
        <MemoryCard />
        <MemoryCard />
        </div>
        <div>
        <MemoryCard />
        <MemoryCard />
        <MemoryCard />
        <MemoryCard />
        </div>
      </div>
    );
  }
}

export default App;

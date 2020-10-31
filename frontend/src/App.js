import React from "react";
import BillInfo from './Components/BillInfo/BillInfo'
import VoteResults from './Components/VoteResults/VoteResults'
import './App.css';


function App() {
  return (
    <div className="App">
      <VoteResults />
      <BillInfo />
    </div>
  );
}

export default App;

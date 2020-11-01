import React from "react";
import BillInfo from './Components/BillInfo/BillInfo'
import VoteResults from './Components/VoteResults/VoteResults'
import './App.css';


function App() {
	const voteTitleStyle={
		width:"30%",
		margin:"auto"
	};
  return (
    <div className="App">
	  <div className="Votes">
	  	<h2 className="vote-title" style={voteTitleStyle}>Vote Results</h2>
	  	<VoteResults />
	  </div>
	  <BillInfo />
    </div>
  );
}

export default App;

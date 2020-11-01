import React from "react";
import BillInfo from './Components/BillInfo/BillInfo'
import VoteResults from './Components/VoteResults/VoteResults'
import './App.css';


function App() {
	const voteTitleStyle={
		width:"40%",
		margin:"auto"
	};
	const BillTitleStyle={
		width:"40%",
		margin:"auto"
	};
  return (
    <div className="App">
	  <div className="Votes">
	  	<h2 className="vote-title" style={voteTitleStyle}>Vote Results</h2>
	  	<VoteResults />
	  </div>
	  <div classNaame="Bills">
	  	<h2 className="bill-title" style={BillTitleStyle}>Bill Info</h2>
	  	<BillInfo />
	  </div>
    </div>
  );
}

export default App;

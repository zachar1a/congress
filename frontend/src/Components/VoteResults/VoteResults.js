import React from "react";
import Card from "../Card/Card";
import Navbar from "../Navbar/Navbar";

const url = "https://state-of-congress.herokuapp.com/api/results/"

//This is for testing the backend
//const url = "http://localhost:8000/api/results/"
class VoteResults extends React.Component{

    constructor(props){
        super(props);
        this.state={
            results: [],
        };
    }
    componentDidMount(){
        fetch(url)
        .then(data=> data.json())
        .then(data=>this.setState({results:data}));
        console.log(this.state.results);
    }

    render(){
        const resultItems = this.state.results.map((result)=>{
            return(
		    <Card name={result.number} title={result.title} chamber={result.chamber} result={result.Result} action={result.action} />
		    /*
                <div className="resultCard">
		    <br/>
                    <br/>Number: <i>{result.number}</i> 
		    <br/>Title: <b>{result.title}</b>
		    	<br/><a href={result.Source}>Congressional Votes</a>
                        <br/>Action: {result.action}
                        <br/>Result: {result.Result}
		    <br/>
                </div>
	    */
            );
         });
        return[
		<Navbar />
            	,resultItems
	];
        };
}

export default VoteResults;

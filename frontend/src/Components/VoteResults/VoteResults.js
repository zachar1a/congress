import React from "react";

const url = "https://state-of-congress.herokuapp.com/api/results/"

//This is for testing the backend
//const url = "localhost:8000/api/results/"
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
                <div className="resultCard">
                    <h2>[{result.sponsor_party}] {result.sponsor_name} {result.sponsor_state}</h2>
                    <sup>
                        {result.title}
                    </sup>
                    <ul>
                <a href={result.infoUrl}>
                        <li>{result.number} {result.result_id}</li>
                </a>
                        <li><b>{result.major_action}</b></li>
                    </ul>
                </div>
            );
         });
        return(
            resultItems
        )
        };
}

export default VoteResults;

import React from "react";

//const url = "https://state-of-congress.herokuapp.com/api/results/"

//This is for testing the backend
const url = "http://localhost:8000/api/results/"
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
                        {result.congress}
                        {result.number}
                        {result.Result}
                </div>
            );
         });
        return(
            resultItems
        )
        };
}

export default VoteResults;

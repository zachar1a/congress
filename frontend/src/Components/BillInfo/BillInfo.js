import React from "react";
import BillCard from "../BillCard/BillCard";

const url = "https://state-of-congress.herokuapp.com/api/info/"

//This is for testing the backend
//const url = "http://localhost:8000/api/info/"
class BillInfo extends React.Component{

    constructor(props){
        super(props);
        this.state={
            bills: [],
        };
    }
    componentDidMount(){
        fetch(url)
        .then(data=> data.json())
        .then(data=>this.setState({bills:data}));
        console.log(this.state.bills);
    }

    render(){
        const billItems = this.state.bills.map((bill)=>{
            return(
		    <BillCard billid={bill.bill_id} 
		    	      title={bill.title}
		    	      sponsorParty={bill.sponsor_party}
		    	      sponsor={bill.sponsor_name}
		    	      sponsorState={bill.sponsor_state}
		    	      infoUrl={bill.infoUrl}
		    	      slug={bill.slug}/>
            );
         });
        return(
            billItems
        )
        };
}

export default BillInfo;

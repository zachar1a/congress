import React from "react";
import BillCard from "../BillCard/BillCard";
import Card from "../Card/Card";

const latestBillUrl= "https://state-of-congress.herokuapp.com/latest-bill/";
const latestVoteUrl= "https://state-of-congress.herokuapp.com/latest-vote/";

/*
const latestBillUrl= "http://localhost:8000/latest-bill/"
const latestVoteUrl= "http://localhost:8000/latest-vote/"
*/
/*
 * These are for development
*/

//This is for testing the backend
//const url = "http://localhost:8000/api/info/"
class BillInfo extends React.Component{

    constructor(props){
        super(props);
        this.state={
		sponsorParty:'',
		sponsor:'',
		sponsorState:'',
		introduced:'',
		billid:'',
		title:'',
		infoUrl:'',
		slug:'',

		voteChamber:'',
		voteName:'',
		voteTitle:'',
		voteResult:'',
		voteAction:''
        };
    }
    componentDidMount(){
        fetch(latestBillUrl)
        .then(data=> data.json())
        .then(data=>this.setState({
		sponsorParty:data.sponsor_party,
		sponsor:data.sponsor_name,
		sponsorState:data.sponsor_state,
		introduced:data.introduced,
		billid:data.bill_id,
		title:data.title,
		infoUrl:data.infoUrl,
		slug:data.slug
	}));

	fetch(latestVoteUrl)
		.then(data=>data.json())
		.then(data=>this.setState({ 
			voteChamber:data.chamber,
			voteName:data.name,
			voteTitle:data.title,
			voteResult:data.Result,
			voteAction:data.action
		})
	);
    }

    render(){
        return[
		<h1 className="bill-header">Latest Bill</h1>,
		<BillCard sponsorParty={this.state.sponsorParty}
			  sponsor={this.state.sponsor} 
			  sponsorState={this.state.sponsorState}
			  introduced={this.state.introduced}
			  billid={this.state.billid}
			  title={this.state.title}
			  infoUrl={this.state.infoUrl}
			  slug={this.state.slug}
		/>,
		<h1 className="vote-header">LatestVote</h1>,
		<Card chamber={this.state.voteChamber}
		      name={this.state.voteName}
		      title={this.state.voteTitle}
		      result={this.state.voteResult}
		      action={this.state.voteAction}
		/>
	]
        };
}

export default BillInfo;

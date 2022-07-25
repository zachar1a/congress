import React from "react";
import BillCard from "../BillCard/BillCard";
import Navbar from "../Navbar/Navbar";

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


    mysort= () => {
      console.log(this.state.bills[0])
      var obj = [...this.state.bills];
      obj.sort((a,b) => a.introduced < b.introduced);
      console.log(obj[0])
      obj.map((bill) =>
          <BillCard
                billid={bill.bill_id}
		    	      title={bill.title}
		    	      introduced={bill.introduced}
		    	      sponsorParty={bill.sponsor_party}
		    	      sponsor={bill.sponsor_name}
		    	      sponsorState={bill.sponsor_state}
		    	      infoUrl={bill.infoUrl}
		    	      slug={bill.slug}/>
      );
      console.log(obj[0]);
      console.log("hello");
    }

    help(){
      return(
        <div>
          <ul>
            <li onClick={this.mysort.bind(this)}>hello</li>
            <li>world</li>
            <li>good</li>
          </ul>
        </div>
      )
    }

    render(){

        return[
          <h1 className="bill-header">Current Bills</h1>,
		      <Navbar />,
          this.help(),
          this.state.bills.map((bill)=>{
            return(
		          <BillCard
                billid={bill.bill_id}
		    	      title={bill.title}
		    	      introduced={bill.introduced}
		    	      sponsorParty={bill.sponsor_party}
		    	      sponsor={bill.sponsor_name}
		    	      sponsorState={bill.sponsor_state}
		    	      infoUrl={bill.infoUrl}
		    	      slug={bill.slug}/>
            );
         })
        ]
        };
}

export default BillInfo;

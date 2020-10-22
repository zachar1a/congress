import React from "react";

const url = "https://state-of-congress.herokuapp.com/api/info/"
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
                <div className="billCard">
                    <h2>[{bill.sponsor_party}] {bill.sponsor_name} {bill.sponsor_state}</h2>
                    <sup>
                        {bill.title}
                    </sup>
                    <ul>
                <a href={bill.infoUrl}>
                        <li>{bill.number} {bill.bill_id}</li>
                </a>
                        <li><b>{bill.major_action}</b></li>
                    </ul>
                </div>
            );
         });
        return(
            billItems
        )
        };
}

export default BillInfo;

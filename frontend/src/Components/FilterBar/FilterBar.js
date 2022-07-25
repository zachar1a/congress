import React from "react";
import "./FilterBar.css";


class FilterBar extends React.Component{
  render(){
    return(
      <div>
            <ul className="filterbar">
                <li>Filter: </li>
                <li>date</li>
                <li>State</li>
                <li>Party</li>
            </ul>
      </div>
    )
  }
}

export default FilterBar;

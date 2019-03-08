import React, { Component } from 'react';
import './reportsidebar.css';

class SideBar extends Component {

   render() {

      const list = [
         {"title": "Block 1"},
         {"title": "Block 2"},
         {"title": "Block 3"}
      ]

      const li = list.map(function (elem) {
         return <li className="selection-list">{elem.title}</li>
      })

      return (
         <div id="side-bar">
            <div id="side-bar-contents">
               <ul>
                  <li className="back-button">Back</li>  
                  <li className="selection-list-title">SIMILARITIES</li>
                  {li}
               </ul>
            </div>
         </div>
      );
   }

}

export default SideBar;
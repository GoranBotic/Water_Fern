import React, { Component } from 'react';
import './sidebar.css';

function choose(elem){
   elem.title = "new thing"

}

class SideBar extends Component {

   render() {
      
      const list = [
         {
            "id": 1,
            "title": "COSC 1P02"},
         {
            "id": 2,
            "title": "MATH 1P05"},
         {
            "id": 3,
            "title": "MATH 1P66"},
         {
            "id": 4,
            "title": "MEME 1P69"}
      ]

      const li = list.map(function (elem) {
         return <li className="selection-list" onClick={choose(elem)}> {elem.title}</li>
      })

      return (
         <div id="side-bar">
            <div id="side-bar-contents">
               <ul>
                  <li className="selection-list-title">COURSE LIST</li>
                  {li}
               </ul>
            </div>
         </div>
      );
   }

}

export default SideBar;
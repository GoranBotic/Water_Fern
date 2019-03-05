import React, { Component } from 'react';
import './sidebar.css';

class SideBar extends Component {

   render() {

      const list = [
         {"title": "COSC 1P02"},
         {"title": "MATH 1P05"},
         {"title": "MATH 1P66"},
         {"title": "MEME 1P69"}
      ]

      const li = list.map(function (elem) {
         return <li className="selection-list">{elem.title}</li>
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
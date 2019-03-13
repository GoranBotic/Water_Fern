import React, { Component } from 'react';
import './sidebar.css';
import { Link } from "react-router-dom";

class SideBar extends Component {

   render() {

      const list = [
         {id: 1, "title": "COSC 1P02", "path": "/report"},
         {id: 2, "title": "MATH 1P05"},
         {id: 3, "title": "MATH 1P66"},
         {id: 4, "title": "MEME 1P69"}
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
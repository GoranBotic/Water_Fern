import React, { Component } from 'react';
import './header.css';

class Header extends Component {
   render() {
      return (
         <div id="header">
            <div className="logo">
               <h2>WaterFern</h2> <span>Professor</span>
            </div>
            <div className="buttons-list">
               <div className="header-button">
                  Logout
               </div>
            </div>
         </div>
      );
   }
}

export default Header;
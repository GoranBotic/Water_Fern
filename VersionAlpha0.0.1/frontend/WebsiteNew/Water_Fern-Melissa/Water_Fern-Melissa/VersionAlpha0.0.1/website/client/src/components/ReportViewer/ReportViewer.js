import React, { Component } from 'react';
import './reportviewer.css';

class ReportViewer extends Component {

   render() {
      return (
         <div className="welcome-box">
            <div className="reportleft">
               Report 1 
            </div>
            <div className="reportright">
               Report 2
            </div>
         </div>
      )
   }
}

export default ReportViewer;
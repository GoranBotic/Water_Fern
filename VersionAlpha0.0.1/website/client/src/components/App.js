import React from 'react';
import { BrowserRouter, Route } from 'react-router-dom';
import './App.css';

import Header from './MainBars/Header';
import SideBar from './MainBars/SideBar';
import WelcomeHome from './WelcomeHome/WelcomeHome';
import Upload from './Upload/Upload';
import ReportViewer from './ReportViewer/ReportViewer';

const Landing = () => <span>Landing</span>;

const App = () => {
   
   const pages = [
      { "path": '/land', "page": Landing, "exact": false},
      { "path": "/", "page": WelcomeHome, "exact": true},
      { "path": "/upload", "page": Upload, "exact": false},
      {"path": "/report", "page": ReportViewer,"exact": false}
   ];

   const routes = pages.map(function (elem) {
      return <Route exact={elem.exact} path={`/home${elem.path}`} component={elem.page} />
   })

   return (
      <div>
         <BrowserRouter>
            <div>
               <Route exact path="/" component={Landing} />
               <Route path="/home" component={Header} />
               <Route path="/home" component={SideBar} />
               <div className="entire-body">
                  { routes }
               </div>
            </div>
         </BrowserRouter>
      </div>
   );

};

export default App;
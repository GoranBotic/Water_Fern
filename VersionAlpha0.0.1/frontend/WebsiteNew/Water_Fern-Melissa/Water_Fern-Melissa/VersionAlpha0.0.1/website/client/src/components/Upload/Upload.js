import React, { Component } from 'react';
import './upload.css';

class Upload extends Component {

   render() {

      return (
       <div className='upload-tool'>
          <form action='/api/v1/uploadsubmission' method='post'>
            <input type='submit' value='Submit' />
            <input type='file' accept='.zip' id='uploadbar' />
          </form>
      </div>
      )

   }

}

export default Upload;
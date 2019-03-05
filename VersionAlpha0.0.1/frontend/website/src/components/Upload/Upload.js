import React, { Component } from 'react';
import './upload.css';

class Upload extends Component {

  chooseFile(e){

  }

   render() {

      return (
       <div className='upload-tool'>
          <form action='/api/v1/uploadsubmission' method='POST' enctype='multipart/form-data'>
            <input type='submit' value='Submit' />
            <input type='file' accept='.zip' name = "file" id='uploadbar' />
            <input type='hidden' name='uID' value = '0'/>
            <input type='hidden' name='aID' value = '0'/>
          </form>
      </div>
      )

   }

}

export default Upload;
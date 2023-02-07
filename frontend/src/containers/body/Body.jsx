import React from 'react';
import { Calculationbox, Infobox } from '../../components';
import './body.css';


const Body = () => {
  return (
    <div className='body'>
        <Infobox />
        <Calculationbox />
    </div>
  )
}

export default Body
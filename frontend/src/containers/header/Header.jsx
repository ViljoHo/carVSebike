import React from 'react';
import './header.css';
import car_min from '../../assets/car_min.jpg';
import ebike_min from '../../assets/ebike_min.jpg';

const Header = () => {
  return (
    <div>

        <div className='header_container'>

          <div className='car_text'>
            Auto
          </div>

          <div className='car'>
            <img src={car_min} alt='car' className='car_jpg'/>
          </div>

          <div className='gap'>
            <h1>
              VS
            </h1>

          </div>

          <div className='ebike_text'>
            Sähköpyörä
          </div>

          <div className='ebike'>
            <img src={ebike_min} alt='ebike' className='ebike_jpg'/>
          </div>

        </div>
        
        
    </div>
  )
}

export default Header
import React, {useState, useEffect} from 'react'
import './calculationbox.css';

const Calculationbox = () => {


    let [kilometers, setKilometers] = useState([])

    useEffect(() => {
        getKilonmeters()
    }, [])

    let getKilonmeters = async () => {
        let response = await fetch('/api/kilometers/1')
        let data = await response.json()
        setKilometers(data.ebikesKilometers)

    }

    let updateKilometers = async () => {
        let response = await fetch('/api/updateKilometers/')
        let data = await response.json()
        console.log(data)
        if (data.ebikesKilometers === '0') {
            alert('Kilometrit ovat ajantasalla')
        }
        else {
            getKilonmeters()
            alert('Kilometrit on nyt päivitetty')
        }
    }

  return (
    <div>
        <div className='calculationInfo'> 
            <div className='numbersBox'>
                <h3>Sähköpyörällä ajetut kilometrit yhteensä:</h3>
                <h3>{parseFloat(kilometers).toFixed(1)}</h3>
            </div>

            <div className='numbersBox'>
                <h3>Autolla ajettu kilometri maksaa noin:</h3>
                <h3>0.30€</h3>

            </div>

            <div className='totalSavings'>
                <h1>Rahaa säästetty:</h1>
                <h1>{parseFloat(kilometers*0.3).toFixed(2) + '€'}</h1>

            </div>
            
        </div>

        <button className='updateButton' onClick={updateKilometers}>
            Päivitä laskelmat
        </button>

    </div>
  )
}

export default Calculationbox
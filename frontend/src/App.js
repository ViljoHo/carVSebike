import './App.css';
//import Header from './components/Header'


import { Body, Footer, Header } from './containers';
import { Navbar } from './components';


function App() {
  return (
    <div className="App">
      <div className='gradient__bg'>
        <Navbar />
        <Header />
      </div>
      <Body />
      <Footer />
    </div>
  );
}

export default App;

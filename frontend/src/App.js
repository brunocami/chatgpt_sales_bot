import './App.css';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom'
import Navbar from './components/navbar';
import Home from './components/Home';
import Terms from './components/terms';

function App() {
  return (
    <Router>
      <Navbar />
      <Routes>
        <Route path='/' Component={Home} />
        <Route path='/legaldisclaimer' Component={Terms} />
      </Routes>
    </Router>
  );
}

export default App;

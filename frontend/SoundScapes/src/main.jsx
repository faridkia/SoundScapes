import React from 'react'
import ReactDOM from 'react-dom/client'
import App from './App.jsx'
import './index.css'
import'bootstrap/dist/css/bootstrap.min.css';
import MusicCard from './components/MusicCard.jsx';
import {
  createBrowserRouter,
  RouterProvider,
  Routes,
  Route,
  Link,
  BrowserRouter,
} from "react-router-dom";

ReactDOM.createRoot(document.getElementById('root')).render(
  <React.StrictMode>
    <BrowserRouter>
      <Routes>
        <Route path='/' element ={<App/>} />
        <Route path='/Login' element ={<div>login page</div>} />
        <Route path='/Register' element ={<div>register page</div>} />
        <Route path='/Profile' element ={<div>profile page</div>} />
        <Route path='/Playlist' element ={<div>playlist page</div>} />
        <Route path='/Music-List' element ={<div>music list page</div>} />
        <Route path='/Music-Play' element ={<MusicCard name= "delam mikhad" singer = "bardia" aks = "https://freesvg.org/img/1548005024.png" />} />
      </Routes>
    </BrowserRouter>

  </React.StrictMode>,
)

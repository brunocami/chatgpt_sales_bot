import React from 'react'
import { Link } from 'react-router-dom';
import { GiFox } from "react-icons/gi";

const Navbar = () => {
    return (
        <nav className="navbar navbar-expand-lg navbar-light bg-light">

            <div className="container-fluid">
                <Link className="navbar-brand" to={'/'}>
                    <GiFox/>
                    AI BOT
                </Link>
                <button className="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarColor03" aria-controls="navbarColor03" aria-expanded="false" aria-label="Toggle navigation">
                    <span className="navbar-toggler-icon"></span>
                </button>
                <div className="collapse navbar-collapse" id="navbarColor03">
                    <ul className="navbar-nav me-auto">
                        <li className="nav-item dropdown">
                            <Link className="nav-link dropdown-toggle" data-bs-toggle="dropdown" to={'/'} role="button" aria-haspopup="true" aria-expanded="false">Productos</Link>
                            <div className="dropdown-menu">
                                <Link className="dropdown-item" to={'/'}>Chatbot Web</Link>
                                <Link className="dropdown-item" to={'/'}>Chatbot Whatsapp</Link>
                                <Link className="dropdown-item" to={'/'}>Chatbot Instagram</Link>
                                <Link className="dropdown-item" to={'/'}>Chatbot Facebook</Link>
                                <div className="dropdown-divider"></div>
                                <Link className="dropdown-item" to={'/'}>Live Chat</Link>
                            </div>
                        </li>
                        <li className="nav-item">
                            <Link className="nav-link" to={'/'}>Casos de uso</Link>
                        </li>
                        <li className="nav-item">
                            <Link className="nav-link" to={'/'}>Precios</Link>
                        </li>
                        <li className="nav-item">
                            <Link className="nav-link" to={'/legaldisclaimer'}>Nosotros</Link>
                        </li>

                    </ul>
                    <button className="btn btn-primary me-3">Ingresá</button>
                    <button className="btn btn-outline-primary">Comenzar</button>
                </div>
            </div>
        </nav>
    )
}

export default Navbar
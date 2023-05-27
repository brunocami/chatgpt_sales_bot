import React from 'react'
import img from '../../assets/images/home-carrousel.jpg'

function Home() {
    return (
        <>
            {/* pantallas pequeñas */}
            <div class="d-block d-sm-none">
                <div className="container-fluid p-5 bg-secondary shadow-lg" style={{ "height": "70vh" }}>
                    <div className="flex-column d-flex align-items-center justify-content-center h-100">
                        <div className="col-sm-6 col-md-5 custom-column">
                            <h1>Misma inversión, mejores resultados</h1>
                            <p>Ahorra tiempo y genera <mark>más ventas automatizando conversaciones</mark> en los canales <mark>Web</mark>, <mark>WhatsApp</mark> y <mark>Redes Sociales</mark> con AI Bot.

                                Entiende, perfila, califica y gestiona cada contacto para bajar tu costo por ventas y atención, mejorando el retorno de tu inversión publicitaria (ROAS).</p>
                            <button className="btn btn-outline-success w-100">Registrarme</button>
                        </div>
                        <div className="col-sm-4 col-md-5 custom-column mt-3">
                            <img src={img} className="img-fluid rounded" alt="Imagen" />
                        </div>
                    </div>
                </div>
                <div className="container-fluid p-5" style={{ "backgroundColor": "#383475" }}>
                    <div className="row d-flex align-items-center justify-content-center text-white" >
                        <div className="col-md-6 custom-column me-5 text-center" >
                            <h1 className='text-white'>Inteligencia Artificial</h1>
                            <p>Todos los beneficios que ya conoces del chatbot potenciados con IA para que puedas lograr mejores conversaciones en la precompra y en la poscompra.</p>
                            <button className="btn btn-outline-primary">Conoce más</button>
                        </div>
                    </div>
                </div>
            </div>
            {/* pantallas grandes */}
            <div class="d-none d-sm-block">
                <div className="container-fluid p-5 bg-secondary shadow-lg" style={{ "height": "70vh" }}>
                    <div className="row d-flex align-items-center justify-content-center h-100">
                        <div className="col-sm-6 col-md-5 custom-column me-5">
                            <h1>Misma inversión, mejores resultados</h1>
                            <p>Ahorra tiempo y genera más ventas automatizando conversaciones en los canales Web, WhatsApp y Redes Sociales con AI Bot.

                                Entiende, perfila, califica y gestiona cada contacto para bajar tu costo por ventas y atención, mejorando el retorno de tu inversión publicitaria (ROAS).</p>
                            <button className="btn btn-outline-success">Registrarme</button>
                        </div>
                        <div className="col-sm-4 col-md-5 custom-column">
                            <img src={img} className="img-fluid rounded" alt="Imagen" />
                        </div>
                    </div>
                </div>
                <div className="container-fluid p-5" style={{ "backgroundColor": "#383475" }}>
                    <div className="row d-flex align-items-center justify-content-center text-white" >
                        <div className="col-md-6 custom-column me-5 text-center" >
                            <h1 className='text-white'>Inteligencia Artificial</h1>
                            <p>Todos los beneficios que ya conoces del chatbot potenciados con IA para que puedas lograr mejores conversaciones en la precompra y en la poscompra.</p>
                            <button className="btn btn-outline-primary">Conoce más</button>
                        </div>
                    </div>
                </div>
            </div>
        </>
    )
}

export default Home
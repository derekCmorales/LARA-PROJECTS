const Instructions = () => {
    return (
        <div className="mx-8 text-gray-500 w-[200px] text-[13px]">
            <h1 className="mb-4">Usa el lienzo para construir tu grafo.</h1>
            <div className="mb-2">
                <p className="float-left text-gray-700 mr-2 font-bold">Para agregar un vértice:</p>
                <p> haz doble clic, luego agrega una etiqueta escribiendo un 
                    <span className="italic"> carácter alfabético único </span>
                </p>
            </div>
            <div className="mb-2">
                <p className="float-left text-gray-700 mr-2 font-bold">Para agregar una arista: </p>
                <p>mantén presionada la tecla shift y arrastra de un vértice a otro, luego agrega un peso escribiendo un
                    <span className="italic"> número</span>
                </p>
            </div>
            <div className="mb-2">
                <p className="float-left text-gray-700 mr-2 font-bold">Para mover un vértice: </p>
                <p>arrástralo</p>
            </div>
            <div className="mb-2">
                <p className="float-left text-gray-700 mr-2 font-bold">Para editar un elemento: </p>
                <p>haz clic en él</p>
            </div>
            <div className="mb-8">
                <p className="float-left text-gray-700 mr-2 font-bold">Para eliminar un elemento: </p>
                <p>presiona la tecla 
                    <span className="italic"> delete </span>
                    (fn + delete en Mac)</p>
            </div>
        </div>
    )
}

export default Instructions;
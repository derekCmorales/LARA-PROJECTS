import Refs from "@/interfaces/refs"

const Select = ({
    refs
} : {
    refs: Refs
}) => {
    return (
        <div className="text-center">
            <div className="inline-block">
                <button 
                    ref={refs.selectModeRef} 
                    className="py-1 px-6 mt-5 float-left text-gray-700 italic border border-gray-800 text-center text-[13px] rounded hover:bg-amber-400">
                        Seleccionar Vértice Inicial
                </button>
                <span 
                    ref={refs.startPromptRef} 
                    className="p-1 mt-5 float-left text-gray-700 text-[13px]" 
                    hidden={true}>
                        Selecciona un vértice para <span className="text-[green]">comenzar</span>.
                </span>
                <span 
                    ref={refs.retryPromptRef} 
                    className="p-1 ml-8 mt-5 float-left text-gray-700 text-[13px]" 
                    hidden={true}>
                        Asegúrate de que todos los vértices tengan una etiqueta y todas las aristas tengan un peso.
                </span>
                <span 
                    ref={refs.emptyPromptRef} 
                    className="p-1 ml-8 mt-5 float-left text-gray-700 text-[13px]" 
                    hidden={true}>
                        Por favor, agrega algunos vértices primero.
                </span>
                <button 
                    ref={refs.startVisRef} 
                    className="py-1 px-6 mt-5 ml-4 float-left text-gray-100 italic border border-gray-800 bg-sky-800 text-center text-[13px] rounded hover:bg-sky-700" 
                    hidden={true}>
                        Visualizar el Algoritmo de Dijkstra
                </button>
                <span 
                    ref={refs.visPromptRef} 
                    className="p-1 mt-5 float-left text-gray-700 text-[13px]" 
                    hidden={true}>
                        Visualizando el Algoritmo de Dijkstra...
                </span>
                <button
                    ref={refs.restartRef} 
                    className="py-1 px-6 mt-5 ml-4 float-left text-gray-700 italic border border-gray-800 text-center text-[13px] rounded hover:bg-amber-400" 
                    hidden={true}>
                        Reiniciar Visualización
                </button>
            </div>
        </div>    
    )
}

export default Select;
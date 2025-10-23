import { RefObject } from "react";

const Pause = ({
    pauseRef
} : {
    pauseRef: RefObject<HTMLButtonElement>
}) => {
    return (
        <div className="mx-8 w-[180px]">
            <button ref={pauseRef} className="mt-4 py-1 px-3 w-fit italic border border-gray-800 text-center text-gray-700 text-[13px] rounded hover:bg-amber-400" hidden={true}>
                Pausa
            </button>
        </div>
    )
}

export default Pause;
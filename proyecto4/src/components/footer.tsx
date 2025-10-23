import Link from "next/link";

const Footer = () => {
    return (
        <div className="mt-6 p-6 text-gray-500 text-center text-[13px]">
            By {
                <div style={{ color: "#2578a8" }} className="inline">
                Derek Calderón & Adrián Matul
            </div>
            }
            <div className="mt-4">
                <img 
                    src="/logo.png" 
                    alt="Lara Logo" 
                    className="mx-auto h-17"
                />
            </div>
        </div>
    );
};

export default Footer;
import React from "react";

const Navbar: React.FC = () => {
    return (
        <nav className="bg-gray-900 text-white py-4 px-6 w-full flex justify-between items-center">
            <h1 className="text-3xl font-bold">E-Learning</h1>
            <ul className="flex space-x-6 text-lg">
                <li><a href="#" className="hover:text-gray-400 transition">Home</a></li>
                <li><a href="#" className="hover:text-gray-400 transition">Courses</a></li>
                <li><a href="#" className="hover:text-gray-400 transition">About</a></li>
                <li><a href="#" className="hover:text-gray-400 transition">Contact</a></li>
            </ul>
        </nav>
    );
};

export default Navbar;

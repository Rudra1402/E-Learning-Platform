import React from "react";

interface FeatureCardProps {
    title: string;
    description: string;
}

const FeatureCard: React.FC<FeatureCardProps> = ({ title, description }) => {
    return (
        <div className="p-6 bg-gray-800 rounded-lg shadow-md w-full text-center text-white">
            <h2 className="text-xl font-semibold">{title}</h2>
            <p className="text-gray-400 mt-2">{description}</p>
        </div>
    );
};

export default FeatureCard;

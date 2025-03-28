import React from "react";
import FeatureCard from "../components/FeaturedCard";

const LandingPage: React.FC = () => {
    return (
        <div className="w-full flex flex-col justify-start items-center bg-gray-900 text-white">
            <header className="text-center py-20">
                <h1 className="text-5xl font-bold">Learn Anytime, Anywhere</h1>
                <p className="text-xl mt-4">Join our platform and start learning today!</p>
                <button className="mt-6 px-8 py-3 bg-blue-500 text-white rounded-lg shadow-md hover:bg-blue-600 transition">
                    Get Started
                </button>
            </header>

            {/* Features Section */}
            <section className="py-12 px-6 grid md:grid-cols-3 gap-4 w-[90%]">
                <FeatureCard title="Expert Instructors" description="Learn from industry experts." />
                <FeatureCard title="Flexible Learning" description="Study at your own pace." />
                <FeatureCard title="Certifications" description="Get recognized for your skills." />
            </section>
        </div>
    );
};

export default LandingPage;

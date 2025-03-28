import React from "react";
import Navbar from "./components/Navbar";
import LandingPage from "./pages/LandingPage";
import Footer from "./components/Footer";

const App: React.FC = () => {
  return (
    <div className="m-0 p-0 h-screen w-screen flex flex-col gap-0 overflow-y-auto">
      <Navbar />
      <LandingPage />
      <Footer />
    </div>
  );
};

export default App;

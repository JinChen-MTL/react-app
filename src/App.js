import React from "react";
import { BrowserRouter as Router, Route, Routes, Link } from "react-router-dom";
import Home from "./Home";
import Products from "./Products";
import About from "./About";
import Contact from "./Contact";
import "./App.css";

const App = () => {
  return (
    <Router>
      <div className="app">
        <header className="header">
          <h1>FurnitureCo</h1>
          <nav className="nav">
            {/* Navigation Links */}
            <Link to="/">Home</Link>
            <Link to="/products">Products</Link>
            <Link to="/about">About Us</Link>
            <Link to="/contact">Contact</Link>
          </nav>
        </header>
        <main className="main-content">
          {/* Routes Configuration */}
          <Routes>
            <Route path="/" element={<Home />} />
            <Route path="/products" element={<Products />} />
            <Route path="/about" element={<About />} />
            <Route path="/contact" element={<Contact />} />
          </Routes>
        </main>
        <footer className="footer">
          <p>&copy; 2024 FurnitureCo. All rights reserved.</p>
        </footer>
      </div>
    </Router>
  );
};

export default App;

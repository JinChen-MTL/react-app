// HorizontalScroller.jsx
import React from "react";

const categories = ["Sofas", "Tables", "Chairs", "Beds", "Lamps", "Rugs"];

const HorizontalScroller = () => {
  return (
    <div className="horizontal-scroller">
      {categories.map((category, index) => (
        <div key={index} className="category-card">
          <h3>{category}</h3>
        </div>
      ))}
    </div>
  );
};

export default HorizontalScroller;

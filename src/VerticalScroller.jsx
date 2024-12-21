// VerticalScroller.jsx
import React from "react";

const products = [
  { name: "Modern Sofa", price: "$499" },
  { name: "Dining Table", price: "$299" },
  { name: "Cozy Chair", price: "$199" },
  { name: "Queen Bed", price: "$599" },
  { name: "Floor Lamp", price: "$79" },
  { name: "Area Rug", price: "$149" },
];

const VerticalScroller = () => {
  return (
    <div className="vertical-scroller">
      {products.map((product, index) => (
        <div key={index} className="product-card">
          <h3>{product.name}</h3>
          <p>{product.price}</p>
        </div>
      ))}
    </div>
  );
};

export default VerticalScroller;

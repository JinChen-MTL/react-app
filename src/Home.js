import React from "react";
import HorizontalScroller from "./HorizontalScroller";
import VerticalScroller from "./VerticalScroller";

const Home = () => {
  return (
    <div>
      <section className="horizontal-section">
        <h2>Explore Our Categories</h2>
        <HorizontalScroller />
      </section>
      <section className="vertical-section">
        <h2>Featured Products</h2>
        <VerticalScroller />
      </section>
    </div>
  );
};

export default Home;

import "./App.css";

function App() {
  return (
    <div className="App">
      <header className="resume-header">
        <h1>Jin Chen</h1>
        <p className="subtitle">Full Stack Developer | React Enthusiast</p>
      </header>
      <main className="resume-content">
        <section className="section">
          <h2>About Me</h2>
          <p>
            I'm Jin Chen, a passionate software developer specializing in
            building elegant, scalable, and user-friendly web applications.
          </p>
        </section>
        <section className="section">
          <h2>Skills</h2>
          <ul>
            <li>JavaScript (ES6+), React, Redux</li>
            <li>Node.js, Express</li>
            <li>HTML5, CSS3, SASS</li>
            <li>REST APIs, GraphQL</li>
            <li>Git, GitHub, Agile Development</li>
          </ul>
        </section>
        <section className="section">
          <h2>Experience</h2>
          <p>
            <strong>Software Developer</strong> at <em>YourCompany</em> <br />
            <span>2020 - Present</span>
          </p>
          <ul>
            <li>
              Developed scalable React components for high-traffic web
              applications.
            </li>
            <li>
              Collaborated with cross-functional teams to deliver projects on
              time.
            </li>
          </ul>
        </section>
        <section className="section">
          <h2>Education</h2>
          <p>
            <strong>Bachelor of Computer Science</strong> <br />
            University of Montreal, 2020
          </p>
        </section>
        <section className="section">
          <h2>Contact</h2>
          <p>Email: jinchen@example.com</p>
          <p>
            LinkedIn:{" "}
            <a
              href="https://linkedin.com/in/jinchen"
              target="_blank"
              rel="noopener noreferrer"
            >
              linkedin.com/in/jinchen
            </a>
          </p>
          <p>
            GitHub:{" "}
            <a
              href="https://github.com/jinchen"
              target="_blank"
              rel="noopener noreferrer"
            >
              github.com/jinchen
            </a>
          </p>
        </section>
      </main>
      <footer className="resume-footer">
        <p>© 2024 Jin Chen. All rights reserved.</p>
      </footer>
    </div>
  );
}

export default App;

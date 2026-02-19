import "@/App.css";

function App() {
  return (
    <iframe
      data-testid="buddysocial-iframe"
      src="/buddysocial.html"
      title="The Buddy Social"
      style={{
        width: "100vw",
        height: "100vh",
        border: "none",
        display: "block",
        margin: 0,
        padding: 0,
        overflow: "hidden",
      }}
    />
  );
}

export default App;

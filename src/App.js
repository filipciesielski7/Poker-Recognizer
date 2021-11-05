import React from "react";
import { AppProvider } from "./contexts/context.js";
import Home from "./pages/home";

function App() {
  return (
    <AppProvider>
      <Home />
    </AppProvider>
  );
}

export default App;

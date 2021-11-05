import React from "react";
import { AppProvider } from "./contexts/context.js";
import Home from "./pages/home";
import Result from "./pages/result";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";

function App() {
  return (
    <Router>
      <AppProvider>
        <Routes>
          <Route exact path="/Poker_Recognizer" element={<Home />} />
          <Route path="/result" element={<Result />} />
          <Route exact path="*" element={<Home />} />
        </Routes>
      </AppProvider>
    </Router>
  );
}

export default App;

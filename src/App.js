import React from "react";
import { AppProvider } from "./contexts/context.js";
import Home from "./pages/home";
import Result from "./pages/result";
import ScrollToTop from "./helpers/scrollToTop";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";

function App() {
  return (
    <Router>
      <ScrollToTop />
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

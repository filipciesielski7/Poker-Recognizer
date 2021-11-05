import React from "react";
import { AppProvider } from "./contexts/context.js";
import Home from "./pages/home";
import Result from "./pages/result";
import {Route, Router} from 'react-router-dom'

function App() {
  return (
    <AppProvider>
      <Router>
         <Route path="/home" component={Home} />
         <Route path="/result" component={Result} />
      </Router>
    </AppProvider>
  );
}

export default App;

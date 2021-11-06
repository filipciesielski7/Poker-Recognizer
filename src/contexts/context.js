import React, { createContext, useContext, useState } from "react";

const AppContext = createContext();

export function useApp() {
  return useContext(AppContext);
}

export function AppProvider({ children }) {
  const [image, setImage] = useState(null);
  const [loading, setLoading] = useState(true);
  const [firstLoad, setFirstLoad] = useState(false);

  const value = {
    image,
    setImage,
    loading,
    setLoading,
    firstLoad,
    setFirstLoad,
  };

  return <AppContext.Provider value={value}>{children}</AppContext.Provider>;
}

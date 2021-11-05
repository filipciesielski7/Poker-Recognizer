import React from "react";
import { Load, Loading } from "../components";
import { useApp } from "../contexts/context.js";
import { Link } from "react-router-dom";

const ResultContainer = () => {
  const { loading } = useApp();

  return (
    <>
      {loading ? <Loading /> : <Loading.ReleaseBody />}
      <Load>
        <Load.Image
          src={`${process.env.PUBLIC_URL}/result.jpg`}
          alt="Twoja kombinacja kart"
        />
        <Link to="/Poker_Recognizer">Strona główna</Link>
      </Load>
    </>
  );
};

export default ResultContainer;

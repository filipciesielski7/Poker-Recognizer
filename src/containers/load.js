import React, { useState } from "react";
import { Load, Loading } from "../components";
import { AiOutlineGithub } from "react-icons/ai";

const LoadContainer = () => {
  const [image, setImage] = useState(null);
  const [loading, setLoading] = useState(false);

  async function onImageChange(event) {
    setLoading(true);
    if (event.target.files && event.target.files[0]) {
      setImage(URL.createObjectURL(event.target.files[0]));
    }
    setTimeout(() => {
      setLoading(false);
    }, 1000);
  }

  return (
    <>
      {loading ? <Loading /> : <Loading.ReleaseBody />}
      <Load>
        {!image ? (
          <Load.Label for="file-upload">Dodaj zdjęcie kart</Load.Label>
        ) : null}
        <Load.OptionsContainer>
          {image ? (
            <Load.SmallLabel for="file-upload">
              Dodaj nowe zdjęcie
            </Load.SmallLabel>
          ) : null}
          <Load.Button>Załaduj losowe</Load.Button>
          <Load.GithubLink
            href="https://github.com/filipciesielski7/Poker_Recognizer"
            target="_blank"
          >
            <AiOutlineGithub size={35} />
          </Load.GithubLink>
        </Load.OptionsContainer>
        <Load.Input
          id="file-upload"
          type="file"
          onChange={onImageChange}
          accept="image/png, image/jpeg, image/jpg"
        />
        <Load.Image
          src={image ? image : `${process.env.PUBLIC_URL}/poker-cards.png`}
          alt="Twoja kombinacja kart"
        />
      </Load>
    </>
  );
};

export default LoadContainer;

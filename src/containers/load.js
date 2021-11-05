import React from "react";
import { Load, Loading } from "../components";
import { AiOutlineGithub } from "react-icons/ai";
import { useApp } from "../contexts/context.js";

const LoadContainer = () => {
  const { image, setImage, loading, setLoading } = useApp();

  async function onImageChange(event) {
    setLoading(true);
    if (event.target.files && event.target.files[0]) {
      setImage(URL.createObjectURL(event.target.files[0]));
    }
    setTimeout(() => {
      setLoading(false);
    }, 1000);
  }

  function onRandomButtonClickChange() {
    setLoading(true);
    let index = Math.ceil(Math.random() * 10);
    setImage(`${process.env.PUBLIC_URL}/examples/example${index}.jpeg`);
    setTimeout(() => {
      setLoading(false);
    }, 1000);
  }

  return (
    <>
      {loading ? <Loading /> : <Loading.ReleaseBody />}
      <Load>
        {!image ? (
          <Load.Label htmlFor="file-upload">Dodaj zdjęcie kart</Load.Label>
        ) : null}
        <Load.OptionsContainer image={image}>
          {image ? (
            <Load.SmallLabel htmlFor="file-upload">
              Dodaj nowe zdjęcie
            </Load.SmallLabel>
          ) : null}
          <Load.SmallOptionsContainer>
            <Load.Button onClick={onRandomButtonClickChange}>
              Załaduj losowe
            </Load.Button>
            <Load.GithubLink
              href="https://github.com/filipciesielski7/Poker_Recognizer"
              target="_blank"
            >
              <AiOutlineGithub size={35} />
            </Load.GithubLink>
          </Load.SmallOptionsContainer>
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

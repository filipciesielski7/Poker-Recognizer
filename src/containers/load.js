import React, { useEffect, useState } from "react";
import { Load, Loading } from "../components";
import { AiOutlineGithub } from "react-icons/ai";
import { useApp } from "../contexts/context.js";
import axios from "axios";

const LoadContainer = () => {
  const { image, setImage, loading, setLoading } = useApp();
  const [userImage, setUserImage] = useState(false);

  useEffect(() => {
    setTimeout(() => {
      setLoading(false);
    }, 1000);
  }, [setLoading]);

  async function handleFormSubmit(e) {
    e.preventDefault();
    const formData = new FormData(e.target);

    const Upload = async () => {
      await fetch("user/upload", {
        method: "POST",
        body: formData,
      }).then((resp) => {
        // console.log(resp);
      });
    };
    Upload();
  }

  var config = {
    headers: {
      "Content-Type": "application/json",
      "Access-Control-Allow-Origin": "*",
    },
  };

  async function handleSubmit(event) {
    event.preventDefault();
    await axios
      .post("upload", { method: "POST", image: image }, config)
      .then((resp) => {
        // console.log(resp);
      });
  }

  function onImageChange(event) {
    setLoading(true);
    setUserImage(true);
    if (event.target.files && event.target.files[0]) {
      setImage(URL.createObjectURL(event.target.files[0]));
    }
    setTimeout(() => {
      setLoading(false);
    }, 300);
  }

  function onRandomButtonClickChange() {
    setLoading(true);
    let index = Math.ceil(Math.random() * 15);
    setImage(`${process.env.PUBLIC_URL}/examples/example${index}.jpg`);
    setTimeout(() => {
      setLoading(false);
    }, 500);
  }

  return (
    <>
      {loading ? <Loading /> : <Loading.ReleaseBody />}
      <Load>
        <Load.Form
          encType="multipart/form-data"
          onSubmit={handleFormSubmit}
          id="my-form"
        >
          <Load.Label htmlFor="img">Dodaj zdjęcie kart</Load.Label>
          <Load.Input
            type="file"
            id="img"
            name="file"
            accept="image/png, image/jpeg, image/jpg"
            onChange={onImageChange}
          ></Load.Input>
        </Load.Form>
        <Load.OptionsContainer image={image}>
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
        {image ? (
          <Load.Image
            src={image}
            alt="Twoja kombinacja kart"
            id="current_image"
          />
        ) : null}
        {!image ? (
          <>
            <Load.Image
              src={`${process.env.PUBLIC_URL}/original.jpg`}
              alt="Twoja kombinacja kart"
              id="current_image"
            />
            Wstępna obróbka obrazu w celu znalezienia konturów kart

            <Load.Image
              src={`${process.env.PUBLIC_URL}/grayed.jpg`}
              alt="Twoja kombinacja kart"
              id="current_image"
            />
            <Load.Image
              src={`${process.env.PUBLIC_URL}/blurred.jpg`}
              alt="Twoja kombinacja kart"
              id="current_image"
            />
            <Load.Image
              src={`${process.env.PUBLIC_URL}/pre_process.jpg`}
              alt="Twoja kombinacja kart"
              id="current_image"
            />
            Przykładowa wykryta karta na podstawie wcześniej znalezionego konturu
            <Load.Image
              src={`${process.env.PUBLIC_URL}/card.jpg`}
              alt="Twoja kombinacja kart"
              id="current_image"
            />
            Obraz po spłaszczeniu karty, zmiany wymiarów karty do 200x300 i czterokrotnym przybliżeniu do rogu karty
            <Load.Image
              src={`${process.env.PUBLIC_URL}/przyblizenie.jpg`}
              alt="Twoja kombinacja kart"
              id="current_image"
            />
            Znalezienie prostokąta ograniczającego dla największego konturu w celu zidentyfikowania rangi karty, po wcześniejszym zastosowaniu odpowiedniego poziomu progowania
            <Load.Image
              src={`${process.env.PUBLIC_URL}/gorna_czesc.jpg`}
              alt="Twoja kombinacja kart"
              id="current_image"
            />
            Znalezienie prostokąta ograniczającego dla największego konturu w celu zidentyfikowania koloru karty, po wcześniejszym zastosowaniu odpowiedniego poziomu progowania
            <Load.Image
              src={`${process.env.PUBLIC_URL}/dolna_czesc.jpg`}
              alt="Twoja kombinacja kart"
              id="current_image"
            />
            Wynik końcowy

             <Load.Image
              src={`${process.env.PUBLIC_URL}/result.jpg`}
              alt="Twoja kombinacja kart"
              id="current_image"
            />
          </>
        ) : null}
        {image ? (
          !userImage ? (
            <Load.Button onClick={handleSubmit}>Uruchom algorytm</Load.Button>
          ) : (
            <Load.Button type="submit" form="my-form">
              Uruchom algorytm
            </Load.Button>
          )
        ) : null}
      </Load>
    </>
  );
};

export default LoadContainer;

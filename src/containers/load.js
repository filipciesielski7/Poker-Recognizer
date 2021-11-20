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
              src={`${process.env.PUBLIC_URL}/results/original.jpg`}
              alt="Twoja kombinacja kart"
              id="current_image"
            />
            <Load.Image
              src={`${process.env.PUBLIC_URL}/results/result.jpg`}
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

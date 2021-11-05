import React, { useEffect } from "react";
import { Load, Loading } from "../components";
import { AiOutlineGithub } from "react-icons/ai";
import { useApp } from "../contexts/context.js";
import axios from "axios";

const LoadContainer = () => {
  const { image, setImage, loading, setLoading, firstLoad, setFirstLoad } =
    useApp();

  useEffect(() => {
    setLoading(true);
    setTimeout(() => {
      setLoading(false);
    }, 1000);
  }, []);

  var config = {
    headers: {
      "Content-Type": "application/json",
      "Access-Control-Allow-Origin": "*",
    },
  };

  const Upload = async (image) => {
    setFirstLoad(true);
    // var formData = new FormData();
    // var imagefile = document.querySelector("#file-upload");
    // formData.append("image", imagefile.files[0]);
    // console.log(formData);
    await axios
      .post("/upload", { method: "POST", image: image }, config)
      .then((data) => {
        // setImage(data.data.filename);
        setLoading(false);
      });
  };

  async function onImageChange(event) {
    setLoading(true);
    if (event.target.files && event.target.files[0]) {
      Upload(fetch(URL.createObjectURL(event.target.files[0])));
    }
  }

  function onRandomButtonClickChange() {
    setLoading(true);
    let index = Math.ceil(Math.random() * 10);
    Upload(`${process.env.PUBLIC_URL}/examples/example${index}.jpeg`);
  }

  return (
    <>
      {loading ? <Loading /> : <Loading.ReleaseBody />}
      <Load>
        {!firstLoad ? (
          <Load.Label htmlFor="file-upload">Dodaj zdjęcie kart</Load.Label>
        ) : null}
        <Load.OptionsContainer image={false}>
          {firstLoad ? (
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
        {/* {!firstLoad ? null : (
          <>
            <Load.Image src={image} alt="Twoja kombinacja kart" />

            <Load.Image
              src={`${process.env.PUBLIC_URL}/examples/test.jpeg`}
              alt="Twoja kombinacja kart"
            />
          </>
        )} */}
        <>
          <Load.Image
            src={`${process.env.PUBLIC_URL}/examples/aktualny.jpeg`}
            alt="Twoja kombinacja kart"
          />

          <Load.Image
            src={`${process.env.PUBLIC_URL}/examples/test.jpeg`}
            alt="Twoja kombinacja kart"
          />
        </>
      </Load>
    </>
  );
};

export default LoadContainer;

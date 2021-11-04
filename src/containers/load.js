import React, { useState } from "react";
import { Load } from "../components";

const LoadContainer = () => {
  const [image, setImage] = useState(null);

  async function onImageChange(event) {
    if (event.target.files && event.target.files[0]) {
      setImage(URL.createObjectURL(event.target.files[0]));
    }
  }

  return (
    <Load>
      <Load.Input
        type="file"
        onChange={onImageChange}
        accept="image/png, image/jpeg, image/jpg"
      />
      {image ? <Load.Image src={image} alt="Your card combination" /> : null}
    </Load>
  );
};

export default LoadContainer;

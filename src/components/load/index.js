import React from "react";
import { Container, Input, Image } from "./styles/load";

export default function Load({ children, ...restProps }) {
  return <Container {...restProps}>{children}</Container>;
}

Load.Input = function LoadInput({ children, ...restProps }) {
  return <Input {...restProps}>{children}</Input>;
};

Load.Image = function LoadImage({ children, ...restProps }) {
  return <Image {...restProps}>{children}</Image>;
};

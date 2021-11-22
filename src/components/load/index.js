import React from "react";
import {
  Container,
  Input,
  Image,
  SmallLabel,
  Label,
  Button,
  StageInfo,
  ButtonLink,
  OptionsContainer,
  SmallOptionsContainer,
  GithubLink,
  Form,
} from "./styles/load";

export default function Load({ children, ...restProps }) {
  return <Container {...restProps}>{children}</Container>;
}

Load.Input = function LoadInput({ children, ...restProps }) {
  return <Input {...restProps}>{children}</Input>;
};

Load.Image = function LoadImage({ children, ...restProps }) {
  return <Image {...restProps}>{children}</Image>;
};

Load.Label = function LoadLabel({ children, ...restProps }) {
  return <Label {...restProps}>{children}</Label>;
};

Load.SmallLabel = function LoadSmallLabel({ children, ...restProps }) {
  return <SmallLabel {...restProps}>{children}</SmallLabel>;
};

Load.Button = function LoadButton({ children, ...restProps }) {
  return <Button {...restProps}>{children}</Button>;
};

Load.StageInfo = function LoadStageInfo({ children, ...restProps }) {
  return <StageInfo {...restProps}>{children}</StageInfo>;
};

Load.ButtonLink = function LoadButtonLink({ children, ...restProps }) {
  return <ButtonLink {...restProps}>{children}</ButtonLink>;
};

Load.OptionsContainer = function LoadOptionsContainer({
  children,
  ...restProps
}) {
  return <OptionsContainer {...restProps}>{children}</OptionsContainer>;
};

Load.SmallOptionsContainer = function LoadSmallOptionsContainer({
  children,
  ...restProps
}) {
  return (
    <SmallOptionsContainer {...restProps}>{children}</SmallOptionsContainer>
  );
};

Load.GithubLink = function LoadGithubLink({ children, ...restProps }) {
  return <GithubLink {...restProps}>{children}</GithubLink>;
};

Load.Form = function LoadForm({ children, ...restProps }) {
  return <Form {...restProps}>{children}</Form>;
};

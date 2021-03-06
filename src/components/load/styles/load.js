import styled from "styled-components/macro";
import { Link as ReactRouterLink } from "react-router-dom";

export const Container = styled.div`
  display: flex;
  padding: 70px 0;
  margin: auto;
  max-width: 1000px;
  flex-direction: column;

  min-height: 80vh;

  align-items: center;
  justify-content: center;

  @media (max-width: 1000px) {
    padding: 70px 30px;
  }
`;

export const Input = styled.input`
  display: none;
`;

export const Image = styled.img`
  max-width: 70vw;
  max-height: 70vh;
  @media (max-width: 600px) {
    max-width: 90vw;
    max-height: 70vh;
  }
  margin: 0 20px 20px 20px;
  border: 1px solid white;
  border-radius: 4px;
`;

export const Label = styled.label`
  border: 1px solid white;
  color: black;
  border-radius: 10px;
  padding: 15px;
  text-align: center;
  // margin: 20px;

  font-size: 12px;
  text-transform: uppercase;
  letter-spacing: 2.5px;
  font-weight: 500;
  background-color: white;
  box-shadow: 0 8px 15px black;
  transition: all 0.3s ease 0s;

  &:hover {
    transform: scale(1.1);
    background: rgba(255, 255, 255);
  }

  &:active {
    transform: translateY(2px);
  }

  @media (max-width: 600px) {
    font-size: 12px;
    padding: 15px;
    // margin: 25px;
  }
  @media (max-width: 450px) {
    font-size: 10px;
    padding: 13px;
    // margin: 15px;
  }
`;

export const SmallLabel = styled.label`
  padding: 10px;
  margin: 0 10px;
  border-radius: 5px;
  font-size: 12px;
  text-transform: uppercase;

  border: none;
  outline: none;
  background: white;
  border: 1px solid white;
  color: black;
  transition: all 0.5s ease 0s;

  box-shadow: 0 0.5px 2px white;

  &:hover {
    transform: scale(1.05);
    background: rgba(255, 255, 255);
    color: black;
  }

  &:active {
    transform: translateY(2px);
    box-shadow: 0 0px 0px white;
  }

  @media (max-width: 450px) {
    font-size: 10px;
    padding: 7px;
  }

  // @media (max-width: 390px) {
  //   font-size: 12px;
  //   padding: 13px;
  // }
`;

export const Button = styled.button`
  padding: 10px;
  margin: 0 10px;
  border-radius: 5px;
  font-size: 12px;
  text-transform: uppercase;

  border: none;
  outline: none;
  background: none;
  border: 1px solid white;
  color: white;
  transition: all 0.5s ease 0s;

  box-shadow: 0 0.5px 2px white;

  &:hover {
    transform: scale(1.05);
    background: rgba(255, 255, 255);
    color: black;
  }

  &:active {
    transform: translateY(2px);
    box-shadow: 0 0px 0px white;
  }

  @media (max-width: 450px) {
    font-size: 10px;
    padding: 7px;
  }

  @media (max-width: 390px) {
    // margin: 10px;
  }
`;

export const ButtonLink = styled(ReactRouterLink)`
  padding: 10px;
  margin: 0 10px;
  border-radius: 5px;
  font-size: 12px;
  text-transform: uppercase;
  text-decoration: none;
  text-align: center;

  border: none;
  outline: none;
  background: none;
  border: 1px solid white;
  color: white;
  transition: all 0.5s ease 0s;

  box-shadow: 0 0.5px 2px white;

  &:hover {
    transform: scale(1.05);
    background: rgba(255, 255, 255);
    color: black;
  }

  &:active {
    transform: translateY(2px);
    box-shadow: 0 0px 0px white;
  }

  @media (max-width: 450px) {
    font-size: 10px;
    padding: 7px;
  }

  @media (max-width: 390px) {
    // margin: 10px;
  }
`;

export const OptionsContainer = styled.div`
  display: flex;
  align-items: center;
  justify-content: space-beetween;
  margin-bottom: 30px;

  @media (max-width: 390px) {
    font-size: 10px;
    // padding: 7px;
    // flex-direction: ${({ image }) => (image ? "column" : "")};
    flex-direction: column;
  }
`;

export const GithubLink = styled.a`
  color: white;
  margin: 0 10px;
  transition: all 0.5s ease 0s;

  &:hover {
    transform: scale(1.05);
  }
`;

export const SmallOptionsContainer = styled.div`
  display: flex;
  align-items: center;
  justify-content: space-beetween;
  // @media (max-width: 390px) {
  //   margin-top: 10px;
  // }
`;

export const Form = styled.form`
  margin-bottom: 20px;
  display: flex;
  flex-direction: column;
  align-items: center;
`;

export const StageInfo = styled.p`
  color: white;
  font-weight: 400;
  font-size: 18px;
  margin-top: 40px;
  margin-bottom: 20px;
  width: 70vw;
  max-width: 750px;
  @media (max-width: 600px) {
    width: 90vw;
  }

  color: gray;
  text-justify: inter-word;
  border-radius: 4px;
  padding: 5px;
  // text-align: center;

  @media (max-width: 950px) {
    font-size: 16px;
  }
  @media (max-width: 400px) {
    font-size: 14px;
  }
  @media (max-width: 300px) {
    font-size: 12px;
  }
`;

export const CardCornerImages = styled.div`
  display: flex;
  align-items: center;
  justify-content: center;
`;

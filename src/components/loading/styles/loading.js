import styled, { createGlobalStyle } from "styled-components";

export const LockBody = createGlobalStyle`
  body {
    overflow: hidden;
  }
`;

export const ReleaseBody = createGlobalStyle`
  body {
    overflow: visible;
  }
`;

export const Container = styled.div`
  position: fixed;
  width: 100%;
  height: 100%;
  background-color: #094c22;
  z-index: 999;

  display: flex;
  justify-content: center;
  align-items: center;
`;

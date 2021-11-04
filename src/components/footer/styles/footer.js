import styled from "styled-components/macro";

export const Container = styled.div`
  display: flex;
  padding: 70px 0;
  margin: auto;
  max-width: 1000px;
  flex-direction: column;

  @media (max-width: 1000px) {
    padding: 70px 30px;
  }
`;

export const Column = styled.div`
  display: flex;
  flex-direction: column;
  text-align: left;
`;

export const Row = styled.div`
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(230px, 1fr));
  grid-gap: 15px;

  @media (max-width: 1000px) {
    grid-template-columns: repeat(auto-fill, minmax(150px, 1fr));
  }
`;

export const Title = styled.p`
  font-size: 14px;
  color: #757575;
  margin-bottom: 30px;
`;

export const Link = styled.a`
  color: white;
  font-size: 13px;
  text-decoration: none;
  margin-bottom: 20px;
`;

export const Text = styled.p`
  font-size: 12px;
  color: #757575;
`;

export const Break = styled.div`
  flex-basis: 100%;
  height: 0;
`;

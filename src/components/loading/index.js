import React from "react";
import { LockBody, ReleaseBody, Container } from "./styles/loading";
import Spinner from "react-spinner-material";

export default function Loading({ src, ...restProps }) {
  return (
    <Container>
      <LockBody />
      <Spinner radius={64} color={"#fff"} stroke={3} visible={true} />
    </Container>
  );
}

Loading.ReleaseBody = function LoadingReleaseBody() {
  return <ReleaseBody />;
};

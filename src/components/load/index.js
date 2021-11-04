import React from "react";
import {
  Container,
} from "./styles/load";

export default function Load({ children, ...restProps }) {
  return <Container {...restProps}>{children}</Container>;
}

// Footer.Row = function FooterRow({ children, ...restProps }) {
//   return <Row {...restProps}>{children}</Row>;
// };

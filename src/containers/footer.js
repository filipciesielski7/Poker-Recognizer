import React from "react";
import { Footer } from "../components";

const FooterContainer = () => {
  return (
    <Footer>
      {/* <Footer.Title>
        Projekt realizowany w ramach przedmiotu "Komunikacja człowiek-komputer"
      </Footer.Title> */}
      <Footer.Break />
      <Footer.Row>
        <Footer.Column>
          <Footer.Link
            href={`${process.env.PUBLIC_URL}/Sprawozdanie.pdf`}
            download
          >
            Sprawozdanie
          </Footer.Link>
        </Footer.Column>
        <Footer.Column>
          <Footer.Link href="mailto:filip.ciesielski@student.put.poznan.pl">
            Kontakt
          </Footer.Link>
        </Footer.Column>
      </Footer.Row>
      <Footer.Break />
      <Footer.Text>
        &copy; {new Date().getFullYear()} Filip Ciesielski, Michał Ciesielski,
        Justyna Frączek
      </Footer.Text>
    </Footer>
  );
};

export default FooterContainer;

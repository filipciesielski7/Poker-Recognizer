import React, { useEffect } from "react";
import { AiOutlineGithub } from "react-icons/ai";
import { Load, Loading } from "../components";
import { useApp } from "../contexts/context.js";

const ResultContainer = () => {
  const { image, loading, setLoading } = useApp();

  useEffect(() => {
    setLoading(true);
    setTimeout(() => {
      setLoading(false);
    }, 400);
  }, [setLoading]);

  return (
    <>
      {loading ? <Loading /> : <Loading.ReleaseBody />}
      <Load>
        <Load.OptionsContainer image={image}>
          <Load.SmallOptionsContainer>
            <Load.ButtonLink to="/Pocker_Recognizer">
              Powrót do strony głównej
            </Load.ButtonLink>
            <Load.GithubLink
              href="https://github.com/filipciesielski7/Poker_Recognizer"
              target="_blank"
            >
              <AiOutlineGithub size={35} />
            </Load.GithubLink>
          </Load.SmallOptionsContainer>
        </Load.OptionsContainer>
        <Load.Image
          src={`${process.env.PUBLIC_URL}/results/original.jpg`}
          alt="Twoja kombinacja kart"
          id="current_image"
        />
        <Load.StageInfo>
          Wyszarzenie, rozmazanie i progowanie obrazu w celu wykrycia konturów
          kart
        </Load.StageInfo>
        <Load.Image
          src={`${process.env.PUBLIC_URL}/results/grayed.jpg`}
          alt="Twoja kombinacja kart"
          id="current_image"
        />
        <Load.Image
          src={`${process.env.PUBLIC_URL}/results/blurred.jpg`}
          alt="Twoja kombinacja kart"
          id="current_image"
        />
        <Load.Image
          src={`${process.env.PUBLIC_URL}/results/pre_process.jpg`}
          alt="Twoja kombinacja kart"
          id="current_image"
        />
        <Load.StageInfo>
          Na podstawie wykrytych współrzędnych konturów kart, wycinamy po kolei
          kazdą z nich przy jednoczesnej zmianie perspektywy, aby zdjęcia
          oddawały widok karty z góry, nawet w sytuacji zrobienia zdjęcia pod
          kątem (poniżej przykład jednej z powyższych kart).
        </Load.StageInfo>
        <Load.Image
          src={`${process.env.PUBLIC_URL}/results/card.jpg`}
          alt="Twoja kombinacja kart"
          id="current_image"
        />
        <Load.StageInfo>
          Następnie zmieniamy wymiary wyciętej karty do 200x300 i wycinamy jej
          róg z rangą oraz kolorem jednocześnie czterokrotne przybliżając.
        </Load.StageInfo>
        <Load.Image
          src={`${process.env.PUBLIC_URL}/results/zoom.jpg`}
          alt="Twoja kombinacja kart"
          id="current_image"
        />
        <Load.StageInfo>
          Znalezienie prostokąta ograniczającego dla największego konturu w
          górnej i dolnej części przybliżonego wczesniej wyciętego rogu w celu
          zidentyfikowania rangi oraz koloru karty, po wcześniejszym
          zastosowaniu odpowiedniego poziomu progowania
        </Load.StageInfo>
        <Load.Image
          src={`${process.env.PUBLIC_URL}/results/symbol.jpg`}
          alt="Twoja kombinacja kart"
          id="current_image"
        />
        <Load.Image
          src={`${process.env.PUBLIC_URL}/results/value.jpg`}
          alt="Twoja kombinacja kart"
          id="current_image"
        />
        <Load.StageInfo>
          Po zidentyfikowaniu wszystkich kart na zdjęciu, uruchamiany zostaje
          algorytm znajdujący najlepszą mozliwą pokerową kombinację kart z tych
          odczytanych na obrazie. Na poniższym obrazie końcowym oprócz nazwy
          znalezionej kombinacji, zaznaczone zostały karty wchodzące w jej
          skład.
        </Load.StageInfo>
        <Load.Image
          src={`${process.env.PUBLIC_URL}/results/result.jpg`}
          alt="Twoja kombinacja kart"
          id="current_image"
        />
        <Load.OptionsContainer image={image}>
          <Load.SmallOptionsContainer>
            <Load.ButtonLink to="/Pocker_Recognizer">
              Powrót do strony głównej
            </Load.ButtonLink>
          </Load.SmallOptionsContainer>
        </Load.OptionsContainer>
      </Load>
    </>
  );
};

export default ResultContainer;

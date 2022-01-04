<h1 align="center">
    Poker Recognizer ♠️
</h1>

_Also available in: [Polski](README.pl.md)_

## About

Poker Recognizer project for Human Computer Communication at Poznan University of Technology.

![result image](./public/result-sample.jpg)

The main goal of this project was to implement a card recognition algorithm using [flask](https://flask.palletsprojects.com/en/2.0.x/) and [OpenCV](https://opencv.org/) library in [python](https://www.python.org/).
Additionally, an algorithm for finding the best poker hand combination was implemented. All results, including the final image with annotated cards and the description of the algorithm based on the uploaded image are presented on a website created with the [React](https://reactjs.org/) library.

## Getting Started

To run this website locally, [yarn](https://yarnpkg.com/) and [pip](https://pypi.org/project/pip/) package managers must be installed on your system. In the projects directory:

1. Clone the repo
   ```sh
   git clone https://github.com/filipciesielski7/Poker_Recognizer.git
   ```
2. Navigate into the Poker_Recognizer directory
   ```
   cd Poker_Recognizer
   ```
3. Run this commands in the root folder to install all needed dependencies:
   ```
   pip install -r requirements.txt
   yarn install
   ```
4. After installing dependencies you can now run the website and python server using:
   ```
   yarn start
   yarn start-api
   ```

Then open http://localhost:3000/ to see the website.

## Contributors

<a href="https://github.com/filipciesielski7/Poker_Recognizer/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=filipciesielski7/Poker_Recognizer" />
</a>

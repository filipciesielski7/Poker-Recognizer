<h1 align="center">
    Poker Recognizer ♠️
</h1>

_Also available in: [Polski](README.pl.md)_

## About

Poker Recognizer project for Human Computer Communication at Poznan University of Technology.

![result image](./public/result-sample.jpg)

The main goal of this project was to implement card recognition algorithm using [flask](https://flask.palletsprojects.com/en/2.0.x/) and [OpenCV](https://opencv.org/) library in [python](https://www.python.org/). 
Additionally, best poker hand combination finder algorithm was also implemented. All the results, including not only final image with recognized and signed cards but also description how implemented algorithm works based on specific uploaded image are repesented on created with [React](https://reactjs.org/) library website.
## Getting Started

To run this website locally [yarn](https://yarnpkg.com/) and [pip](https://pypi.org/project/pip/) package menagers must be installed on your system. In the projects directory:

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
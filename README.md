# Make 24 Solver

On a scorching hot summer day in Shenzhen, China, the scene was set for a memorable family gathering. It was one of those idyllic moments when the universe seemed to align, and I was blissfully unaware of the tragedy that awaited me.

As we sat around the table, relishing the feast before us, laughter filled the air. By my side sat my cousin, an energetic primary school student whose schedule overflowed with extracurricular activities. To quote her father who back then worked for a tech company in Shenzhen, she was "much busier" than him.

In our conversation, her parents mentioned a card game called <a href="https://en.wikipedia.org/wiki/24_(puzzle)" target="_blank">***Make 24***</a>. That was the first time that I heard about this game, but apparently it originated from Shanghai and is famous in China. Her parents told me that she has been practicing so much that they no longer stood a chance against her. To be the champion feels good, but only when there are still people who are brave enough to challenge you. Her parents already gave up, so naturally she needed to expand her territory, and that's how I became her next contender.

Napoleon achieved many remarkable victories and expanded his empire throughout much of continental Europe, but even he was defeated in the pivotal Battle of Waterloo in 1815. As a person who studied physics and math in university, I knew that if someone would deliver the Battle of Waterloo to her ambitious expedition, it had to be me. I must admit that she is brilliant, but someone had to show her the power of grownups. I felt bad for her. Of course I want to be a kind brother figure, but when it comes to math there is no mercy. I knew that in a few minutes, she will lose all the confidence she had in this game, and might even be staring at the stain on the ceiling thinking about how much more there is to learn. I am sorry but that is just how serious I get with competitions.

A few minutes later, I found a spider as I stared closely at that stain on the ceiling. Actually I think there were also some baby spiders.

Brutally defeated, I sat on my bed that night thinking about how fast she was and how I would never be able to beat that directly. Once again she proved her strength. I am sure she has a bright future ahead of her. So here, with tears of lameness, I present to you a solver that I used to prove to her later that week that I can win as long as I have a computer. It could be quite useful if you also have a smart cousin.

## Installation
After cloning the repository, the `make24` package can be installed by running
```
pip install -e .
```
in the root directory. This allows us to simply import our functions, e.g., by running
```
from make24 import make24_solver
```
in Python.

## Structure
```
.
├── README.md
├── VERSION.txt
├── demos
│   ├── Demo of Make 24 Solver.ipynb
│   ├── Generate neq_eqs_TF array.ipynb
│   └── neq_eqs_TF.csv
├── make24
│   ├── __init__.py
│   ├── analysis.py
│   ├── solver.py
│   └── utils.py
├── requirements.txt
└── setup.py

```

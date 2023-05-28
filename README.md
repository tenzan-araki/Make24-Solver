# Make 24 Solver

On a scorching hot summer day in Shenzhen, China, I was having lunch with my family and some close relatives. By my side sat my cousin, an energetic primary school student whose schedule overflowed with extracurricular activities.

In our conversation, her parents mentioned a card game about arithmetics called <a href="https://en.wikipedia.org/wiki/24_(puzzle)" target="_blank">***Make 24***</a>. They told me that she has been practicing it so much that they no longer stood a chance against her. As the champion in her family, she was looking for someone to challenge her, and that's how I became her next contender.

Napoleon achieved many remarkable victories and expanded his empire throughout much of continental Europe, but even he was defeated in the Battle of Waterloo in 1815. As a person who studied physics and math in university, the whole family thought that if someone were to deliver the Battle of Waterloo to her ambitious expedition, it had to be me. Unfortunately for her, I like competitions, and especially when it comes to math there is no mercy. I just hoped that after I defeat her, she won't lose confidence in this game or even start staring at the stain on the ceiling after being struck by how cruel reality is. 

The battle began, and a few minutes later, I found a few spiders as I stared closely at that stain on the ceiling. I think they were a family.

Brutally defeated, I sat on my bed that night thinking about how fast she was and how I would never be able to beat that directly. Our Napoleon proved her strength, and I am sure she has a bright future ahead of her. So here, with tears of lameness, I present to you a solver that I wrote to prove that I can still win as long as I have a computer. I used it against her later that week, mostly winning, and from what I heard she wrote an essay about it for school. It could be quite useful if you also have a smart cousin.

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

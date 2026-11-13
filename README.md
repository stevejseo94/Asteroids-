# 🚀 Asteroids

A classic retro-style arcade space shooter built in Python using **Pygame**. Pilot your starfighter through a dense asteroid belt, blast incoming space rocks into fragments, and survive as long as possible to set a new high score!

![Gameplay Preview](https://canva.link/hk234j6g4aw709m)

---

## ✨ Features

* **Classic Arcade Physics:** Smooth 360-degree rotation, momentum-based thrust, and screen-wrapping movement.
* **Dynamic Asteroid Splitting:** Large asteroids break apart into faster medium and small fragments when shot.
* **Progressive Difficulty:** Waves increase in speed and density the longer you survive.
* **Retro Visuals & Audio:** Crisp vector-inspired graphics paired with classic arcade sound effects.

---

## 🎮 Controls

| Key | Action |
| :--- | :--- |
| **W** or **Up Arrow** | Engage thrusters (accelerate forward) |
| **A / D** or **Left / Right Arrows** | Rotate ship counter-clockwise / clockwise |
| **Spacebar** | Fire laser cannon |
| **P** | Pause game |
| **Enter** | Resume game / Restart game |
| **Esc** | Quit game |

---

## 🚀 How to Play (Quick Start)

### Prerequisites
Make sure you have **Python 3.8+** installed on your computer.

### Installation & Launch
1. **Clone the repository:**
   ```bash
   git clone https://github.com/stevejseo94/Asteroids-.git
   cd asteroids-pygame
   ```

2. **Install Pygame:**
   ```bash
   pip install pygame
   ```

3. **Run the game:**
   ```bash
   uv run main.py
   ```

---

## 🕹️ Scoring & Rules

* **Large Asteroid:** +20 points (splits into 2 medium asteroids)
* **Medium Asteroid:** +50 points (splits into 2 small asteroids)
* **Small Asteroid:** +100 points (destroyed completely)
* **Lives:** You start with **1 life**. Colliding with an asteroid ends the game. Pressing returns when the game is over restarts the game. 

---

## 🛠️ Built With

* [Python](https://python.org) — Core programming language
* [Pygame](https://pygame.org) — 2D graphics, input handling, and audio engine

---

## 📄 License

This project was created for demonstration and educational purposes. Feel free to fork, modify, and share!

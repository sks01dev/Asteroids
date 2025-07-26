
# 🪐 Asteroids – Classic Arcade Clone in Python (Pygame)

A modern remake of the classic **Asteroids** arcade game using **Python** and **Pygame**. Fly your ship, shoot bullets, and destroy asteroids that split into smaller fragments. Simple, fast, and addictive!

---

## 🎮 Gameplay Features

- 🚀 Player ship movement with rotation and momentum
- 🔫 Bullet shooting with rate limiting
- 💥 Asteroids that split into smaller ones when hit
- 🧠 Collision detection using vector math
- ♻️ Asteroids removed or split on collision
- 🧱 Modular, object-oriented structure

---

## 🕹️ Controls

| Key        | Action             |
|------------|--------------------|
| `W`        | Move forward        |
| `S`        | Move backward       |
| `A`        | Rotate left         |
| `D`        | Rotate right        |
| `Spacebar` | Shoot bullets       |
| `Esc`      | Quit game (optional)|

---

## 📁 Project Structure

```

Asteroids/
├── main.py               # Main game loop and setup
├── constants.py          # All game constants
├── player.py             # Player ship class and controls
├── shot.py               # Bullet behavior
├── asteroid.py           # Asteroid class, movement, splitting
├── asteroidfield.py      # Spawns initial asteroid field
├── circleshape.py        # Base class with collision logic
├── assets/               # (Optional) game assets like images or sounds
└── README.md             # You're reading it!

````

---

## 📦 Installation

### ✅ Requirements

- Python 3.8+
- Pygame 2.0+

### 🐍 Create Virtual Environment (Recommended)

```bash
python -m venv venv
source venv/bin/activate    # Linux/macOS
venv\Scripts\activate       # Windows
````

### 📥 Install Dependencies

```bash
pip install pygame
```

---

## ▶️ Running the Game

```bash
python main.py
```

---

## 🧠 How It Works

* **Player** inherits from `CircleShape`, handles movement, shooting.
* **Asteroids** inherit from `CircleShape`, split into two smaller ones if hit and large enough.
* **Shots** are small fast-moving bullets that destroy asteroids.
* **CircleShape** base class provides position, radius, and collision logic.

---

## 🪨 Asteroid Splitting Logic

* When a bullet hits an asteroid:

  * The asteroid calls `.split()`.
  * If large enough, it spawns two smaller asteroids in opposite directions.
  * Otherwise, it is just destroyed.

---

## 🛠️ Customization Ideas

* Add sound effects (`pygame.mixer`)
* Add score tracking and HUD
* Add player lives and a game-over screen
* Add level progression or enemy ships
* Export to WebAssembly using [pygame-ce](https://github.com/pygame-community/pygame-ce)

---



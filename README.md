# ⚔️ RPG Battle System

A turn-based battle system built in Python to practice advanced Object-Oriented Programming (OOP) concepts in a practical and interactive scenario.

The project simulates battles between characters with unique classes, attributes, combat styles, and polymorphic behaviors.

---

# 📸 Project Demonstration

## 🥊 Battle Start

Combat initialization:

<img width="305" height="122" alt="image" src="https://github.com/user-attachments/assets/b625cb8e-1609-4951-bc33-0668a7085ad2" />

---

## ⚔️ Characters Attacking

Polymorphic combat interactions between characters:

<img width="259" height="118" alt="image" src="https://github.com/user-attachments/assets/ae76e035-9d44-4524-ae11-3b8272091e3e" />

<img width="260" height="120" alt="image" src="https://github.com/user-attachments/assets/7bbd50fb-c31a-4e4e-922e-67a941077073" />

<img width="245" height="121" alt="image" src="https://github.com/user-attachments/assets/643f9336-a524-4edc-b125-8b6b9a9838b4" />

---

## ☠️ Defeated Character

Character defeat handling and health validation:

<img width="289" height="149" alt="image" src="https://github.com/user-attachments/assets/7387dbe4-7862-4481-81c2-ea07b6723f4c" />

---

## 📊 Final Character Status

Final battle results and remaining stats:

<img width="255" height="339" alt="image" src="https://github.com/user-attachments/assets/3d69146c-0e12-48b1-8906-b5fb298b1564" />

---

# 🚀 Technologies Used

* Python 3

---

# 📚 Applied Object-Oriented Programming Concepts

This project was designed to reinforce software engineering and OOP principles through a game-oriented architecture.

---

## ✅ Classes and Objects

Each character is instantiated from a dedicated class derived from the base `Personagem` class.

---

## ✅ Encapsulation

Protected attributes are used to preserve internal object state and improve data integrity.

```python
self._nome
self._vida
self._ataque
```

---

## ✅ Inheritance

The specialized classes:

* `Guerreiro`
* `Mago`
* `Arqueiro`

inherit common behaviors and attributes from the parent class.

```python
class Guerreiro(Personagem)
```

---

## ✅ Polymorphism

One of the core concepts implemented in the project.

Each subclass overrides the `atacar()` method with its own combat style:

* Warrior → heavy sword attack
* Mage → fireball spell
* Archer → critical arrow shot

Although every object uses the same method name:

```python
personagem.atacar(alvo)
```

each class executes the action differently.

---

## ✅ Method Overriding

The attack behavior is redefined inside each subclass:

```python
def atacar(self, alvo):
```

This allows each character type to have unique combat interactions.

---

## ✅ Object Interaction

Objects dynamically communicate with each other during battle execution:

```python
guerreiro.atacar(mago)
```

The attacker interacts directly with another object instance.

---

## ✅ State Management

Characters maintain internal mutable state:

* current health
* attack value
* defeat status

Health is dynamically updated throughout combat.

---

## ✅ Business Logic & Validation

The system contains several gameplay validations:

* health cannot go below 0
* defeated characters cannot attack
* battle loop ends when only one fighter remains

---

# 🎮 Character Classes

## 🛡️ Guerreiro (Warrior)

* Health: 150
* Attack: 20
* Durable melee fighter with heavy attacks.

---

## 🔮 Mago (Mage)

* Health: 120
* Attack: 40
* High magical damage dealer.

---

## 🏹 Arqueiro (Archer)

* Health: 100
* Attack: 50
* Agile ranged attacker with critical strikes.

---

# ⚔️ Battle System

The battle is executed automatically using loops and conditional logic.

During combat:

* characters attack one another
* damage is applied
* health is updated in real time
* defeated characters are removed from active combat

Example output:

```text
Thorin usou ESPADA PESADA em Merlin!
Merlin recebeu 20 de dano!
Vida atual de Merlin: 100

================================
```

---

# 📂 Project Structure

```text
📦 rpg-battle-system
 ┣ 📜 main.py
 ┗ 📜 README.md
```

---

# 💡 Skills Demonstrated

This project demonstrates practical knowledge of:

* Object-Oriented Programming
* System Modeling
* Inheritance
* Encapsulation
* Polymorphism
* Method Overriding
* State Management
* Battle Logic
* Object Interaction
* Python Programming

---

# 🔥 Possible Future Improvements

* Special abilities
* Mana system
* Inventory system
* Experience (XP)
* Level progression
* Boss battles
* Save system
* Graphical interface
* Multiplayer combat

---

# 👩‍💻 Developed by

[Ana Caroline Vasconcellos](https://github.com/Vasconcellos-cipher) 🚀

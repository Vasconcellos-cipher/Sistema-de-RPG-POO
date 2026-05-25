# ⚔️ RPG Battle System

A mini turn-based battle system built in Python to practice Object-Oriented Programming (OOP) concepts in a practical scenario.

The project simulates combat between characters with distinct classes, attributes, and behaviors.

---

# 📸 Project Demonstration

## 🥊 Battle Start

Combat initiation:

<img width="305" height="122" alt="image" src="https://github.com/user-attachments/assets/b625cb8e-1609-4951-bc33-0668a7085ad2" />

---

## ⚔️ Characters Attacking

Character interactions and combat turns:

<img width="259" height="118" alt="image" src="https://github.com/user-attachments/assets/ae76e035-9d44-4524-ae11-3b8272091e3e" />

<img width="260" height="120" alt="image" src="https://github.com/user-attachments/assets/7bbd50fb-c31a-4e4e-922e-67a941077073" />

<img width="245" height="121" alt="image" src="https://github.com/user-attachments/assets/643f9336-a524-4edc-b125-8b6b9a9838b4" />

---

## ☠️ Defeated Character

When a character loses all their health points (HP):

<img width="289" height="149" alt="image" src="https://github.com/user-attachments/assets/7387dbe4-7862-4481-81c2-ea07b6723f4c" />

---

## 📊 Final Character Status

The final result of the battle:

<img width="255" height="339" alt="image" src="https://github.com/user-attachments/assets/3d69146c-0e12-48b1-8906-b5fb298b1564" />

---

# 🚀 Technologies Used

* Python 3

---

# 📚 Applied Object-Oriented Programming Concepts

This project was developed to implement and reinforce fundamental OOP principles.

## ✅ Classes and Objects

Each game character is instantiated from a specific class derived from the base `Character` class.

---

## ✅ Encapsulation

Character attributes are protected and encapsulated using Python standard naming conventions:

```python
self._health
self._attack
self._name

```

---

## ✅ Inheritance

The specific classes:

* Warrior
* Mage
* Archer

inherit core attributes and behaviors from the parent `Character` class.

---

## ✅ Code Reusability with `super()`

Subclasses invoke and reuse the constructor logic of the parent class utilizing:

```python
super().__init__()

```

---

## ✅ Methods

Characters possess dynamic behaviors implemented through methods, such as:

* attack
* take damage
* display status

---

## ✅ Object Interaction

Objects interact dynamically with each other during the execution of the combat loop:

```python
warrior.attack(mage)

```

---

## ✅ Business Logic & Validation

The system features robust conditional validation:

* Minimum health capped at 0
* Verification of defeated status
* Restriction of actions for defeated characters

---

# 🎮 Game Characters

## 🛡️ Warrior

* Health: 150
* Attack: 20
* Class focused on high defense and durability.

---

## 🔮 Mage

* Health: 120
* Attack: 40
* Class focused on high magical damage output.

---

## 🏹 Archer

* Health: 100
* Attack: 50
* Class focused on swift and high-impact physical strikes.

---

# ⚔️ How the Battle Works

The simulation runs automatically driven by control flow loops.

As long as there are multiple characters standing:

* Characters perform attacks
* Damage is calculated and applied
* Health status is dynamically updated
* Defeated characters are filtered out

System output example:

```text
Thorin atacou Merlin!
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

# 👩‍💻 Developed by

[Ana Caroline Vasconcellos](https://github.com/Vasconcellos-cipher) 🚀


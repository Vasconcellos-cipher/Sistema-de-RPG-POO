# ⚔️ RPG Battle System

Um mini sistema de batalha em Python desenvolvido para praticar Programação Orientada a Objetos (POO) de forma aplicada.

O projeto simula batalhas entre personagens com diferentes classes, atributos e comportamentos.

---

# 📸 Demonstração do Projeto

## 🥊 Início da batalha

Coloque aqui um print mostrando o começo do combate:

<img width="305" height="122" alt="image" src="https://github.com/user-attachments/assets/b625cb8e-1609-4951-bc33-0668a7085ad2" />


---

## ⚔️ Personagens atacando

Coloque prints mostrando as interações entre os personagens:

<img width="259" height="118" alt="image" src="https://github.com/user-attachments/assets/ae76e035-9d44-4524-ae11-3b8272091e3e" />

<img width="260" height="120" alt="image" src="https://github.com/user-attachments/assets/7bbd50fb-c31a-4e4e-922e-67a941077073" />

<img width="245" height="121" alt="image" src="https://github.com/user-attachments/assets/643f9336-a524-4edc-b125-8b6b9a9838b4" />

---

## ☠️ Personagem derrotado

Coloque um print mostrando quando um personagem perde toda a vida:

<img width="289" height="149" alt="image" src="https://github.com/user-attachments/assets/7387dbe4-7862-4481-81c2-ea07b6723f4c" />


---

## 📊 Status final dos personagens

Coloque um print mostrando o resultado final da batalha:

<img width="255" height="339" alt="image" src="https://github.com/user-attachments/assets/3d69146c-0e12-48b1-8906-b5fb298b1564" />


---

# 🚀 Tecnologias utilizadas

* Python 3

---

# 📚 Conceitos de Programação Orientada a Objetos aplicados

Este projeto foi desenvolvido para praticar conceitos importantes de POO.

## ✅ Classes e Objetos

Cada personagem do jogo é uma classe derivada da classe principal `Personagem`.

---

## ✅ Encapsulamento

Os atributos dos personagens são protegidos utilizando convenções do Python:

```python
self._vida
self._ataque
self._nome
```

---

## ✅ Herança

As classes:

* Guerreiro
* Mago
* Arqueiro

herdam atributos e comportamentos da classe principal `Personagem`.

---

## ✅ Reutilização de código com `super()`

As subclasses reutilizam a lógica da classe pai utilizando:

```python
super().__init__()
```

---

## ✅ Métodos

Os personagens possuem comportamentos como:

* atacar
* tomar dano
* mostrar status

---

## ✅ Interação entre objetos

Os personagens interagem entre si durante a batalha:

```python
guerreiro.atacar(mago)
```

---

## ✅ Regras de negócio

O sistema possui validações importantes:

* vida mínima igual a 0
* personagens derrotados
* bloqueio de ataques após derrota

---

# 🎮 Personagens do jogo

## 🛡️ Guerreiro

* Vida: 150
* Ataque: 20
* Classe focada em resistência.

---

## 🔮 Mago

* Vida: 120
* Ataque: 40
* Classe focada em dano mágico.

---

## 🏹 Arqueiro

* Vida: 100
* Ataque: 50
* Classe focada em ataques rápidos e fortes.

---

# ⚔️ Como funciona a batalha

A batalha acontece automaticamente utilizando estruturas de repetição.

Enquanto houver mais de um personagem vivo:

* os personagens atacam
* recebem dano
* têm a vida atualizada
* podem ser derrotados

Exemplo de saída do sistema:

```text
Thorin atacou Merlin!
Merlin recebeu 20 de dano!
Vida atual de Merlin: 100

================================
```

---

# 📂 Estrutura do projeto

```text
📦 rpg-battle-system
 ┣ 📜 main.py
 ┗ 📜 README.md
```

---

# 👩‍💻 Desenvolvido por

[Ana Caroline Vasconcellos](https://github.com/Vasconcellos-cipher) 🚀

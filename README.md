# Cake Mania Bot
Python color bot to play Cake Mania

## Introduction
The goal of this project is to create a simple python bot to play the game Cake Mania. The idea is based off a tutorial (https://code.tutsplus.com/tutorials/how-to-build-a-python-bot-that-can-play-web-games--active-11117) to play Sushi Go Round, a similar point and click cooking game. By building the code with Cake Mania, the concepts will be the same but the graphics and gameplay mechanics will provide a challenge to recreate the functionality of the tutorial

## Type of Bot
There are many types of bots that can play games. This bot is what is called a color bot. This means it will look at predefined portions of the screen and look at the colors of the portion of the screen to determine what appears in that section of the screen. After determining the action to take, it will send mouse inputs to take the action.

## Game Mechanics
The game used is the flash version of Cake Mania (http://www.shockwave.com/gamelanding/cakemania.jsp). This is good to get the basic mechnaics down and play around with the bot. The flash version has the limitation that the kitchen cannot be upgraded, so the desktop version will be needed to get the full game.

In cake mania, you own a cake shop. Customers come into the shop and you must give them menus. They will order a cake based on the equipment you have available. Cakes can have 1 or two tiers, each tier frosted. Finally, cakes can have a topper on top.

Each part of a cake is made at a different station in the kitchen. There are up to 3 ovens, up to 3 frosting stations, and up to 2 different topper stations with multiple different toppers at each station. The kitchen starts with a single oven and frosting station, the rest must be purchased. Each station can also be upgraded. Ovens and frosting stations can be upgraded to perform faster and the topping station will add additional toppers when upgraded.

Cakes must be made from the bottom up. A 2 tiered cake with a topper first needs to cook the bottom layer. That layer is the frosted while the second layer is baked. The second layer is placed on top of the first and frosted. The entire cake is then taken to the topping station where the topper is added.

At any given time, there can be up to 4 customers in the shop. They are in fixed positions, but as cakes are handed out to customers, they will move up in the queue.
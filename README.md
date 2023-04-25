# Chaser Game
(DSA_Project_2023)

In this project we have implemented a graphing system for a fun little game design. The concept of the game is that the player has to reach an end goal by chosing turns i.e up, down ,left or right(the player can not move diagnolly). The challenge arises as the player somehow needs to go past the chaser(red dot) which is guarding the winning point. The chaser follows a dijkstra's algorithm to find the shortest path to the player and takes one step whenever the player decides to move.

Version 1.0:

In this version the chaser is also able to see when the player is in its LOS(line of sight) but currently that does not effect the game in any shape or form. But in the coming days we might update the graph to increase in size and that would make it so that when the chaser sees the player, the players is slowed. Meaning in that version the player moves two places in the direction they chose and one when they are slowed making it more challenging.

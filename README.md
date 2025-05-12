# 4kitsw10_COM526_1 (Introduction to AI Assessment)
## Who 
I developed this project during my 2025 Software Engineering degree’s Introduction to AI module, using my student GitHub credentials (4kitsw10). I am the sole contributor and maintainer of this project. 

## What 
This project comprises the practical assessment for my Introduction to AI module. The specification required me to develop in incrementally advanced AI for an automated cleaning robot, each version demonstrating my ability to develop a specific AI technique. This project was written in Python.

### Version 1: Intelligent Agent
Version one of the cleaning robot is a basic Intelligent Agent, it randomly explores a map in 2D space until its battery is depleted. It features collision detection and can only move in the direction its facing. Its intelligent enough to determine if it’s about to move into an occupied space and turn until it has a valid move. Version one also defines the charging station Intelligent Agent. The charging station can only charge the cleaning robot if the robot occupies the station’s charging zone.

### Version 2: Pathfinding
Version 2 extends version 1 by introducing pathfinding. Now, rather than randomly exploring the map, the robot is smart enough to remember the volume of dirt in surrounding coordinates and pathfind its way to the dirtiest location. When the battery gets low, the cleaner uses its pathfinder to return to the charging stations charge zone.

### Version 3: Fuzzy Logic
Version 3 implements Fuzzy Logic to manage the battery by adjusting the cleaners fan speed of in response to the current battery and the volume of dirt its currently cleaning.

### Version 4: Machine Learning
Finally, version 4 implements machine learning to identify the type of debris located at a coordinate. The model was trained on provided dummy data and allows the cleaner to avoid unmanageable debris.

## When 
I developed this project in the first semester of my second year of my Software Engineering course, September to December of 2024.

## Where 
This project was developed at Solent University. 

## Why
This project was developed to demonstrate my skills at developing introductory level AI systems, including Intelligent Agents, Pathfinding, Fuzzy Logic, and Machine Learning. This project is the foundation for my future third year AI assessment. I received a First for this assessment (75/100).

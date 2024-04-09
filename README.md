# Hackathon Météo France

**Défi : Ilot de chaleur urbain**

Equipe :
- Béatrice Maranget (Géomaticienne)
- Romain Bouzige (Géomaticien)  
- Sofiane Bouaziz (PhD en IA)
- Elise Chin (Data Scientist)

Réutilisation : https://www.data.gouv.fr/fr/reuses/des-icu-du-futur/


## 1. Problématique et proposition de valeur 

Notre projet vise à relever le défi de la lutte contre les îlots de chaleur urbains dans la région Île-de-France (IDF). Actuellement, l'Institut Paris Région (IPR) propose une carte interactive permettant de visualiser ces îlots de chaleur, à partir d'une multitude de paramètres tels que le nombre de surfaces bâties, les obstacles à la vue du ciel, l'imperméabilisation des sols, la chaleur anthropique, et bien d'autres. Cependant, deux problématiques se présentent. Premièrement, cette solution se concentre uniquement sur les caractéristiques morphologiques, sans tenir compte des données météorologiques dont le rôle est crucial dans la génération d'îlots de chaleur. Deuxièmement, l'étude de l'IPR est basée sur des données anciennes datant des années 2010, ce qui la rend obsolète et non conforme aux développements actuels.

Dans ce contexte, notre objectif est de tester les prédictions de l'IPR en utilisant les données publiques fournies par Météo France, à la fois les données quotidiennes de base et les données de référence SIM. Nous avons ainsi tenté de démontrer l'importance des données météorologiques dans l'amélioration des solutions existantes. Par la suite, nous avons exploré l'impact de la résolution spatiale sur la génération d'îlots de chaleur urbains.

## 2. Solution

Notre approche repose sur une méthode de projection des données qui vise à fusionner les informations de l'IPR avec les données météorologiques de Météo France, permettant ainsi de détecter les écarts et les anomalies. Dans un premier temps, nous avons sélectionné et extrait les données météorologiques de base des stations localisées dans la région Île-de-France, ainsi que les données de référence SIM correspondantes. En parallèle, nous avons recueilli les données de l'IPR, notamment les îlots de chaleur de forte intensité. 

Compte tenu de la précision géographique des données météorologiques des stations, une simple projection directe avec les données de l'IPR ne suffisait pas à obtenir des résultats précis. Pour résoudre ce problème, nous avons mis en place une méthode de génération de zones tampons autour de chaque point météorologique. Ensuite, nous avons calculé le nombre d'îlots de chaleur présents dans ces zones tampons. Les données de référence SIM, déjà structurées sous forme de grilles avec des tampons, n'ont pas nécessité cette étape de génération de zones tampons. Une fois cette projection réalisée, nous avons appliqué une méthode de standardisation pour évaluer la présence d'îlots de chaleur en fonction des températures. Enfin, nous avons comparé ces résultats avec les données de l'IPR pour identifier d'éventuelles divergences ou anomalies.

## 3. Impact envisagé

Notre solution offre la capacité de détecter les anomalies dans les prédictions de l'IPR, remettant ainsi en question leur fiabilité et démontrant l'impact des données météorologiques de Météo France pour corriger ces erreurs. Elle fournit un outil précieux aux collectivités territoriales, pour les permettre de prendre des décisions éclairées en matière d'aménagement urbain et d'intégrer efficacement les données météorologiques pour obtenir des résultats plus précis.

Les utilisateurs ciblés sont principalement les collectivités territoriales, qui peuvent exploiter notre solution pour proposer des choix d'aménagement plus pertinents et pour explorer des pistes intégrant les données de Météo France.

Par ailleurs, deux perspectives d'avenir s'avèrent prometteuses. Tout d'abord, la généralisation de notre solution à d'autres régions que l'Île-de-France, une démarche tout à fait réalisable grâce au code source que nous fournissons. Ensuite, l'exploration de méthodes avancées de fusion de données basées sur l'intelligence artificielle, notamment l'utilisation de réseaux génératifs, pourrait permettre d'accroître la précision de la détection des îlots de chaleur et d'ouvrir de nouvelles perspectives dans la lutte contre ce phénomène.

<p align="center"> 
 <img width="1000" height="400" alt="Ekran Resmi 2021-06-28 01 15 28" src="https://github.com/ItayG6454/Data-Science-Portfolio/blob/main/photos/long%20lives%20cutted.jpg">
</p>

# Prediciting Life Expactancy

### The Dataset
The dataset is taken from [WHO (World Health Organiztion)](https://www.who.int/data/gho/data/themes/mortality-and-global-health-estimates).
Each country has 15 observations -one for a year that contains social data (number years of schooling, alcohol consumption) economic data (GDP) and social health diseases (measles, hepatitis and HIV).
At first step we preformed **data cleaning** while taking in count outliers and abilty to preform back/front - filling. 
### Exploratory Data Analysis
At this stage we tries to understand **initial trends and correlations** for better understanding of the data.
For example, what is the difference between developed and developing countries:

<p align="center"> 
 <img width="500" height="400" src="https://github.com/ItayG6454/Data-Science-Portfolio/blob/main/photos/life_dist.png">
</p>

### Models and R2 Scores
After **Skewing and Encoding** as a prepration of the data for modeling.
We applied 7 different models and measured their preformance upon both the test set and K-fold CV sets.
After comparison, we analyized the feature preformance in order to detemined *whice factors has most imact on life expectancy* according to the best model. 
##### The results of models comparison - **Gradient Boost** preformed the best $R^2$ score:
<p align="center"> 
 <img width="800" height="400" src="https://github.com/ItayG6454/Data-Science-Portfolio/blob/main/photos/Models%20comp.png">
</p>

##### The results of factors comparison:
<p align="center"> 
 <img width="900" height="500" src="https://github.com/ItayG6454/Data-Science-Portfolio/blob/main/photos/features%20comp.png">
</p

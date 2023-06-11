# Machine Learning Path

## Description
The idea of MasTour revolves around providing tour guide recommendations based on the compatibility between tourists and tour guides. This compatibility is determined not only by the tourists' travel preferences but also by the alignment of their personality types with those of the tour guides.

MasTour aims to enhance the travel experience by considering various factors, including:

- **Travel Preferences**: Mastour takes into account the tourists' preferences for different types of tours, such as historical, adventure, nature and wildlife, culinary, wellness and retreat, architectural, educational, and shopping tours. These preferences help in matching tourists with tour guides who specialize in and have expertise in the preferred tour types.

- **Personality Matching**: Mastour assesses the personality traits of both tourists and tour guides. It considers traits like extroversion, openness to new experiences, conscientiousness, agreeableness, and emotional stability. By aligning compatible personality traits, Mastour aims to create a harmonious and enjoyable experience between tourists and tour guides.

- **Compatibility Score**: Mastour calculates a compatibility score that represents the degree of alignment between the tourists and tour guides based on their preferences and personality traits. This score helps in ranking the tour guides according to their level of compatibility with the tourists.

By incorporating travel preferences and personality matching, MasTour provides personalized and tailored tour guide recommendations, ensuring that tourists are matched with guides who not only align with their travel interests but also complement their personalities.

Through this approach, MasTour aims to create memorable and fulfilling travel experiences by facilitating strong connections between tourists and tour guides, resulting in a more enjoyable and satisfying exploration of destinations.

### Personality Classification
### Matchmaking Feature
### Dataset

To build the personality prediction model we use a big five personality test dataset from Kaggle. This dataset contains 1,015,342 questionnaire answers collected online by Open Psychometrics and can be accessed [here](https://www.kaggle.com/datasets/tunguz/big-five-personality-test).

To build the matchmaking model, we collected primary data through a Google Form survey. The Google Form can be accessed [here](https://docs.google.com/forms/d/e/1FAIpQLScI-_8k0maIxFXTGHLj-qNT8wQToCuOT9TrCMpav35_6bie1A/viewform). From this survey form, we received responses from 101 participants. After the data cleaning process, we obtained a total of 28 tour guide data and 73 tourist data, which are available for access here(soon).

### Reference

Akdağ, Melih. (2020). Five Personality Clusters (K-Means). Accessed on May 16th 2023 via [Five Personality Clusters (K-Means)](https://www.kaggle.com/code/akdagmelih/five-personality-clusters-k-means).
Sivri, S. Zeynep. (2022). Five Personality Clustering. Accessed on May 16th 2023 via [Five Personality Clustering](https://www.kaggle.com/code/zeynepsivri/five-personality-clustering).
M, Siddharth. (2021). Performing Multi-class Classification on FIFA Dataset Using Keras. Accessed on May 24th 2023 via M, Siddharth. (2021). [Performing Multi-class Classification on FIFA Dataset Using Keras](https://www.analyticsvidhya.com/blog/2021/07/performing-multi-class-classification-on-fifa-dataset-using-keras/).
Chng, Gerry. (2020). Using the Right Dimensions for Your Neural Network. Accessed on May 24th 2023 via [Using the Right Dimensions for Your Neural Network](https://towardsdatascience.com/using-the-right-dimensions-for-your-neural-network-2d864824d0df).
Ahmed, Shariq. (2020). Machine Learning Matchmaking. Accessed on June 4th 2023 via [Machine Learning Matchmaking](https://towardsdatascience.com/machine-learning-matchmaking-4416579d4d5e).
Sharma, Pulkit. (2020). Understanding Distance Metrics Used in Machine Learning. Accessed on June 4th 2023 via [Understanding Distance Metrics Used in Machine Learning](https://www.analyticsvidhya.com/blog/2020/02/4-types-of-distance-metrics-in-machine-learning/).

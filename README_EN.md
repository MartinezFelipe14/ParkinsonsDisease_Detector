This project was developed by Felipe R. Martinez based on the research projects mentioned below. Social Networks: [GitHub](https://github.com/MartinezFelipe14) / [LinkedIn](https://www.linkedin.com/in/martinezfelipe14/)

------------------------------------------------------------------------------------------------------------------------

This project uses a model of Artificial Intelligence with supervised learning to calculate the probability of an individual having Parkinson's disease, based on a database provided by the UC Irvine Machine Learning Repository. The model was inspired by the studies conducted by Max A. Little, Patrick E. McSharry, Eric J. Hunter, Lorraine O. Ramig and others, as documented in the following articles:

- 'Exploiting Nonlinear Recurrence and Fractal Scaling Properties for Voice Disorder Detection', Little MA, McSharry PE, Roberts SJ, Costello DAE, Moroz IM. BioMedical Engineering OnLine 2007, 6:23 (26 June 2007)
- A Tsanas, MA Little, PE McSharry, LO Ramig (2009) 'Accurate telemonitoring of Parkinson.s disease progression by non-invasive speech tests', IEEE Transactions on Biomedical Engineering.

These research projects were fundamental to the development of this AI model, which uses voice measurements to identify characteristics associated with the condition. The intention of this project is to provide a useful tool to help in early detection and monitoring the progression of the Parkinson's progression.

------------------------------------------------------------------------------------------------------------------------

Information about the indicators:

subject#: An integer that uniquely identifies each subject or participant in the study.
age: Subject's age.
sex: Subject's gender, where '0' represent male and '1' represent female.
test_time: Time since recruitment for the study, where the integer part represents the number of days since recruitment.
Jitter(%), Jitter(Abs), Jitter:DDP: Various measures of variation in voice fundamental frequency.
Shimmer, Shimmer(dB), Shimmer:APQ3, Shimmer:APQ5, Shimmer:DDA: Various measures of variation in voice amplitude.
NHR, HNR: Two measures of the ratio between noise and tonal components in voice.
RPDE: A measure of nonlinear dynamic complexity.
DFA: Fractal scale exponent of the signal.
PPE: A nonlinear measure of fundamental frequency variation.



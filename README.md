# EEG: alcoholic or not?

## Motivation

This is a repository of a project done as a part of *Machine Perception* course in the program of *Artificial
Intelligence* master's studies at Poznan University of Technology.

## Problem statement

The dataset was published by Henri Begleiter at the Neurodynamics Laboratory at the State University of New York Health
Center at Brooklyn of Kaggle platform. The detailed description can be found under the
link: https://www.kaggle.com/datasets/nnair25/Alcoholics.

After the link mentioned above, problem statement is as follows:
> This data arises from a large study to examine EEG correlates of genetic predisposition to alcoholism. It contains
> measurements from 64 electrodes placed on subject's scalps which were sampled at 256 Hz (3.9-msec epoch) for 1 second.
>
> There were two groups of subjects: alcoholic and control. Each subject was exposed to either a single stimulus (S1) or
> to two stimuli (S1 and S2) which were pictures of objects chosen from the 1980 Snodgrass and Vanderwart picture set.
> When two stimuli were shown, they were presented in either a matched condition where S1 was identical to S2 or in a
> non-matched condition where S1 differed from S2.

## The most significant accomplishments

- We performed EDA, where we have shown that the two classes are balanced. We also noticed that it's easy to make time
  series stationary, which was a good promise for successfully problem accomplishment.
- We computed 3 statistics per each time series: minimum, average and maximum; which compressed the input data
  from [64, 256] to 3 * 256 values. Later on these variables were used as an input for logistic regression. The model
  achieved accuracy and f1 above 0.94.
- We examined the capabilities of shallow recurrent neural networks to the given task. We've shown that these models
  perform as well as logistic regression, but it seems to be unlikely to outperform logistic regression. That seems to
  imply that there is a noise in the data or there are other circumstances making the data hard. Thus even the optimal
  classifier may have non-zero risk.
- We used the explainability of logistic regression to show which sensors and characteristics suggest that the examined
  person is an alcoholic.
- We augmented the data to prove that it's possible to train a model yielding predictions of similar quality to ones
  described above having much fewer data.
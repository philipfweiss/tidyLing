# TidyLing

TidyLing is an online resource for linguists. It takes linguistics papers in .tex format and returns the data (examples) in the paper in a .csv file. This allows authors to upload or submit their papers with the data provided in a separate file for other researchers to use and cite.

In a tidy dataset, each observation is a row and each variable in a column ([Wickham 2014](http://vita.had.co.nz/papers/tidy-data.html)). Tidy data sets are easy to manipulate, model, and visualize.

# TidyLing data

Tidy linguistic data (tidyling data) is a tidy dataset for linguistic examples. In TidyLing datasets each linguistic example occupies a row and the columns are the variables of interest to linguists such as the transliteration, the gloss, the translation, and the judgement. The table below shows an example tidyling dataset.

| Judgement | Transliteration | Gloss | Translation | Language | Context | Source | document name | tags | notes | 
|------|---------|-------------|-----|--------|-------|-------|-------|-------|------ |
| # | Colorless green ideas sleep furuously| | | English | | Chomsky (1957) | chomskynoam1957.tex | | | 
| ? | Amir raft xune | Amir went home | Amir went home | Farsi | | Jasbi (2017) | jasbi2017.tex |farsi, word order|this is a made up example |
| # | man xoshhalam| 1SG happy-1SG | I am happy | Farsi | Writing a linguistics paper| Jasbi (2017) | jasbi2017.tex | farsi, adjective, | |

# TexLing

While we aim to accommodate different styles of linguistic examples in LaTex, it is helpful to our parser if linguists use conventional ways of writing up examples that match the TidyLing ouput. We have developed the TidyLing Tex commands to develop such common conventions.

# Sharing Linguistic Data

A large part of linguistics research relies on natives speaker judgments as primary empirical data. However, such data are often hard to access. 

# Join the Team

TidyLing is a project by Masoud Jasbi, Sebastian Schuster, and Philip Weiss. We are currently working on making our parser more and more accurate in detecting linguistics examples in documents. If you are interested in helping email masoudj@stanford.edu.

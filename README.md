# TidyLing

TidyLinguist is an online resource for linguists. It takes linguistics papers in Latex, Word, or PDF format and returns a csv file in what we call TidyLing format with the linguistic examples in the paper.

## TidyLing Format

In a tidyling format each linguistic example occupies a row and the columns are the variables of interest to linguistis such as the transliteration, the gloss, the translation, and the judgement.

| Judgement | Transliteration | Gloss | Translation | Language | Context | Source | document name | notes | 
|------|:---------:|:-------------:|:-----:|:--------:|:-------:|:-------:|:-------:|:-------:|
| ? | example 1 | right-aligned | $1600 | | | | | |
| # | example 2 | centered      |   $12 | | | | | |
| | example 3 | are neat      |    $1 | | | | | |

TidyLing is a tidy data set for linguistics examples. In a tidy dataset, each observation is a row and each variable in a column ([Wickham 2014](http://vita.had.co.nz/papers/tidy-data.html)).

# Database of Linguistics Examples

A large part of linguistics research relies on natives speaker judgments as primary empirical data. However, the valuable natives speaker judgments are often hard to access and search. 

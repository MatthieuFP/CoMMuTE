# Contrastive Multilingual Multimodal Translation Evaluation

The aim of Multimodal Machine Translation is to disambiguate sentences in a source language into the target language thanks to additional visual inputs. We release a Contrastive Multilingual Multimodal Translation Evaluation dataset (CoMMuTE) whose goal is to evaluate models' ability to exploit images in order to disambiguate English sentences and produce correct translations in French, German or Czech. 
Concretely, CoMMuTE is composed of lexically ambiguous sentences in English where there are two possible translations depending of the image for each example. Models are asked to rank the pairs of translations based on the perplexity score. 

## Example

## Evaluation
To evaluate models, please provide a text file with perplexity scores for the correct translations and another one with the incorrect translations scores. The expected format is "1.3456\n5.6432\n...". Then, run the following command line:

`python3 evaluate.py correct.txt incorrect.txt`

## License
The evaluation datasets are distributed under a CC BY-NC-SA 4.0 licence.




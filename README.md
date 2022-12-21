# Contrastive Multilingual Multimodal Translation Evaluation

The aim of Multimodal Machine Translation is to disambiguate sentences in a source language into the target language thanks to additional visual inputs. We release a **C**ontrastive **M**ultilingual **Mu**ltimodal **T**ranslation **E**valuation dataset (CoMMuTE) whose goal is to evaluate models' ability to exploit images in order to disambiguate English sentences and produce correct translations in French, German or Czech. 
Concretely, CoMMuTE is composed of lexically ambiguous sentences in English where there are two possible translations depending of the image for each example. Models are asked to rank the pairs of translations based on the perplexity score. 

Half of the English source sentences are from [<ins>DiscEvalMT</ins>](https://github.com/rbawden/discourse-mt-test-sets).

## Download images
Images can be downloaded [<ins>here</ins>](https://drive.google.com/drive/folders/1FrvKN1PyR7zeGLllCLp50TbM0OS8LCSc?usp=sharing). To extract the content, please run the following command line:

`tar -xvzf images.tar.gz`

## Example

English source sentence to be translated into French:

_He finally made it to the **<ins>bank</ins>**._

Image 1             |  Image 2
:-------------------------:|:-------------------------:
<a href="https://zupimages.net/viewer.php?id=22/51/aao0.jpeg"><img src="https://zupimages.net/up/22/51/aao0.jpeg" width="250" height="171" /></a> | <a href="https://zupimages.net/viewer.php?id=22/51/c9r9.jpeg"><img src="https://zupimages.net/up/22/51/c9r9.jpeg" width="250" height="171" /></a>
_Il a réussi à aller à la **<ins>banque</ins>**._  |  _Il a réussi à atteindre la **<ins>rive</ins>**._

In this English source sentence, **_bank_** is ambiguous and can be translated in two different ways. The image solves the ambiguity, if you show the image 1 (resp. 2) , the correct translation is "**_banque_**" (resp. "**_rive_**").
## Evaluation
To evaluate models, please provide a text file with perplexity scores for the correct translations and another one with the incorrect translations scores. The expected format is "1.3456\n5.6432\n...". Then, run the following command line:

`python3 evaluate.py correct.txt incorrect.txt`

## Citation

If you use this corpus, please cite:
```
@article{CoMMuTE,
  doi = {10.48550/ARXIV.2212.10140},
  url = {https://arxiv.org/abs/2212.10140},
  author = {Futeral, Matthieu and Schmid, Cordelia and Laptev, Ivan and Sagot, Benoît and Bawden, Rachel},
  title = {Tackling Ambiguity with Images: Improved Multimodal Machine Translation and Contrastive Evaluation},
  publisher = {arXiv},
  year = {2022}
}
```

## License
The evaluation datasets are distributed under a CC BY-NC-SA 4.0 licence.




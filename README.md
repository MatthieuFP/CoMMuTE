# Contrastive Multilingual Multimodal Translation Evaluation

The aim of Multimodal Machine Translation is to disambiguate sentences in a source language into the target language thanks to additional visual inputs. We release a **C**ontrastive **M**ultilingual **Mu**ltimodal **T**ranslation **E**valuation dataset (CoMMuTE) whose goal is to evaluate models' ability to exploit images in order to disambiguate English sentences and produce correct translations in French, German or Czech. 
Concretely, CoMMuTE is composed of lexically ambiguous sentences in English where there are two possible translations depending of the image for each example. Models are asked to rank the pairs of translations based on the perplexity score. More details can be found in the ACL 2023 paper "Tackling ambiguity with Images" by Matthieu Futeral, Cordelia Schmid, Ivan Laptev, Benoît Sagot and Rachel Bawden. Paper is available [here](https://aclanthology.org/2023.acl-long.295/).

Half of the English source sentences are from [<ins>DiscEvalMT</ins>](https://github.com/rbawden/discourse-mt-test-sets).

## Download images
Images can be downloaded [<ins>here</ins>](https://drive.google.com/drive/folders/1FrvKN1PyR7zeGLllCLp50TbM0OS8LCSc?usp=sharing). To extract the content, please run the following command line:

`tar -xvzf images.tar.gz`

Images of the validation set (only available in French) can be downloaded [<ins>here</ins>](https://drive.google.com/drive/folders/1FrvKN1PyR7zeGLllCLp50TbM0OS8LCSc?usp=sharing). To extract the content, please run the following command 
line:

`tar -xvzf images_dev.tar.gz`

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
@inproceedings{futeral-etal-2023-tackling,
    title = "Tackling Ambiguity with Images: Improved Multimodal Machine Translation and Contrastive Evaluation",
    author = "Futeral, Matthieu  and
      Schmid, Cordelia  and
      Laptev, Ivan  and
      Sagot, Beno{\^\i}t  and
      Bawden, Rachel",
    editor = "Rogers, Anna  and
      Boyd-Graber, Jordan  and
      Okazaki, Naoaki",
    booktitle = "Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)",
    month = jul,
    year = "2023",
    address = "Toronto, Canada",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2023.acl-long.295",
    doi = "10.18653/v1/2023.acl-long.295",
    pages = "5394--5413"
}
```

If you use en-ar, en-zh, en-ru or en-fr_dev, please cite additionally:
```
@misc{futeral2024zeroshotmultimodalmachinetranslation,
      title={Towards Zero-Shot Multimodal Machine Translation}, 
      author={Matthieu Futeral and Cordelia Schmid and Beno{\^\i}t Sagot and Rachel Bawden},
      year={2024},
      eprint={2407.13579},
      archivePrefix={arXiv},
      primaryClass={cs.CL},
      url={https://arxiv.org/abs/2407.13579}, 
}
```

## License
The evaluation datasets are distributed under a CC BY-NC-SA 4.0 licence.




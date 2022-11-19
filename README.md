# Letter Statistics

Once I was curious to see what words can have hidden. If there is any patterns or just to have some statistics to train my skills.

Here is my ongoing project which is all about words and letters.

I am currently working with few txt files in both polish and english to have some differences.

# Experiments

After few experiments with collecting letter occurances, most recursive letters, vowels, consonants etc. I have come to a conclusion that there is a pattern behind it all. Just take a look at this charts comparing various files. The overall shapes are similar and percentage amount of each letter in all the texts is mind-blowingly close.

![Chart comparing Lalka and Hamlet-PL](https://i.imgur.com/CQdVbXS.png)
![Chart comparing Pan Tadeusz and Lalka](https://i.imgur.com/Xgk3GaB.png)
![Chart comparing Hamlet-EN and 'Romeo and Juliet'](https://i.imgur.com/jqZF4mz.png)

# Statistics

|| English Words | Polish Words | Hamlet-EN | Hamlet-PL |
|:--------|:--------:|:--------:|:--------:|:--------:|
| Total Letters| 3494707 | 36090123 | 122288 | 144927 |
| Vowels| 1438930 (~41.17%) | 15835894 (~43.88%) | 51284 (~41.94%) | 59901 (~41.33%) |
| Consonants| 2055777 (~58.83%) | 20254229 (~56.12%) | 71004 (~58.06%) | 85026 (~58.67%) |
| Most recursive letter | "e" with 376456 occurances (~10.77%) | "a" with 3388277 occurances (~9.39%) | "e" with 16335 occurances (~13.36%) | "a" with 12103 occurances (~8.35%) |

# Sources of txt files:
- Lalka Bolesława Prusa
    - Volume 1 [Wolne Lektury](https://wolnelektury.pl/katalog/lektura/lalka-tom-pierwszy/)
    - Volume 2 [Wolne Lektury](https://wolnelektury.pl/katalog/lektura/lalka-tom-drugi/)
- Pan Tadeusz Adama Mickiewicza [Wolne Lektury](https://wolnelektury.pl/katalog/lektura/pan-tadeusz/)
- Hamlet Williama Shakespeare (Polish Version) [Wolne Lektury](https://wolnelektury.pl/katalog/lektura/hamlet/)
- Hamlet Williams Shakespeare (English Version) [Github/cgovella Project Gutenberg EBook](https://github.com/cgovella/learning/blob/master/edx-python/case%20studies/gutenverg/Books/English/shakespeare/Hamlet.txt)
- Romeo and Juliet [Github/cgovella Project Gutenberg EBook](https://github.com/cgovella/learning/blob/master/edx-python/case%20studies/gutenverg/Books/English/shakespeare/Romeo%20and%20Juliet.txt)
- List of accepted polish words for word games based on rules by Słownij Języka Polskiego [sjp.pl](https://sjp.pl/sl/growy/)
- List of english words [Github/dwyl](https://github.com/dwyl/english-words/)
- Best rated polish essay [Wiedza z Wami](https://wiedzazwami.com.pl/przyklad-rozprawki-maturalnej-na-37-punktow/)
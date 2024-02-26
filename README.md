# English Learning System

##  *I*. Essentials
- Mission:
  * This project is not something random. I have developed it in order to help others in learning English.When I first started (02/11/23) my idea was to create something that people will be happy to use, program that will automate some boring process in our lifestyle.

- Where the idea came from?
   * An old Chinese saying goes - "*If you want to help others - help yourself first*". From then on I have tought about
my own learning process and there was nothing more boring in it than writing every new word from my English classes x30 times.
- The idea itself:
  * After all, I came up with the idea of creating program that enables you to learn English words in very innovative way.
  * Check how to use it [here](https://github.com/sldimitrov/english_learning_system/blob/main/README.md#how-to-use-the-program).
- The innovative way:
   * Writing every new word in a sentence which exposes its definition is our method and it is much better!
   * Read more [information](https://github.com/sldimitrov/english_learning_system/blob/main/README.md#why-writing-whole-sentences-with-the-new-words-instead-of-just-them) about it here.

## *II*. How to use the program?
### Set-up
* The first thing you need to do in order to use the program is to fork the repository 
![Screenshot 2024-02-26 233401](https://github.com/sldimitrov/english_learning_system/assets/135168991/007c2b18-a556-45bf-bcb4-fcd4fa260b09)
---
* Once having a local copy of the project you should gather some words, which meaning is unknown for you. From then on you should open the file - 'list_of_words.txt' ![dir_photo](https://github.com/sldimitrov/english_learning_system/assets/135168991/fb83d993-bf4a-40ae-8f9e-78838993d5f4)
Current file [location](https://github.com/sldimitrov/english_learning_system/blob/main/learning_system_project/list_of_words.txt) of the file.
---
* After you have located this text file. Open [Cambridge Dictionary](https://dictionary.cambridge.org/#google_vignette) and search for the definition of every word you want to.
* You should input the data into the file as in the following example:
![Screenshot 2024-02-26 222338](https://github.com/sldimitrov/english_learning_system/assets/135168991/8631ac94-6c8f-4431-9a5b-20d58062fd62)

- ERROR WARNINGS:
  * PATTERN : 'word' - 'definition'
  * DO NOT FORGET TO INPUT SPACES OR TO SEPARATE THE WORD AND THE DEFINITION WITH '-' !
  * THE PROGRAM DOES NOT WORK WITH BULGARIAN DEFINITIONS !
---
**Install Project Requirements**
* You need to open the Python Terminal and write the following command:
```python
pip install -r requirements.txt
 ```
* If that command does not work you can try again with:
```python
pip install pyttsx3 
 ```

### Running the program
- After the set-up above you are ready to run the program.
  * Open main.py file in your forked repository and run it. If everything is working fine you should be greeted with user-friendly messages. After that the following question will pop up and if you are using the program for a first time you ought to make an account
![entry_photo](https://github.com/sldimitrov/english_learning_system/assets/135168991/a4b5990e-b204-47f5-a412-29cab5082cdb)
---
   * Once you register succesfully you will be asked to login.
![Screenshot 2024-02-26 234857](https://github.com/sldimitrov/english_learning_system/assets/135168991/ab9d7f69-4aa2-454e-bc3a-65098780f406)
---
   * After you pass login sucessfully you will acces the English Learning System
![menu_photo](https://github.com/sldimitrov/english_learning_system/assets/135168991/fb8b8ce8-c123-47f1-a564-69e6998fd8b0)
   * From then on if you have any questions or you do not understand something choose 6 for info or connect with me. My accounts you can fine [here]()

## Software Use - Live Demo



## *III.* Why writing new words into sentences rather than just the words?
<img align="right" width=240px height=200px alt="side_sticker" src="https://dana.org/app/uploads/2023/09/qa-what-happens-synapse.jpeg"/>
It is proven by scientists that if you connect something that is unusual and new for you
with something familiar it will let to a neural connection in your brain. This is the scientific explanation
that stays behind the main method we use in this Learning System. Put any new word
in a sentence that exposes the definition of the unknown word. After the connection happens
it become much more easier for you to memorize its meaning. Next time you hear or read this word your brain will give you the
whole sentence and with that the definition will appear in your mind.


## *IV.* Knowledge stack
 ### The first part of the project - *User Authentication*. 
In order to develop it I had used `try-except blocks` to handle errors with my `Custom Exceptions`, and `functions` to validate the User input.
`SQLlite database` is the place where the program saves the User credentials after `hashing the password` with the support of the
`hashlib` library. To `append` and `read` `data` `from` the `database` I have used `SQL` commands.
 ### The second part - *English Learning System*.
 
  `Functions` helped me to *separate* the *big problem* into *small ones* which I had
solved easily. Nevertheless, `file-handling` take big role in the project. We can append, read and delete information from files.
Data-types that are commonly used are `lists` and `dictionaries` with `comprehensions` on some places to make the *code* more *readable*.
This part of the project is dealing with some `super methods` like ''__name__''.
 #### `To sum up`, in this project `I have used every one of the things I have learned since I started my career as Software Developer`. Not only that, but it helped me to learn much more. Now it is your time to use what I am offering you and `learn on your own` - [here](https://github.com/sldimitrov/english_learning_system/blob/main/learning_system_project/__main__.py)

## *V.* Adjustments

Fork the repository and free to show imagination - change the script.
* express yourself
* add new functionality
* add try-except statements
* add more user-friendly messages
* add whatever you want and said feedback ;)
* JUST do NOT forget to *fork* and *star* the repo!
```python 
n_times = float('inf')
print('Thank you for the attention!' * n_times)
```

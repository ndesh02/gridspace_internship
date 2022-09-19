# Gridspace Internship Application by Neha Deshmukh

## Contact and Availabilty

1. My name is Neha Deshmukh, my email address is n2deshmu@uwaterloo.ca and my phone number is 289-926-7906.
2. I'm a Computer Engineering student at the University of Waterloo and my anticipated graduation date is April 2025.
3. My preferred start date is January 2023 and the end date would be the end of April.
4. I would love to work in Los Angeles!

## Technical Background
1. I have taken a course on C++, a course on Systems Programming and Concurrency that used C, a course on Data Structures and Algorithms and a course on Digital Computers that taught RISC-V. I have learned 

2. My largest software project was a customer facing mobile app that was used for logging covid and drug tests. There were multiple facets to the project: cases where customers would log the results for their own usage, cases where employees would log their results so that they would be automatically sent to their employer, and cases where the results needed to be automatically uploaded into an ATS (Application Tracking System). I also took the initiative to create an external site to interface with some of the customer data (useful for large corportations to track and download drug test results en masse) and created a secure website from scratch in 2 weeks. This involved the use of multiple technologies: Xamarin (used to develop iOS and Android applications), Razor pages (for the external site) and APIs to send requests to the ATS and the development of our own API endpoints.

3. I'd say that I am fairly comfortable with Systems Programming. I am taking a course on it right now, so by the time Winter 2023 comes around I should be fairly proficient. I also know C quite well, and am fairly comfortable with all the lower level aspects such as memory management. I have taken a course on Digital Computers that taught us assembly (RISC-V) so I am comfortable with low level programming.

4. I have a wide variety of things I like to do in my free time. Recently, I have been reading quite a bit of historical fiction as well as non-fiction. I also enjoy listening to podcasts about modern history. Another hobby of mine is painting. I taught myself how to paint landscapes a year ago and I find it to be a good creative outlet, especially when I am stressed. I have also learnt how to crochet recently and enjoy making a lot of stuffed toys - they make great birthday gifts! One last hobby of mine is playing Stardew Valley - I got into it a few years ago and haven't been able to stop playing since. These are a few of the things I like to do in my free time and some others haven't made it onto the list.

5. One personal project that I made for fun was a game called Fox vs Bats. I used the open source game engine, Godot, to create this project. The reason I decided to start creating the game was out of a desire to learn how to use a game engine. I had downloaded Unity, but I liked the idea of the open source engine more and all of the fundamental concepts were the same I learnt about game design and the tradeoffs of frames per second versus computing power consumed. Once I was done, my game had 10 playable levels and I distributed it amongst friends and family. 

6. My background in math is solid. I have taken 3 calculus courses in university, and have learned Fourier series. This has helped me model signals and systems. I have also taken discrete math courses and am currently taking probability and statistics. In addition, I have also taken the Machine Learning Course on Coursera by Stanford University and this taught me the fundamentals and math behind artifical intelligence.

7. I think that good code isn't littered with comments or overly clever - it should be self explanatory. Comments should be added where explanations are needed, but for the most part the variable names and the structure should be apparent. I also think it's best to take the most straightforward solution (without compromising on efficiency). This will help maximize readability as well - another feature of good code. It's also important to organize the code in small chunks such as classes, methods and functions that do one thing to maximize reusuability. Finally, good code must actually work. This means that it has been tested and rewritten as needed.

Contrasting C and Python: 
- In python, variables are untyped. So, you don't need to declare them. In C, you must declare the variable before using it. You can also decide whether to allocate it on the stack or the heap. When allocating on the heap, it's best practice to initialize all your variables (for example an entire array) to some default value in order to avoid future hard to debug issues. 
- In C, it's best to avoid passing by value and better to use pointers (or pass by reference). In python, pointers aren't available so you must pass by value.
- In C, it's best to explicitly compare values (don't rely on truthiness). This also helps improve the readability of the code. Since python variables are untyped, this is less important in python.
- In C, always use { } to open and close statements. This helps improve readability and avoid bugs. Since python relies on indentation, this is not the case in that language.

8. I've heard great things about Gridspace and would love the opportunity to work for you! I am most excited to develop my machine learning and AI skills since I know that you are creating cutting edge AI technology. I have also heard that this is a fast paced work environment, and I want to develop my problem solving skills. 

9. (Mention full stack)

## Technical Discussion Questions

Technical Discussion Questions

1. Compare a Python list to a NumPy ndarray.
A ndarray is a grid of values (all must have the same type) and is indexed by tuples (comprised of non-negative integers). They have a property called rank which is the number of dimensions, and their shape is a tuple (ints) that gives the size of the array for each dimension. 
Python lists are similar, but are resizable and can be comprised of multiple types. Also, multi-dimensional python arrays are created by storing a 1-dimensional list inside another. The reason we use NumPy ndarrays is because they consume less and have faster performance. NumPy also has several linear algebra functions built in which makes matrix operations simpler. 

2. According to the Universal Approximation theorem, neural networks can approximate any continuous function (with at least one hidden layer and some non-linear activation functions). However, this means that they cannot always approximate discontinuous functions. For example, f(x) = 1/(x-5). This function has a discontinuity at 5, so a neural network will not be able to approximate it. This is because the loss function of neural networks uses differentiation. However, it is not possible to differentiate at a discontinuity. So, neural networks can't approximate discontinuous functions. 

3. I would use a int[][] array but with a twist. Assuming ints in the language are 32-bit ints, I would store 6 5-bit ints in each. This would make it slightly more difficult to lookup values, but I would be wasting a lot less space.

An adjacency list is better than an adjacency matrix for a sparse graph. Adjacency matrices use O(n^2) memory, have O(1) lookup of specific edges, slow to iterate over all edges, O(1) to add a new edge. Adjacency lists use O(V + E) memory, have O(k) lookup of specific edges, fast to iterate over all edges and are faster to add or remove a node. Since the matrix is sparse, O(n^2) memory would be worse than O(V+E) memory which is one of the main reasons to choose the adjacency list over the matrix.

4. It is human nature to ask successful people how they became successful. However, while this may seem intuitive, it is the wrong approach. If you only ask successful people for advice, you have an extremely biased sample. Instead of looking at the entire dataset (which should include unsuccessful people), we look at those who have succeeded and draw conclusions based on only their characteristics. So, the statistical reason to be wary of accepting life advice from successful people is a biased dataset. It would be better to take a random sample of people so that we can determine the common characteristics of those who didn't succeed, or see that part of the reason some people are successful is simply random chance.

5. With public key encryption, there exists a public key and a private key. The public key is visible to all and is used to encrypt data. The private key is the only way to decrypt data encrypted with the public key. Some common public key encryptions are RSA and ED25519.

A variant that requires 2 out of 3 keys to decrypt would be something with 2 private keys and 1 public key. The public key would be used to encrypt the data and both private keys would be needed to decrypt it. This would be more secure than having just one private key.

6. The algorithm would have to be similar to a O(n!) algorithm, but with the parity twist. Let's first look at O(n!). I can think of a very bad algorithm I could use to calculate n!, with a time complexity of O(n!). It is below:

void badCalculator(int n){

for(int i = 0; i<n; i++){
 badCalculator(n-1);
}

}

Here you can see that the loop executes n times, and the function called inside the loop executes (n-1)! times.

Now, we must find some way to adapt this algorithm to O(n!!) time complexity. We want the loop to execute n times, and the inner function 
to execute (n-2)!! times.

void doubleFactorialTime(int n){

for(int j = 0; j<n; j++){
 doubleFactorialTime(n-2);
}
}

The above function will have a time complexity of n!!.

7. Humans can hear tones at a maximum of 20 kHz. However, research has shown that we can detect the absence of some sounds or components until 32 kHz. So, most sampling for humans happens at 44.1 kHz or 48 kHz. However, lots of people listen to music at lower frequencies. Human speech is not as rich in sound or frequency as music. I know that telephones use about 8 kHz as a sampling rate. So, anywhere between 8 kHz and 48 kHz would be reasonable, with 48 kHz having much richer sound quality. 

Since porpoises have a much higher auditory range, we can invoke the same principles as we did for humans. 150 kHz would be enough but would be less rich in quality. So, we can use a sampling rate of 240 kHz (150 * 32 / 20) for the porpoises so the sound is richer.

8. 
It depends of what the purpose of the conlang is. However, some things I would definitely include are:
- Consonants and vowels. I would have fewer connecting vowels since those languages sound "harder" or more guttaral and I like the sound of that.
- Inflection: I want some words to change how they're inflected based on the mood or context.
- Grammar: my language will have a grammar structure similar to that of French. I want there to be very specific rules, especially when 
conjugating verbs.
- Writing system: I want my writing system to convey the inflection on words based on mood and context. This way, inflection can be written 
down.

9. With such complex words, the language processing model must be extensively developed. Since so many possible combinations of words arise, it's less feasible to create an entire dictionary of words. This means that the model must be able to "decode" each word and understand the components that go into it. An approach would be to search and analyze documents written in this language and form a collection of texts with accompanying translations for the algorithm to learn from. This way we can teach the processing model how to decode Nahuatl. This languages adds prefixes and suffixes to the words themselves, so it would be good to have one algorithm to remove those and then another to translate the base from and show a translation. 

<h1 align="center">Battleships Game</h1>

![Responsive Test](assets/images/ceart-responsive.png)

---

[Live Website](https://conorwalsh1.github.io/ceart-kids-quiz/)

[Github Repository](https://github.com/conorwalsh1/ceart-kids-quiz)

---

# About

Welcome to Ceart (Ceart is the Irish translation of the word 'Correct'), an online multiple choice quiz for kids that tests their knowledge of the Irish language. I set out to create a quiz that is both easy to navigate and clear in it's intent.

As most people who learn the Irish language do so when they are a child, I prioritised a landing page which welcomes the site visitor using clear and easy to read English in a small paragraph with a large button that reads "Start Quiz". The welcome message informs the user that they have ten questions to answer and it also encourages the user to try again if they answer incorrectly. Once the start quiz button is clicked, the welcome message will disappear and the quiz will begin. 

The site user will be asked a question at the top of the screen under which they will have four buttons with each button containing a possible answer. If the correct button is clicked, the button selected will turn green and the "Correct" score tracker will increment by 1, however if they choose incorrectly, the button selected will turn red and the "Incorrect" score tracker will increment by 1 for each wrong answer selected

The quiz is comprised of a total of ten questions with each question being labelled with a number to show the user where they stand in terms of total questions remaining. Once the tenth question has been answered, the quiz area will be cleared of questions and answer buttons and a closing message will inform the user that they have reached the end of the quiz. The closing message will congratulate them on completing the quiz and will ask them how they fared. The user will be informed that if they would like to restart they quiz, they need only click on the little green map of Ireland thaat remains at the top of the page in the logo. Their final scores will be stored at the top of the page, showing how many answers they got correct and how many were answered incorrectly.

This website was built using a Macbook Pro 13". 
    
## Features

-   Responsive on all device sizes. On wider screens the questions and buttons stretch out to make use of space but on smaller screens the media queries ensure the quiz is adaptive and clean

-   Correct and Incorrect scores increment as according to users selecting the correct answer ot incorrect answer.

-   When hovered over, the 'Start Quiz' and 'Next' buttons transition to orange to encourage user to click.

-   Accessibility has been added in terms of both aria labels and aria labelled by to ensure the site is usable for anyone using screen readers.

-   The 'Next' button toggles through questions until there are no questions left to display, at which point the closing message appears on screen.

-   Ten seperate questions with different answers. If the correct answer is selected, button turns green. If incorrect button selected, button turns red.

-   Welcome message upon loading the quiz informing player how the quiz works.

-   Closing message upon completing the quiz congratulating the player, telling them how they scored and directing them to click the green map of Ireland in the logo if they would like to restart. There are four different messages that a player could receive, depending on their final score.

-   The green map of Ireland in the logo contains a link so that when it is clicked, it will refresh the page, thereby restarting the quiz.

## Features To Add In Future

-   Different topics of quiz questions, such as sport, history, geography.

-   Different variations of difficulty to keep site users coming back (perhaps images to accompany certain questions on an easier mode.).

-   A highscore page that stores users names and scores.

-   A timer so that players can test themselves to try and beat their previous times.

## Technologies Used

### Languages Used

-   [HTML5](https://en.wikipedia.org/wiki/HTML5)
-   [CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)
-   [Javascript](https://en.wikipedia.org/wiki/JavaScript)

### Frameworks, Libraries & Programs Used

1. [Google Fonts:](https://fonts.google.com/)
    - Google fonts were used to import the 'Coming Soon' font into the style.css file which is used throughout the body of the project.
2. [Balsamiq:](https://fontawesome.com/)
    - Balsamiq was used to draft up the wireframes for the project which helped me visualise what I wanted to achieve.
3. [Git](https://git-scm.com/)
    - Git was used for version control by utilizing the Gitpod terminal to commit to Git and Push to GitHub.
4. [GitHub:](https://github.com/)
    - GitHub is used to store the projects code after being pushed from Git.
5. [Logo Makr:](https://logomakr.com/)
    - Logo Makr was used to create the Ceart logo which included the green map of Ireland.
6. [Responsive Design:](http://ami.responsivedesign.is/)
    - Responsive design was used to create responsive design imitator image.
7. [Chrome DevTools:](https://developer.chrome.com/docs/devtools/)
    - Used to test code throughout the project by using the console and by trying out different variations of code before settling on any type and implementing it into the project.



## Testing

The W3C Markup Validator, W3C CSS Validator and JSHint were used to validate every page of the project to ensure there were no syntax errors in the project.
    <h2 align="center">HTML Validator Results</h2>
-   [W3C Markup Validator](https://validator.w3.org/#validate_by_input) 
    ![HTML Validator Results](assets/images/ceart-html-test.png)
    <h2 align="center">CSS Validator Results</h2>
-   [W3C CSS Validator](https://jigsaw.w3.org/css-validator/#validate_by_input)
    ![CSS Validator Results](assets/images/ceart-css-test.png)
    <h2 align="center">JavaScript Validator Results</h2>    
-   [JSHint](https://https://jshint.com/)
    ![JavaScript Validator Results](assets/images/ceart-js-test.png)

### Testing User Stories from User Experience (UX) Section

-   #### First Time Visitor Goals

    1. As a First Time Visitor, I want to easily understand the main purpose of the site..

        1. Upon entering the site, users are automatically greeted with a clean unobstructed interface which contains the name of the site and a welcome message explaining the sites purpose.
        2. The rules of the quiz are explained clearly.
        3. The user is shown a large "Start Quiz" button which calls the function to start the quiz

    2. As a First Time Visitor, I want to be able to easily be able to navigate through the quiz without any confusion.

        1. The site has been designed to be fluid and never to entrap the user. Once the quiz starts, the user will have an option of four different buttons to select, all of which can be pressed for each question. The 'Next' button guides the user through the quiz until they have answered all questions
        2. The user will be alerted with a closing message once all questions have been answered.

    3. As a First Time Visitor, I want to have an experience that is meaningful and informative.

        1. The quiz has been set up in a way that the questions are not difficult but not easy either. As a first time visitor, I want to feel stimulated enough that I would like to return again.
        2. The encouraging language in the opening and closing messages is scripted in a way that aims to provoke a positive emotional reaction in the site user.

-   #### Returning Visitor Goals

    1. As a Returning Visitor, I want to challenge the score I received on the previous occasion.

        1. The tally for correct and incorrect score will always appear at the top of the screen. It gives the visitor a way of tracking their score so they have something to compare it against when they return.
        2. The score shows both correct and incorrect so the visitor has two ways of challenging themselves.

    2. As a Returning Visitor, I want to be able to complete the quiz without any distractions

        1. The quiz is set up in a way that the visitors eyes are only drawn to the quiz area which is contained in a black box with brown border.
        2. There is nothing included on the site that isn't necessary which promotes a concentrated learning environment.

-   #### Frequent User Goals

    1. As a Frequent User, I want to improve my Irish language skills.

        1. The site has a familiar layout which is truly unique. This allows the site visitor to focus purely on learning Irish through the quiz.

    2. As a Frequent User, I want to check to see if there are any changes to either the questions in terms of topics or difficulties.

        1. If any changes were to be implemented either through topics or question difficulties, the user would be notified in the welcome message so the landing page acts as a notice board for any changes on site.

### Further Testing

-   The Website was tested on Google Chrome, Internet Explorer, and Safari browsers.
-   The website was viewed on a variety of devices such as Desktop, Laptop, Samsung 4K Television, iPad, iPhone 7 (Regular and Plus), & iPhoneX.
-   Friends and family members were asked to review the site and documentation to point out any bugs and/or user experience issues.

### Known Bugs

-   There are no known bugs at this time.

## Deployment

### GitHub Pages

The project was deployed to GitHub Pages using the following steps...

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/)
2. At the top of the Repository (not top of page), locate the "Settings" Button on the menu.
    - Alternatively Click [Here](https://raw.githubusercontent.com/) for a GIF demonstrating the process starting from Step 2.
3. Scroll down the Settings page until you locate the "GitHub Pages" Section.
4. Under "Source", click the dropdown called "None" and select "Master Branch".
5. The page will automatically refresh.
6. Scroll back down through the page to locate the now published site [link](https://github.com) in the "GitHub Pages" section.

### Forking the GitHub Repository

By forking the GitHub Repository we make a copy of the original repository on our GitHub account to view and/or make changes without affecting the original repository by using the following steps...

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/)
2. At the top of the Repository (not top of page) just above the "Settings" Button on the menu, locate the "Fork" Button.
3. You should now have a copy of the original repository in your GitHub account.

### Making a Local Clone

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/)
2. Under the repository name, click "Clone or download".
3. To clone the repository using HTTPS, under "Clone with HTTPS", copy the link.
4. Open Git Bash
5. Change the current working directory to the location where you want the cloned directory to be made.
6. Type `git clone`, and then paste the URL you copied in Step 3.

```
$ git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY
```

7. Press Enter. Your local clone will be created.

```
$ git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY
> Cloning into `CI-Clone`...
> remote: Counting objects: 10, done.
> remote: Compressing objects: 100% (8/8), done.
> remove: Total 10 (delta 1), reused 10 (delta 1)
> Unpacking objects: 100% (10/10), done.
```

Click [Here](https://help.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository#cloning-a-repository-to-github-desktop) to retrieve pictures for some of the buttons and more detailed explanations of the above process.

## Credits

### Code

-   [Digital Ocean](https://www.digitalocean.com/community/tutorials/how-to-add-a-favicon-to-your-website-with-html) : I copied the template code on this site so that my favicon would work correctly.

-   [Stack Overflow](https://stackoverflow.com/questions/2573979/force-page-reload-with-html-anchors-html-js) : I wanted to force a page reload once the logo was clicked and I acheived this using information here.

-   [Stack Overflow](https://stackoverflow.com/questions/12194435/cannot-set-property-display-of-undefined) : I came across a bug stating "Cannot set display of undefined" in Dev tools. I followed an approach here to eradicate the issue.

-   [Stack Overflow](https://stackoverflow.com/questions/22549032/illegal-use-of-break-statement-javascript) : I was trying to use the "break" statement which I thought would end the loop generating quiz questions but it said "illegal use of break". I then researched online and found that the "return" statement was a better fit as it would break the execution flow of the function and that break was used more for 'for' or 'while' loops.

-   [Stack Overflow](https://stackoverflow.com/questions/3304014/how-to-interpolate-variables-in-strings-in-javascript-without-concatenation) : I used this resource to figure out how to interpolate the final score into the string of if statements that appear in the generateNextQuestion function.

-   [YouTube](https://www.youtube.com/watch?v=MLfAW55_4cY) : I followed the first part of this tutorial to acheive the desired effect of a hover olay for my buttons.

-   [W3Schools](https://www.w3schools.com/cssref/pr_border-style.asp) : I used this site as I was looking to remove a border style that was appearing dotted when I just wanted a simple plain border.

-   [W3Schools](https://www.w3schools.com/jsref/prop_pushbutton_disabled.asp) : I used this site as I was looking for a way to stop the correct answer button from being clicked more than once which was incrementing the score infinitely based on how many time the user clicked the same correct answer.

- My functions incrementScore and incrementIncorrectScore were taken from the 'Love Maths' Code Institute walkthrough, I replaced the Id's with my own.

### Problems Overcame

-   I found Javascript quite tough initially. When I started the project I relied heavily on a Youtube tutorial (https://www.youtube.com/watch?v=riDzcEQbX6k&t=1374s) which created a multiple choice quiz exactly how I wanted it to look but I could not explain how any of the Javascript functions worked. I spoke with my tutor Maria who advised that the Javascript code must be custom written. I deleted the project and went back to the start of the Javascript course and I went through the modules again, this time bookmarking parts I realised I could use in my own project and thereby gaining a better understanding of JS. By the time I came through the JS module, I felt much more prepared and I started writing my own custom JS. You will be able to see in the commits where I deleted the JS code and started afresh.

-   One function I had a lot of trouble with was the correctAnswer function. I spent a number of days working different angles but I was delighted to get it working in the end. What I figured out was that I was missing was the event parameter within the function itself.

-   I kept receiving an error once the quiz came to a close, saying :

    TypeError: Cannot read property 'question' of undefined
       at generateQuestion (script.js:29)
       at HTMLButtonElement.generateNextQuestion (script.js:57)

    I kept looking through the course material and found the "break" statement which I thought would end the loop. I tried but it still wouldn't work. I then researched online and found that the "return" statement was a better fit as it would break the execution flow of the function and that break was used more for 'for' or 'while' loops.

-   When the site was being tested, a user brought to my attention that the answer buttons could be clicked infinitely, which was an issue as the correct score could be incremented above ten which was how many questions and possible correct answers were present. I went about creating a function to resolve this issue by creating one function that disabled the buttons once the correct answer was clicked and another function that reactivated the buttons once the 'Next' button was clicked. I was happy to just block the user from clicking the correct answer more than once as the quiz is built for children, I want them to feel encouraged to try again to find out what the correct answer is, even if by process of elimination.



### Content

-   Code Institute README.md template.

-   All other content was written by Conor Walsh.


### Acknowledgements

-   I would like to thank my mentor Maria Hynes for guiding me along the right path throughout our mentoring sessions. There were times I struggled with getting the way I wanted the code to look out of my head and onto the screen, but she gave me great motivation to persevere and I am very grateful for her assistance. I would also like to thank the tutors that helped me along the way.

![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

Welcome conorwalsh1,

This is the Code Institute student template for deploying your third portfolio project, the Python command-line project. The last update to this file was: **August 17, 2021**

## Reminders

* Your code must be placed in the `run.py` file
* Your dependencies must be placed in the `requirements.txt` file
* Do not edit any of the other files or your code may not deploy properly

## Creating the Heroku app

When you create the app, you will need to add two buildpacks from the _Settings_ tab. The ordering is as follows:

1. `heroku/python`
2. `heroku/nodejs`

You must then create a _Config Var_ called `PORT`. Set this to `8000`

If you have credentials, such as in the Love Sandwiches project, you must create another _Config Var_ called `CREDS` and paste the JSON into the value field.

Connect your GitHub repository and deploy as normal.

## Constraints

The deployment terminal is set to 80 columns by 24 rows. That means that each line of text needs to be 80 characters or less otherwise it will be wrapped onto a second line.

-----
Happy coding!

https://www.youtube.com/watch?v=waTN4mBWMtA - Board
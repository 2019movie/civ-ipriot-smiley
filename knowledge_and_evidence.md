<style>

body {
    counter-reset: h2counter;
}

/* H1 - No numbering */
h1 {
    /* No counter reset or increment */
}

/* H2 - Level 1 numbering */
h2 {
    counter-reset: h3counter;
}

h2::before {
    counter-increment: h2counter;
    content: counter(h2counter) ". ";
}

/* H3 - Level 2 numbering */
h3 {
    counter-reset: h4counter;
}

h3::before {
    counter-increment: h3counter;
    content: counter(h2counter) "." counter(h3counter) " ";
}

/* H4 - Level 3 numbering (optional) */
h4 {
    counter-reset: h5counter;
}

h4::before {
    counter-increment: h4counter;
    content: counter(h2counter) "." counter(h3counter) "." counter(h4counter) " ";
}

</style>

# Evidence and Knowledge

This document includes instructions and knowledge questions that must be completed to receive a *Competent* grade on this portfolio task.

## Required evidence

### Answer all questions in this document

- Each answer should be complete, well-articulated, and within the specified word count limits (if added) for each question.
- Please make sure **all** external sources are properly cited.
- You must **use your own words**. Please include your full chat transcripts if you use generative AI in any way.
- Generative AI hallucinates, is not an authoritative source

### Make all the required modifications to the code

- Please follow the instructions in this document to make the changes needed to the code.

- When requested to upload evidence, upload all screenshots to `screenshots/` and embed them in this document. For example:

```markdown
![Example Running Code](screenshots/screenshot1.png)
```

- You must upload the code into your GitHub repository.
- While you can use a branch, your code should be in main when you submit.
- Upload a zip of this repository to Blackboard when you are ready to submit.
- You will be notified of your result via Blackboard
- However, if using GitHub classrooms, you may also receive additional feedback on GitHub directly

### Optional: Use of Raspberry Pi and SenseHat

Raspberry Pi or SenseHat is **optional** for this activity. You can use the included `sense_hat.py` file to simulate the SenseHat on your computer.

If you use a Pi, please **delete** the `sense_hat.py` file.

### Accessible version of the code

This project relies on visual patterns that appear on an LED matrix. If you have any accessibility requirements, you can use the `udl/accessible` branch to complete the project. This branch provides an accessible code version that uses text-based patterns instead of visual ones.

Please discuss this with your lecturer before using that branch.

## Specific Tasks & Questions

Address the following tasks and questions based on the code provided in this repository.

### Set up the project locally

1. Fork this repository (if not using GitHub Classrooms)
2. Clone your repository locally
3. Run the project locally by executing the `main.py` file
4. Evidence this by providing screenshots of the project directory structure and the output of the `main.py` file

![Local Execution (INSERT YOUR SCREENSHOT)](screenshots/CREATE_A_SCREENSHOT_OF_YOUR_local_setup.png)

If you are running on a Raspberry Pi, you can use the following command to run the project and then screenshot the result:

```bash
ls
python3 main.py
```

### Fundamental code comprehension

 Answer each of the following questions **as they relate to that code** supplied by in this repository (ignore `sense_hat.py`):

1. Examine the code for the `smiley.py` file and provide  an example of a variable of each of the following types and their corresponding values (`_` should be replaced with the appropriate values):

   | Type                    | name           | value                        |
   |-------------------------|----------------|------------------------------|
   | built-in primitive type | WHITE          | (255,255,255)                |
   | built-in composite type | self.pixels    | [O, Y, Y...]                 |
   | user-defined type       | Smiley (class) | contain attribute and method |

2. Fill in (`_`) the following table based on the code in `smiley.py`:

   | Object                   | Type   |
   | ------------             |--------|
   | self.pixels              | List   |
   | A member of self.pixels  | Tuple  |
   | self                     | Smiley |

3. Examine the code for `smiley.py`, `sad.py`, and `happy.py`. Give an example of each of the following control structures using an example from **each** of these files. Include the first line and the line range:

   | Control Flow | File      | First line | Line range       |
   | ------------ |-----------|------------|------------------|
   |  sequence    | smiley.py | 13         | 13 to 26         |
   |  selection   | sad.py    | 26         | 26 to 29         |
   |  iteration   | happy.py     | 30          | 30 to 31 |

4. Though everything in Python is an object, it is sometimes said to have four "primitive" types. Examining the three files `smiley.py`, `sad.py`, and `happy.py`, identify which of the following types are used in any of these files, and give an example of each (use an example from the code, if applicable, otherwise provide an example of your own):

   | Type                    | Used?         | Example                     |
   | ----------------------- |---------------|-----------------------------|
   | int                     | happy.py      | mouth contain list of int   |
   | float                   | happy.py      | delay=0.25                  |
   | str                     | None of files | f'delay by {delay} second.' |
   | bool                    | smiley.py     | dimmed = True                  |

5. Examining `smiley.py`, provide an example of a class variable and an instance variable (attribute). Explain **why** one is defined as a class variable and the other as an instance variable.

> Class variable such as Colour (e.g. WHITE = (255,255,255) ). All smiley objects share the same colors, it is efficient to store these values as class variables.
> Instance variable, example: self.pixels. Instance variables are defined within __init__ method and prefixed with self. Each instance of the Smiley class can have its own separate pixels list for different pixel arrangement.

6. Examine `happy.py`, and identify the constructor (initializer) for the `Happy` class:
   1. What is the purpose of a constructor (in general) and this one (in particular)?

   > Constructor in python are __init__ method. It runs when the object creates and set the state, such as allocate memory for instance variable.
   > For happy.py, the constructor has few purposes: 1) call the constructor of parent classes (Smiley.__init__() and Blinkable.__init__()) 2) calls draw_mouth() method 3) calls draw_eyes() method.

   2. What statement(s) does it execute (consider the `super` call), and what is the result?

   > The following statements execute:
> Smiley.__init__()
>          
> self.sense_hat = SenseHat()

        Y = self.YELLOW
        O = self.BLANK
        self.pixels = [
            O, Y, Y, Y, Y, Y, Y, O,
            Y, Y, Y, Y, Y, Y, Y, Y,
            Y, Y, Y, Y, Y, Y, Y, Y,
            Y, Y, Y, Y, Y, Y, Y, Y,
            Y, Y, Y, Y, Y, Y, Y, Y,
            Y, Y, Y, Y, Y, Y, Y, Y,
            Y, Y, Y, Y, Y, Y, Y, Y,
            O, Y, Y, Y, Y, Y, Y, O,
        ]
>         self.draw_mouth()
>         self.draw_eyes()
> It result with proper initialised attributes and behaviours from the parent classes.

### Code style

1. What code style is used in the code? Is it likely to be the same as the code style used in the SenseHat? Give to reasons as to why/why not:

> Pep8 coding style in used. Naming conventions use CamelCash, methods and variables use snake_case.
> Each class has clear responsibility, documentation (such as docstrings)
> sense_hat.py is likely the same coding style which is Pep8. The naming conventions and docstrings documentation shows that.
> 

2. List three aspects of this convention you see applied in the code.

> 1) Class naming convention using CamelCase.
> 2) Methods and variables naming convention using snake_case.
> 3) Docstrings used to describe purpose of class, parameters and behaviour.
>

3. Give two examples of organizational documentation in the code.

> 1) Method docstrings explains used to enhance code readability. For example:
> in sad.py
>    def draw_mouth(self):
        """
        Draws the mouth feature on a smiley
        """
> 2) Docstring on class level. For example:
> class Blinkable(ABC):
    """
    Specify what anything that claims to be 'blinkable' should be able to do.
    """
>

### Identifying and understanding classes

> Note: Ignore the `sense_hat.py` file when answering the questions below

1. List all the classes you identified in the project. Indicate which classes are base classes and which are subclasses. For subclasses, identify all direct base classes.
  
  Use the following table for your answers:

| Class Name | Super or Sub? | Direct parent(s) |
| Smiley | Base class |  |
| Blinkable | Base class           |     |
|   Happy |   Sub         |      Smiley, Blinkable         |
|   Sad  | Sub |  Smiley  |


2. Explain the concept of abstraction, giving an example from the project (note "implementing an ABC" is **not** in itself an example of abstraction). (Max 150 words)

> Abstraction is concept of hide the complex implementation and expose the key features to user. The smiley.py file illustrated the use of Abstraction.
> The interface to render smiley which hide the complex logic of setting colour of each pixel. The simple method "show()" make it much simple to user without understand how SenseHat works internally. 
>

3. What is the name of the process of deriving from base classes? What is its purpose in this project? (Max 150 words)

> Inheritance is process deriving from base classes.
> The purpose in reusing code, for Happy class can reuse existing methods and attributes defined in Smiley and Blinkable classes. It minimise code duplications and encourage modular design.
> Inheritance organise the codebase by clear class hierarchy, it is easier to understand relationships between different components.
>

### Compare and contrast classes

Compare and contrast the classes Happy and Sad.

1. What is the key difference between the two classes?
   > The key differences are visual represtation of draw_mouth() method and draw_eyes() methods
   >
2. What are the key similarities?
   > Both classes inherit from Smiley class
   > Both classes's __init__ constructor call super().__init__() to initialise pixels correctly.
   >
3. What difference stands out the most to you and why?
   > draw_mouth() method between Sad class and Happy class create distinct visual emotional representation.
   >
4. How does this difference affect the functionality of these classes
   > The differences directly affect the outcome of show() method between Sad and Happy class. 
   >

### Where is the Sense(Hat) in the code?

1. Which class(es) utilize the functionality of the SenseHat?
   > Smiley class directly use functionality of SenseHat.
   >
2. Which of these classes directly interact with the SenseHat functionalities?
   > Smiley class directly interteract with SenseHat. It creates an instance of SenseHat in constructor, use set_pixels method and use low_light property.
   >
3. Discuss the hiding of the SenseHAT in terms of encapsulation (100-200 Words)
   > In the context of SenseHat, Smiley class apply the encapsulation principle of object oriented programming concept that restrict direct access. The Smiley class provide a mock implementation that hide the actual SenseHat functionalities under the show() method. It can prevent user misuse the SenseHat functionality and keep user away from complex details of SenseHat.
   >

### Sad Smileys Can’t Blink (Or Can They?)

Unlike the `Happy` smiley, the current implementation of the `Sad` smiley does not possess the ability to blink. Let's first explore how blinking has been implemented in the Happy Smiley by examining the blink() method, which takes one argument that determines the duration of the blink.

**Understanding Blink Mechanism:**

1. Does the code's author believe that every `Smiley` should be able to blink? Explain.

> The absence of blinking in Sad class may indicate author believe blinking only appropriate for certain smiley types.
>

2. For those smileys that blink, does the author expect them to blink in the same way? Explain.

> The blinking action defines in Happy class shows a specific way of drawing the eyes during the blink. In the case of Sad class, it could be potentially similar but differ in how it visually represent as well as duration.
>

3. Referring to the implementation of blink in the Happy and Sad Smiley classes, give a brief explanation of what polymorphism is.

> Polymorphism allows same method used for different underlying forms of data types. In the case of Happy and Sad classes, polymorphism potentially implement the same method signature such as blink() with different behaviours.
>

4. How is inheritance used in the blink method, and why is it important for polymorphism?

> Inheritance used in the blink() method under Happy class which inherited from Blinkable class. This is important for polymorphism because it allows different subclasses like Happy and potentially Sad class implement blink() while define their own specific behaviour. It promote code reusability, flexibility which allows different similey types to share consistent interface with unique logic.
>
1. **Implement Blink in Sad Class:**

   - Create a new method called `blink` within the Sad class. Ensure you use the same method signature as in the Happy class:

   ```python
   def blink(self, delay=0.25):
       pass  # Replace 'pass' with your implementation
   ```

2. **Code Implementation:** Implement the code that allows the Sad smiley to blink. Use the implementation from the Happy Smiley as a reference. Ensure your new method functions similarly by controlling the blink duration through the `delay` argument.

3. **Testing the Implementation:**

- Test the new blink functionality on your Raspberry Pi or within the Python classes provided. You might need to adjust the `main.py` script to incorporate Sad Smiley's new blinking capability.

Include a screenshot of the sad smiley or the modified `main.py`:

![Sad Smiley Blinking](screenshots/sad_blinking.png)

- Observe and document the Sad smiley as it blinks its eyes. Describe any adjustments or issues encountered during implementation.

  > The updated Sad class implements the blink() method. The implementation use blink() method with default parameter for delay between blinks set to 0.25 seconds. It performs correctly from testing.

  ### If It Walks Like a Duck…

  Previously, you implemented the blink functionality for the Sad smiley without utilizing the class `Blinkable`. Assuming you did not use `Blinkable` (even if you actually did), consider how the Sad smiley could blink similarly to the Happy smiley without this specific class.

  1. **Class Type Analysis:** What kind of class is `Blinkable`? Inspect its superclass for clues about its classification.

     > Blinkable class is Abstract Base Class, if sad inherited from it, subclass will prevent instantiation without define a blink method.

  2. **Class Implementation:** `Blinkable` is a class intended to be implemented by other classes. What generic term describes this kind of class, which is designed for implementation by others? **Clue**: Notice the lack of any concrete implementation and the naming convention.

  > Blinkable is an abstract class because it inherits from ABC (Abstract Base class), it also contains abstract method "blink()" that subclasses must implement.

  3. **OO Principle Identification:** Regarding your answer to question (2), which Object-Oriented (OO) principle does this represent? Choose from the following and justify your answer in 1-2 sentences: Abstraction, Polymorphism, Inheritance, Encapsulation.

  > The Blinkable class represent abstraction principle, it provide definition of common subclass without specific implementation details such as generic blink() method.

  4. **Implementation Flexibility:** Explain why you could grant the Sad Smiley a blinking feature similar to the Happy Smiley's implementation, even without directly using `Blinkable`.

  > Implementing a blink() method directly in Sad class and use inherited methods from Smiley class without rely on Blinkable. This approach adheres to object oriented principles while allow flexibility and customised behaviour.

  5. **Concept and Language Specificity:** In relation to your response to question (4), what is this capability known as, and why is it feasible in Python and many other dynamically typed languages but not in most statically typed programming languages like C#? **Clue** This concept is hinted at in the title of this section.

  > Multiple inheritance is the capability for a class to inherit from multiple parent classes. It is feasibile in Python because Pythone is dynamically typed. Types are checked at runtime rather than compile time which allow multiple inheritance without strict constrains on types of classes.

  ***

  ## Refactoring

  ### Does a Smiley Have to Be Yellow?

  While our current implementation predominantly features yellow smileys, emotional expressions like sickness or anger typically utilize colors like green, red, or orange. We'll explore the feasibility of integrating these colors into our smileys.

  1. **Defined Colors and Their Location:**

     1. Which colors are defined and in which class(s)?
        > Colours are defined in Smiley Class. E.g. WHITE = (255,255,255)
     2. What type of variables hold these colors? Are the values expected to change during the program's execution? Explain your answer.
        > They are Class Variables, each colour contains 3 integer values as a tuple. They are immutable throughout the program execution as Tuple in Python are immutable data structure after creation.
     3. Add the color blue to the appropriate class using the appropriate format and values.

  2. **Usage of Color Variables:**

     1. In which classes are the color variables used?
        > Your answer here

  3. **Simple Method to Change Colors:**
  4. What is the easiest way you can think to change the smileys to green? Easiest, not necessarily the best!
     > Your answer here

  Here's a revised version of the "Flexible Colors – Step 1" section for the smiley project, incorporating your specifications for formatting and content updates:

  ### Flexible Colors – Step 1

  Changing the color of the smileys once is straightforward, but it isn't very flexible. To facilitate various colors for smileys, it is advisable not to hardcode values in any class. This approach was identified earlier as a necessary change. Let's start by removing the built-in assumptions about color in our classes.

  1. **Add a method called `complexion` to the `Smiley` class:** Implement this instance method to return `self.YELLOW`. Using the term "complexion" instead of "color" provides a more abstract terminology that focuses on the meaning rather than implementation.

  2. **Refactor subclasses to use the `complexion` method:** Modify any subclass that directly accesses the color variable to instead utilize the new `complexion` method. This ensures that color handling is centralized and can be easily modified in the future.

  3. **Determine the applicable Object-Oriented principle:** Consider whether Abstraction, Polymorphism, Inheritance, or Encapsulation best applies to the modifications made in this step.

  4. **Verify the implementation:** Ensure that the modifications function as expected. The smileys should still display in yellow, confirming that the new method correctly replaces the direct color references.

  This step is crucial for setting up a more flexible system for color management in the smiley display logic, allowing for easy adjustments and extensions in the future.

  ### Flexible Colors – Step 2

  Having removed the hardcoded color values, we now enhance the base class to support dynamic color assignments more effectively.

  1. **Modify the `__init__()` method in the `Smiley` class:** Introduce a default argument named `complexion` and assign `YELLOW` as its default value. This allows the instantiation of smileys with customizable colors.

  2. **Introduce a new instance variable:** Create a variable called `my_complexion` and assign the `complexion` parameter to it. This step ensures that each smiley instance can maintain its own color state.

  3. **Rationale for `my_complexion`:** Using a distinct instance variable like `my_complexion` avoids potential conflicts with the method parameter names and clarifies that it is an attribute specific to the object.

  4. **Bulk rename:** We want to update our grid to use the value of complexion, but we have so many `Y`'s in the grid. Use your IDE's refactoring tool to rename all instances of the **symbol** `Y` to `X`. Where `X` is the value of the `complexion` variable. Include a screenshot evidencing you have found the correct refactor tool and the changes made.

  ![Bulk Rename](screenshots/bulk_rename.png)

  5. **Update the `complexion` method:** Adjust this method to return `self.my_complexion`, ensuring that whatever color is assigned during instantiation is what the smiley displays.

  6. **Verification:** Run the updated code to confirm that Smileys still defaults to yellow unless specified otherwise.

  ### Flexible Colors – Step 3

  With the foundational changes in place, it's now possible to implement varied smiley colors for different emotional expressions.

  1. **Adjust the `Sad` class initialization:** In the `Sad` class's initializer method, change the superclass call to include the `complexion` argument with the value `self.BLUE`, as shown:

     ```python
     super().__init__(complexion=self.BLUE)
     ```

  2. **Test color functionality for the Sad smiley:** Execute the program to verify that the Sad smiley now appears blue.

  3. **Ensure the Happy smiley remains yellow:** Confirm that changes to the Sad smiley do not affect the default color of the Happy smiley, which should still display in yellow.

  4. **Design and Implement An Angry Smiley:** Create an Angry smiley class that inherits from the `Smiley` class. Set the color of the Angry smiley to red by passing `self.RED` as the `complexion` argument in the superclass call.

  ***

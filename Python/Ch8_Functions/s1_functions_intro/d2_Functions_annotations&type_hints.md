# Function Annotations

* Function annotation make it clear what kind of values your functions can accept, and what they return.
* If you annotate any part of a function definition, you should annotate all of it.
    * Either all parameters and the return value should be annotated or don't use any annotation.  

          Eg: 
          
              1. def sum_eo(number: int, term: string) -> int:
          
              2. def banner_text(text: str = " ", screen_width: int = 80): -> None

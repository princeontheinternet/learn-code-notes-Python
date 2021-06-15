# Parameters
1. Parameters are like placeholders for the real values that you'll pass to your function.
2. They are just variable but, they're given a value when you call the function.
3. They are also referred as `formal parameter`

# Arguments  
1. Arguments are the values that will be used by parameters, when we call a function.
2. Each parameter must be given a value by providing argument in the function call.
3. Providing values as argument is called passing the arguments.

# Different types of Parameters:

1. positional-or-keyword:
   
       def func(foo, bar=None):
   
2. var-positional:
   
       def func(*args, **kwargs):

3. keyword-only:

       def func(arg, *, kw_only1, kw_only2):

    

# Rules 

1. Any **positional-or-keyword** arguments that we define, must come first in the parameter list.

2. If we have **var-positional** parameter then it must come after any **positional-or-keyword** arguments.

3. Any parameter defined after a **var-positional** parameter must be **keyword-only** arguments.

4. Any **var-keyword** arguments appear last.
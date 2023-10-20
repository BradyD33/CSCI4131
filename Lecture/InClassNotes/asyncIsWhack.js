/*
HTTP requests

-Protocol version
-request type
-URL with path, parameters and nothing else
-headers
-Body if present

Postman API

Use for debugging get/post requests and stuff
Make sure you use the right client- your PC so desktop
Play around with this rn bro



Outline
-concurrency
-slow functions and why
-callback functions
-Promises -- the new paradigm
-async/await -- a better solution
-Fetch api


Concurrency is important for non-linear code, three types

1. Simultaneous processing
-multiple threads, processes, or computers running at the same time
-possible on the web
-Thoughful scoping and limited globals
------Javascript is entirely single threaded

2. Event driven
-code is non-linear because it is triggered
-Requires different ways of thinking

3. Slow functions  !!Relevant!!
-slow computations are really hard in js its built to not happen and will break shit like crazy
-Screen tearing occurs when a process is too busy to display the screen

Why we may freeze
-one event handler
-when busy handling event it cant do anything else
-Browser not for heavy computations
-Basically we will blocking
!!! REMEMBER setTimeout() !!!

How to not do this
-dont write slow loops
-making http requests do be slow


Handling these slow functions that we need
-Callback functions
-Promises
-async await

Nonblocking operations will not be able to immediately return a value as async allows the code to continue prior to finishing

Callbacks - The OG
-Callback functions enters the slow functions as a parameter
-Once the blocking function does its work then we hand the return value to the callback
-Never get a return value, it calls the function with the data that you get within the slow function itself 
!!! slowFunctionExample(x, y, callback Function) -- the values x and y will be used in slow function but then callback will call within after the blocking function
-Upsides
--Easy to use
--Not much new to learn
--Popularly used
--Easy to work with
-Two big downsides
--Non standardized
---Every function has its own rules
---Error handling is often forgotten or weird
--Bad-chaining
---Gets pretty ugly if you need multiple callbacks in a row
---Callback hell brother


Promises --New kid on the block (git it?)
-Instead of take a callback we retun a promise
-Promise object represents non-blocking functions result
-Promises have three possible "States"
--Pending(not done yet)
--Fulfilled (Completed successfully)
--Rejected
-Why is this better?
--Standardization is important
---Harder to learn, but only learn it once
---True syntax changes become possible
----Error handling is now front and center
--Treating this like data allows us to manipulate
---Promise.all(promises) returns a new promise that will now wait until all are resolved
---Promise.race(promises) returns a new promise whck has the behavior of the first solved resolve

-.then(cb) 
---Call cb with result when ready else throw an exception
-.then(cb,err)
---Call err function if object is rejection
-.catch(err)
--call err on rejection
-.finally(call)
--Once all is resolved we can call this function

then chaining
-does not actually return the same promise
-it returns a connected promise at the end of the .then chain
*/
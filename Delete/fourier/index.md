---
layout: Default
---
<html>
<title>Fourier Analysis</title>
<link href="css/styles.css" rel="stylesheet" type="text/css">
<meta name="viewport" content="width=device-width" />

# Fourier Analysis

We're going to leave the mathematics and equations out of it on this page!

## So what is this Fourier Analysis?

Put simply, the Fourier transform is a way of splitting a signal/wave/data up into a bunch of sine waves. 


Here’s an example wave:

<canvas id="combo-sine-wave" class="sketch" width=500 height=300></canvas>

This wavy pattern here can be split up into sine waves. That is, when we add up the two sine waves we get back the original wave.

<canvas id="combo-sine-wave-split" class="sketch" width=500 height=500></canvas>

The Fourier transform is a way for us to take the combined wave, and get each of the sine waves back out. In this example, you can almost do it in your head, just by looking at the original wave.

Why? Turns out a lot of things in the real world interact based on these sine waves. We usually call them the wave's frequencies.

The most obvious example is sound – when we hear a sound, we don’t hear that squiggly line, but we hear the different frequencies of the sine waves that make up the sound.

<button id="together-button" class="button">Play Full Wave</button>

<button id="split-button-1" class="button">Play High Frequency</button>

<button id="split-button-2" class="button">Play Low Frequency</button>

Being able to split them up on a computer can give us an understanding of what a person actually hears. We can understand how high or low a sound is, or figure out what note it is.

We can also use this process on waves that don't look like they're made of sine waves.

Let's take a look at this guy. It’s called a square wave.

<canvas id="square-wave" class="sketch" width=500 height=300></canvas>

It might not look like it, but it also can be split up into sine waves.

<canvas id="square-wave-split" class="sketch" width=500 height=500></canvas>

We need a lot of them this time – technically an infinite amount to perfectly represent it. As we add up more and more sine waves the pattern gets closer and closer to the square wave we started with.

<canvas id="square-wave-build-up" class="sketch" width=500 height=500></canvas>
<input id="square-wave-build-up-slider" type="range" min="0" max="1" value="0" step="any" >

<button id="square-wave-button" class="button">Play Wave</button>

*Drag the slider above to play with how many sine waves there are.*

Visually, you'll notice that actually the first few sine waves are the ones that make the biggest difference. With the slider halfway, we have the general shape of the wave, but it's all wiggly. We just need the rest of the small ones to make the wigglyness flatten out.

When you listen to the wave, you'll hear the sound get lower, because we're removing the higher frequencies.

This process works like that for any repeating line. Give it a go, try drawing your own!

<div class="multi-container">
<div class="sketch" >
    <canvas id="wave-draw" class="sketch-child" width=500 height=300></canvas>
    <p id="wave-draw-instruction" class="instruction wave-instruction">Draw here!</p>
</div>
<canvas id="wave-draw-split" class="sketch" width=500 height=500></canvas>
</div>
<input id="wave-draw-slider" type="range" min="0" max="1" value="1" step="any">
<button id="wave-draw-button" class="button">Play Wave</button>

*Move the slider to see how as we add more sine waves, it gets closer and closer to your drawing*

Again, aside from the extra wigglyness, the wave looks pretty similar with just half of the sine waves.

We can actually use the fact that the wave is pretty similar to our advantage. By using a Fourier transform, we can get the important parts of a sound, and only store those to end up with something that's pretty close to the original sound.

Normally on a computer we store a wave as a series of points.

<canvas id="wave-samples" class="sketch" width=500 height=500></canvas>

What we can do instead is represent it as a bunch of sine waves. Then we can compress the sound by ignoring the smaller frequencies. Our end result won't be the same, but it'll sound pretty similar to a person.

<canvas id="wave-frequencies" class="sketch" width=500 height=500></canvas>

This is essentially what MP3s do, except they're more clever about which frequencies they keep and which ones they throw away.

## Further 'reading'

[The webpage from which the open source code was sourced for this page](http://www.jezzamon.com/fourier/index.html)

[An Interactive Guide To The Fourier Transform](https://betterexplained.com/articles/an-interactive-guide-to-the-fourier-transform/)  
A great article that digs more into the mathematics of what happens.

[But what is the Fourier Transform? A visual introduction.](https://www.youtube.com/watch?v=spUNpyF58BY)  
A great Youtube video by 3Blue1Brown, also explaining the maths of Fourier transforms from an audio perspective.

[A Tale of Math & Art: Creating the Fourier Series Harmonic Circles Visualization](https://alex.miller.im/posts/fourier-series-spinning-circles-visualization/)  
Another article explaining how you can use epicycles to draw a path, explained from a linear algebra perspective.

[Fourier transform (Wikipedia)](https://en.wikipedia.org/wiki/Fourier_transform)  
And of course, the Wikipedia article is pretty good too.

This webpage has been adapted from an open-source repository, you can check out the code on [GitHub](https://github.com/Jezzamonn/fourier)! 

<script src="main.bundle.js"></script>
</html>
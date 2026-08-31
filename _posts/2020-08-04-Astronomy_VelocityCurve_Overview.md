---
layout: post
date:   2020-07-19
title: Determining a Velocity Curve of the Milky Way Galaxy
summary: Instructions and handouts for determining a velocity curve of the MWG
tags: ['School-Teachers', 'Students', 'Hobbyists' ]
categories: ['Astronomy']
order: 6
---

**OVERVIEW FOR THE TEACHER**

* [Unit Description and Outline]({{ site.baseurl }}/FilesUploaded/VelocityCurve_UnitOutline.pdf){: .button}

  The whole unit on two pages: what the students build toward, in what order, and
  why. Written for AP Physics — the stated goal is that students deduce the
  existence of dark matter in the Milky Way from its rotation curve.


- **Level:** HS Advanced, College

- **Objective:**  In this sequence of activities, using a horn telescope, the students will take measurements of HI spectra along the galactic plane of the Milky Way Galaxy. From their observations of galactic quadrants II & III the students will be able to deduce that the MWG is rotating. From their observations of galactic quadrant I the students will be able to determine a velocity curve of the MWG and compare it to expected curves for different galactic mass distributions.


- **Pre-Knowledge of Students:** 

    + The students have been exposed to the horn telescope and understand how to read a spectrum. 
    
    + The students understand what radio waves are, and they understand that the spin-flip in hydrogen atoms is the source of the 21-cm waves detected by the horn telescope. 

    + The students understand how to apply the Doppler shift to the spectrum peaks in order to find the relative velocity of the detected hydrogen.

    + The students understand trigonometry.

    + The students understand relative velocity.

    + The students understand Newton’s law of gravitation and can relate it to the orbital motion of satellites.

- **Key Terms:**  horn telescope, HI spectrum, galactic coordinates, Horizontal Coordinates, Stellarium, Doppler Shift, red shift, blue shift, relative velocity, circular motion, law of gravitation, orbital motion

- **Related Videos for Teacher:** [Galaxy Survey Trailer](https://youtu.be/tDCPp8RIM4g)

- **Teacher Preparation:**  
    + This activity can be done with a single horn shared with the class, or with multiple horns assigned to groups of students.
    
    + The students have used a horn telescope before. It is recommended that the following lessons have been completed:
        - Intro to the Horn Telescope
        
        - Electromagnetic Spectrum
        
        - The 21 cm Wavelength of Neutral Hydrogen
        
        - Understanding Coordinate Systems 
        
    + The teacher should be familiar with the implications of red-shifted and blue-shifted signals, and understand that the general trend of blue-shifted peaks from quadrant II and red-shifted peaks from quadrant III imply that the galaxy rotates in a CW sense in reference to standard galactic coordinates.

    + The teacher should be familiar with the tangent method and how the motion of an object along the line of sight at the tangent point — in quadrant I, motion away from the sun, hence the red-shifted peaks the students look for — is related to the galactic distances and angles involved. See the Teacher Notes under Part 2: Galactic Quadrant I Observation.

- **Sequence of activities:** - The Teacher Notes for each part provide more details.

**INTRO:** The students can run through this sequence of activities to build a rudimentary understanding of the concepts and exposure to the horn telescope
    
   a. These 4 activities could be grouped together so that smaller groups could work with the horn telescope for the one hands on activity.
    
   b. The students may have had some of these experiences if other lesson modules have been done (Basic Observational Tools) 
       
 **PART I** The students collect spectra at different galactic longitudes along the galactic plane in quadrants II and III.
     
   a. The student analyze the spectra to determine the relative velocity of the detected hydrogen.
    
   b. The students determine that the galaxy is rotating.
    
  **PART II** The students then collect spectra at different galactic longitudes along the galactic plane in quadrant I.
    
   a. Assuming circular motion of the galaxy, the speed of the tangent point along the observation line is calculated.
    
   b. A graph showing galactic speed vs distance from the galactic center is created using these results.
    
   c. This graph is compared to the graph expected in different models of mass distribution in the galaxy.


### Intro Activities for Radio Astronomy

OBJECTIVE: These activities allow this *Velocity Curve of the MWG* module be able to stand alone from start to finish. There is also some overlap with the *Basic Observational Tools* module. These basic activities will bring fuller understanding to creating the galactic velocity curve.

*Teacher Notes*  Since there is an activity with "discovering" what the horn telescope can do, it is suggested to assign all 4 activities so that students can be busy while other small groups are working with the scope(s) your have set up. (Most teachers very likely with have only one telescope.)

* [Introduction to Horn Telescope](https://WVURAIL.org/dspira-lessons/FilesUploaded/VelocityCurve_HornIntro.pdf){: .button}
   
* [Introduction to Horn Telescope Follow-up](https://WVURAIL.org/dspira-lessons/FilesUploaded/VelocityCurve_HornIntro_Followup.pdf)
   
* [The Electromagnetic Spectrum](https://WVURAIL.org/dspira-lessons/FilesUploaded/VelocityCurve_E%26MSpectrum.pdf){: .button}

   Further reading for this activity:
   [introduction to wavelengths and radiation]({{ site.baseurl }}/FilesUploaded/EMSpectrum_Introduction.pdf).
   
* [The 21 cm Wavelength of Neutral Hydrogen](https://WVURAIL.org/dspira-lessons/FilesUploaded/VelocityCurve_21cmHI.pdf){: .button}
   
* [Celestial Coordinate Systems](https://WVURAIL.org/dspira-lessons/FilesUploaded/VelocityCurve_CoordinateSystems.pdf){: .button}
   
* [Using Stellarium](https://WVURAIL.org/dspira-lessons/FilesUploaded/VelocityCurve_Stellarium.pdf){: .button}


### Part 1: Galactic Quadrants II & III Observation

OBJECTIVE: In this activity, the students collect spectra of the MWG along the galactic plane in quadrants II & III. From these they should be able to deduce that the MWG is rotating and the direction of rotation.

[Teacher Notes for Part 1](https://docs.google.com/document/d/1h9is9YnnfDidLnlvs-DnXlyzXIjT0EhrLDdnONAByHg/edit?usp=sharing){: .button}

[Student Handout for Part 1 Observation](https://docs.google.com/document/d/1jcMV-8X8Cd7rryGCsednTlc0fFRrgvAGkFyJUQAGJh8/edit?usp=sharing){: .button}

[Student Handout for Part 1 Analysis & Interpretation](https://docs.google.com/document/d/1aVUFzAvC14gPeV6RSYumYPlkclgILeoaI5LpUZNSV5U/edit?usp=sharing){: .button}



### Analysis Code (optional)

For classes that want to fit the data numerically rather than by eye, a Jupyter
notebook is provided that performs the sine fit and plots the result:

* [Galactic Plane Sine Fit notebook](https://github.com/WVURAIL/dspira-lessons/tree/master/code/velocity_curve){: .button}

Students replace the sample data in `quadII_III_velocity_vs_longitude.csv` with
their own measurements and re-run. The fitted amplitude and phase give a
quantitative handle on the rotation the students deduced qualitatively above.


### Part 2: Galactic Quadrant I Observation

OBJECTIVE: In this activity, the students collect spectra of the MWG along the galactic plane in quadrant I. The students will determine the speeds of the most red-shifted part of the spectra, and then apply the tangent method to determine the galaxy's velocity as a function of distance from the galactic center.

[Teacher Notes for Part 2](https://docs.google.com/document/d/1BSLoZjrFtA2qEoVzgvXjHdufQFRWmxtQWSAl8k1yJu8/edit?usp=sharing){: .button}

[Student Handout for Part 2 Observation](https://docs.google.com/document/d/1V4wUx8VtX358x-gIWdH9FaYi3579bz_Unl38_ShrbKE/edit?usp=sharing){: .button}

[Student Handout for Part 2 Analysis & Interpretation](https://docs.google.com/document/d/1J9w1DH5fQW24XDvesYTzsR943Px_13uTZQQS5qi6rxg/edit?usp=sharing){: .button}



### Example handouts from an earlier run

The worksheets one class actually used for Part 1 in 2018, included as an
**example of how a teacher structured the observation** — not as handouts to use
unchanged.

> ⚠️ The observing sheet is built around that class's own dates and period — two
> mornings in October, 8:00–8:45 am. Nothing in it is pre-computed for you: the
> students look their own azimuth and altitude up in Stellarium and fill the
> table in themselves. But the dates and times are that school's, so replace
> them with yours. The Part 1 and Part 2 handouts above are the current version
> of the lessons.

* [Galactic Plane Observation 1, 2018]({{ site.baseurl }}/FilesUploaded/VelocityCurve_GalacticPlaneObservation1_2018.pdf){: .button} — the observing sheet. Its spreadsheet analysis section is useful whatever dates you observe on.
* [Galactic Plane Observation 1: Conclusions, 2018]({{ site.baseurl }}/FilesUploaded/VelocityCurve_GalacticPlaneObservation1_Conclusions_2018.pdf){: .button} — a real set of class results for quadrants II and III, with the uncertainty estimate and the conclusions questions.


### All Velocity Curve handouts in one place

   * [Galactic Plane Quadrants II&III Observations: Teacher Notes](https://docs.google.com/document/d/1h9is9YnnfDidLnlvs-DnXlyzXIjT0EhrLDdnONAByHg/edit?usp=sharing)
   
   * [Galactic Plane Quadrants II&III Observations](https://docs.google.com/document/d/1jcMV-8X8Cd7rryGCsednTlc0fFRrgvAGkFyJUQAGJh8/edit)
   
   * [Galactic Plane Quadrants II&III Observations: Conclusions](https://docs.google.com/document/d/1aVUFzAvC14gPeV6RSYumYPlkclgILeoaI5LpUZNSV5U/edit)
      
   * [Galactic Plane Quadrant I Observations: Teacher Notes](https://docs.google.com/document/d/1BSLoZjrFtA2qEoVzgvXjHdufQFRWmxtQWSAl8k1yJu8/edit)
   
   * [Galactic Plane Quadrant I Observations](https://docs.google.com/document/d/1V4wUx8VtX358x-gIWdH9FaYi3579bz_Unl38_ShrbKE/edit)
   
   * [Galactic Plane Quadrant I Observations: The Tangent Method](https://docs.google.com/document/d/1wA_tVKYrAyjvuVqUY9c_stwNpO1dGDFnIL6TiHq5hx8/edit?usp=sharing)   
   
   * [Galactic Plane Quadrant I Observations: Analysis & Conclusions](https://docs.google.com/document/d/1J9w1DH5fQW24XDvesYTzsR943Px_13uTZQQS5qi6rxg/edit)  



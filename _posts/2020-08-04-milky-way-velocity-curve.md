---
permalink: /Astronomy_VelocityCurve_Overview
layout: post
date:   2020-07-19
title: Determining a Velocity Curve of the Milky Way Galaxy
summary: Instructions and handouts for determining a velocity curve of the MWG
tags: ['School-Teachers', 'Students', 'Hobbyists' ]
categories: ['Astronomy']
order: 6
meta_description: "Use horn telescope data to plot the Milky Way rotation curve. Find instructions and classroom handouts for this DSPIRA astronomy activity."
equipment: "Observation handouts, Stellarium, and a calibrated horn telescope for collecting spectra. Analysis uses a spreadsheet or the optional notebook."
preparation: "Review Doppler shifts and galactic coordinates. Replace the historical observing dates and locations before planning your own observations."
---

**OVERVIEW FOR THE TEACHER**

* [Unit Description and Outline]({{ site.baseurl }}/assets/lessons/velocity-curve/unit-outline.pdf){: .btn .btn-wvu-blue}

  The whole unit on two pages: what the students build toward, in what order, and
  why. Written for AP Physics. Students use the Milky Way's rotation curve to deduce the existence of dark matter.


- **Level:** HS Advanced, College

- **Objective:** Students use a horn telescope to measure HI spectra along the Milky Way's galactic plane. Observations of galactic quadrants II and III show students that the MWG is rotating. Students use observations of galactic quadrant I to determine a velocity curve. They compare it with expected curves for different galactic mass distributions.


- **Pre-Knowledge of Students:** 

    + The students have been exposed to the horn telescope and understand how to read a spectrum. 

    + Students understand radio waves and the hydrogen spin-flip transition. This transition produces the 21 cm waves detected by the horn telescope. 

    + Students apply Doppler shifts to spectral peaks to find the detected hydrogen's relative velocity.

    + The students understand trigonometry.

    + The students understand relative velocity.

    + The students understand Newton’s law of gravitation and can relate it to the orbital motion of satellites.

- **Key Terms:** horn telescope, HI spectrum, galactic coordinates, horizontal coordinates, Stellarium. Doppler shift, red shift, blue shift, relative velocity. Circular motion, law of gravitation, orbital motion

- **Related Videos for Teacher:** [Galaxy Survey Trailer](#video-tDCPp8RIM4g)

<figure class="lesson-video" id="video-tDCPp8RIM4g">
{% include youtube.html title="Galaxy Survey Trailer" url="https://youtu.be/tDCPp8RIM4g" video="tDCPp8RIM4g" %}
</figure>

- **Teacher Preparation:**  
    + Share one horn with the class, or assign separate horns to student groups.

    + The students have used a horn telescope before. It is recommended that the following lessons have been completed:
        - Intro to the Horn Telescope

        - Electromagnetic Spectrum

        - The 21 cm Wavelength of Neutral Hydrogen

        - Understanding Coordinate Systems 

    + Teachers should understand red-shifted and blue-shifted signals. Quadrant II generally shows blue-shifted peaks, while quadrant III shows red-shifted peaks. Together, these trends imply clockwise galactic rotation in standard galactic coordinates.

    + Teachers should understand the tangent method and its relationship between galactic distances, angles, and line-of-sight motion. In quadrant I, tangent-point motion is away from the Sun. This produces the red-shifted peaks students seek. See the Teacher Notes under Part 2: Galactic Quadrant I Observation.

- **Sequence of activities:** - The Teacher Notes for each part provide more details.

**INTRO:** These activities introduce the concepts and give students experience with the horn telescope

   a. Group these four activities together. Small groups can take turns using the horn telescope for the practical activity.

   b. The students may have had some of these experiences if other lesson modules have been done (Basic Observational Tools) 

 **PART I** The students collect spectra at different galactic longitudes along the galactic plane in quadrants II and III.

   a. The student analyze the spectra to determine the relative velocity of the detected hydrogen.

   b. The students determine that the galaxy is rotating.

  **PART II** The students then collect spectra at different galactic longitudes along the galactic plane in quadrant I.

   a. Assuming circular motion of the galaxy, the speed of the tangent point along the observation line is calculated.

   b. A graph showing galactic speed vs distance from the galactic center is created using these results.

   c. This graph is compared to the graph expected in different models of mass distribution in the galaxy.


## Intro Activities for Radio Astronomy

OBJECTIVE: These activities allow this *Velocity Curve of the MWG* module be able to stand alone from start to finish. There is also some overlap with the *Basic Observational Tools* module. These basic activities will bring fuller understanding to creating the galactic velocity curve.

*Teacher Notes* Assign all four activities so students have work to complete while others use the telescope. Small groups can then take turns discovering what the horn can do. (Most teachers very likely with have only one telescope.)

* [Introduction to Horn Telescope]({{ site.baseurl }}/assets/worksheets/velocity-curve/horn-introduction.pdf){: .btn .btn-wvu-blue}

* [Introduction to Horn Telescope Follow-up]({{ site.baseurl }}/assets/worksheets/velocity-curve/horn-introduction-answer-key.pdf)

* [The Electromagnetic Spectrum]({{ site.baseurl }}/assets/worksheets/velocity-curve/electromagnetic-spectrum.pdf){: .btn .btn-wvu-blue}

   Further reading for this activity:
   [introduction to wavelengths and radiation]({{ site.baseurl }}/assets/lessons/electromagnetic-spectrum/introduction.pdf).

* [The 21 cm Wavelength of Neutral Hydrogen]({{ site.baseurl }}/assets/lessons/velocity-curve/hydrogen-21cm.pdf){: .btn .btn-wvu-blue}

* [Celestial Coordinate Systems]({{ site.baseurl }}/assets/lessons/velocity-curve/coordinate-systems.pdf){: .btn .btn-wvu-blue}

* [Using Stellarium]({{ site.baseurl }}/assets/worksheets/velocity-curve/stellarium.pdf){: .btn .btn-wvu-blue}


## Part 1: Galactic Quadrants II and III Observation
{: #part-1-galactic-quadrants-ii--iii-observation}

OBJECTIVE: In this activity, the students collect spectra of the MWG along the galactic plane in quadrants II and III. From these they should be able to deduce that the MWG is rotating and the direction of rotation.

[Teacher Notes for Part 1](https://docs.google.com/document/d/1h9is9YnnfDidLnlvs-DnXlyzXIjT0EhrLDdnONAByHg/edit?usp=sharing){: .btn .btn-wvu-blue}

[Student Handout for Part 1 Observation](https://docs.google.com/document/d/1jcMV-8X8Cd7rryGCsednTlc0fFRrgvAGkFyJUQAGJh8/edit?usp=sharing){: .btn .btn-wvu-blue}

[Student Handout for Part 1 Analysis and Interpretation](https://docs.google.com/document/d/1aVUFzAvC14gPeV6RSYumYPlkclgILeoaI5LpUZNSV5U/edit?usp=sharing){: .btn .btn-wvu-blue}



## Analysis Code (optional)

A Jupyter notebook is available for classes that want a numerical fit. It performs a sine fit and plots the result:

* [Galactic Plane Sine Fit notebook](https://github.com/WVURAIL/dspira/tree/main/lesson-examples/velocity-curve){: .btn .btn-wvu-blue}

Students replace the sample data in `quadrants_ii_iii_velocity_vs_longitude.csv` with
their own measurements and re-run. The fitted amplitude and phase give a
quantitative handle on the rotation the students deduced qualitatively above.


## Part 2: Galactic Quadrant I Observation

OBJECTIVE: In this activity, the students collect spectra of the MWG along the galactic plane in quadrant I. Students determine the speeds represented by the spectra's most red-shifted features. They then use the tangent method to calculate galactic velocity at different distances from the galactic center.

[Teacher Notes for Part 2](https://docs.google.com/document/d/1BSLoZjrFtA2qEoVzgvXjHdufQFRWmxtQWSAl8k1yJu8/edit?usp=sharing){: .btn .btn-wvu-blue}

[Student Handout for Part 2 Observation](https://docs.google.com/document/d/1V4wUx8VtX358x-gIWdH9FaYi3579bz_Unl38_ShrbKE/edit?usp=sharing){: .btn .btn-wvu-blue}

[Student Handout for Part 2 Analysis and Interpretation](https://docs.google.com/document/d/1J9w1DH5fQW24XDvesYTzsR943Px_13uTZQQS5qi6rxg/edit?usp=sharing){: .btn .btn-wvu-blue}



## Example handouts from an earlier run

One class used these worksheets for Part 1 in 2018. They illustrate **how a teacher structured the observation**. Adapt them before using them with your class.

> ⚠️ The observing sheet uses that class's dates and schedule.
> Observations took place on two October mornings, from 8:00 to 8:45 am. Nothing is pre-computed.
> Students find their own azimuth and altitude in Stellarium and complete the table themselves. But the dates and times are that school's, so replace
> them with yours. The Part 1 and Part 2 handouts above are the current version
> of the lessons.

* [Galactic Plane Observation 1, 2018]({{ site.baseurl }}/assets/worksheets/velocity-curve/galactic-plane-observation-1-2018.pdf){: .btn .btn-wvu-blue} — the observing sheet. Its spreadsheet analysis section is useful whatever dates you observe on.
* [Galactic Plane Observation 1: Conclusions, 2018]({{ site.baseurl }}/assets/worksheets/velocity-curve/galactic-plane-observation-1-conclusions-2018.pdf){: .btn .btn-wvu-blue}. Class results for quadrants II and III, including uncertainty estimates and conclusion questions.


## All Velocity Curve handouts in one place

An [earlier Part 2 worksheet from 2019]({{ '/assets/worksheets/velocity-curve/galactic-plane-observation-2-2019.pdf' | relative_url }}) is also available.
It includes teacher notes and an observation plan. Adapt its class-specific details before use.

   * [Galactic Plane Quadrants II and III Observations: Teacher Notes](https://docs.google.com/document/d/1h9is9YnnfDidLnlvs-DnXlyzXIjT0EhrLDdnONAByHg/edit?usp=sharing)

   * [Galactic Plane Quadrants II and III Observations](https://docs.google.com/document/d/1jcMV-8X8Cd7rryGCsednTlc0fFRrgvAGkFyJUQAGJh8/edit)

   * [Galactic Plane Quadrants II and III Observations: Conclusions](https://docs.google.com/document/d/1aVUFzAvC14gPeV6RSYumYPlkclgILeoaI5LpUZNSV5U/edit)

   * [Galactic Plane Quadrant I Observations: Teacher Notes](https://docs.google.com/document/d/1BSLoZjrFtA2qEoVzgvXjHdufQFRWmxtQWSAl8k1yJu8/edit)

   * [Galactic Plane Quadrant I Observations](https://docs.google.com/document/d/1V4wUx8VtX358x-gIWdH9FaYi3579bz_Unl38_ShrbKE/edit)

   * [Galactic Plane Quadrant I Observations: The Tangent Method](https://docs.google.com/document/d/1wA_tVKYrAyjvuVqUY9c_stwNpO1dGDFnIL6TiHq5hx8/edit?usp=sharing)   

   * [Galactic Plane Quadrant I Observations: Analysis and Conclusions](https://docs.google.com/document/d/1J9w1DH5fQW24XDvesYTzsR943Px_13uTZQQS5qi6rxg/edit)

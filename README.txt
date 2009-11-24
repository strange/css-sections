============
CSS-Sections
============

Disclaimer
==========

This is just some code I've been using to create grids. It works for me and I
keep this code in a repository online for my own convenience.

The 960 Grid System (http://960.gs/) et al. is probably what you want to use.

Introduction
============

`CSS-Sections` is CSS grids in disguise.

The philosophy behind `CSS-Sections` is a simple one: a section container
(`.sections`) can fit a number of sections (`.section`). More important
sections can claim additional "weight" but will as such reduce the amount of
"weight" available to other, less significant, sections.

The "weight" the different sections claim is translated into `width` when the
CSS file included in this repository is applied.

The following weight-changing CSS classes are defined:

* `.sesquiweight` (takes up one and a half the space of a regular section)
* `.doubleweight` (dito but double the space)
* `.tripleweight` (dito but triple the space)
* `.quadweight` (dito but four times the space)
* `.quinweight` (dito but five times the space)
* `.halfweight` (half the space of a regular section)

A section container can display six sections of regular weight horizontally.
Use basic addition to calculate the number of sections of varying weights a
container can take::

    doubleweight + doubleweight + doubleweight = 2 + 2 + 2 = 6
    regular section + quinweight = 1 + 5 = 6
    doubleweight + quadweight = 2 + 4 = 6
    tripleweight + tripleweight = 3 + 3 = 6
    doubleweight + doubleweight + doubleweight = 2 + 2 + 2 = 6
    halfweight + sesquiweight + quadweight = 0.5 + 1.5 + 4 = 6

Usage
=====

Just link the included stylesheet (`sections.css`) (or copy-paste it's contents
into your own stylesheet) and add proper classes to your elements::

    <div class="sections">
        <div class="section quinweight">Section</div>
        <div class="section">Section</div>
    </div>

See ``example/index.html`` for more examples.

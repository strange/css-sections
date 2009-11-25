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

A section container can display 12 sections of regular weight horizontally.

The following weight-changing CSS classes are defined (yes, trying to come up
with more memorable names):

* `.doubleweight` (takes up double the space of a regular section)
* `.tripleweight` (dito but triple the space)
* `.quadweight` (dito but four times the space)
* `.quinweight` (dito but five times the space)
* `.hexweight` (dito but six times the space)
* `.septweight` (dito but seven times the space)
* `.octweight` (dito but eight times the space)
* `.nonweight` (dito but nine times the space)
* `.decweight` (dito but ten times the space)
* `.undecweight` (dito but eleven times the space)

Use basic addition to calculate the number of sections of varying weights a
container can take::

    quadweight + quadweight + quadweight = 4 + 4 + 4 = 12
    doubleweight + decweight = 2 + 10 = 12
    tripleweight + tripleweight + tripleweight = 3 + 3 + 3 = 12

Usage
=====

Just link the included stylesheet (`sections.css`) (or copy-paste it's contents
into your own stylesheet) and add proper classes to your elements::

    <div class="sections">
        <div class="section hexweight">Section</div>
        <div class="section hexweight">Section</div>
    </div>

See ``example/index.html`` for more examples.
